# Contributing to SprintZero

Thanks for looking. This started as coursework and is now a working prototype, so there is
real room to improve it — and a few things that are deliberate and worth understanding
before you change them.

## The one rule

**Every boundary gets a probe that fails loudly.**

This is not a testing preference, it is the reason the project works. Almost every failure
mode here is *silent*:

- a verdict that renders as valid when QA blocked it
- reference data that is registered but never reaches the prompt
- one project's evidence appearing in another project's synthesis
- an evidence citation that resolves to nothing
- a stored verdict that replays looking better than it did live

None of those throw an exception. None are visible in a screenshot. If you add a boundary,
add an assertion that fails with a message explaining *what the user would experience* —
not just what is technically wrong.

Compare:

```python
# Not useful
assert degraded is False

# Useful
violations.append(
    "DEGRADED VIOLATION: reasonless block rendered as a substantive QA-FAILED. "
    "Nothing was checked — it must not assert a finding."
)
```

Probes have earned their place repeatedly. During development they caught: a lookup that
created directories as a side effect, artefact filenames colliding within the same second,
a newly-created project whose workspace returned 500, and a stored failure that replayed
as a pass. Every one was invisible otherwise.

## Getting set up

```bash
python3 -m venv venv
./venv/bin/pip install -r requirements.txt
cp .env.example .env          # add your key (only needed to run the app, not the probes)
./venv/bin/python app.py      # http://127.0.0.1:5001
```

## Running the probes

**The eight offline probes need no API key and cost nothing.** Run these before every PR:

```bash
for p in _probe_design_tokens _probe_qa_gate _probe_signal_first_ia _probe_parse_retry \
         _probe_projects _probe_intake _probe_reference_data _probe_history; do
  ./venv/bin/python "$p.py" || echo "FAILED: $p"
done
```

These others **spend real money** on live API calls. Do not run them casually, and never in
CI:

| Probe | Cost |
|---|---|
| `_probe_streaming.py` | 2 generations (~2 min) |
| `_probe_qa_latency.py` | 2 per run, default 3 runs |
| `_probe_agent1_models.py` | 2 per candidate configuration |
| `_probe_phase4_full_flow.py` | 2 generations |
| `_probe_packaging.py` | Free, but builds and launches the bundle |

## Things that are deliberate

Please open an issue to discuss before changing any of these — they look like oversights
and are not.

**Agent 2 returns only `<qa_review>`; the server merges it.** This is what structurally
prevents the QA agent from rewriting the verdict it is reviewing. It stamps, it does not
re-synthesise. Letting it return the whole document would remove the guarantee.

**Evidence strength and QA status are separate colour axes.** Strength is neutral;
semantic colour is reserved for the gate. This came directly out of user research — the
old UI coloured a `WEAK` verdict like a failure, and surfacing weak evidence is the system
*working*. `_probe_design_tokens.py` fails the build if they merge again.

**History is not fed back into prompts.** Each verdict stays independently reproducible,
the prompt does not grow as a project accumulates history, and results do not depend on
the order themes were submitted.

**Both agents are pinned to `claude-opus-4-7`.** A newer model measured 2.4–3.2× slower
with truncated output, because thinking is on by default there and was off before. If you
want to change models, re-run `_probe_agent1_models.py` and put the numbers in the PR. See
[docs/DECISIONS.md](docs/DECISIONS.md).

**The QA agent's seven checks run in one call, in order.** The protocol says "in order".
Parallelising them would be roughly a 3× speedup and is genuinely tempting — but it is a
protocol change, not a refactor, and the guardrail is that QA depth is never traded for
speed. Worth discussing; not worth doing quietly.

## Good first contributions

- **PDF ingest.** Currently refused by name with an explanation. Text extraction plus the
  existing unit annotation would be a clean, self-contained addition.
- **The A-002 corpus annotation protocol.** Unit segmentation is blank-line splitting. A
  real annotation protocol — source-type-aware boundaries, per-unit metadata — is specified
  in the registry and never written. This is the highest-value open item.
- **Retrieval.** Every file is sent in full with every query. A retrieval step would let
  the tool handle an evidence base larger than a case study.
- **Export.** A verdict is a research artefact; there is no way to get one out as Markdown
  or PDF.
- **Windows and Linux packaging.** The desktop build is macOS-only (pywebview + `.icns`).

## Pull requests

1. Branch from `main`.
2. Run the offline probes; they must all pass.
3. Add or extend a probe if you touched a boundary.
4. Write the commit message for someone reading it in a year: what changed, and *why* it
   was worth changing. If a measurement informed it, include the numbers.
5. If behaviour changed, update the schema or protocol docs in the same PR. The prompts in
   `agents/prompts/` are contracts, and a contract that disagrees with the code is worse
   than no contract.

## Reporting a bug

Include what you expected, what happened, and whether any probe caught it. If the model
returned malformed output, the raw response is saved in `state/failures/` — attach it.

Please do not include your API key in an issue, and check that any project data you paste
is yours to share.

## Conduct

By participating you agree to the [Code of Conduct](CODE_OF_CONDUCT.md). Be decent; assume
good faith.
