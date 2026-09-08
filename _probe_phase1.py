"""Phase 1 probe: exercise app.py's loader + Anthropic call path and print raw output."""
import sys

from app import MODEL, build_system_blocks, client, load_corpora

QUESTION = (
    "Evaluate this theme: Weather Underground users distrust the app's "
    "forecast accuracy because the displayed conditions feel stale."
)

corpora = load_corpora()
response = client.messages.create(
    model=MODEL,
    max_tokens=16000,
    system=build_system_blocks(corpora),
    messages=[{"role": "user", "content": QUESTION}],
)
text = next((b.text for b in response.content if b.type == "text"), "")
sys.stdout.write(text)
sys.stdout.write("\n")
