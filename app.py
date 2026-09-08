import os
import re
import xml.etree.ElementTree as ET

import anthropic
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request

import instrumentation
import state
from agents import agent2_qa

load_dotenv()

app = Flask(__name__)
client = anthropic.Anthropic()

with open("agents/prompts/sprintzero_copilot_role_task.txt") as f:
    BASE_SYSTEM_PROMPT = f.read()

with open("agents/prompts/sprintzero_output_schema.xml") as f:
    OUTPUT_FORMAT = f.read()

MODEL = "claude-opus-4-7"
CORPORA_DIR = "corpora"
ROLES = ("framework", "corpus", "context")
ROLE_LABELS = {
    "framework": "Framework",
    "corpus": "Reference data",
    "context": "Domain context",
}

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


CODE_FENCE_RE = re.compile(r"^```(?:xml)?\s*\n(.*?)\n```\s*$", re.DOTALL)
SPRINTZERO_RESPONSE_RE = re.compile(
    r"(<SprintZero_response>.*?</SprintZero_response>)", re.DOTALL
)


def load_corpora():
    loaded = {role: [] for role in ROLES}
    for role in ROLES:
        path = os.path.join(CORPORA_DIR, role)
        if not os.path.isdir(path):
            continue
        for filename in sorted(os.listdir(path)):
            if filename.endswith(".md"):
                with open(os.path.join(path, filename)) as f:
                    loaded[role].append({"filename": filename, "content": f.read()})
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
        context_block = (
            "=== PROJECT STATE (server-managed; treat as authoritative) ===\n\n"
            "Project context for this query is COMPLETE. Treat the following as the "
            "established project_context record. Do not produce an INTAKE response. "
            "Do not produce a CHALLENGE response on intake grounds. Proceed directly "
            "to evaluating the submitted theme.\n\n"
            f"{project_xml}\n\n"
            f"The query_id for this query is {query_id}. Use this exact value in your "
            "<query_id> attribute — do not invent or alter it."
        )
        blocks.append({"type": "text", "text": context_block})
    blocks[-1]["cache_control"] = {"type": "ephemeral"}
    return blocks


def summarise_corpora(corpora, project_state=None):
    display_names = (project_state or {}).get("display_names") or {}
    groups = []
    for role in ROLES:
        items = corpora[role]
        if not items:
            continue
        groups.append({
            "label": ROLE_LABELS[role],
            "items": [
                {
                    "name": display_names.get(item["filename"], item["filename"]),
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


@app.route("/", methods=["GET"])
def home():
    corpora = load_corpora()
    project_state = state.load_state()
    return render_template(
        "index.html",
        loaded_files=summarise_corpora(corpora, project_state),
        project_state=project_state,
    )


@app.route("/ask", methods=["POST"])
def ask():
    """Phase 1 of the two-agent flow.

    Runs Agent 1 only. Returns the rendered Agent 1 output plus a skeleton
    placeholder for Agent 2 (rendered server-side inside #qa-region). Also
    returns the Agent 1 XML as a string so the client can hand it to /qa
    for Agent 2 to review.
    """
    question = (request.form.get("question") or "").strip()
    if not question:
        return jsonify({"error": "empty question"}), 400

    corpora = load_corpora()
    project_state = state.load_state()
    query_id = state.generate_query_id(project_state)

    system_blocks = build_system_blocks(corpora, project_state, query_id)
    try:
        response = instrumentation.observe(
            "agent1_synthesis",
            lambda: client.messages.create(
                model=MODEL,
                max_tokens=16000,
                system=system_blocks,
                messages=[{"role": "user", "content": question}],
            ),
            model=MODEL,
            query_id=query_id,
            system_prefix_chars=sum(len(b["text"]) for b in system_blocks),
        )
    except anthropic.AuthenticationError:
        return jsonify({"error": "Invalid API key. Check ANTHROPIC_API_KEY in .env."}), 500
    except anthropic.APIError as e:
        return jsonify({"error": f"API error: {e.message}"}), 500

    raw_answer = next((b.text for b in response.content if b.type == "text"), "")
    root, parse_error = parse_response(raw_answer)

    if parse_error:
        return jsonify({
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
            ),
            "query_id": query_id,
        })

    response_type = root.findtext("attributes/response_type")
    state.save_state(project_state)

    # qa_review is intentionally NOT present on root yet — right_pane.html will
    # render the skeleton (when synthesis) which JS will swap once /qa returns.
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
    agent1_xml = ET.tostring(root, encoding="unicode") if is_synthesis else None

    return jsonify({
        "response_type": response_type,
        "chat_html": chat_html,
        "right_pane_html": right_pane_html,
        "agent1_xml": agent1_xml,
        "query_id": query_id,
    })


@app.route("/qa", methods=["POST"])
def qa():
    """Phase 2 of the two-agent flow.

    Receives Agent 1's full XML, runs Agent 2 against it, returns the
    rendered qa_surface partial so the client can swap it into #qa-region.
    """
    data = request.get_json(silent=True) or {}
    agent1_xml = (data.get("agent1_xml") or "").strip()
    if not agent1_xml:
        return jsonify({"error": "missing agent1_xml"}), 400

    root, parse_error = parse_response(agent1_xml)
    if parse_error or root is None:
        return jsonify({"error": f"Could not re-parse Agent 1 XML: {parse_error}"}), 400

    qa_review, qa_error = agent2_qa.run_qa_review(client, MODEL, agent1_xml)
    if qa_review is None:
        return jsonify({"error": f"QA review failed: {qa_error}"}), 500

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

    # The gate acts on Agent 1's verdict, so /qa also returns the fragment that
    # invalidates it. Rendered server-side and patched into the existing banner
    # by the client - re-rendering the whole pane would risk Agent 1's spine.
    verdict_invalidation_html = None
    if qa_status == "QA_FAILED":
        verdict_invalidation_html = render_template(
            "partials/verdict_invalidation.html",
            required_action=required_action,
            blocking=blocking,
            degraded=degraded,
        )

    return jsonify({
        "qa_html": qa_html,
        "qa_status": qa_status,
        "qa_degraded": degraded,
        "verdict_invalidation_html": verdict_invalidation_html,
    })


if __name__ == "__main__":
    app.run(debug=True, port=5001)
