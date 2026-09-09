"""Project storage probe: isolation, migration, and the intake gate.

Storage went from one hard-coded project to many. Three things must hold, and
all three fail silently if they break:

  isolation   Two projects must not see each other's reference data, history,
              or query counter. A leak here would put one client's evidence in
              another client's synthesis, which is the worst failure this
              application can have.
  migration   The founding Weather Underground project must survive, keep its
              query counter, and arrive with its corpus registered. Migration
              must be idempotent and must not destroy the legacy file.
  intake gate A new project must start INCOMPLETE, because that is what makes
              Agent 1 run its intake protocol instead of evaluating against
              context nobody supplied.

Free and deterministic — no model calls. Test projects are cleaned up.
"""
import sys

import resources
import state

violations = []
CREATED = []


def cleanup():
    for pid in CREATED:
        try:
            state.delete_project(pid)
        except Exception:
            pass


# --- 1. Migration ----------------------------------------------------------
legacy = resources.legacy_state_file()
migrated_project = state.load_project(state.LEGACY_PROJECT_ID)

if legacy.exists():
    if migrated_project is None:
        violations.append(
            "MIGRATION: legacy state file exists but the project was not migrated."
        )
    else:
        if migrated_project.get("query_counter", 0) <= 0:
            violations.append(
                "MIGRATION: query_counter was not carried over; query IDs would "
                "restart and collide with existing history."
            )
        if not migrated_project["project_context"].get("research_objective"):
            violations.append("MIGRATION: project_context was not carried over.")
        registered = [r["id"] for r in migrated_project.get("registry", [])]
        if "S-001" not in registered:
            violations.append(
                f"MIGRATION: founding corpus not registered; registry has {registered}."
            )
        else:
            entry = next(r for r in migrated_project["registry"] if r["id"] == "S-001")
            asset = resources.reference_dir(state.LEGACY_PROJECT_ID) / entry["file"]
            if not asset.exists():
                violations.append(
                    f"MIGRATION: registry names {entry['file']} but the file is absent. "
                    "A registry entry with no file is worse than no entry."
                )
    if not legacy.exists():
        violations.append("MIGRATION: the legacy state file was destroyed.")
    if state.migrate_legacy():
        violations.append(
            "MIGRATION NOT IDEMPOTENT: a second run migrated again, which would "
            "overwrite a project that has since moved on."
        )
    print(f"1. migration : counter={migrated_project.get('query_counter')} "
          f"registry={[r['id'] for r in migrated_project.get('registry', [])]}")
else:
    print("1. migration : no legacy state file present — skipped")

# --- 2. Creation and the intake gate ---------------------------------------
a = state.create_project("Probe Alpha", "NEW_PRODUCT", "Find out whether X.")
CREATED.append(a["project_id"])

if state.context_is_complete(a):
    violations.append(
        "INTAKE GATE: a new project was marked COMPLETE. Agent 1 would skip "
        "intake and evaluate against context nobody supplied."
    )
missing = state.missing_context_fields(a)
if "business_decisions_pending" not in missing or "target_market" not in missing:
    violations.append(
        f"INTAKE GATE: missing_context_fields did not report the unasked required "
        f"fields; got {missing}."
    )
for field in ("project_name", "project_type", "research_objective"):
    if field in missing:
        violations.append(f"CREATION: {field} was captured by the form but reported missing.")
print(f"2. creation  : id={a['project_id']} complete={state.context_is_complete(a)} "
      f"missing={missing}")

# Validation must reject junk rather than storing it.
for bad_args, why in (
    (("", "NEW_PRODUCT", "obj"), "empty name"),
    (("Name", "NOT_A_TYPE", "obj"), "invalid project_type"),
    (("Name", "NEW_PRODUCT", "  "), "empty research objective"),
):
    try:
        p = state.create_project(*bad_args)
        CREATED.append(p["project_id"])
        violations.append(f"VALIDATION: {why} was accepted.")
    except ValueError:
        pass

# --- 3. Isolation ----------------------------------------------------------
b = state.create_project("Probe Beta", "EXISTING_PRODUCT_REDESIGN", "Find out whether Y.")
CREATED.append(b["project_id"])

if a["project_id"] == b["project_id"]:
    violations.append("ISOLATION: two projects share an id.")

# Same name must not collide onto the same directory.
c = state.create_project("Probe Alpha", "UNKNOWN", "A different objective entirely.")
CREATED.append(c["project_id"])
if c["project_id"] == a["project_id"]:
    violations.append(
        "ISOLATION: a duplicate project name reused the same id — the second "
        "project would overwrite the first."
    )

# Counters advance independently.
state.generate_query_id(a)
state.generate_query_id(a)
state.save_project(a)
qid_b = state.generate_query_id(b)
state.save_project(b)
if state.load_project(b["project_id"])["query_counter"] != 1:
    violations.append("ISOLATION: query counters are shared between projects.")
if not qid_b.endswith("001"):
    violations.append(f"ISOLATION: second project's first query id was {qid_b}.")

# Reference and history directories must not be shared.
for name, fn in (("reference", resources.reference_dir), ("history", resources.history_dir)):
    if fn(a["project_id"]).resolve() == fn(b["project_id"]).resolve():
        violations.append(f"ISOLATION: projects share a {name} directory.")

(resources.reference_dir(a["project_id"], create=True) / "leak-check.md").write_text("alpha only")
if list(resources.reference_dir(b["project_id"]).glob("*.md")):
    violations.append(
        "ISOLATION LEAK: a file written to one project's reference directory is "
        "visible from another's."
    )
print(f"3. isolation : {a['project_id']} / {b['project_id']} / {c['project_id']}")

# --- 4. Index and round-trip ------------------------------------------------
ids = [p["project_id"] for p in state.list_projects()]
for pid in (a["project_id"], b["project_id"], c["project_id"]):
    if pid not in ids:
        violations.append(f"INDEX: {pid} was created but is not listed.")

reloaded = state.load_project(a["project_id"])
if reloaded["project_context"]["research_objective"] != "Find out whether X.":
    violations.append("ROUND-TRIP: project_context did not survive save/load.")
if state.load_project("no-such-project") is not None:
    violations.append("LOOKUP: a missing project did not return None.")
# Reading must not write. Resolving a path used to mkdir it, so a mistyped URL
# left an empty directory behind that then read as a real project.
for probe_id in ("no-such-project", "../escape", "a/b", "also-not-real"):
    state.load_project(probe_id)
    state.project_exists(probe_id)
    resources.reference_dir(probe_id)
    resources.history_dir(probe_id)
    if (resources.projects_root() / probe_id).exists():
        violations.append(
            f"READ CREATED STATE: looking up {probe_id!r} created a directory. "
            "A mistyped project id would litter the store with empty projects."
        )
# Ids arrive from URLs once routing lands. A traversing id must be refused
# outright, not resolved to somewhere outside the project store.
for bad_id in ("../escape", "a/b", "..", "", "x" * 200):
    if state.project_exists(bad_id):
        violations.append(f"TRAVERSAL: {bad_id!r} was treated as an existing project.")
    if state.load_project(bad_id) is not None:
        violations.append(f"TRAVERSAL: {bad_id!r} loaded something.")

# --- 5. apply_context: the intake completion path ---------------------------
changed = state.apply_context(reloaded, {
    "business_decisions_pending": "Whether to fund workstream A or B.",
    "target_market": "UK small businesses.",
    "context_completeness": "COMPLETE",
    "research_objective": "",           # empty must not blank the existing value
    "not_a_schema_field": "ignore me",
})
if not changed:
    violations.append("APPLY CONTEXT: a real update reported no change.")
if reloaded["project_context"]["research_objective"] != "Find out whether X.":
    violations.append(
        "APPLY CONTEXT: an empty incoming value overwrote a field the creation "
        "form had already captured."
    )
if "not_a_schema_field" in reloaded["project_context"]:
    violations.append("APPLY CONTEXT: an unknown field was written into project_context.")
if not state.context_is_complete(reloaded):
    violations.append("APPLY CONTEXT: context_completeness was not applied.")
if state.missing_context_fields(reloaded):
    violations.append(
        f"APPLY CONTEXT: still missing {state.missing_context_fields(reloaded)} "
        "after a completing intake."
    )

xml = state.project_context_xml(reloaded)
if "<business_decisions_pending>" not in xml or "not_a_schema_field" not in xml:
    pass  # the field must be absent; checked below
if "not_a_schema_field" in xml:
    violations.append("XML: an unknown field leaked into the system prompt.")
if "<project_context>" not in xml or "</project_context>" not in xml:
    violations.append("XML: project_context_xml did not produce a wrapped element.")
print(f"4. context   : complete={state.context_is_complete(reloaded)} "
      f"xml_fields={xml.count('<') // 2 - 1}")

# --- 6. A brand-new project must actually open -------------------------------
# The workspace once hard-coded the founding project's filenames into its
# activity log, so every newly created project 500'd on render. Only a fresh
# project catches that; the migrated one carries the keys that hid it.
import app  # noqa: E402 - imported late so the probe can run state-only checks first

http = app.app.test_client()
fresh = state.create_project("Render Probe", "NEW_PRODUCT", "Whether the page renders.")
CREATED.append(fresh["project_id"])

response = http.get(f"/projects/{fresh['project_id']}")
if response.status_code != 200:
    violations.append(
        f"NEW PROJECT WORKSPACE: rendering a project with no reference data and "
        f"no display names returned {response.status_code}. A newly created "
        "project would be unusable."
    )
if http.get("/").status_code != 200:
    violations.append("LANDING: the project list failed to render.")
if http.get("/projects/definitely-not-real").status_code != 404:
    violations.append("ROUTING: an unknown project id did not 404.")
print(f"5. rendering : new project workspace {response.status_code}, landing 200")

cleanup()

print("\n===== PROJECT STORAGE ASSERTIONS =====")
if violations:
    for v in violations:
        sys.stdout.write(f"FAIL: {v}\n")
    sys.exit(1)
print("PASS: projects are isolated; migration preserved and idempotent;")
print("      new projects start INCOMPLETE so intake runs.")
