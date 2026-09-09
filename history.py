"""Per-project record of every theme that reached a verdict.

Before this, a verdict existed only in the browser tab that produced it: eighty
seconds of synthesis and fifty of adversarial review, gone on refresh. A
research tool that cannot show you what it concluded last week is a toy.

What is stored is the full merged document, not a summary. That costs a few
kilobytes and buys the ability to re-render a past verdict through the same
right_pane.html the live flow uses — no second renderer to build, and no risk
of a history view drifting from the real one. The summary fields alongside it
exist so the list can be drawn without parsing every document.

Deliberately NOT fed back into later prompts. Each verdict stays independently
reproducible, the prompt does not grow as a project accumulates history, and
results do not depend on the order themes were submitted. `prior_research_and
_insights` stays whatever the researcher wrote.

Only synthesis turns are recorded — EVALUATION and GAP_FLAG. An intake
conversation or a challenge is not a verdict and would only clutter the record.
"""
import datetime
import json
import re
import xml.etree.ElementTree as ET

import resources

# Query ids are generated server-side as SZ-YYYYMMDD-NNN, but they arrive back
# from the client on the /qa call, so they are treated as untrusted filenames.
VALID_QUERY_ID = re.compile(r"^SZ-\d{8}-\d{3,}$")

RECORDED_TYPES = ("EVALUATION", "GAP_FLAG")


def is_valid_query_id(query_id):
    return bool(query_id and VALID_QUERY_ID.match(query_id))


def _path(project_id, query_id, create=False):
    return resources.history_dir(project_id, create=create) / f"{query_id}.json"


def summarise(root):
    """The fields the list view needs, pulled once at write time."""
    verdict = root.find("verdict")
    stamp = root.find("qa_review/overall_qa_stamp")
    return {
        "response_type": root.findtext("attributes/response_type"),
        "qa_status": root.findtext("attributes/qa_status"),
        "qa_verdict": stamp.findtext("qa_verdict") if stamp is not None else None,
        "classification": verdict.findtext("classification") if verdict is not None else None,
        "confidence_score": verdict.findtext("confidence_score") if verdict is not None else None,
        "stability_status": verdict.findtext("stability_status") if verdict is not None else None,
        "one_line_verdict": verdict.findtext("one_line_verdict") if verdict is not None else None,
    }


def record(project_id, query_id, theme, root):
    """Write one history record. Returns the path, or None if not recordable."""
    if not is_valid_query_id(query_id):
        return None
    summary = summarise(root)
    if summary["response_type"] not in RECORDED_TYPES:
        return None

    payload = {
        "query_id": query_id,
        "created_at": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
        "theme": (theme or "").strip(),
        **summary,
        "document_xml": ET.tostring(root, encoding="unicode"),
    }
    path = _path(project_id, query_id, create=True)
    tmp = path.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    tmp.replace(path)  # atomic: a half-written record would break the list view
    return path


def load(project_id, query_id):
    if not is_valid_query_id(query_id):
        return None
    path = _path(project_id, query_id)
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def list_records(project_id):
    """Summaries, newest first. document_xml is dropped — the list does not need it."""
    directory = resources.history_dir(project_id)
    if not directory.exists():
        return []
    rows = []
    for path in directory.glob("SZ-*.json"):
        try:
            entry = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue  # one corrupt record must not hide the rest
        entry.pop("document_xml", None)
        rows.append(entry)
    return sorted(rows, key=lambda r: r.get("created_at") or "", reverse=True)


def count(project_id):
    directory = resources.history_dir(project_id)
    return len(list(directory.glob("SZ-*.json"))) if directory.exists() else 0


def document(project_id, query_id):
    """The stored document, re-parsed for rendering. None if unreadable."""
    entry = load(project_id, query_id)
    if entry is None:
        return None, None
    try:
        return ET.fromstring(entry["document_xml"]), entry
    except (KeyError, ET.ParseError):
        return None, entry
