import json
import os
import re
import threading
import xml.etree.ElementTree as ET

import anthropic
from dotenv import load_dotenv

import credentials
from urllib.parse import quote

from flask import (Flask, Response, abort, jsonify, redirect, render_template,
                   request, stream_with_context, url_for)

import history
import instrumentation
import model_client
import reference
import resources
import state
from agents import agent2_qa

load_dotenv()

# Explicit folders: a frozen bundle unpacks to a temp dir, and a double-clicked
# .app inherits "/" as its working directory, so Flask's relative defaults and
# every bare relative open() below would resolve against the wrong place.
app = Flask(
    __name__,
    template_folder=str(resources.resource("templates")),
    static_folder=str(resources.resource("static")),
)
client = anthropic.Anthropic()

BASE_SYSTEM_PROMPT = resources.read_text("agents", "prompts", "sprintzero_copilot_role_task.txt")
OUTPUT_FORMAT = resources.read_text("agents", "prompts", "sprintzero_output_schema.xml")

# Agent 1 and Agent 2 are separately configurable - see model_client for why.
AGENT1_MODEL = model_client.AGENT1_MODEL
AGENT2_MODEL = model_client.AGENT2_MODEL

CORPORA_DIR = str(resources.resource("corpora"))
ROLES = ("framework", "corpus", "context")
ROLE_LABELS = {
    "framework": "Framework",
    "corpus": "Reference data",
    "context": "Domain context",
}

# Real progress, replacing the timed animation the client used to run. Each
# entry fires the first time its closing tag appears in the streamed output, so
# the activity log reports what the agent has actually finished. The measured
# baseline spent ~85s (Agent 1) and ~47s (Agent 2) generating output that was
# already partly complete and entirely unshown.
AGENT1_PROGRESS = [
    ("insight_under_evaluation", "Insight framed"),
    ("behavioural_mechanism", "Behavioural mechanism mapped"),
    ("evidence_chain", "Evidence chain assembled"),
    ("verdict", "Verdict committed"),
    ("reasoning_step", "Reasoning committed"),
    ("falsification_attempt", "Falsification attempt complete"),
    ("transfer_assumption_check", "Transfer assumption checked"),
    ("gap_flags", "Gap flags recorded"),
    ("decision_support", "Decision support written"),
    ("reframed_insight", "Insight reframed"),
]

QA_CHECK_NAMES = [
    ("check_reasoning_validity", "Reasoning Validity"),
    ("check_counter_signal_engagement", "Counter-Signal Engagement"),
    ("check_confidence_integrity", "Confidence Integrity"),
    ("check_transfer_assumption_depth", "Transfer Assumption Depth"),
    ("check_behavioural_mechanism_specificity", "Behavioural Mechanism Specificity"),
    ("check_tacit_knowledge_prompt_specificity", "Tacit Knowledge Prompt Specificity"),
    ("check_decision_support_overreach", "Decision Support Overreach"),
]


def extract_qa_checks(qa_review_element):
    out = []
    if qa_review_element is None:
        return out
    for elem_name, display_name in QA_CHECK_NAMES:
        check_el = qa_review_element.find(elem_name)
        if check_el is None:
            continue
        verdict = check_el.findtext("verdict") or "SKIPPED"
        finding = check_el.findtext("finding") or ""
        out.append({"name": display_name, "verdict": verdict, "finding": finding})
    return out


def qa_gate_reason(qa_review_element, qa_status):
    """Why the QA gate blocked the verdict, and whether it gave a reason at all.

    Returns (required_action, blocking_findings, degraded).

    `degraded` is the UI-only state for a QA_FAILED carrying no machine-readable
    reason. It matters because agent2_qa.merge_qa_review maps an unknown or
    absent qa_verdict to QA_FAILED: a malformed Agent 2 response can therefore
    invalidate a sound verdict. Rendering that identically to a substantive
    failure would repeat, in a new place, the exact misread this work removes -
    so the surface says "QA could not complete" instead of asserting a failure
    the agent never actually found.

    Degradation is only meaningful when the gate actually blocked. A clean pass
    legitimately carries no required_action, and must never be marked degraded.
    """
    if qa_status != "QA_FAILED":
        return None, None, False
    if qa_review_element is None:
        return None, None, True
    stamp = qa_review_element.find("overall_qa_stamp")
    if stamp is None:
        return None, None, True
    required_action = (stamp.findtext("required_action") or "").strip() or None
    blocking = (stamp.findtext("blocking_findings") or "").strip() or None
    return required_action, blocking, not (required_action or blocking)


ENUM_TOKEN_RE = re.compile(r"^([A-Z][A-Z_]{2,})\b")


@app.template_filter("signal_token")
def signal_token(value, limit=30):
    """Reduce a schema field to the status it leads with.

    Fields like transfer_verdict are specified as an enum but the model often
    writes the enum followed by a sentence of justification. A Tier 2 chip is a
    glanceable status; rendering the whole paragraph inside one broke the strip
    layout. The full text is still shown in the Tier 3 card.
    """
    text = (value or "").strip()
    if not text:
        return ""
    match = ENUM_TOKEN_RE.match(text)
    if match:
        return match.group(1)
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "\u2026"


def sse(event, payload):
    """One Server-Sent Event frame."""
    return f"event: {event}\ndata: {json.dumps(payload)}\n\n"


VERDICT_FRAGMENT_RE = re.compile(r"<verdict>.*?</verdict>", re.DOTALL)


def make_section_reporter(sections):
    """Returns on_progress(text) that emits each section once, in completion order.

    Appends to a list rather than yielding, because the Anthropic stream calls
    this synchronously from inside its own loop - the Flask generator drains
    the list between chunks. It also runs on the worker thread, which has no
    Flask app context, so it captures the verdict as raw XML and leaves
    rendering to the generator.

    The verdict closes roughly 20s into a ~90s synthesis, well before the
    remaining sections. Emitting it immediately is the difference between the
    reader seeing the answer at 20s and seeing it at 90s.
    """
    seen = set()
    pending = []

    def on_progress(accumulated):
        for tag, label in sections:
            if tag in seen:
                continue
            if f"</{tag}>" in accumulated:
                seen.add(tag)
                pending.append({"kind": "progress", "tag": tag, "label": label})
                if tag == "verdict":
                    match = VERDICT_FRAGMENT_RE.search(accumulated)
                    if match:
                        pending.append({"kind": "verdict", "xml": match.group(0)})

    return on_progress, pending


CHECK_VERDICT_RE = re.compile(r"<verdict>\s*([A-Z_]+)\s*</verdict>")


def make_check_reporter():
    """As above, but reports each QA check with the verdict it landed on."""
    seen = set()
    pending = []

    def on_progress(accumulated):
        for tag, label in QA_CHECK_NAMES:
            if tag in seen:
                continue
            close = f"</{tag}>"
            idx = accumulated.find(close)
            if idx == -1:
                continue
            seen.add(tag)
            fragment = accumulated[accumulated.rfind(f"<{tag}>", 0, idx):idx]
            m = CHECK_VERDICT_RE.search(fragment)
            pending.append({
                "tag": tag,
                "label": label,
                "verdict": m.group(1) if m else "SKIPPED",
            })

    return on_progress, pending


CODE_FENCE_RE = re.compile(r"^```(?:xml)?\s*\n(.*?)\n```\s*$", re.DOTALL)
SPRINTZERO_RESPONSE_RE = re.compile(
    r"(<SprintZero_response>.*?</SprintZero_response>)", re.DOTALL
)


# Which roles ship with the app rather than belonging to a project. The
# framework (A-001) is a system asset - Agent 2 hard-requires it at import -
# and context holds domain knowledge shared across projects. Corpus is the
# researcher's own evidence and comes from the project, never from here.
GLOBAL_ROLES = ("framework", "context")


def load_corpora(project=None):
    """Framework and context ship with the app; corpus belongs to the project.

    Called with no project only by tooling that needs the global assets.
    """
    loaded = {role: [] for role in ROLES}
    for role in GLOBAL_ROLES:
        path = os.path.join(CORPORA_DIR, role)
        if not os.path.isdir(path):
            continue
        for filename in sorted(os.listdir(path)):
            if filename.endswith(".md"):
                with open(os.path.join(path, filename)) as f:
                    # No "display": global assets fall through to the
                    # project's display_names, then to the filename.
                    loaded[role].append({
                        "filename": filename,
                        "content": f.read(),
                    })
    if project is not None:
        loaded["corpus"] = reference.load_assets(project)
    return loaded


def build_system_blocks(corpora, project_state=None, query_id=None):
    blocks = [
        {"type": "text", "text": BASE_SYSTEM_PROMPT},
        {"type": "text", "text": OUTPUT_FORMAT},
    ]
    for role in ROLES:
        for item in corpora[role]:
            blocks.append({
                "type": "text",
                "text": f"--- {role.upper()}: {item['filename']} ---\n\n{item['content']}",
            })
    if project_state is not None and query_id is not None:
        project_xml = state.project_context_xml(project_state)
        query_id_rule = (
            f"The query_id for this query is {query_id}. Use this exact value in your "
            "<query_id> attribute — do not invent or alter it."
        )

        if state.context_is_complete(project_state):
            context_block = (
                "=== PROJECT STATE (server-managed; treat as authoritative) ===\n\n"
                "Project context for this query is COMPLETE. Treat the following as the "
                "established project_context record. Do not produce an INTAKE response. "
                "Do not produce a CHALLENGE response on intake grounds. Proceed directly "
                "to evaluating the submitted theme.\n\n"
                f"{project_xml}\n\n"
                f"{query_id_rule}"
            )
        else:
            # The intake protocol in A-004 and the INTAKE response type in the
            # schema have existed from the start; the block above was
            # unconditional, so they were unreachable. A project created from
            # the short form arrives here INCOMPLETE and the copilot collects
            # the rest conversationally.
            missing = ", ".join(state.missing_context_fields(project_state)) or "none"
            context_block = (
                "=== PROJECT STATE (server-managed; treat as authoritative) ===\n\n"
                "Project context for this project is INCOMPLETE. The fields below were "
                "captured when the project was created and are established; do not ask "
                "for them again.\n\n"
                f"Required fields still missing: {missing}.\n\n"
                "Run the INTAKE PROTOCOL (Step 0). Produce an INTAKE response asking "
                "for the missing fields. Do not evaluate the submitted theme while "
                "context is incomplete — if the researcher has submitted a theme, "
                "acknowledge it and collect the missing context first.\n\n"
                "When the researcher's answers complete the record, return the FULL "
                "<project_context> element with every field populated and "
                "<context_completeness>COMPLETE</context_completeness>. The server "
                "persists that element verbatim, so anything you omit is lost.\n\n"
                f"{project_xml}\n\n"
                f"{query_id_rule}"
            )
        blocks.append({"type": "text", "text": context_block})
    blocks[-1]["cache_control"] = {"type": "ephemeral"}
    return blocks


def summarise_corpora(corpora, project_state=None):
    """What the knowledge-base panel lists. Names come from the registry."""
    display_names = (project_state or {}).get("display_names") or {}
    groups = []
    for role in ROLES:
        items = corpora.get(role) or []
        if not items:
            continue
        groups.append({
            "label": ROLE_LABELS[role],
            "items": [
                {
                    "name": item.get("display")
                            or display_names.get(item["filename"], item["filename"]),
                    "asset_id": item.get("asset_id"),
                    "chars": len(item["content"]),
                }
                for item in items
            ],
        })
    return groups


def strip_wrapper(text):
    """Defensive strip — model occasionally wraps XML in Markdown fences or prose."""
    text = text.strip()
    match = CODE_FENCE_RE.match(text)
    if match:
        return match.group(1).strip()
    match = SPRINTZERO_RESPONSE_RE.search(text)
    if match:
        return match.group(1).strip()
    return text


def parse_response(text):
    """Returns (root, error). On parse failure root is None and error is the parser message."""
    if not text:
        return None, "empty response"
    cleaned = strip_wrapper(text)
    try:
        return ET.fromstring(cleaned), None
    except ET.ParseError as e:
        return None, str(e)


PROJECT_TYPE_LABELS = [
    ("EXISTING_PRODUCT_ITERATION", "Existing product — iteration"),
    ("EXISTING_PRODUCT_REDESIGN", "Existing product — redesign"),
    ("NEW_PRODUCT", "New product"),
    ("UNKNOWN", "Not sure yet"),
]


def require_project(project_id):
    """Load a project or 404. Ids come from the URL, so they are untrusted."""
    project = state.load_project(project_id)
    if project is None:
        abort(404)
    return project


def landing_projects():
    """Index entries decorated with the counts the landing screen shows."""
    rows = []
    for entry in state.list_projects():
        pid = entry["project_id"]
        rows.append({
            **entry,
            "reference_count": len(list(resources.reference_dir(pid).glob("*.md"))),
            "history_count": history.count(pid),
        })
    return rows


@app.route("/", methods=["GET"])
def home():
    return render_template(
        "landing.html",
        projects=landing_projects(),
        project_types=PROJECT_TYPE_LABELS,
        form={},
        error=None,
    )


@app.route("/projects", methods=["POST"])
def create_project():
    try:
        project = state.create_project(
            request.form.get("project_name"),
            request.form.get("project_type"),
            request.form.get("research_objective"),
        )
    except ValueError as e:
        return render_template(
            "landing.html",
            projects=landing_projects(),
            project_types=PROJECT_TYPE_LABELS,
            form=request.form,
            error=str(e),
        ), 400
    return redirect(url_for("workspace", project_id=project["project_id"]))


@app.route("/projects/<project_id>", methods=["GET"])
def workspace(project_id):
    project_state = require_project(project_id)
    state.touch_project(project_id)
    corpora = load_corpora(project_state)
    return render_template(
        "index.html",
        loaded_files=summarise_corpora(corpora, project_state),
        project_state=project_state,
        source_types=reference.SOURCE_TYPES,
        reference_error=request.args.get("reference_error"),
        history_count=history.count(project_id),
    )


@app.route("/projects/<project_id>/history", methods=["GET"])
def project_history(project_id):
    project = require_project(project_id)
    return render_template(
        "history.html",
        project_state=project,
        records=history.list_records(project_id),
    )


@app.route("/projects/<project_id>/history/<query_id>", methods=["GET"])
def history_detail(project_id, query_id):
    project = require_project(project_id)
    root, entry = history.document(project_id, query_id)
    if entry is None:
        abort(404)
    # Rendered through the same right_pane.html the live flow uses, so a past
    # verdict cannot drift from how it originally appeared.
    qa_review = root.find("qa_review") if root is not None else None
    required_action, blocking, degraded = qa_gate_reason(
        qa_review, entry.get("qa_status"))
    return render_template(
        "history_detail.html",
        project_state=project,
        entry=entry,
        root=root,
        response_type=entry.get("response_type"),
        qa_checks=extract_qa_checks(qa_review),
        qa_degraded=degraded,
        required_action=required_action,
        blocking=blocking,
        replay_qa_status=entry.get("qa_status"),
        replay_gate=(entry.get("qa_status") == "QA_FAILED"),
    )


@app.route("/projects/<project_id>/reference", methods=["POST"])
def add_reference(project_id):
    """Paste text or upload text files. Both land in the same ingest path."""
    project = require_project(project_id)
    title = request.form.get("title") or ""
    source_type = request.form.get("source_type") or ""
    pasted = request.form.get("pasted_text") or ""
    uploads = [f for f in request.files.getlist("files") if f and f.filename]

    added, errors = [], []
    try:
        if pasted.strip():
            added.append(reference.ingest(project, title, source_type, pasted))
        for storage in uploads:
            filename, text = reference.read_upload(storage)
            # One title for one paste; uploads are named by their own filename
            # so a multi-file add does not collapse into one ambiguous title.
            label = title.strip() if (title.strip() and len(uploads) == 1 and not pasted.strip()) \
                else filename.rsplit(".", 1)[0]
            added.append(reference.ingest(project, label, source_type, text))
        if not added and not errors:
            errors.append("Paste some text or choose a file to add.")
    except reference.IngestError as e:
        errors.append(str(e))

    if added:
        state.save_project(project)

    target = url_for("workspace", project_id=project_id)
    if errors:
        return redirect(f"{target}?reference_error={quote(errors[0])}")
    return redirect(target)


@app.route("/projects/<project_id>/reference/<asset_id>/delete", methods=["POST"])
def delete_reference(project_id, asset_id):
    project = require_project(project_id)
    if reference.remove(project, asset_id) is not None:
        state.save_project(project)
    return redirect(url_for("workspace", project_id=project_id))


@app.route("/projects/<project_id>/ask", methods=["POST"])
def ask(project_id):
    """Phase 1 of the two-agent flow, streamed.

    Runs Agent 1 and emits Server-Sent Events as sections of the response
    complete, then a final `done` frame carrying the rendered HTML. The client
    used to run a timed animation against a blocking call; these are the real
    section completions instead.
    """
    question = (request.form.get("question") or "").strip()
    if not question:
        return jsonify({"error": "empty question"}), 400

    project_state = require_project(project_id)
    corpora = load_corpora(project_state)
    query_id = state.generate_query_id(project_state)
    system_blocks = build_system_blocks(corpora, project_state, query_id)

    def generate():
        box = {}

        def run_attempt():
            """One Agent 1 generation, yielding its progress frames as it goes.

            A fresh reporter per attempt, deliberately: on a retry the reader
            should see the sections land again, not sit in silence because the
            tags were already reported once.
            """
            on_progress, pending = make_section_reporter(AGENT1_PROGRESS)
            result = {}

            def run():
                try:
                    text, _ = model_client.stream_text(
                        client,
                        label="agent1_synthesis",
                        model=AGENT1_MODEL,
                        max_tokens=16000,
                        system=system_blocks,
                        messages=[{"role": "user", "content": question}],
                        on_progress=on_progress,
                        query_id=query_id,
                        system_prefix_chars=sum(len(b["text"]) for b in system_blocks),
                    )
                    result["text"] = text
                except anthropic.AuthenticationError:
                    credentials.clear_keychain()
                    result["error"] = (
                        "Invalid API key. The stored key has been cleared — "
                        "restart SprintZero to enter a new one, or set "
                        "ANTHROPIC_API_KEY in the environment."
                    )
                except anthropic.APIError as e:
                    result["error"] = f"API error: {getattr(e, 'message', e)}"
                except Exception as e:  # noqa: BLE001 - surfaced, not swallowed
                    result["error"] = f"Agent 1 failed: {e}"

            worker = threading.Thread(target=run, daemon=True)
            worker.start()

            # Drain progress while the model writes.
            while worker.is_alive() or pending:
                while pending:
                    item = pending.pop(0)
                    if item["kind"] == "verdict":
                        # Render Tier 1 the moment the verdict closes, rather
                        # than making the reader wait for the other nine
                        # sections. A malformed fragment is skipped silently:
                        # this is an early view, and the settled render follows.
                        try:
                            element = ET.fromstring(item["xml"])
                        except ET.ParseError:
                            continue
                        yield sse("verdict", {
                            "html": render_template(
                                "partials/verdict_banner.html",
                                verdict=element,
                                early=True,
                            ),
                        })
                    else:
                        yield sse("progress", item)
                if worker.is_alive():
                    worker.join(timeout=0.15)

            box.clear()
            box.update(result)

        # The model intermittently emits structurally invalid XML - a mismatched
        # tag, roughly one run in six - and the whole ~80s generation is lost
        # when it does. One retry, because a fresh sample almost always parses
        # and the alternative is handing the researcher nothing. The malformed
        # output is written to disk either way: it used to exist only in the
        # browser pane that reported it, which made a rare fault unfixable.
        root = None
        raw_answer = ""
        parse_error = None
        saved = []

        for attempt in (1, 2):
            if attempt == 2:
                yield sse("progress", {
                    "kind": "progress",
                    "tag": "retry",
                    "label": "Output was not valid XML — retrying synthesis",
                    "retry": True,
                })

            yield from run_attempt()

            if "error" in box:
                yield sse("error", {"error": box["error"]})
                return

            raw_answer = box.get("text", "")
            root, parse_error = parse_response(raw_answer)
            if root is not None:
                if attempt == 2:
                    yield sse("progress", {
                        "kind": "progress",
                        "tag": "retry_ok",
                        "label": "Retry produced valid output",
                    })
                break

            path = instrumentation.save_failed_output(
                "agent1", raw_answer, parse_error,
                attempt=attempt, query_id=query_id,
            )
            if path:
                saved.append(str(path))

        if root is None:
            yield sse("done", {
                "response_type": "PARSE_ERROR",
                "chat_html": render_template(
                    "partials/chat_messages.html",
                    response_type="PARSE_ERROR",
                    parse_error=parse_error,
                ),
                "right_pane_html": render_template(
                    "partials/right_pane.html",
                    response_type="PARSE_ERROR",
                    parse_error=parse_error,
                    raw_answer=raw_answer,
                    saved_paths=saved,
                    attempts=2,
                ),
                "query_id": query_id,
            })
            return

        response_type = root.findtext("attributes/response_type")

        # An INTAKE response carries the project_context the copilot has
        # assembled. Persist it: that is what moves a project from the three
        # fields the form captured to COMPLETE, after which the block above
        # stops asking and synthesis proceeds.
        incoming_context = root.find("project_context")
        if incoming_context is not None:
            fields = {child.tag: (child.text or "") for child in incoming_context}
            state.apply_context(project_state, fields)

        state.save_project(project_state)

        # qa_review is intentionally NOT present on root yet — right_pane.html
        # renders the pending QA band, which the client resolves once /qa lands.
        chat_html = render_template(
            "partials/chat_messages.html",
            root=root,
            response_type=response_type,
        )
        right_pane_html = render_template(
            "partials/right_pane.html",
            root=root,
            response_type=response_type,
            qa_checks=[],
        )

        is_synthesis = response_type in ("EVALUATION", "GAP_FLAG")
        yield sse("done", {
            "response_type": response_type,
            "chat_html": chat_html,
            "right_pane_html": right_pane_html,
            "agent1_xml": ET.tostring(root, encoding="unicode") if is_synthesis else None,
            "query_id": query_id,
        })

    return Response(
        stream_with_context(generate()),
        mimetype="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )


@app.route("/projects/<project_id>/qa", methods=["POST"])
def qa(project_id):
    """Phase 2 of the two-agent flow, streamed.

    Receives Agent 1's full XML, runs Agent 2 against it, and emits one event
    per completed check so the seven land visibly rather than arriving together
    after ~47s of blank screen. The final frame carries the rendered surface and
    the fragment that invalidates Agent 1's verdict when the gate fails.
    """
    require_project(project_id)
    data = request.get_json(silent=True) or {}
    agent1_xml = (data.get("agent1_xml") or "").strip()
    query_id = (data.get("query_id") or "").strip()
    theme = data.get("theme") or ""
    if not agent1_xml:
        return jsonify({"error": "missing agent1_xml"}), 400

    root, parse_error = parse_response(agent1_xml)
    if parse_error or root is None:
        return jsonify({"error": f"Could not re-parse Agent 1 XML: {parse_error}"}), 400

    def generate():
        on_progress, pending = make_check_reporter()
        result = {}

        def run():
            review, err = agent2_qa.run_qa_review(
                client, AGENT2_MODEL, agent1_xml, on_progress=on_progress
            )
            result["review"] = review
            result["error"] = err

        worker = threading.Thread(target=run, daemon=True)
        worker.start()

        while worker.is_alive() or pending:
            while pending:
                yield sse("check", pending.pop(0))
            if worker.is_alive():
                worker.join(timeout=0.15)

        qa_review = result.get("review")
        if qa_review is None:
            yield sse("error", {"error": f"QA review failed: {result.get('error')}"})
            return

        agent2_qa.merge_qa_review(root, qa_review)
        qa_checks = extract_qa_checks(qa_review)
        qa_status = root.findtext("attributes/qa_status")
        required_action, blocking, degraded = qa_gate_reason(qa_review, qa_status)

        qa_html = render_template(
            "partials/qa_surface.html",
            root=root,
            qa_checks=qa_checks,
            qa_degraded=degraded,
        )

        # The gate acts on Agent 1's verdict, so /qa also returns the fragment
        # that invalidates it. Patched into the existing banner by the client -
        # re-rendering the whole pane would risk Agent 1's spine.
        verdict_invalidation_html = None
        if qa_status == "QA_FAILED":
            verdict_invalidation_html = render_template(
                "partials/verdict_invalidation.html",
                required_action=required_action,
                blocking=blocking,
                degraded=degraded,
            )

        # Record against the project once the document is complete — that is,
        # after the QA gate has stamped it. Recorded whatever the verdict, so a
        # blocked one is visible in the history rather than quietly missing;
        # the stored qa_status says which it was.
        history.record(project_id, query_id, theme, root)

        yield sse("done", {
            "qa_html": qa_html,
            "qa_status": qa_status,
            "qa_degraded": degraded,
            "verdict_invalidation_html": verdict_invalidation_html,
        })

    return Response(
        stream_with_context(generate()),
        mimetype="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )


if __name__ == "__main__":
    app.run(debug=True, port=5001)
