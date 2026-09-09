"""Reference data: ingest, annotate, register.

Every claim SprintZero makes is supposed to be anchored to a named evidence
unit — the output schema requires each `evidence_chain` unit to carry an `<id>`,
and the reasoning cites those ids. The founding corpus has `R01…Rn` markers
written into it by hand. Pasted text has nothing.

Without unit ids, Agent 1 invents them: the citations look right and reference
nothing, which is worse than an obvious failure. So text is annotated at ingest.

The annotation is deliberately crude — split on blank lines, number in order,
prefix by source type. No chunking strategy, no embeddings, no semantic
boundaries. It exists to make citations resolvable, not to be clever, and the
file says so in a data-limitations preamble that Agent 1 reads. The prefixes
extend the convention the RAG registry already names (`R` for reviews,
`INT` for interviews).

The protocol that would make this rigorous — A-002, the corpus annotation
protocol — is registered as PLANNED and has never been written. This is the
minimum that keeps evidence traceable until it is.
"""
import datetime
import re

import resources

# Prefixes follow the registry's stated convention and extend it consistently.
SOURCE_TYPES = {
    "app_store_reviews": {"label": "App store reviews", "prefix": "R"},
    "interviews": {"label": "Interview transcript", "prefix": "INT"},
    "survey_responses": {"label": "Survey responses", "prefix": "SV"},
    "support_tickets": {"label": "Support tickets", "prefix": "TK"},
    "research_notes": {"label": "Research notes", "prefix": "N"},
    "other": {"label": "Other", "prefix": "U"},
}

ACCEPTED_EXTENSIONS = (".txt", ".md", ".markdown")

# The whole asset is placed in the system prompt — there is no retrieval step —
# so an oversized paste does not degrade quality, it costs money and latency on
# every single query against the project. Refuse it plainly instead.
MAX_ASSET_CHARS = 250_000


class IngestError(ValueError):
    """Raised with a message intended to be shown to the researcher."""


def _now_date():
    return datetime.date.today().isoformat()


def split_units(raw_text):
    """Blank-line separated blocks, in order, empties dropped."""
    return [b.strip() for b in re.split(r"\n\s*\n", raw_text or "") if b.strip()]


def next_asset_id(project):
    """Next S-nnn for this project. Situational is the per-project tier."""
    used = set()
    for entry in project.get("registry", []):
        match = re.match(r"^S-(\d+)$", entry.get("id", ""))
        if match:
            used.add(int(match.group(1)))
    n = 1
    while n in used:
        n += 1
    return f"S-{n:03d}"


def _slug(text):
    slug = re.sub(r"[^a-z0-9]+", "-", (text or "").lower()).strip("-")
    return slug[:50] or "reference"


def annotate(title, asset_id, source_type, raw_text):
    """Render an ingested document with stable, citable unit ids.

    The data-limitations preamble mirrors the founding corpus's own, and is
    there for Agent 1 as much as for the reader: it must know these boundaries
    were assigned mechanically before it leans on them.
    """
    spec = SOURCE_TYPES[source_type]
    prefix = spec["prefix"]
    units = split_units(raw_text)
    ids = [f"{prefix}{i:02d}" for i in range(1, len(units) + 1)]

    span = f"{ids[0]}–{ids[-1]}" if ids else "none"
    lines = [
        f"# {title}",
        "",
        f"- Asset id: {asset_id}",
        f"- Collection: Situational",
        f"- Source type: {spec['label']}",
        f"- Added: {_now_date()}",
        f"- Evidence units: {len(units)} ({span})",
        "",
        "## Data limitations — read before evaluating",
        "",
        "This asset was ingested as raw text. Evidence unit boundaries were "
        "assigned automatically at blank-line breaks and numbered in document "
        "order; they were not curated, and a unit may hold more or less than "
        "one coherent signal.",
        "",
        "Unit ids are stable and citable — use them in evidence_chain — but do "
        "not treat the segmentation itself as analysis. If a unit spans two "
        "distinct signals, say so rather than citing it as one.",
        "",
        "## Evidence units",
        "",
    ]
    for unit_id, body in zip(ids, units):
        lines.append(f"### {unit_id}")
        lines.append("")
        lines.append(body)
        lines.append("")
    return "\n".join(lines), ids


def ingest(project, title, source_type, raw_text, pre_annotated=False):
    """Annotate, write, and register one reference asset. Mutates `project`.

    Registration and the file write happen together on purpose: the registry's
    own governance rule is that nothing enters the system unregistered, and an
    entry pointing at a missing file is worse than no entry at all.
    """
    title = (title or "").strip()
    if not title:
        raise IngestError("Give the reference data a title.")
    if source_type not in SOURCE_TYPES:
        raise IngestError("Choose a source type.")

    raw_text = (raw_text or "").strip()
    if not raw_text:
        raise IngestError("There was no text to add.")
    if len(raw_text) > MAX_ASSET_CHARS:
        raise IngestError(
            f"That is {len(raw_text):,} characters. The limit is "
            f"{MAX_ASSET_CHARS:,} per file, because every reference file is sent "
            "in full with every query. Split it into smaller files."
        )

    units = split_units(raw_text)
    if not units:
        raise IngestError("There was no usable text to add.")

    asset_id = next_asset_id(project)
    body, unit_ids = annotate(title, asset_id, source_type, raw_text)
    filename = f"{asset_id}-{_slug(title)}.md"

    target = resources.reference_dir(project["project_id"], create=True) / filename
    target.write_text(body, encoding="utf-8")

    entry = {
        "id": asset_id,
        "collection": "Situational",
        "file": filename,
        "title": title,
        "source_type": source_type,
        "unit_prefix": SOURCE_TYPES[source_type]["prefix"],
        "unit_count": len(unit_ids),
        "added_at": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
        "chars": len(body),
        "strength": "anecdotal",
        "status": "EXISTS",
        "pre_annotated": pre_annotated,
    }
    project.setdefault("registry", []).append(entry)
    return entry


def read_upload(storage):
    """Decode one uploaded file, or raise a message worth showing.

    PDFs are refused by name rather than silently producing mojibake — a PDF
    read as text yields binary noise that would be cited as evidence.
    """
    filename = (storage.filename or "").strip()
    lower = filename.lower()
    if lower.endswith(".pdf"):
        raise IngestError(
            f"{filename} is a PDF. PDF support is not built yet — export it to "
            "plain text or Markdown and add that instead."
        )
    if not lower.endswith(ACCEPTED_EXTENSIONS):
        raise IngestError(
            f"{filename or 'That file'} is not a text file. Accepted: "
            f"{', '.join(ACCEPTED_EXTENSIONS)}."
        )
    blob = storage.read()
    try:
        return filename, blob.decode("utf-8")
    except UnicodeDecodeError:
        try:
            return filename, blob.decode("latin-1")
        except Exception:
            raise IngestError(f"{filename} could not be read as text.")


def remove(project, asset_id):
    """Deregister and delete one asset. Returns the entry, or None."""
    registry = project.get("registry", [])
    entry = next((e for e in registry if e.get("id") == asset_id), None)
    if entry is None:
        return None
    path = resources.reference_dir(project["project_id"]) / entry["file"]
    if path.exists():
        path.unlink()
    project["registry"] = [e for e in registry if e.get("id") != asset_id]
    return entry


def load_assets(project):
    """Registered assets, as {id, filename, title, content}.

    Driven by the registry, not by a directory listing: an unregistered file
    sitting in the folder is not evidence and must not reach the prompt.
    """
    out = []
    directory = resources.reference_dir(project["project_id"])
    for entry in project.get("registry", []):
        path = directory / entry["file"]
        if not path.exists():
            continue  # registry and disk disagree; the probe reports this
        out.append({
            "asset_id": entry["id"],
            "filename": entry["file"],
            "display": entry.get("title") or entry["file"],
            "content": path.read_text(encoding="utf-8"),
        })
    return out


def orphans(project):
    """Registry entries with no file, and files with no entry. For diagnostics."""
    directory = resources.reference_dir(project["project_id"])
    registered = {e["file"] for e in project.get("registry", [])}
    on_disk = {p.name for p in directory.glob("*.md")} if directory.exists() else set()
    return {
        "missing_files": sorted(registered - on_disk),
        "unregistered_files": sorted(on_disk - registered),
    }
