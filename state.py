"""Per-project JSON state.

Replaces the single hard-coded project this started as. That was deliberately
prototype-scoped, and the file layout was already project-shaped
(`state/<project_id>.json`) — only the constant was fixed. This keeps the same
idea and gives each project a directory of its own:

    state/projects.json                     the landing-screen index
    state/projects/<id>/project.json        project_context + counter + registry
    state/projects/<id>/reference/          user-supplied reference data
    state/projects/<id>/history/            one record per evaluated theme

A project's `project_context` is stored verbatim in the shape the output schema
defines, so project_context_xml() renders it into the system prompt unchanged.

New projects start INCOMPLETE on purpose. The creation form asks for three
fields; Agent 1's INTAKE protocol collects the rest conversationally on the
first query. That protocol already exists in the prompt and the schema — it was
simply unreachable while app.py told Agent 1 never to use it.
"""
import datetime
import json
import re
import shutil

import resources

# The schema's project_context fields, in schema order. Anything absent is
# rendered as absent rather than empty, so Agent 1 can see what it must ask for.
CONTEXT_FIELDS = (
    "project_name",
    "project_type",
    "research_objective",
    "business_decisions_pending",
    "prior_research_and_insights",
    "target_market",
    "known_constraints",
    "primary_stakeholder",
    "context_completeness",
)

PROJECT_TYPES = (
    "NEW_PRODUCT",
    "EXISTING_PRODUCT_REDESIGN",
    "EXISTING_PRODUCT_ITERATION",
    "UNKNOWN",
)

LEGACY_PROJECT_ID = "weather-underground-redesign"


# ------------------------------------------------------------------ helpers

def _now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")


def slugify(name):
    slug = re.sub(r"[^a-z0-9]+", "-", (name or "").lower()).strip("-")
    return slug[:60] or "project"


def _read_json(path, default):
    if not path.exists():
        return default
    try:
        with open(path) as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError):
        return default


def _write_json(path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with open(tmp, "w") as f:
        json.dump(payload, f, indent=2)
    tmp.replace(path)  # atomic: a half-written project.json would lose a project


# -------------------------------------------------------------- the index

def list_projects():
    """Landing-screen index, most recently opened first."""
    migrate_legacy()
    index = _read_json(resources.projects_index_path(), [])
    return sorted(index, key=lambda p: p.get("last_opened_at") or "", reverse=True)


def _write_index(entries):
    _write_json(resources.projects_index_path(), entries)


def _upsert_index(project):
    entries = [e for e in _read_json(resources.projects_index_path(), [])
               if e.get("project_id") != project["project_id"]]
    entries.append({
        "project_id": project["project_id"],
        "project_name": project.get("project_name") or project["project_id"],
        "created_at": project.get("created_at"),
        "last_opened_at": project.get("last_opened_at"),
        "context_completeness": project["project_context"].get("context_completeness"),
    })
    _write_index(entries)


# ------------------------------------------------------------- projects

VALID_PROJECT_ID = re.compile(r"^[a-z0-9][a-z0-9-]{0,79}$")


def is_valid_project_id(project_id):
    """Project ids reach us from URLs, so they are untrusted input.

    An id is a single lowercase slug and nothing else — no separators, no
    parent references. Anything else is refused rather than normalised, so a
    traversing id cannot resolve to a path outside the project store.
    """
    return bool(project_id and VALID_PROJECT_ID.match(project_id))


def project_path(project_id):
    return resources.project_dir(project_id) / "project.json"


def project_exists(project_id):
    if not is_valid_project_id(project_id):
        return False
    return project_path(project_id).exists()


def load_project(project_id):
    """Returns the project dict, or None if there is no such project."""
    if not is_valid_project_id(project_id):
        return None
    migrate_legacy()
    if not project_exists(project_id):
        return None
    project = _read_json(project_path(project_id), None)
    if project is None:
        return None
    project.setdefault("registry", [])
    project.setdefault("query_counter", 0)
    project.setdefault("project_context", {})
    return project


def save_project(project):
    _write_json(project_path(project["project_id"]), project)
    _upsert_index(project)
    return project


def touch_project(project_id):
    project = load_project(project_id)
    if project is None:
        return None
    project["last_opened_at"] = _now()
    return save_project(project)


def create_project(project_name, project_type, research_objective):
    """Create a project from the three fields the form asks for.

    Everything else is left absent and marked INCOMPLETE, which is what makes
    Agent 1 run its intake protocol on the first query instead of evaluating
    against context nobody supplied.
    """
    project_name = (project_name or "").strip()
    if not project_name:
        raise ValueError("Project name is required.")
    if project_type not in PROJECT_TYPES:
        raise ValueError(f"project_type must be one of {', '.join(PROJECT_TYPES)}.")
    research_objective = (research_objective or "").strip()
    if not research_objective:
        raise ValueError("Research objective is required.")

    base = slugify(project_name)
    project_id, n = base, 2
    while project_exists(project_id):
        project_id, n = f"{base}-{n}", n + 1

    now = _now()
    project = {
        "project_id": project_id,
        "project_name": project_name,
        "created_at": now,
        "last_opened_at": now,
        "query_counter": 0,
        "registry": [],
        "project_context": {
            "project_name": project_name,
            "project_type": project_type,
            "research_objective": research_objective,
            "context_completeness": "INCOMPLETE",
        },
    }
    return save_project(project)


def delete_project(project_id):
    """Remove a project and everything under it. Used by tests and the UI."""
    directory = resources.projects_root() / project_id
    if directory.exists():
        shutil.rmtree(directory)
    _write_index([e for e in _read_json(resources.projects_index_path(), [])
                  if e.get("project_id") != project_id])


# ------------------------------------------------------- context + queries

def context_is_complete(project):
    return project["project_context"].get("context_completeness") == "COMPLETE"


def missing_context_fields(project):
    """Required schema fields the project still lacks. Drives the intake prompt."""
    required = (
        "project_name", "project_type", "research_objective",
        "business_decisions_pending", "target_market",
    )
    pc = project["project_context"]
    return [f for f in required if not (pc.get(f) or "").strip()]


def apply_context(project, incoming):
    """Merge a project_context returned by Agent 1's INTAKE response.

    Only known schema fields are accepted, and only non-empty values, so a
    partial intake cannot blank out what the creation form already captured.
    """
    pc = project.setdefault("project_context", {})
    changed = False
    for field in CONTEXT_FIELDS:
        value = (incoming.get(field) or "").strip()
        if value and value != pc.get(field):
            pc[field] = value
            changed = True
    if changed:
        project["project_name"] = pc.get("project_name") or project.get("project_name")
    return changed


def generate_query_id(project):
    """Mutate project in place; increment counter; return SZ-YYYYMMDD-NNN."""
    project["query_counter"] = project.get("query_counter", 0) + 1
    today = datetime.date.today().strftime("%Y%m%d")
    return f"SZ-{today}-{project['query_counter']:03d}"


def project_context_xml(project):
    """Render project_context fields as XML for inclusion in the system prompt."""
    pc = project["project_context"]
    fields = "\n".join(
        f"  <{key}>{pc[key]}</{key}>"
        for key in CONTEXT_FIELDS
        if pc.get(key) is not None and pc.get(key) != ""
    )
    return f"<project_context>\n{fields}\n</project_context>"


# -------------------------------------------------------------- migration

def migrate_legacy():
    """Move the single hard-coded project into the per-project layout.

    Idempotent, and deliberately non-destructive: the original state file and
    the repo's corpora/ files are left where they are. Running this twice, or
    on a fresh install with no legacy state, does nothing.
    """
    legacy = resources.legacy_state_file()
    if not legacy.exists() or project_exists(LEGACY_PROJECT_ID):
        return False

    old = _read_json(legacy, None)
    if old is None:
        return False

    now = _now()
    project = {
        "project_id": LEGACY_PROJECT_ID,
        "project_name": old.get("project_name") or "Weather Underground Redesign",
        "created_at": now,
        "last_opened_at": now,
        "query_counter": old.get("query_counter", 0),
        "project_context": old.get("project_context", {}),
        "registry": [],
        # Carried forward so the knowledge-base panel reads identically after
        # migration. The registry supersedes it once reference data lands.
        "display_names": old.get("display_names", {}),
        "migrated_from": str(legacy),
    }

    # Carry the founding corpus in as this project's first registered reference
    # asset. S-001 is the id it already has in the RAG registry.
    source = resources.resource("corpora", "corpus", "weather_underground.md")
    if source.exists():
        filename = "S-001-weather-underground-app-store-reviews.md"
        target = resources.reference_dir(LEGACY_PROJECT_ID, create=True) / filename
        if not target.exists():
            shutil.copyfile(source, target)
        project["registry"].append({
            "id": "S-001",
            "collection": "Situational",
            "file": filename,
            "title": (old.get("display_names", {}) or {}).get(
                "weather_underground.md", "WU AppStore Reviews"),
            "source_type": "app_store_reviews",
            "unit_prefix": "R",
            "added_at": now,
            "chars": target.stat().st_size,
            "strength": "anecdotal",
            "status": "EXISTS",
            "pre_annotated": True,  # already carries R01..Rn markers by hand
        })

    save_project(project)
    return True
