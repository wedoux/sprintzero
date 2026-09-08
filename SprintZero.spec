# -*- mode: python ; coding: utf-8 -*-
"""PyInstaller spec for the SprintZero macOS app.

The datas map below matters more than it looks. Every path here is laid out to
match what resources.resource() asks for at runtime, because PyInstaller does
not follow bare relative opens - templates, corpora and the agent prompts are
data, not imports, so nothing collects them automatically. A missing entry is
not a build error; it is a silent failure at launch, which is why the build is
verified by _probe_packaging.py rather than by eye.

keyring's macOS backend is imported dynamically and has to be named explicitly
for the same reason.
"""

block_cipher = None

a = Analysis(
    ["desktop.py"],
    pathex=[],
    binaries=[],
    datas=[
        # Read-only resources, at the paths resources.resource() expects.
        ("templates", "templates"),
        ("corpora", "corpora"),
        ("agents/prompts", "agents/prompts"),
        ("assets/icon.icns", "assets"),
    ],
    hiddenimports=[
        # Selected at runtime by keyring, so not visible to static analysis.
        "keyring.backends.macOS",
        "keyring.backends.chainer",
        "keyring.backends.fail",
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        # Build-time and measurement only - never needed by the shipped app.
        "PyInstaller",
        "PIL",
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="SprintZero",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,          # no terminal window behind the app
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name="SprintZero",
)

app = BUNDLE(
    coll,
    name="SprintZero.app",
    icon="assets/icon.icns",
    bundle_identifier="com.sprintzero.copilot",
    info_plist={
        "CFBundleName": "SprintZero",
        "CFBundleDisplayName": "SprintZero",
        "CFBundleShortVersionString": "0.1.0",
        "CFBundleVersion": "0.1.0",
        "NSHighResolutionCapable": True,
        # Talks only to 127.0.0.1 (its own Flask server) and the Anthropic API.
        "NSAppTransportSecurity": {"NSAllowsLocalNetworking": True},
        "LSMinimumSystemVersion": "11.0",
    },
)
