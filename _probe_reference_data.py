"""Reference data probe: evidence must be registered, citable, and isolated.

Every claim this application makes is anchored to an evidence unit id, and the
reasoning cites those ids. Three ways that goes wrong, none of them visible in
the output:

  uncitable   Text ingested without unit ids means Agent 1 invents them. The
              citations look correct and resolve to nothing, which is worse
              than an obvious failure — it is a confident fabrication.
  unregistered A file on disk that no registry entry names is not evidence.
              The registry's own governance rule is that nothing enters the
              system unregistered; loading by directory listing would break it.
  cross-project A file added to one project appearing in another's synthesis is
              the worst failure this application can have.

Also asserts the ingest refusals — PDF, wrong type, oversized, empty — because
each of them silently produces garbage evidence if it gets through.

Free and deterministic — no model calls.
"""
import sys

import app
import reference
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


REVIEWS = """The forecast said sunny, it rained all afternoon.

Temperature is always about an hour behind reality.

Works fine for me, I check it every morning."""

NOTES = """Participant hesitated before trusting the widget.

They cross-checked with a second app before leaving the house."""

alpha = state.create_project("Ref Alpha", "NEW_PRODUCT", "Whether trust is the issue.")
beta = state.create_project("Ref Beta", "UNKNOWN", "Something else entirely.")
CREATED += [alpha["project_id"], beta["project_id"]]

# --- 1. Ingest, ids, and annotation ----------------------------------------
first = reference.ingest(alpha, "App Store reviews", "app_store_reviews", REVIEWS)
second = reference.ingest(alpha, "Interview notes", "interviews", NOTES)
state.save_project(alpha)

if [first["id"], second["id"]] != ["S-001", "S-002"]:
    violations.append(f"ASSET IDS: expected S-001/S-002, got {first['id']}/{second['id']}.")
if first["unit_count"] != 3 or second["unit_count"] != 2:
    violations.append(
        f"UNITS: expected 3 and 2 units, got {first['unit_count']} and {second['unit_count']}."
    )
if first["unit_prefix"] != "R" or second["unit_prefix"] != "INT":
    violations.append(
        f"PREFIX: source type did not drive the unit prefix; got "
        f"{first['unit_prefix']}/{second['unit_prefix']}."
    )

body = (resources.reference_dir(alpha["project_id"]) / first["file"]).read_text()
for expected in ("R01", "R02", "R03"):
    if f"### {expected}" not in body:
        violations.append(f"UNCITABLE: unit {expected} was not written into the asset.")
if "R04" in body:
    violations.append("UNITS: more unit ids were assigned than there were units.")
if "Data limitations" not in body:
    violations.append(
        "HONESTY: the data-limitations preamble is missing. Agent 1 must know "
        "the segmentation was mechanical before it leans on it."
    )
if body.index("### R01") > body.index("### R02"):
    violations.append("UNITS: unit ids are not in document order.")
print(f"1. ingest    : {first['id']}({first['unit_count']}×{first['unit_prefix']}) "
      f"{second['id']}({second['unit_count']}×{second['unit_prefix']})")

# --- 2. Registry and disk must agree ----------------------------------------
o = reference.orphans(alpha)
if o["missing_files"] or o["unregistered_files"]:
    violations.append(f"REGISTRY: registry and disk disagree: {o}.")

# A file nobody registered must not become evidence.
stray = resources.reference_dir(alpha["project_id"], create=True) / "stray-unregistered.md"
stray.write_text("# Not registered\n\nThis must never reach the prompt.")
loaded = reference.load_assets(alpha)
if any("Not registered" in a["content"] for a in loaded):
    violations.append(
        "UNREGISTERED: a file that no registry entry names was loaded as evidence."
    )
if reference.orphans(alpha)["unregistered_files"] != ["stray-unregistered.md"]:
    violations.append("REGISTRY: orphans() did not report an unregistered file.")
stray.unlink()
print(f"2. registry  : {len(loaded)} assets loaded, unregistered file ignored")

# --- 3. It must actually reach the prompt -----------------------------------
corpora = app.load_corpora(alpha)
prompt = "\n".join(b["text"] for b in app.build_system_blocks(corpora, alpha, "SZ-TEST-001"))
for marker in ("R01", "forecast said sunny", "INT01", "hesitated before trusting"):
    if marker not in prompt:
        violations.append(
            f"NOT IN PROMPT: {marker!r} is registered but never reaches Agent 1. "
            "The reference data would be invisible to the synthesis."
        )
if len(corpora["corpus"]) != 2:
    violations.append(f"LOADING: expected 2 corpus assets, got {len(corpora['corpus'])}.")
# The global framework must still be there — Agent 2 hard-requires it.
if not corpora["framework"]:
    violations.append("LOADING: the global framework asset disappeared.")
print(f"3. prompt    : corpus={len(corpora['corpus'])} framework={len(corpora['framework'])}")

# --- 4. Isolation ------------------------------------------------------------
beta_loaded = reference.load_assets(beta)
if beta_loaded:
    violations.append(
        f"CROSS-PROJECT LEAK: {len(beta_loaded)} of another project's assets are "
        "visible from a project that has none."
    )
beta_corpora = app.load_corpora(beta)
if beta_corpora["corpus"]:
    violations.append("CROSS-PROJECT LEAK: another project's evidence reached this corpus.")
if reference.next_asset_id(beta) != "S-001":
    violations.append("ISOLATION: asset id numbering is shared between projects.")
print(f"4. isolation : beta sees {len(beta_loaded)} assets, next id {reference.next_asset_id(beta)}")

# --- 5. Refusals -------------------------------------------------------------
class FakeUpload:
    def __init__(self, filename, blob):
        self.filename = filename
        self._blob = blob

    def read(self):
        return self._blob


for storage, why in (
    (FakeUpload("report.pdf", b"%PDF-1.4 binary"), "a PDF"),
    (FakeUpload("data.csv", b"a,b,c"), "a non-text extension"),
    (FakeUpload("", b"x"), "a nameless file"),
):
    try:
        reference.read_upload(storage)
        violations.append(f"REFUSAL: {why} was accepted.")
    except reference.IngestError as e:
        if why == "a PDF" and "PDF" not in str(e):
            violations.append("REFUSAL: the PDF message does not explain what to do.")

for args, why in (
    (("", "interviews", "text"), "an empty title"),
    (("T", "not_a_type", "text"), "an unknown source type"),
    (("T", "interviews", "   "), "empty text"),
    (("T", "interviews", "x" * (reference.MAX_ASSET_CHARS + 1)), "an oversized paste"),
):
    try:
        reference.ingest(beta, *args)
        violations.append(f"REFUSAL: {why} was accepted.")
    except reference.IngestError:
        pass

# A refused ingest must leave nothing behind.
if beta.get("registry"):
    violations.append("REFUSAL: a rejected ingest still registered an asset.")
if list(resources.reference_dir(beta["project_id"]).glob("*.md")):
    violations.append("REFUSAL: a rejected ingest still wrote a file.")
print("5. refusals  : pdf, wrong type, nameless, empty, oversized all refused cleanly")

# --- 6. Removal ---------------------------------------------------------------
path = resources.reference_dir(alpha["project_id"]) / first["file"]
removed = reference.remove(alpha, first["id"])
state.save_project(alpha)
if removed is None:
    violations.append("REMOVAL: removing a registered asset returned nothing.")
if path.exists():
    violations.append("REMOVAL: the asset file survived removal and still occupies disk.")
if any(e["id"] == first["id"] for e in alpha["registry"]):
    violations.append("REMOVAL: the registry entry survived removal.")
if any(a["asset_id"] == first["id"] for a in reference.load_assets(alpha)):
    violations.append(
        "REMOVAL: a removed asset is still loaded as evidence and would keep "
        "reaching the prompt."
    )
if reference.remove(alpha, "S-999") is not None:
    violations.append("REMOVAL: removing a nonexistent asset reported success.")
# The freed id must be reusable rather than silently colliding.
if reference.next_asset_id(alpha) != "S-001":
    violations.append(
        f"REMOVAL: freed id was not reused; next is {reference.next_asset_id(alpha)}."
    )
print(f"6. removal   : {first['id']} deregistered and deleted; next id "
      f"{reference.next_asset_id(alpha)}")

cleanup()

print("\n===== REFERENCE DATA ASSERTIONS =====")
if violations:
    for v in violations:
        sys.stdout.write(f"FAIL: {v}\n")
    sys.exit(1)
print("PASS: evidence is registered, citable, isolated per project, and")
print("      bad input is refused before it becomes evidence.")
