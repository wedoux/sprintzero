# Security Policy

## Scope

SprintZero is a single-user local prototype. It binds to `127.0.0.1`, has no
authentication, and runs Flask's development server. **It is not hardened for
multi-user or internet-facing deployment and should not be exposed to a network.**

## Handling of credentials

The application never stores an API key in the repository or in an application bundle.
Keys are resolved in this order:

1. `ANTHROPIC_API_KEY` from the environment (including a local, gitignored `.env`)
2. The macOS Keychain
3. A one-time prompt, whose answer is written to the Keychain

`_probe_packaging.py` walks the built macOS bundle on every build and fails if it finds a
key literal, a `.env` file, or a trace file. Please keep that probe passing.

## What gets written to disk

- `state/projects/` — your projects, reference data, and verdict history
- `state/failures/` — raw model output that failed to parse, kept for diagnosis
- `state/latency_trace.jsonl` — per-call timing and token counts

All three are gitignored. **`state/failures/` and your reference data may contain
whatever research material you loaded**, so treat that directory as sensitive and check
before sharing it.

## Reporting a vulnerability

Please do not open a public issue for a security problem. Report it privately through
GitHub's ["Report a vulnerability"](../../security/advisories/new) form, or contact the
maintainer through their GitHub profile.

Please include reproduction steps and what an attacker could achieve. Expect an initial
response within a week.

## Out of scope

Because this is a local single-user tool, the following are known and accepted:

- No authentication or authorisation
- Flask's development server rather than a production WSGI server
- The macOS app bundle is unsigned and unnotarised
- Prompt injection via reference data. Reference data is untrusted input that is placed in
  the model's context by design; the QA agent reviews reasoning, not content safety.
