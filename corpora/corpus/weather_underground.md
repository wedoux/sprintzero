# Corpus — Weather Underground iOS App Store Reviews

**Project:** SprintZero — AI-augmented product discovery framework
**Case study:** Weather Underground iOS app — European market lens
**Sprint phase:** Problem Framing / Insight Evaluation

---

## 1. Data Limitations — Read Before Evaluating

> ⚠️ These constraints govern every verdict. They are not footnotes. Read them before touching the corpus.

- **Review date range:** 2020–2026. Pre-2023 reviews describe a different product version under different ownership. Weight recent reviews (2024–2026) more heavily. Do not treat 2020 and 2026 signals as equivalent.
- **Geographic bias:** All location signals are US-based. No EU-specific data exists in this corpus. Any EU conclusion requires an explicit transfer assumption to be stated and justified — not just flagged in passing.
- **Rating skew:** App Store reviews overrepresent dissatisfied users. The 3.9 average across 31k ratings suggests a large, silent majority not captured here.
- **Ownership context:** IBM acquired Weather Underground in 2015; The Weather Channel subsequently took operational control. Multiple complaints are about platform strategy decisions (feature removal, monetisation), not product quality. These are categorically different signals.
- **Review R13 date anomaly:** Dated 2026-12-02, which is future-dated relative to this file's creation (April 2026). Treat with caution. Do not use as a primary signal.
- **Review R12 rating:** Not provided by the reviewer. Do not infer sentiment from rating alone for this review.

---

## 2. Raw Signals — Structured Review Corpus

Each review is tagged with: [DATE] [RATING] [LOCATION SIGNAL] [BEHAVIOURAL SIGNAL IF PRESENT]

---

**R01**
- Date: 2020-07-22
- Rating: 4/5
- Location signal: Florida, US
- Behavioural signal: Daily active user despite complaints
- Text excerpt: *"Love the Doppler radar... The app was better when it didn't have so much 'stuff'... I still use the app daily because of the radar."*
- Key signal: Feature overload complaint, not accuracy. Retention despite frustration.

---

**R02**
- Date: 2023-02-26
- Rating: 4/5
- Location signal: Unspecified, US implied
- Behavioural signal: Continued use despite degraded experience
- Text excerpt: *"Since IBM took over in 2015 it has slowly chipped away the greatness of this App... NOAA Wx Radio ended, along with a Braille Page, Wx television show, API Feed, and the Blog page."*
- Key signal: Long-term feature erosion under IBM/Weather Channel ownership. Platform trust decline, not forecast accuracy.

---

**R03**
- Date: 2020-04-01
- Rating: 1/5
- Location signal: Unspecified, US implied
- Behavioural signal: None — passive acceptance of update
- Text excerpt: *"You still get accurate, hyper-local forecasts that are hard to beat."*
- Key signal: ⚡ COUNTER-SIGNAL. User explicitly defends forecast accuracy while rating 1/5 due to UI/UX changes, not data quality.

---

**R04**
- Date: 2020-09-08
- Rating: 2/5
- Location signal: Unspecified, US implied
- Behavioural signal: Implicit churn risk (*"fix the app quick before you lose a ton of users"*)
- Text excerpt: *"It no longer lists precipitation volume... the daily forecast with the temperature graph is now too wide... 1 in 12 men are color blind."*
- Key signal: UI degradation complaints. Accessibility concern raised (colour blindness). No accuracy complaint.

---

**R05**
- Date: 2023-01-31
- Rating: 1/5
- Location signal: Unspecified, US implied
- Behavioural signal: Deleted app after repeated reinstalls. Explicit churn.
- Text excerpt: *"For over 6 months this app only ever states that every day is 76 degrees... I've deleted and reinstalled the app more than 10 times. Did a factory reset."*
- Key signal: ⚠️ MISCLASSIFICATION RISK — This is a GPS/location data caching bug, not a forecast model failure. The app displayed stale cached data regardless of location. This is NOT evidence of forecast inaccuracy. High risk of being counted as an "accuracy" signal in error.

---

**R06**
- Date: 2020-05-08
- Rating: 1/5
- Location signal: Unspecified, US implied
- Behavioural signal: Explicit app abandonment during severe weather (*"I IGNORE YOUR APP"*)
- Text excerpt: *"It's tornado season. When a storm is coming, I IGNORE YOUR APP. I don't have time to go zoom-zoom with the pretty tachometer."*
- Key signal: Navigation friction causes safety-relevant abandonment. High-stakes use case degraded by UI complexity.

---

**R07**
- Date: 2020-04-01
- Rating: 1/5
- Location signal: Unspecified, US implied
- Behavioural signal: Explicit intent to find alternative (*"I am looking for a new weather app"*)
- Text excerpt: *"Daily summaries replaced by a conspicuous advert: 'Upgrade now to get 15 days of summaries' for $48/year... the Wundermap itself has been made less useful and visible."*
- Key signal: Monetisation strategy perceived as feature removal. Platform trust failure, not forecast quality.

---

**R08**
- Date: 2025-05-31
- Rating: 1/5
- Location signal: Unspecified, US implied
- Behavioural signal: Dedicated hardware abandoned (*"I dedicated an iPad; its only function was sitting on the countertop 24/7"*)
- Text excerpt: *"The Weather Channel bought the app, took away 3/4 of the features... Wunderground was like having a leased line to the National Weather Service."*
- Key signal: Power user churn. Extreme prior commitment (dedicated device) converted to complete abandonment. Institutional-grade data access was the core value proposition.

---

**R09**
- Date: 2026-01-28
- Rating: 4/5
- Location signal: Unspecified
- Behavioural signal: Multi-year reliance, continued use
- Text excerpt: *"I have relied on this app for years and keep hoping the developers will improve the automatic refresh when I change a location... I have to force a refresh by drilling down into a particular day."*
- Key signal: Location switching bug — same failure class as R05 (stale data on location change). UI workaround behaviour observed.

---

**R10**
- Date: 2025-12-29
- Rating: 2/5
- Location signal: Unspecified
- Behavioural signal: Continued use despite stated frustrations ("this is still my favorite")
- Text excerpt: *"This is still by far my favorite weather app despite it not being developed, rarely seeing updates, and having constant glitches... Have to close to reset and load frequently."*
- Key signal: Lock-in despite deterioration. No viable alternative perceived. Passive churn risk.

---

**R11**
- Date: 2025-11-12
- Rating: 4/5
- Location signal: Unspecified
- Behavioural signal: Continued use
- Text excerpt: *"The combined precipitation probability and amount charts, and the temp charts, for either daily or hourly, are the most useful and easy to understand at a glance."*
- Key signal: ⚡ POSITIVE SIGNAL — data visualisation praised. Counter-evidence to blanket UI degradation narrative.

---

**R12**
- Date: 2026-01-30
- Rating: Not provided
- Location signal: Unspecified
- Behavioural signal: Multi-app user — deliberate comparison behaviour
- Text excerpt: *"I use multiple weather apps daily due to my work. WU is my preferred app. I really like the weather stations as I can get a better and more detailed idea of the weather close to me."*
- Key signal: Hyper-local station data is the differentiated value. Multi-app behaviour suggests hedging, not loyalty.

---

**R13**
- Date: 2026-12-02 ⚠️ [FUTURE DATE — treat with caution]
- Rating: 4/5
- Location signal: Unspecified
- Behavioural signal: App freeze requiring force-close (~weekly)
- Text excerpt: *"About once a week the app is frozen with old info and either crashes after about 10 seconds or you have to force close the app."*
- Key signal: Stale data on freeze — same failure class as R05 and R09. Three reviews describe the same mode: stale/cached data after location change or app freeze. Do not treat as an independent signal until date anomaly is resolved.
