"""Filesystem locations that differ between the repo and the .app bundle.

Three things move when the app is frozen:

  read-only data  Prompts, corpora and templates ship inside the bundle, which
                  PyInstaller unpacks to a temp dir named by sys._MEIPASS. The
                  repo used bare relative paths ("corpora", "agents/prompts/…"),
                  which resolve against the working directory - and a
                  double-clicked .app inherits "/" as its working directory, so
                  every one of those reads would fail.

  writable state  The bundle is read-only and unpacked fresh on each launch, so
                  project state cannot live beside the code. It goes to
                  Application Support, which also means state survives an app
                  update.

  credentials     Never in the bundle. See credentials.py.
"""
import os
import sys
from pathlib import Path

FROZEN = getattr(sys, "frozen", False)

APP_NAME = "SprintZero"

# Read-only resources: the unpacked bundle when frozen, the repo otherwise.
BUNDLE_ROOT = Path(getattr(sys, "_MEIPASS", Path(__file__).parent)).resolve()

# Writable state: Application Support when frozen, the repo when developing so
# a dev run does not quietly diverge from what the installed app is reading.
if FROZEN:
    STATE_ROOT = Path.home() / "Library" / "Application Support" / APP_NAME
else:
    STATE_ROOT = Path(__file__).parent


def resource(*parts):
    """Absolute path to a read-only resource shipped with the app."""
    return BUNDLE_ROOT.joinpath(*parts)


def state_dir():
    """Writable directory for project state. Created on demand."""
    path = STATE_ROOT / "state"
    path.mkdir(parents=True, exist_ok=True)
    return path


def diagnostics_dir():
    """Where malformed model output is kept so a failure can be looked at later.

    Beside the state, so it follows the same repo-vs-Application-Support split:
    a failure during a live session is otherwise unrecoverable, because the raw
    output only ever existed in a browser pane.
    """
    path = STATE_ROOT / "state" / "failures"
    path.mkdir(parents=True, exist_ok=True)
    return path


# ---------------------------------------------------------------- projects
# Everything below is per-project writable state. It follows the same
# repo-vs-Application-Support split as state_dir(): a packaged app keeps its
# projects in Application Support, so they survive an app update, while a dev
# run keeps them in the repo. The two do not see each other, by design.


def projects_root():
    path = STATE_ROOT / "state" / "projects"
    path.mkdir(parents=True, exist_ok=True)
    return path


def projects_index_path():
    """The list of projects shown on the landing screen."""
    return STATE_ROOT / "state" / "projects.json"


# These four RESOLVE a path; they deliberately do not create it. Creating on
# read meant that merely looking up a project — including from a mistyped URL —
# left an empty directory behind that then looked like a real project. Writers
# create what they need; state._write_json already mkdirs its parent, and
# Path.glob on a missing directory returns nothing rather than raising.


def project_dir(project_id):
    return projects_root() / project_id


def reference_dir(project_id, create=False):
    """User-supplied reference data for one project."""
    path = project_dir(project_id) / "reference"
    if create:
        path.mkdir(parents=True, exist_ok=True)
    return path


def history_dir(project_id, create=False):
    """One record per evaluated theme."""
    path = project_dir(project_id) / "history"
    if create:
        path.mkdir(parents=True, exist_ok=True)
    return path


def legacy_state_file():
    """The single hard-coded project's state file, pre-multi-project.

    Named here rather than in state.py so the migration has one place to look
    and does not re-derive the old layout.
    """
    return STATE_ROOT / "state" / "weather-underground-redesign.json"


def read_text(*parts):
    return resource(*parts).read_text(encoding="utf-8")
