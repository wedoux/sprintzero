"""Flat JSON state for the single hard-coded project. Prototype scope only."""
import datetime
import json
from pathlib import Path

PROJECT_ID = "weather-underground-redesign"
STATE_DIR = Path(__file__).parent / "state"
STATE_FILE = STATE_DIR / f"{PROJECT_ID}.json"

DEFAULT_STATE = {
    "project_id": PROJECT_ID,
    "project_name": "Weather Underground Redesign",
    "display_names": {
        "evaluation.md": "SZ Standard Evaluation",
        "weather_underground.md": "WU AppStore Reviews",
    },
    "project_context": {
        "project_name": "Weather Underground iOS — Trust Investigation",
        "project_type": "EXISTING_PRODUCT_ITERATION",
        "research_objective": (
            "Determine whether reported forecast inaccuracy in Weather Underground iOS reviews "
            "is a forecast-model problem or a data-freshness problem, and which engineering "
            "workstream should own the fix."
        ),
        "business_decisions_pending": (
            "Engineering leadership must decide in the next sprint whether to allocate the Q3 "
            "trust-recovery budget to the forecast modelling team or to the iOS caching and "
            "refresh subsystem. Only one workstream can be funded."
        ),
        "prior_research_and_insights": (
            "None on file. Treat as first-pass synthesis on the current S-001 corpus."
        ),
        "target_market": (
            "US iOS users of Weather Underground who have left an App Store review in 2022 to "
            "2024. Scope is explicitly US-only for this evaluation."
        ),
        "known_constraints": (
            "Engineering capacity is committed elsewhere through end of Q2. Only one workstream "
            "can be funded in Q3."
        ),
        "primary_stakeholder": (
            "Engineering lead and product lead, jointly, deciding the Q3 budget allocation."
        ),
        "context_completeness": "COMPLETE",
    },
    "query_counter": 0,
}


def load_state():
    if not STATE_FILE.exists():
        STATE_DIR.mkdir(parents=True, exist_ok=True)
        save_state(DEFAULT_STATE)
        return json.loads(json.dumps(DEFAULT_STATE))
    with open(STATE_FILE) as f:
        state = json.load(f)
    for key, default_value in DEFAULT_STATE.items():
        if key not in state:
            state[key] = default_value
    return state


def save_state(state):
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


def generate_query_id(state):
    """Mutate state in place; increment counter; return SZ-YYYYMMDD-NNN."""
    state["query_counter"] = state.get("query_counter", 0) + 1
    today = datetime.date.today().strftime("%Y%m%d")
    return f"SZ-{today}-{state['query_counter']:03d}"


def project_context_xml(state):
    """Render project_context fields as XML for inclusion in the system prompt."""
    pc = state["project_context"]
    fields = "\n".join(
        f"  <{key}>{value}</{key}>"
        for key, value in pc.items()
        if value is not None and value != ""
    )
    return f"<project_context>\n{fields}\n</project_context>"
