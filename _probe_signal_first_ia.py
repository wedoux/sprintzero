"""Signal-first IA probe: layered hierarchy, with nothing lost on the way.

The restructure moved nine peer accordions into three tiers. The failure mode
that matters is silent content loss - a field that used to render and now does
not, which no visual check would catch. This probe renders a fully-populated
synthetic Agent 1 response and asserts:

  1. Signal-first ORDER  - QA band, verdict and lead signal precede the detail.
  2. NO CONTENT LOSS     - every field the flat layout rendered still renders.
  3. DEPTH ON DEMAND     - Tier 3 is collapsed; Tier 1 is not collapsible.
  4. CHIP INTEGRITY      - every Tier 2 chip target resolves to a real element.
"""
import re
import sys
import xml.etree.ElementTree as ET

import app

FULL = """<SprintZero_response>
  <attributes>
    <response_type>EVALUATION</response_type>
    <qa_status>QA_PENDING</qa_status>
  </attributes>
  <insight_under_evaluation><original_theme>MARKER_THEME</original_theme></insight_under_evaluation>
  <behavioural_mechanism>
    <behaviour>MARKER_BEHAVIOUR</behaviour>
    <trigger_condition>MARKER_TRIGGER</trigger_condition>
    <consequence>MARKER_CONSEQUENCE</consequence>
  </behavioural_mechanism>
  <verdict>
    <classification>UNCERTAIN</classification>
    <confidence_score>0.61</confidence_score>
    <stability_status>EMERGING</stability_status>
    <one_line_verdict>MARKER_ONELINE</one_line_verdict>
  </verdict>
  <evidence_chain>
    <corroborating_evidence>
      <unit><id>R01</id><signal>MARKER_CORR_ONE</signal></unit>
      <unit><id>R02</id><signal>MARKER_CORR_TWO</signal></unit>
    </corroborating_evidence>
    <counter_signals>
      <unit><id>R03</id><signal>MARKER_COUNTER</signal></unit>
    </counter_signals>
    <source_diversity>MARKER_DIVERSITY</source_diversity>
  </evidence_chain>
  <reasoning_step>
    <proposed_classification>MARKER_PROPOSED</proposed_classification>
    <counter_consideration>MARKER_COUNTERCONS</counter_consideration>
    <classification_commitment>MARKER_COMMITMENT</classification_commitment>
  </reasoning_step>
  <falsification_attempt>
    <falsification_query>MARKER_FALSQUERY</falsification_query>
    <falsification_result>SURVIVED</falsification_result>
    <falsification_evidence>MARKER_FALSEVIDENCE</falsification_evidence>
  </falsification_attempt>
  <transfer_assumption_check>
    <corpus_population>MARKER_CORPUSPOP</corpus_population>
    <target_population>MARKER_TARGETPOP</target_population>
    <structural_risks>MARKER_RISKS</structural_risks>
    <transfer_verdict>TRANSFER_UNCERTAIN</transfer_verdict>
    <corpus_required>MARKER_TRANSFERCORPUS</corpus_required>
  </transfer_assumption_check>
  <gap_flags>
    <gap>
      <gap_type>MARKER_GAPTYPE</gap_type>
      <gap_description>MARKER_GAPDESC</gap_description>
      <corpus_required>MARKER_GAPCORPUS</corpus_required>
    </gap>
  </gap_flags>
  <decision_support>
    <decision_this_changes>MARKER_CHANGES</decision_this_changes>
    <decision_this_enables>MARKER_ENABLES</decision_this_enables>
    <decision_this_cannot_support>MARKER_CANNOT</decision_this_cannot_support>
  </decision_support>
  <reframed_insight>
    <proposed_wording>MARKER_WORDING</proposed_wording>
    <diff_summary>MARKER_DIFF</diff_summary>
    <evidence_ids>MARKER_EVIDENCEIDS</evidence_ids>
  </reframed_insight>
</SprintZero_response>"""

root = ET.fromstring(FULL)
with app.app.app_context():
    from flask import render_template
    html = render_template(
        "partials/right_pane.html", root=root,
        response_type="EVALUATION", qa_checks=[],
    )

violations = []

# --- 1. Signal-first order --------------------------------------------------
def pos(needle, label):
    i = html.find(needle)
    if i == -1:
        violations.append(f"ORDER: {label} not found in the rendered pane ({needle!r}).")
    return i

i_band = pos('id="qa-band"', "QA band")
i_verdict = pos('class="verdict-banner', "verdict banner")
i_lead = pos('class="lead-signal"', "lead signal")
i_strip = pos('class="signal-strip"', "signal strip")
i_spine = pos('class="spine"', "Tier 3 spine")

if -1 not in (i_band, i_verdict, i_lead, i_strip, i_spine):
    order = [
        ("QA band", i_band), ("verdict", i_verdict), ("lead signal", i_lead),
        ("signal strip", i_strip), ("Tier 3 detail", i_spine),
    ]
    for (na, a), (nb, b) in zip(order, order[1:]):
        if a > b:
            violations.append(
                f"ORDER VIOLATION: {na!r} renders after {nb!r}. The pane must lead "
                "with the gate and the verdict, and put detail last."
            )

# --- 2. No content loss -----------------------------------------------------
markers = sorted(set(re.findall(r"MARKER_[A-Z_]+", FULL)))
for m in markers:
    if m not in html:
        violations.append(
            f"CONTENT LOSS: {m} rendered under the flat layout but is absent now. "
            "The restructure must relocate content, never drop it."
        )

# --- 3. Depth on demand -----------------------------------------------------
# Tier 3 cards must be collapsed; an <details open> defeats signal-first.
if re.search(r'<details[^>]*\bopen\b', html):
    violations.append("TIER 3 VIOLATION: a detail card renders open by default.")

# Tier 1 must not be collapsible at all.
band_block = html[i_band:i_strip] if -1 not in (i_band, i_strip) else ""
if "<details" in band_block:
    violations.append(
        "TIER 1 VIOLATION: the decision band contains a <details>. "
        "The verdict and gate must always be visible."
    )

# Every Tier 3 card is a details element.
n_cards = len(re.findall(r'<details class="spine-card', html))
if n_cards < 8:
    violations.append(f"TIER 3: expected at least 8 detail cards, found {n_cards}.")

# --- 4. Chip integrity ------------------------------------------------------
targets = re.findall(r'data-target="([^"]+)"', html)
if not targets:
    violations.append("TIER 2 VIOLATION: no signal chips rendered.")
ids = set(re.findall(r'id="([^"]+)"', html))
for t in targets:
    if t not in ids:
        violations.append(
            f"CHIP VIOLATION: chip targets {t!r} but no element carries that id. "
            "A chip that jumps nowhere is worse than no chip."
        )

# --- 5. Grouping ------------------------------------------------------------
groups = re.findall(r'class="tier3-group-label">([^<]+)<', html)
if len(groups) < 2:
    violations.append(
        f"GROUPING VIOLATION: Tier 3 has {len(groups)} group(s); the point of the "
        "restructure was to stop presenting peer accordions."
    )

print("===== SIGNAL-FIRST IA ASSERTIONS =====")
print(f"markers checked: {len(markers)} | cards: {n_cards} | "
      f"chips: {len(targets)} | groups: {groups}")
if violations:
    for v in violations:
        sys.stdout.write(f"FAIL: {v}\n")
    sys.exit(1)
print("PASS: signal-first order holds; no content lost; depth stays on demand.")
