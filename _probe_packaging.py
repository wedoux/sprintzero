"""Packaging probe: the bundle must be complete, and must contain no secrets.

Two independent failure modes, both silent:

  missing data  Templates, corpora and prompts are data, not imports, so
                PyInstaller does not collect them automatically. A missing file
                is not a build error - the app builds, launches, and dies on
                first use with a traceback nobody sees, because a bundled app
                has no console.

  leaked secret The hard guardrail. .env is gitignored, but nothing stops a
                spec entry or a stray copy from sweeping it into a bundle that
                then gets shared. This asserts the shipped app carries no
                credential of any kind.

Run after every build:  ./venv/bin/python _probe_packaging.py
"""
import os
import re
import sys
from pathlib import Path

BUNDLE = Path(__file__).parent / "dist" / "SprintZero.app"
RES = BUNDLE / "Contents" / "Resources"
MACOS = BUNDLE / "Contents" / "MacOS"

violations = []

if not BUNDLE.exists():
    sys.stdout.write(f"FAIL: no bundle at {BUNDLE}. Build it first:\n"
                     "      ./venv/bin/pyinstaller --noconfirm SprintZero.spec\n")
    sys.exit(1)

# --- 1. Required resources, at the paths resources.resource() will ask for ---
REQUIRED = [
    "templates/index.html",
    "templates/landing.html",
    "templates/partials/styles.html",
    "templates/partials/reference_panel.html",
    "templates/partials/verdict_banner.html",
    "templates/history.html",
    "templates/history_detail.html",
    "templates/partials/right_pane.html",
    "templates/partials/qa_surface.html",
    "templates/partials/verdict_invalidation.html",
    "templates/partials/chat_messages.html",
    "templates/partials/agent1_skeleton.html",
    "templates/partials/qa_skeleton.html",
    "agents/prompts/sprintzero_output_schema.xml",
    "agents/prompts/sprintzero_copilot_role_task.txt",
    "agents/prompts/qa_agent_protocol.md",
    "corpora/framework/evaluation.md",
    "corpora/corpus/weather_underground.md",
]
for rel in REQUIRED:
    # PyInstaller may place datas under Resources or beside the executable.
    if not ((RES / rel).exists() or (MACOS / rel).exists()):
        violations.append(
            f"MISSING RESOURCE: {rel} is not in the bundle. The app will fail "
            "at launch with no visible error."
        )

# --- 2. No secrets. The guardrail. -----------------------------------------
FORBIDDEN_FILES = (".env", ".env.local", "latency_trace.jsonl", "id_rsa", ".netrc")
KEY_RE = re.compile(r"sk-ant-[A-Za-z0-9_\-]{8,}")

scanned = 0
for root, dirs, files in os.walk(BUNDLE):
    dirs[:] = [d for d in dirs if d not in {"__pycache__"}]
    for name in files:
        path = Path(root) / name
        if name in FORBIDDEN_FILES:
            violations.append(
                f"SECRET LEAK: {path.relative_to(BUNDLE)} was bundled. "
                "The app must ship no credentials."
            )
        # Scan text-ish payload files for key material.
        if path.suffix.lower() in {".py", ".txt", ".md", ".xml", ".html", ".json",
                                   ".cfg", ".ini", ".env", ""} and path.stat().st_size < 4_000_000:
            try:
                blob = path.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue
            scanned += 1
            hit = KEY_RE.search(blob)
            if hit:
                violations.append(
                    f"SECRET LEAK: an Anthropic key literal appears in "
                    f"{path.relative_to(BUNDLE)}."
                )

# --- 3. The app must not have a hardcoded key anywhere in its own source ----
for src in Path(__file__).parent.glob("*.py"):
    if KEY_RE.search(src.read_text(encoding="utf-8", errors="ignore")):
        violations.append(f"SECRET LEAK: hardcoded key literal in {src.name}.")

# --- 4. Bundle basics -------------------------------------------------------
if not (BUNDLE / "Contents" / "Info.plist").exists():
    violations.append("BUNDLE: Info.plist missing.")
icons = list((BUNDLE / "Contents" / "Resources").glob("*.icns"))
if not icons:
    violations.append("BUNDLE: no .icns icon — the app will show a blank tile.")
if not (MACOS / "SprintZero").exists():
    violations.append("BUNDLE: no launchable executable at Contents/MacOS/SprintZero.")

# --- 5. It must actually serve. A complete bundle that hangs at startup is
#        still a broken app, and that is exactly what shipped the first time:
#        the socket bound, never listened, and nothing raised. ---------------
if not violations and os.environ.get("SPRINTZERO_SKIP_LAUNCH") != "1":
    import contextlib
    import subprocess
    import time
    import urllib.request

    env = dict(os.environ)
    # Deliberately NOT key-shaped: assertion 3 scans this very file for key
    # literals, and a realistic placeholder here would trip it. The launch
    # test never reaches the API, so any non-empty value works.
    env.setdefault("ANTHROPIC_API_KEY", "probe-placeholder-no-api-call-is-made")
    proc = subprocess.Popen(
        [str(MACOS / "SprintZero")],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, env=env,
    )
    served = None
    try:
        deadline = time.time() + 40
        while time.time() < deadline and served is None:
            time.sleep(1)
            out = subprocess.run(
                ["lsof", "-nP", "-iTCP", "-sTCP:LISTEN"],
                capture_output=True, text=True,
            ).stdout
            for line in out.splitlines():
                if "SprintZer" in line and "127.0.0.1:" in line:
                    port = line.split("127.0.0.1:")[1].split()[0]
                    with contextlib.suppress(Exception):
                        with urllib.request.urlopen(
                            f"http://127.0.0.1:{port}/", timeout=10
                        ) as r:
                            served = (r.status, r.read().decode("utf-8", "ignore"))
                    break
    finally:
        proc.terminate()
        with contextlib.suppress(Exception):
            proc.wait(timeout=10)

    if served is None:
        violations.append(
            "LAUNCH FAILURE: the bundle never served a page. It builds and runs "
            "but does not listen — check ~/Library/Application Support/SprintZero/"
            "startup.log, or re-run with SPRINTZERO_DEBUG_STACKS=8."
        )
    else:
        status, body = served
        print(f"launch test: bundle served HTTP {status}, {len(body):,} bytes")
        if status != 200:
            violations.append(f"LAUNCH FAILURE: bundle served HTTP {status}.")
        for marker in ("qa-band", "signal-strip", "tier3-group", "streamPhase"):
            if marker not in body:
                violations.append(
                    f"LAUNCH: served page is missing {marker!r} — the bundled "
                    "templates are stale or incomplete."
                )

print("===== PACKAGING ASSERTIONS =====")
print(f"bundle: {BUNDLE}")
print(f"required resources checked: {len(REQUIRED)} | files scanned for secrets: {scanned}")
if violations:
    for v in violations:
        sys.stdout.write(f"FAIL: {v}\n")
    sys.exit(1)
print("PASS: bundle is complete and carries no credentials.")
