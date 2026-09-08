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


def read_text(*parts):
    return resource(*parts).read_text(encoding="utf-8")
