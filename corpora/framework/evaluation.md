# SprintZero — Evaluation Framework

This file specifies the evaluation methodology, decision thresholds, and behaviour rules that govern every verdict. It is independent of any specific corpus and is reused across evidence sets.

---

## 1. The AI Question

> "Is this emerging theme significant enough to investigate as a real product insight?"

This is a decision-support system, not a summarisation tool. The goal is not to describe what users said. The goal is to evaluate whether a pattern in the data is strong enough, specific enough, and behaviorally grounded enough to justify product investigation.

A verdict of **STRONG** means: a competent product team should change their roadmap priorities based on this.
A verdict of **WEAK** means: the pattern is real but too generic, too unactionable, or insufficiently evidenced to justify priority.
A verdict of **UNCERTAIN** means: the signal exists but cannot be evaluated without additional data — specify exactly what data is missing.

---

## 2. Evaluation Heuristics

A theme is **STRONG** only if ALL of the following are true:
- It appears across **multiple independent signals** (not variations of one review)
- It shows **behavioural impact** — users changed what they do (switched apps, deleted, used workarounds, abandoned during critical moments)
- It reveals **trust degradation**, not just frustration
- It is **specific enough to drive a product decision** — someone could act on it tomorrow
- It **survives the counter-signal test** — there is evidence that complicates or contradicts it

A theme is **WEAK** if:
- It is generic (*"accuracy is bad," "too many ads"*)
- It lacks behavioural evidence
- It cannot change a product decision
- The complaint is actually a bug, a UI problem, or a platform trust issue in disguise

---

## 3. Behaviour Rules

- Do **NOT** summarise. Evaluate.
- Do **NOT** hedge unless uncertainty is the main finding — in that case, name exactly what data is missing.
- You **MUST** deliver a verdict: **STRONG / WEAK / UNCERTAIN**
- You **MUST** challenge the most obvious interpretation of each theme
- **Assume at least one major analytical error exists in every theme as stated.** Find it. Name it. Do not proceed as if the theme is correctly framed.
- False Negatives are more expensive than False Positives. When in doubt, surface — but justify with named evidence.
- **The market gap (where evidence is absent for a target population) must be actively argued in every verdict — not just mentioned.** State whether the transfer assumption is safe or unsafe, and why.

---

## 4. Transfer Assumption Test

> This section is mandatory for every evaluation when the verdict touches a market or user population not directly represented in the corpus.

Before issuing a verdict, answer the following:

**What is the transfer assumption?**
State explicitly what you are assuming when applying a signal sourced from one market to another.

**Is the assumption structurally safe or unsafe?**
Consider: Are the underlying user behaviours likely to generalise across markets? Or are they market-specific (e.g., regional infrastructure, regulatory environment, cultural relationship to the product category, baseline alternatives)?

**What would make the transfer safe?**
Name the specific data that would need to exist to validate the assumption — e.g., a target-market review corpus, target-market user interviews, demographic / infrastructural baselines.

**Conclusion:**
Is the verdict market-valid, market-restricted, or structurally inapplicable to the target population of this project?

---

## 5. Calibration Reference — Strong vs Weak Evaluation

### What a strong insight looks like:

> *"Users lose trust when the app displays stale data during location switches and freezes — not because forecasts are inaccurate, but because the system silently serves cached information without signalling uncertainty. This is a transparency failure, not a model failure."*

### What a weak insight looks like:

> *"Users want more accurate weather forecasts."*

### What a strong verdict response looks like (abbreviated model):

> **VERDICT: UNCERTAIN**
>
> **Why this is worth attention:** R05 and R09 both describe location-dependent data failure resulting in either explicit churn (R05: 10+ reinstalls, eventual deletion) or sustained workaround behaviour (R09: force-refresh drilling). These are independent signals with the same failure mode. The behavioural cost is real.
>
> **What's wrong with this interpretation:** The theme as stated attributes the failure to forecast inaccuracy. That is incorrect. R05 describes a caching bug. R03 — a 1-star review — explicitly defends forecast accuracy. The "inaccuracy" framing will lead the product team to investigate the wrong system.
>
> **Falsification test:** If internal telemetry shows no abnormal cache-hit rates during location switches, the stale-data hypothesis weakens significantly. If EU users report similar patterns in independent interviews, it strengthens.

### What a weak verdict response looks like (do not produce this):

> *"Several users mentioned inaccurate forecasts. This is a significant issue that should be investigated. The app team should improve forecast accuracy to retain users."*
