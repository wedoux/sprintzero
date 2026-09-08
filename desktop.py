"""macOS entry point: SprintZero as a double-clickable app.

Mechanism: pywebview over the existing Flask server. The app is already a local
web app, so the bundle only needs a native window pointed at 127.0.0.1 — and
pywebview uses the OS's own WKWebView, shipping no second runtime. Tauri would
add a Rust toolchain and still have to ship Python; Electron would bundle
Chromium and Node on top of Python.

Order matters here. Credentials are resolved BEFORE app is imported, because
app.py constructs the Anthropic client at import time; resolving afterwards
would build a client with no key. Any startup failure is reported in a native
dialog rather than a traceback nobody will see — a bundled app has no console.
"""
import faulthandler
import os
import socket
import sys
import threading
import time
import traceback
from pathlib import Path


def log_path():
    """A bundled app has no console, so startup problems go to a file."""
    try:
        import resources
        directory = resources.STATE_ROOT
    except Exception:
        directory = Path.home() / "Library" / "Application Support" / "SprintZero"
    directory.mkdir(parents=True, exist_ok=True)
    return directory / "startup.log"


def log(message):
    try:
        with open(log_path(), "a") as f:
            f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}  {message}\n")
    except OSError:
        pass


def patch_slow_reverse_dns():
    """Stop the dev server hanging on a reverse-DNS lookup at bind time.

    http.server's server_bind() calls socket.getfqdn(host) after binding but
    before listen(). Inside the .app bundle that lookup blocks for tens of
    seconds, so the socket is bound, never listening, and the window opens onto
    a server that is not there — with no error anywhere, because nothing has
    failed. It was diagnosed with SPRINTZERO_DEBUG_STACKS.

    Only literal loopback addresses are short-circuited; every other name still
    goes to the real resolver. server_name is cosmetic for our purposes.
    """
    original = socket.getfqdn

    def getfqdn(name=""):
        if name in ("", "0.0.0.0", "127.0.0.1", "::1", "localhost"):
            return "localhost"
        return original(name)

    socket.getfqdn = getfqdn


def free_port():
    """Ask the OS for an unused port rather than assuming 5001 is available."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def fatal(message):
    """Report a startup failure where a user will actually see it."""
    try:
        import subprocess
        subprocess.run([
            "osascript", "-e",
            f'display alert "SprintZero could not start" message "{message}" as critical',
        ], timeout=60)
    except Exception:
        sys.stderr.write(f"SprintZero could not start: {message}\n")
    sys.exit(1)


def main():
    # A bundled app cannot be attached to with a debugger easily. Setting
    # SPRINTZERO_DEBUG_STACKS=<seconds> dumps every thread's stack to the log
    # after that delay, which is how the startup hang below was diagnosed.
    delay = os.environ.get("SPRINTZERO_DEBUG_STACKS")
    if delay:
        try:
            faulthandler.dump_traceback_later(
                float(delay), exit=False, file=open(log_path(), "a")
            )
        except (ValueError, OSError):
            pass

    patch_slow_reverse_dns()

    import credentials

    if credentials.resolve() is None:
        fatal("No Anthropic API key was provided, so SprintZero cannot run.")

    try:
        import webview
        from app import app as flask_app
    except Exception:
        fatal(
            "A required component failed to load. Details:\\n\\n"
            + traceback.format_exc()[-600:].replace('"', "'").replace("\n", "\\n")
        )
        return

    port = free_port()

    server_error = {}

    def serve():
        # threaded=True so the SSE endpoints do not block each other; debug and
        # the reloader must stay off inside a bundle. Werkzeug's own dev server
        # is fine here: this binds to loopback for a single local user.
        try:
            flask_app.run(host="127.0.0.1", port=port, debug=False,
                          use_reloader=False, threaded=True)
        except BaseException:
            # A daemon thread dying quietly is how a bundled app becomes a
            # window that never loads. Capture it and surface it.
            server_error["traceback"] = traceback.format_exc()
            log("server thread failed:\n" + server_error["traceback"])

    threading.Thread(target=serve, daemon=True).start()

    # Do not open a window onto a server that is not up. Poll the port rather
    # than sleeping a guessed interval.
    deadline = time.monotonic() + 25
    ready = False
    while time.monotonic() < deadline:
        if server_error:
            break
        try:
            with socket.create_connection(("127.0.0.1", port), timeout=0.4):
                ready = True
                break
        except OSError:
            time.sleep(0.15)

    if not ready:
        detail = server_error.get("traceback", "The server did not start within 25s.")
        log("startup failed: " + detail)
        fatal(
            "The local server did not start.\n\nDetails were written to:\n"
            + str(log_path())
        )
        return

    log(f"server ready on 127.0.0.1:{port}")

    webview.create_window(
        "SprintZero",
        f"http://127.0.0.1:{port}",
        width=1440,
        height=940,
        min_size=(1080, 720),
    )
    webview.start()


if __name__ == "__main__":
    main()
