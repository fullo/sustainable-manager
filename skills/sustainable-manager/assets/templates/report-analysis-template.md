# Sustainability Report Analysis — [Company name]

**Analysis type / Tipo di analisi:** Document Analysis + Greenwashing Detection
**Source document / Documento di origine:** [filename, pages read]
**Standard(s) recognized / Standard riconosciuti:** [GRI / ESRS / VSME / TNFD / none]
**Template version:** 1.0 — July 2026

---

> **How to use this template / Come usare questo modello**
>
> 1. This is the standard **output** format for analyzing an *existing* report — not for building one (for that, use `template-<sector>.md`).
> 2. **Anti-fabrication rule:** every figure in the KPI table MUST carry a page and a verbatim quote. If a metric is not in the document, it goes in *Missing disclosures*, never invented into the table.
> 3. Delete guidance notes (blockquotes starting with ">") before delivering.
> 4. Mirrors `assets/schemas/report-analysis-schema.json` — fill that JSON in parallel to feed charts and the comparative dashboard (`scripts/analysis_dashboard.py`).
> 5. All judgments are working drafts to review, not certifications.

---

## 1. At a glance / In sintesi

| Item | Detail |
|---|---|
| Reporting entity | [Company legal name / group perimeter] |
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

> Each row is source-anchored. `Page` = physical page in the file. For **Scope 2, report both market-based and location-based** when the document gives them (as separate rows) — a single Scope 2 figure hides a gap that can exceed 50%.

| Metric | Value | Unit | Page | Quote |
|---|---|---|---|---|
| Scope 1 | [value] | tCO2e | [p.] | "[verbatim quote]" |
| Scope 2 — location-based | [value] | tCO2e | [p.] | "[quote]" |
| Scope 2 — market-based | [value] | tCO2e | [p.] | "[quote]" |
| Scope 3 | [value / partial / absent] | tCO2e | [p.] | "[quote]" |
| Energy consumption | [value] | MWh / GWh | [p.] | "[quote]" |
| [Water / Waste / Workforce / …] | [value] | [unit] | [p.] | "[quote]" |

---

## 3. Completeness / Completezza

**Present / Presenti**
- [Disclosure present — e.g. Scope 1 & 2 both methods, GRI 305-1, double materiality]

**Missing (expected but absent) / Mancanti (attese ma assenti)**
- [Disclosure absent — e.g. Scope 3, external assurance, SBTi baseline & target, water withdrawal]

> What is absent is often more revealing than what is shown. Judge "missing" against the applicable framework and the sector's material topics — and verify an absence before asserting it (don't assume).

---

## 4. Greenwashing assessment / Valutazione greenwashing

**Overall risk / Rischio complessivo:** [🟢 Low / 🟡 Medium / 🔴 High]

| Claim | Rating | Page | Why |
|---|---|---|---|
| "[claim text]" | [Substantiated / Partially substantiated / Unsubstantiated / **Misleading**] | [p.] | [reason grounded in the data] |

> **Rating scale** (see `references/greenwashing-detection.md`):
> - **Substantiated** — specific metric, stated methodology, ideally third-party assurance.
> - **Partially substantiated** — data exists but incomplete, unverified, or lacking context.
> - **Unsubstantiated** — qualitative claim, no supporting data.
> - **Misleading** — data exists but is presented so as to create a false impression.
>
> Check the **reduce-before-offset** hierarchy and **relative-vs-absolute** (an intensity or market-based "−X%" headline while absolute location-based emissions grow).

---

## 5. Strengths & weaknesses / Punti di forza e debolezza

**Strengths / Punti di forza**
- [Strength 1]

**Weaknesses / Punti di debolezza**
- [Weakness 1]

---

## 6. Prioritized recommendations / Raccomandazioni prioritarie

1. [Most urgent, concrete next step — e.g. "Map Scope 3 cat. 1 with `scope3-mapper` (spend-based to start)"]
2. [Next]
3. [Next]

---

## 7. Independent verification / Verifica indipendente *(optional)*

> Fill this section **only** if a verification pass was actually run — e.g. `/adversarial-verify` or a self-check that re-opens each cited page against the source. The core skill does not orchestrate multi-agent verification by itself; leave the section out if no pass was done rather than implying one.
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
| Verification performed | [Yes / No] |
| Confidence | [0–100] |
| Hallucinations (values/pages not in the document) | [count] |
| Summary | [how reliable is this analysis?] |

**Issues found / Rilievi**
- [**Verdict** (confirmed / imprecise / refuted / unverifiable) · severity — claim → evidence: page, quote, real value]

---

*Sources & methodology / Fonti e metodologia:* analysis produced with the `sustainable-manager` skill following `references/greenwashing-detection.md`. Outputs are working drafts, not certified assessments — review with legal counsel and auditor.
