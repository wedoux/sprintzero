"""API key resolution. Nothing here ever writes a key into the bundle.

Resolution order, first hit wins:

  1. ANTHROPIC_API_KEY in the environment  - unchanged for development, and the
     way CI or a wrapper script would inject one.
  2. The macOS Keychain                    - where the packaged app keeps it.
  3. A first-run prompt                    - asked once, then stored in (2).

The packaged .app therefore ships with no credential of any kind, and the key
is never written to disk in plaintext: the Keychain holds it, encrypted and
per-user. A .env file still works in development because app.py calls
load_dotenv() before this runs, which populates (1).

The prompt is a native macOS dialog rather than a webview form, because it has
to run before the Flask server starts - there is no page to render it in yet.
"""
import os
import subprocess
import sys

SERVICE = "SprintZero"
ACCOUNT = "anthropic-api-key"
ENV_VAR = "ANTHROPIC_API_KEY"


def _keyring():
    try:
        import keyring
        return keyring
    except ImportError:
        return None


def from_env():
    return (os.environ.get(ENV_VAR) or "").strip() or None


def from_keychain():
    kr = _keyring()
    if kr is None:
        return None
    try:
        value = kr.get_password(SERVICE, ACCOUNT)
    except Exception:
        return None  # locked or unavailable keychain is not fatal
    return (value or "").strip() or None


def store_in_keychain(api_key):
    kr = _keyring()
    if kr is None:
        return False
    try:
        kr.set_password(SERVICE, ACCOUNT, api_key)
        return True
    except Exception:
        return False


def clear_keychain():
    """Used when a stored key turns out to be invalid, so the app can re-ask."""
    kr = _keyring()
    if kr is None:
        return
    try:
        kr.delete_password(SERVICE, ACCOUNT)
    except Exception:
        pass


def prompt_for_key():
    """Native dialog. Returns the key, or None if the user cancelled."""
    script = (
        'display dialog "SprintZero needs an Anthropic API key.\\n\\n'
        'It is stored in your macOS Keychain and never written into the app."'
        ' default answer "" with hidden answer'
        ' with title "SprintZero" buttons {"Quit", "Save"} default button "Save"'
    )
    try:
        result = subprocess.run(
            ["osascript", "-e", script],
            capture_output=True, text=True, timeout=300,
        )
    except (OSError, subprocess.SubprocessError):
        return None
    if result.returncode != 0:
        return None  # user pressed Quit
    for part in result.stdout.strip().split(", "):
        if part.startswith("text returned:"):
            return part.split("text returned:", 1)[1].strip() or None
    return None


def resolve(allow_prompt=True):
    """Return an API key, or None. Also exports it so the SDK picks it up."""
    key = from_env() or from_keychain()

    if key is None and allow_prompt and sys.platform == "darwin":
        key = prompt_for_key()
        if key:
            store_in_keychain(key)

    if key:
        os.environ[ENV_VAR] = key
    return key
