# SprintZero: notes for Claude Code

SprintZero is a reasoning-QA layer for UX research synthesis. Agent 1, the Research Copilot, produces a structured XML verdict. Agent 2, the QA Validation Agent, appends `<qa_review>` and can block that verdict. Start with `docs/ARCHITECTURE.md` and `docs/DECISIONS.md`.

**Current work:** v2, releases R0 and R1. The build spec is `docs/internal/v2-R0-R1-spec.md`. Read it before planning. `docs/internal/` is internal and gitignored: never quote it in commits, public docs or code comments.

## How we work
- **Plan first.** Before changing any file, state the plan and its reasoning, framed as act / don't act, then wait for Nikos to approve. Group small, related edits into one plan.
- **Prefer a testable slice to a comprehensive build.** If verification steps start to dominate the work, say so and propose a lighter path.
- **Never lose work.** Check `git status` first. Uncommitted changes belong to Nikos: ask before stashing, committing or discarding them.
- **Branches.** One branch per piece of work. Commit locally with imperative, sentence-style messages (see `git log`). **Never push, and never publish anything**, unless Nikos says so in this session.
- Author name on anything public: **Nikos Antonogiannis**.
- Spelling: British English in docs and UI copy (colour, licence, behaviour).

## Conventions in this repo
- Python app: `./venv/bin/python app.py`. Dependencies are in `requirements.txt` (runtime) and `requirements-build.txt` (packaging).
- **Probes:** `_probe_*.py` scripts are deterministic boundary tests with the model stubbed (no API calls). Run them with `./venv/bin/python _probe_<name>.py`; they also run in CI (`.github/workflows/probes.yml`). New behaviour gets a probe that fails loudly.
- **Prompts:** `agents/prompts/`. The schema (`sprintzero_output_schema.xml`) holds **structure only**. Behaviour rules go in `sprintzero_copilot_role_task.txt` (Agent 1) or `qa_agent_protocol.md` (Agent 2).
- **The model reasons; the app records provenance.** IDs, citations and history are written by code, never trusted from model output.
- **Decisions:** anything architectural gets a `D-0xx` entry in `docs/DECISIONS.md`, recording what was decided, why, and what was rejected.
- **API key:** `.env` or the macOS Keychain (`credentials.py`). Never print it or commit it. Before any live model run that costs money, give a token estimate and ask first.

## Attribution: hard rule
Parts of the v2 planning approach draw on a third-party, copyrighted research framework. The terms that must never appear in this repo or the skill repo are listed in §2, principle 8, of the spec. Use the plain wording the spec gives instead. Any credit line is added by Nikos himself, after he has cleared it with the framework's author. This file is public, so don't name the framework or its author here either.
