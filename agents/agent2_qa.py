"""Agent 2 — QA Validation Agent.

Runs after Agent 1 synthesis. Reads Agent 1's <SprintZero_response> XML, applies the
seven checks from the QA protocol, and returns only the <qa_review> element. The
caller merges that element into Agent 1's response and flips qa_status accordingly.

Hard guard: A-001 (evaluation framework) and A-006 (output schema) must exist;
Agent 2 refuses to load if either is missing. C-001 (domain_weather_apps.md) is
optional — if absent, Check 4 degrades to general domain knowledge per the protocol
and Agent 2 is instructed to note the degradation in its output.
"""
import os
import re
import xml.etree.ElementTree as ET
from pathlib import Path

import model_client

REPO_ROOT = Path(__file__).parent.parent
QA_PROTOCOL_PATH = REPO_ROOT / "agents" / "prompts" / "qa_agent_protocol.md"
OUTPUT_SCHEMA_PATH = REPO_ROOT / "agents" / "prompts" / "sprintzero_output_schema.xml"
FRAMEWORK_PATH = REPO_ROOT / "corpora" / "framework" / "evaluation.md"  # A-001
C001_PATH = REPO_ROOT / "corpora" / "context" / "domain_weather_apps.md"

# Hard guard per QA protocol: A-001 and A-006 are required inputs.
if not OUTPUT_SCHEMA_PATH.exists():
    raise FileNotFoundError(
        f"Agent 2 cannot run: A-006 schema missing at {OUTPUT_SCHEMA_PATH}"
    )
if not FRAMEWORK_PATH.exists():
    raise FileNotFoundError(
        f"Agent 2 cannot run: A-001 framework missing at {FRAMEWORK_PATH}"
    )

with open(QA_PROTOCOL_PATH) as f:
    QA_PROTOCOL = f.read()
with open(OUTPUT_SCHEMA_PATH) as f:
    OUTPUT_SCHEMA = f.read()
with open(FRAMEWORK_PATH) as f:
    FRAMEWORK = f.read()

C001 = None
if C001_PATH.exists():
    with open(C001_PATH) as f:
        C001 = f.read()

CODE_FENCE_RE = re.compile(r"^```(?:xml)?\s*\n(.*?)\n```\s*$", re.DOTALL)
QA_REVIEW_RE = re.compile(r"(<qa_review.*?</qa_review>)", re.DOTALL)


def build_qa_system_blocks():
    blocks = [
        {"type": "text", "text": QA_PROTOCOL},
        {"type": "text", "text": OUTPUT_SCHEMA},
        {
            "type": "text",
            "text": f"--- FRAMEWORK: A-001 evaluation framework ---\n\n{FRAMEWORK}",
        },
    ]
    if C001 is not None:
        blocks.append({
            "type": "text",
            "text": f"--- CONTEXT: C-001 domain_weather_apps.md ---\n\n{C001}",
        })
    else:
        blocks.append({
            "type": "text",
            "text": (
                "--- CONTEXT GAP NOTICE ---\n\n"
                "C-001 (domain_weather_apps.md) is not loaded for this run. Per the "
                "QA protocol, Check 4 (Transfer Assumption Depth) must degrade to "
                "general domain knowledge. You MUST note this degradation explicitly "
                "in your Check 4 finding. Do not silently skip the check."
            ),
        })
    blocks[-1]["cache_control"] = {"type": "ephemeral"}
    return blocks


def build_qa_user_message(agent1_xml):
    return (
        "The following is the complete Agent 1 SprintZero_response. Perform the "
        "seven checks defined in the QA protocol against this output.\n\n"
        "Return ONLY the <qa_review> element. The first character of your response "
        "must be `<` of `<qa_review>` and the last character must be `>` of "
        "`</qa_review>`. Do not return the full SprintZero_response. Do not wrap "
        "in Markdown fences. Do not add commentary.\n\n"
        f"{agent1_xml}"
    )


def _strip_wrapper(text):
    text = text.strip()
    m = CODE_FENCE_RE.match(text)
    if m:
        text = m.group(1).strip()
    m = QA_REVIEW_RE.search(text)
    if m:
        return m.group(1).strip()
    return text


def run_qa_review(client, model, agent1_xml, on_progress=None):
    """Call Agent 2; return (qa_review_element, error_message). On failure, element is None.

    Streams. `on_progress(accumulated_text)` fires as the review is written so
    the caller can report checks as they land rather than after all seven have
    completed - the measured 47s baseline was almost entirely output generation,
    so there was a lot of finished work sitting behind a blocking call.
    """
    system_blocks = build_qa_system_blocks()
    user_message = build_qa_user_message(agent1_xml)
    try:
        text, _final = model_client.stream_text(
            client,
            label="agent2_qa",
            model=model,
            max_tokens=12000,
            system=system_blocks,
            messages=[{"role": "user", "content": user_message}],
            on_progress=on_progress,
            agent1_xml_chars=len(agent1_xml),
            system_prefix_chars=sum(len(b["text"]) for b in system_blocks),
        )
    except Exception as e:
        return None, f"Agent 2 API call failed: {e}"

    if not text:
        return None, "Agent 2 returned empty response"

    cleaned = _strip_wrapper(text)
    try:
        element = ET.fromstring(cleaned)
    except ET.ParseError as e:
        return None, f"Agent 2 output did not parse: {e}"

    if element.tag != "qa_review":
        return None, f"Agent 2 returned <{element.tag}>, expected <qa_review>"

    return element, None


def merge_qa_review(agent1_root, qa_review_element):
    """Append qa_review to Agent 1's root and update qa_status in attributes."""
    agent1_root.append(qa_review_element)

    stamp = qa_review_element.find("overall_qa_stamp")
    qa_verdict = stamp.findtext("qa_verdict") if stamp is not None else None
    if qa_verdict in ("QA_PASSED", "QA_PASSED_WITH_NOTES"):
        new_status = "QA_PASSED"
    elif qa_verdict == "QA_FAILED":
        new_status = "QA_FAILED"
    else:
        new_status = "QA_FAILED"

    attrs = agent1_root.find("attributes")
    if attrs is not None:
        qa_status_elem = attrs.find("qa_status")
        if qa_status_elem is not None:
            qa_status_elem.text = new_status

    return agent1_root
