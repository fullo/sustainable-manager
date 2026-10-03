# Sustainability Report Analysis — [Company name]

**Analysis type / Tipo di analisi:** Document Analysis + Greenwashing Detection
**Source document / Documento di origine:** [filename, pages read — and which pages were read visually]
**Analysis date / Data dell'analisi:** [YYYY-MM-DD]
**Standard(s) recognized / Standard riconosciuti:** [GRI / ESRS / VSME / TNFD / none]
**Template version:** 1.2 — October 2026 (sustainable-manager v2.7.4; schema 1.2)

---

> **How to use this template / Come usare questo modello**
>
> 1. This is the standard **output** format for analyzing an *existing* report — not for building one (for that, use `template-<sector>.md`).
> 2. **Anti-fabrication rule:** every figure in the KPI table MUST carry a page and a verbatim quote. If a metric is not in the document, it goes in *Missing disclosures*, never invented into the table.
> 3. Delete guidance notes (blockquotes starting with ">") before delivering.
> 4. Mirrors `assets/schemas/report-analysis-schema.json` — fill that JSON in parallel to feed charts and the comparative dashboard (`scripts/analysis_dashboard.py`).
> 5. All judgments are working drafts to review, not certifications.
> 6. Keep the section order and the table columns as given, so that analyses can be compared automatically.

---

## 1. At a glance / In sintesi

| Item | Detail |
|---|---|
| Reporting entity | [Company legal name] |
| Perimeter | [legal entity / group (consolidated) / mixed — say which KPIs use which] |
| Sector | [Main activity] |
| Reporting period | [FY start — FY end] |
| Framework status | [**in accordance** / **with reference to** / *inspired by* / none] — *"inspired by ESRS" is NOT ESRS compliance* |
| External assurance | [Present — type / **Absent**] |

**Executive summary / Sintesi esecutiva**
- [Takeaway 1 — the single most important finding]
- [Takeaway 2]
- [Takeaway 3]

---

## 2. Key metrics extracted / KPI estratti

> Each row is source-anchored. `Page` = physical page in the file; if the figure appears on several pages list them (main page first); for spreads add the printed page in brackets. For **Scope 2, report both market-based and location-based** when the document gives them (as separate rows) — a single Scope 2 figure hides a gap that can exceed 50%. For table values quote the row label plus the cells in reading order, and make sure the quote contains the value. Quotes transcribed from a screenshot, map or scanned page: add *(image)* after the quote (schema `quote_source: "image"`). Reports using ISO 14064-1 categories: report the categories as published (mapping to Scopes in `references/greenwashing-detection.md`).

| Metric | Value | Unit | Page | Quote |
|---|---|---|---|---|
| Scope 1 | [value] | tCO2e | [p.] | "[verbatim quote]" |
| Scope 2 — location-based | [value] | tCO2e | [p.] | "[quote]" |
| Scope 2 — market-based | [value] | tCO2e | [p.] | "[quote]" |
| Scope 3 | [value, or partial: list categories covered] | tCO2e | [p.] | "[quote]" |
| Energy consumption | [value] | MWh / GWh | [p.] | "[quote]" |
| [Water / Waste / Workforce / …] | [value] | [unit] | [p.] | "[quote]" |

> If a metric (e.g. Scope 3) is absent → *Missing* in §3, never a row here.

**Derived values / Valori derivati** *(analyst calculation — not in the document, never in the KPI table)*
- [name: value — computed from: formula and pages, e.g. "Scope 1+2 = 8,504 + 2,338 = 10,842 (p.78)"]

---

## 3. Completeness / Completezza

**Present / Presenti**
- [Disclosure present — e.g. Scope 1 & 2 both methods, GRI 305-1, double materiality]

**Missing (expected but absent) / Mancanti (attese ma assenti)**
- [Disclosure absent — e.g. Scope 3, external assurance, SBTi baseline & target, water withdrawal]

> What is absent is often more revealing than what is shown. Judge "missing" against the applicable framework and the sector's material topics — and verify an absence before asserting it (don't assume): check image-only pages, screenshots, charts and scanned letters (e.g. assurance statements) first.

**Internal consistency / Coerenza interna**
- [Mismatch — p.X vs p.Y: what differs; analyst recalculation if any]

> Standard step: recompute totals and % changes from the report's own tables and compare figures repeated in highlights, tables, annexes and content index. Write "No inconsistencies found" if the check was done and found nothing.

---

## 4. Greenwashing assessment / Valutazione greenwashing

**Overall risk / Rischio complessivo:** [🟢 Low / 🟡 Medium / 🔴 High] — **rule applied:** [which rubric rule triggered the level]

| Claim | Rating | Page | Quote | Why |
|---|---|---|---|---|
| [short claim] | [Substantiated / Partially substantiated / Unsubstantiated / **Misleading**] | [p.] | "[verbatim quote]" | [reason grounded in the data; EmpCo item if relevant] |

> **Rating scale** (see `references/greenwashing-detection.md`):
> - **Substantiated** — specific metric, stated methodology, ideally third-party assurance.
> - **Partially substantiated** — data exists but incomplete, unverified, or lacking context.
> - **Unsubstantiated** — qualitative claim, no supporting data.
> - **Misleading** — data exists but is presented so as to create a false impression.
>
> Check the **reduce-before-offset** hierarchy and **relative-vs-absolute** (an intensity or market-based "−X%" headline while absolute location-based emissions grow).
>
> **Overall risk rubric** (definitions and full text in `references/greenwashing-detection.md`; apply in order, highest level triggered wins): 🔴 R1 Misleading *headline* claim on a *core* topic not corrected nearby · R2 offset-based claim ≥10% of reported emissions or presented as a headline · R3 tradeable credits without third-party validation/verification — 🟡 M1 any other Misleading · M2 offset-based claim below R2 · M3 ≥3 distinct Unsubstantiated outcome claims · M4 material internal inconsistency · M5 no assurance + material gap — 🟢 none of these. State the rule code, the triggering claims and, if arguable, the single fact that would flip the level.

---

## 5. Regulatory context / Contesto normativo (as of [date])

> One line per relevant act: applicability to *this* entity (perimeter, size, sector) and source. Use `eu-regulation-matrix/references/regulation-thresholds.md` and `references/efrag-updates.md`; say when a point is an assumption or not verified.

| Act | Status / dates | Applicability to the entity | Source |
|---|---|---|---|
| [e.g. CSRD as amended by Dir. (EU) 2026/470] | [in force 18/3/2026; transposition by 19/3/2027] | [out of scope: N employees, EUR X M — report is voluntary] | [skill reference / primary source] |
| [EmpCo — Dir. (EU) 2024/825, D.Lgs. 30/2026] | [applies since 27/9/2026] | [B2C claims at risk if reused in marketing] | [...] |

---

## 6. Strengths & weaknesses / Punti di forza e debolezza

**Strengths / Punti di forza**
- [Strength 1]

**Weaknesses / Punti di debolezza**
- [Weakness 1]

---

## 7. Prioritized recommendations / Raccomandazioni prioritarie

1. [Most urgent, concrete next step — e.g. "Map Scope 3 cat. 1 with `scope3-mapper` (spend-based to start)"]
2. [Next]
3. [Next]

---

## 8. Verification / Verifica

> Always state what was done. **Performed = Yes** only after an independent re-reading pass — `/adversarial-verify`, or a self-check that re-opens every cited page and re-derives every value and rating. Running `scripts/quote_check.py` (even with a visual look at some pages) is **not** a verification: write "Performed: No — automated quote check only" with the script result (found / image-sourced / failed / warnings) and leave Confidence, Hallucinations and Issues empty. The core skill does not orchestrate multi-agent verification by itself.
>
> **Want this confirmed by multiple independent agents?** For a report headed to a bank, an auditor, or a public disclosure, run an adversarial pass: several agents re-read the source as ground truth and try to refute each figure and claim (Chain-of-Verification). Install and run:
> ```
> claude plugin marketplace add fullo/claude-plugins-marketplace   # once, if not already added
> claude plugin install adversarial-verify@fullo-plugins
> /adversarial-verify
> ```
> Note this is **token-intensive** — each report is re-read in full by several agents, so one long report can cost tens of thousands of tokens and a multi-report benchmark hundreds of thousands. Best run on a plan with adequate capacity (e.g. Claude Max, or a raised usage limit).

| Item | Result |
|---|---|
| Verification performed | [Yes / No] — Yes only for adversarial-verify or a self-check re-opening every cited page |
| Method | [adversarial verify / self-check (pages re-opened) / automated quote check only / none] |
| Quote check | [e.g. 57/58 found in text, 1 image-sourced (manual check), 0 failed, 3 warnings] |
| Confidence | [0–100] |
| Hallucinations (values/pages not in the document) | [count] |
| Summary | [how reliable is this analysis?] |

**Issues found / Rilievi**
- [**Verdict** (confirmed / imprecise / refuted / unverifiable) · severity — claim → evidence: page, quote, real value]

---

*Sources & methodology / Fonti e metodologia:* analysis produced with the `sustainable-manager` skill following `references/greenwashing-detection.md`. Outputs are working drafts, not certified assessments — review with legal counsel and auditor.
