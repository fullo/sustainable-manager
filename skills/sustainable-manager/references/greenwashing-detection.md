# Greenwashing Detection & Critical Report Analysis

## Table of Contents
1. [What is Greenwashing](#what-is-greenwashing)
2. [EU Regulatory Context](#eu-regulatory-context)
3. [The Analysis Framework](#the-analysis-framework)
4. [Common Greenwashing Patterns](#common-greenwashing-patterns)
5. [Sector-Specific Red Flags](#sector-specific-red-flags)
6. [Claim Rating Methodology](#claim-rating-methodology)
7. [Report Completeness Checklist](#report-completeness-checklist)

---

## What is Greenwashing

Greenwashing is the practice of making misleading claims about the environmental or sustainability performance of a company, product, or service. It ranges from outright fabrication (rare) to selective disclosure, vague language, and misleading framing (very common).

The key question is always: **does the claim create an impression that is more favorable than the underlying data supports?**

---

## EU Regulatory Context

### Green Claims Directive (Proposal — pending, not adopted)
The Green Claims Directive proposal (COM(2023) 166, procedure 2023/0085) is pending but not withdrawn: it is listed among pending proposals in the Commission Work Programme 2026 and awaits the Council's first-reading position (status October 2026). It is not law — do not cite it as an applicable requirement. As proposed, it would require:
- **Substantiation**: Claims must be supported by widely recognized scientific evidence
- **LCA-based methodology**: Environmental claims about products require lifecycle assessment
- **Specific, not generic**: already law for B2C communication under EmpCo (see below); the proposal would add ex-ante substantiation and verification
- **Third-party verification**: Claims must be verified by an independent body
- **Transparency**: Methodology and underlying data must be accessible

### Unfair Commercial Practices Directive (Updated) — the operative rule
Directive (EU) 2024/825 (Empowering Consumers, EmpCo) applies since **27 September 2026** to business-to-consumer communication (Italy: D.Lgs. 30/2026, amending the Codice del Consumo). It bans, in B2C commercial practices (Annex I UCPD blacklist + new Art. 6(2)(d) UCPD):
- **Generic environmental claims** ("environmentally friendly", "eco-friendly", "green", "ecological", "climate friendly", "energy efficient", "biodegradable", "biobased"… — recital 9) without recognised excellent environmental performance relevant to the claim (e.g. EU Ecolabel, EN ISO 14024 type I schemes, top class under EU law). "Biodegradable" cannot rest on the EU Ecolabel unless its criteria cover biodegradability for that product (recital 10)
- **Claims, based on GHG offsetting, that a product has a neutral, reduced or positive GHG impact** ("climate neutral", "CO2 neutral certified", "climate compensated", "reduced climate impact" — recital 12). Such claims are allowed only when based on the product's actual lifecycle impact. Advertising investments in carbon-credit projects remains allowed if not misleading and not presented as product neutrality. The item concerns GHG and products: biodiversity credits are not covered by this specific item — assess them under the general misleading-action rules
- **Sustainability labels** not based on a certification scheme (third-party verification, publicly available terms, independent monitoring) or established by public authorities
- **Whole-product / whole-business claims** when the claim concerns only a certain aspect or activity
- **Claims on future environmental performance** ("net zero by 2050", "carbon neutral by 2035") without clear, objective, publicly available and verifiable commitments set out in a detailed and realistic implementation plan with measurable, time-bound targets and allocated resources, regularly verified by an independent third-party expert whose findings are made available to consumers (new Art. 6(2)(d) UCPD)

**Scope note**: EmpCo applies to commercial communication to consumers. A sustainability report is not per se advertising, but the same claims reused on websites, packaging, apps or campaigns are in scope; B2C-heavy companies (or public-service providers whose users are consumers) are most exposed. Content published before 27 September 2026 and still online: treat it as assessed at the time it is made available — this is an interpretation to be confirmed by legal counsel, not a rule stated in the Directive.

### CSRD/ESRS Anti-Greenwashing
ESRS reporting itself acts as an anti-greenwashing mechanism:
- Mandatory double materiality assessment prevents cherry-picking topics
- Standardized metrics enable comparison
- External assurance requirement (limited assurance; the planned move to reasonable assurance was dropped by Directive (EU) 2026/470)
- Digital taxonomy (XBRL) enables automated verification

---

## The Analysis Framework

When evaluating a sustainability report or claim, work through these layers:

### Layer 1: Data Verification
For every quantitative claim, check:
- Is there a specific number with units and year?
- Is there a baseline year for comparison?
- Is the methodology stated? (GHG Protocol, ISO 14064, LCA standard)
- Is the scope clear? (Scope 1 only? Scope 1+2? Full Scope 3?)
- Is there year-over-year data showing the trend?
- Has the data been externally assured? By whom? (Check image-only pages: assurance letters are often scanned images)
- **Internal consistency**: do totals add up and % changes match the report's own tables? Are figures repeated in highlights, tables, annexes and content index identical? Record every mismatch with both pages (template §3, schema `data_quality_flags`); recomputed values are "analyst calculation", never KPIs

### Layer 2: Completeness Assessment
What's present vs. what's missing:
- All three GHG scopes reported?
- Material topics identified through formal materiality assessment?
- Negative trends disclosed alongside positive ones?
- Targets with base year, milestone years, and final target year?
- Governance structure for sustainability oversight?
- Executive compensation linked to sustainability KPIs?

### Layer 3: Claim-Data Alignment
Does the narrative match the numbers?
- "Carbon neutral" but emissions are rising → misleading
- "Water positive" but no data on actual water consumption → unsubstantiated
- "Net zero by 2050" but no near-term targets → aspirational, not science-based
- "Sustainable packaging" but no LCA data → vague

### Layer 4: Science Alignment
Are the claims aligned with scientific consensus?
- Are targets SBTi-approved or just self-set?
- Does the reduction pathway match 1.5C / well-below 2C?
- Is the hierarchy respected (reduce > substitute > compensate)?
- Are offsets/removals used for residual emissions only, or as primary strategy?
- Are planetary boundaries referenced for non-climate impacts?

### Layer 5: Comparability
Can the claims be meaningfully compared?
- Which reporting framework is used? (GRI, ESRS, SASB, none?)
- Are metrics standardized or proprietary?
- Are boundaries consistent across years?
- Are restatements of historical data disclosed?

---

## Common Greenwashing Patterns

### 1. The Offset Illusion
**Pattern**: "Carbon neutral" or "net zero" achieved primarily through purchased offsets or carbon credits rather than emission reductions.

**Detection**: Compare absolute emissions trend with offset volume. If emissions are flat or rising while "neutrality" is claimed, offsets are doing the heavy lifting.

**Science check**: SBTi Net-Zero Standard allows offsets for maximum 10% residual emissions after 90%+ reduction. Anything beyond that is not science-aligned.

### 2. The Intensity Trick
**Pattern**: Reporting emission/energy/water intensity (per unit revenue, per employee, per product) that improves, while absolute impacts grow.

**Detection**: Always ask for both absolute and intensity metrics. A company growing 20% with 10% intensity improvement has still increased absolute impacts by 8%.

**When intensity is legitimate**: For comparing operational efficiency across companies of different sizes, or tracking decoupling progress. But it should never replace absolute metrics.

### 3. The Scope Gap
**Pattern**: Reporting only Scope 1 and 2 emissions (direct and purchased energy) while ignoring Scope 3 (value chain), which typically represents 70-90% of total emissions for most sectors.

**Detection**: Check if Scope 3 is reported. If not, the total carbon picture is fundamentally incomplete. For manufacturing, retail, finance, and tech sectors, Scope 3 dominance is well-established.

### 4. The Cherry-Pick
**Pattern**: Highlighting the best-performing metric while hiding underperformance elsewhere.

**Detection**: Look at all ESG dimensions, not just the ones the company emphasizes. A company with excellent environmental metrics may have poor social or governance performance. Cross-reference with the materiality assessment.

### 5. The Future Promise
**Pattern**: Bold long-term targets (2030, 2040, 2050) with no near-term milestones, no current baseline, and no credible pathway.

**Detection**: Check for:
- Near-term targets (2025-2030) with specific milestones
- Capex allocated to the transition
- Governance accountability for targets
- Annual progress reporting

### 6. The Anecdote Scale-Up
**Pattern**: Showcasing one flagship project, facility, or initiative and implying it represents the whole company.

**Detection**: Is the showcased project representative? What percentage of operations does it cover? Is there company-wide data alongside the case study?

### 7. The Vague Commitment
**Pattern**: Using qualitative language that sounds good but commits to nothing measurable: "committed to", "working toward", "aspire to", "believe in".

**Detection**: For every qualitative claim, ask: what's the KPI? What's the target? By when? Without these, it's a statement of intent, not a commitment.

### 8. The Misleading Comparison
**Pattern**: Comparing against a carefully chosen baseline year (often a peak year) to inflate improvement, or comparing against worst-in-class rather than best practice.

**Detection**: Is the baseline year justified? What happened in that year? Compare against industry averages and science-based benchmarks rather than company-selected baselines.

---

## Sector-Specific Red Flags

### Technology / Cloud / AI
- Datacenter energy consumption growing while claiming carbon neutrality
- Scope 3 from hardware manufacturing and end-of-life not reported
- Water use for cooling not contextualized against local water stress
- AI training energy costs excluded or minimized
- "100% renewable energy" via RECs without additionality

### Finance / Banking
- Financed emissions (Scope 3 Category 15) not reported
- "Green" portfolio highlighted while fossil fuel exposure hidden
- ESG fund claims without robust exclusion criteria
- Climate scenario analysis without portfolio-level impact

### Manufacturing / Industry
- Scope 3 upstream (raw materials) underreported
- Pollution metrics limited to regulated substances only
- Circular economy claims without material flow data
- Worker safety data excludes contractors or value chain

### Food & Agriculture
- Land use change emissions from supply chain omitted
- Water footprint in water-stressed agricultural regions not assessed
- Biodiversity impacts from sourcing not measured
- "Sustainable sourcing" claims without certification evidence

### Cross-sector checks (apply where relevant to the activity)
- Operational energy (plants, networks, data centres, fleets) not reported separately from offices or shops; no intensity metric tied to the activity's own output unit
- Use-phase energy of products sold (Scope 3 cat. 11) or leased/lent to customers (usually cat. 13, downstream leased assets) omitted — check the report's classification
- Outsourcing, asset sharing or divestments moving emissions out of the perimeter without saying so
- Avoided emissions (e.g. from recycling or substitution) presented as reductions of the inventory: they are not
- Different rate metrics mixed (e.g. collection rate vs recycling rate vs recovery rate): report each as defined in the document
- Packaging and logistics: check Scope 3 cat. 1, 4, 9 and 12 where they are likely material; recycled-content, "returnable" or "biodegradable" claims need share and scope (EmpCo whole-product rule; PPWR)
- "Trees planted" / offsets presented as absorption of the year's emissions (EmpCo bans offset-based product claims of neutral, reduced or positive GHG impact)
- Public ownership does not by itself exempt an entity from CSRD: scope depends on size (Dir. (EU) 2026/470: more than 1,000 employees and more than EUR 450M turnover). Below the thresholds the report is voluntary: check the declared standard, the assurance and the perimeter
- Forest-risk inputs (paper, wood, other EUDR commodities): FSC/PEFC certification is not EUDR due diligence; check Annex I scope by CN code (see `eu-regulation-matrix/references/regulation-thresholds.md` §6)

### Legal-form impact reports and private labels
- Società Benefit publish an annual impact report assessed against an external standard (L. 208/2015, art. 1, commi 376-384: report attached to the financial statements and published on the company website, if one exists (c. 383), impact assessed with an external standard per Annexes 4-5 (c. 382-383); an SB not pursuing its common-benefit aims falls under the misleading-advertising rules and the Codice del consumo (c. 384)): it is not a CSRD/VSME report; assess it with this checklist
- Private certification marks: under EmpCo (Annex I pt 2a UCPD) a sustainability label may be displayed only if based on a certification scheme meeting the Directive's definition or established by public authorities; whether a given private mark (e.g. B Corp) meets it is an assessment, and the other UCPD rules still apply — check before treating it as evidence

### ISO 14064-1 vs GHG Protocol
Reports using ISO 14064-1:2018 categories map approximately as: **Cat. 1 ≈ Scope 1**; **Cat. 2 ≈ Scope 2** (check which basis, market or location, is stated); **Cat. 3-6 ≈ Scope 3** (map to the 15 GHG Protocol categories). Report the categories as published and note the mapping as an analyst interpretation.

### Energy audit (Italy)
Large companies must carry out an energy audit every four years under art. 8 D.Lgs. 102/2014 (exempt from periodicity if an ISO 50001 system includes it; large companies consuming less than 50 toe/year are exempt, c. 3-bis; energy-intensive companies (energivori) are obliged regardless of size, c. 3; results communicated to ENEA). A report citing it gives an energy baseline; absence in a large company is a gap.

### Fashion / Textiles
- Microplastic emissions not quantified
- Chemical management limited to final product (not production process)
- Living wage claims without third-party verification across supply chain
- "Recycled material" percentage at product vs. company level

---

## Claim Rating Methodology

Rate each claim on a 4-level scale:

### Substantiated
- Backed by specific, quantitative data with clear methodology
- Third-party verified or audited
- Consistent with recognized scientific evidence
- Trend data available showing trajectory
- Example: "Scope 1+2 emissions reduced 42% vs. 2019 baseline (SBTi-approved target, assured by Deloitte)"
- Assurance is not required when the claim is fully traceable in the document (figure, method, perimeter, basis and baseline all stated and recomputable): rate it Substantiated and note "not assured"

### Partially Substantiated
- Some data exists but incomplete or unverified
- Methodology stated but not externally assured
- Missing context (no baseline, no scope boundary, no trend)
- Example: "Reduced emissions by 20%" (but no scope, no baseline year, no assurance)

### Unsubstantiated
- Qualitative claim with no supporting data
- No methodology, no metrics, no verification
- Example: "We are committed to sustainability" or "We believe in a green future"

### Misleading
- Data exists but is presented in a way that creates a false impression
- Selective disclosure that hides material information
- Metrics that technically improve while underlying reality worsens
- Example: "Carbon neutral since 2020" (via offsets while absolute emissions increased 30%)

### Overall Risk Rubric
Aggregate the claim ratings into one overall greenwashing risk. Apply the definitions and steps below in order; the result is the highest level triggered. Do not override the result with an overall impression: if you disagree, keep the rubric level and say why in the note.

**Definitions**
- **Headline claim**: a claim on the cover, the highlights / key-figures pages, the CEO or chair letter, the executive summary, a KPI box or infographic, or a product, brand or marketing claim; also any claim repeated in two or more sections (the same claim, not merely a related theme). Every other claim (body text, tables, notes) is a **body claim**. **Short documents (≤5 physical pages)**: every claim in the summary, KPI box/table or title counts as headline; if the document has none of these, every claim on its first page does.
- **Core topic**: (i) GHG emissions / climate — always core; (ii) the topic of the entity's main revenue-generating activity (e.g. the resource it supplies, the material it processes, the service it sells; for a project document, the subject of the project) — always core, **even when the report's own materiality ranking places it outside the top 3**; (iii) the report's own top-3 material topics (by its materiality ranking; if it does not rank them, the topics it places in the highest-impact group). A topic is core if any of (i)-(iii) applies.
- **Quantitative vs narrative**: a quantitative claim states a number, percentage, ranking or measurable outcome. A narrative claim that asserts an **absolute** environmental outcome ("zero waste", "nothing is wasted", "100% green", "climate neutral", "impatto zero", "devoid of habitat") is treated as quantitative (it implies 0% or 100%). Other narrative claims (values, commitments, generic adjectives) can be Unsubstantiated but never Misleading.
- **Corrected nearby**: the report itself gives the data that dispels the false impression (the other basis, the absolute figure, the baseline, the perimeter) on the same page, in the same table or infographic, or within 2 physical pages in the same section, or the claim explicitly points to that table. "Within 2 pages" is **inclusive** and counted on physical pages (the PDF page index): |page of claim − page of correction| ≤ 2 (claim p.48, correction p.50 → corrected nearby; p.51 → not). For spreads (2 printed pages per physical sheet) count physical sheets, not printed page numbers; never mix the two.
- **Offset-based claim**: a neutrality, "net zero", "compensated", "offset", "absorbed" or "climate positive" claim that rests on credits, offsets, tree planting or removals rather than on reductions in the inventory — including compensation performed by a supplier (e.g. "fuel compensated by the supplier") and claimed by the entity. A **future** neutrality target is offset-based only if the document says the target will be met in part through credits, offsets or removals (a quantity is not needed); a parallel initiative on sinks or tree planting not stated as a means to meet the target does not make it offset-based — rate the target as a future-performance claim (EmpCo). **Offset share** = quantity compensated / total emissions reported for the same year (Scope 1 + 2 + the Scope 3 categories reported). A neutrality claim covers by definition the whole claimed perimeter (share = 100% of that perimeter).
- **Credits "claimed" (R3)**: credits or certificates count as claimed when the document presents a quantity of them (calculated, generated, accrued, "eligible", "obtainable") as an outcome, result or asset of the project or entity — whether or not they have been issued on a registry, sold or retired. **Exception**: a calculation explicitly labelled as an illustrative estimate or simulation, with a statement that no credit is or will be issued, sold or used for any claim, is not "claimed". "Without third-party validation/verification" = the document names no validation/verification body and no accredited scheme for those credits (absence of evidence counts as absence). R3 concerns credits generated or issued by the entity or project; credits **purchased** from third parties and retired to support a claim are assessed under R2/M2, and trigger R3 only if the document shows they are not certified under any named scheme (e.g. "self-certified", "internal credits").

**Step 1 — 🔴 High** if any of:
- (R1) a Misleading claim that is a headline claim on a core topic and is **not** corrected nearby;
- (R2) an offset-based claim whose offset share is ≥10%, or that is a headline claim (if the share cannot be computed from the report, apply R2 only when the claim is a headline claim, and say which denominator is missing);
- (R3) tradeable credits or certificates (carbon, biodiversity, plastic…) issued, sold or claimed without third-party validation/verification (e.g. an ISO/IEC 17029 V&V body or the scheme's accredited verifier).

**Step 2 — 🟡 Medium** if no 🔴 trigger and any of:
- (M1) any other Misleading claim (body claim, non-core topic, or headline claim corrected nearby);
- (M2) an offset-based claim below the R2 threshold;
- (M3) 3 or more distinct Unsubstantiated claims asserting an outcome (the same generic wording repeated on several pages counts once; pure statements of values or intent do not count);
- (M4) a material internal inconsistency: ≥1% difference on a headline or core figure between sections, or a highlights figure that does not match its table (beyond rounding of the last published digit — see *Rounding tolerance* below); **or a qualitative inconsistency on a headline claim or core topic**: the document states two incompatible facts — different dates, baselines, site/project identity or perimeter for the same object, a plan or action described in the future tense while dated evidence in the same document shows a later state, or two claims that cannot both be true. Only figures with the same perimeter, period and basis are compared (a Group vs entity difference is a perimeter note, not an inconsistency, unless the report labels both the same way);
- (M5) no external assurance together with a material gap (no Scope 3 at all, no energy data, or a core topic without any metric).

**Step 3 — 🟢 Low** otherwise: no Misleading or offset-based claim, at most 2 Unsubstantiated outcome claims, no material inconsistency, and assured or fully traceable data.

**Report** the rule code (e.g. "R2", "M1+M3"), the claim(s) and pages that triggered it, and — when the opposite level is arguable — the single fact that would flip it (e.g. "share 9% vs 10% threshold", "correction 3 pages away"). In the schema, put this in `greenwashing.overall_risk_rule`.

**Misleading vs Partially substantiated — figure correct, perimeter or basis unstated or partly covered.** Decide on the claim's wording and on what the document itself shows; outside knowledge alone never makes a claim Misleading.

| Situation (figure itself correct) | Rating |
|---|---|
| Perimeter/basis not stated with the claim, the document gives no other basis or perimeter for comparison, and the wording does not extend the figure beyond what it covers (e.g. "Scope 2 −30%" with no basis stated anywhere) | Partially substantiated (missing context) |
| Perimeter/basis stated with the claim or elsewhere, and the claim covers only part of the business but says so (e.g. "−20% energy in our Italian plants") | Partially substantiated, or Substantiated if fully traceable |
| The wording or placement extends the figure to a wider perimeter or basis than it covers (e.g. "our emissions −30%" when only market-based Scope 2 fell; one site's "100% renewable" presented as the company's), **or** the basis/perimeter the document itself gives elsewhere reverses the direction of the claim (location-based or absolute emissions rising while the headline says they fell) | Misleading — then apply *Corrected nearby* (R1 vs M1) |
| A qualitative relative label attached to a correct count or share (e.g. "N low-impact vehicles", "eco-friendly range = 40% of sales") | Partially substantiated if the document defines or breaks down the label; Unsubstantiated if it does not; Misleading only if the document's own data show the labelled items do not perform better than the comparator, or the label is absolute ("zero-impact") |

**Claims contradicted by the document itself.** When the document's own data contradict a claim (e.g. "nothing is wasted" while a table shows residues landfilled; "the area has no habitat" while the baseline reports habitat cover): (a) if the claim is quantitative or absolute (see *Quantitative vs narrative*), rate it **Misleading** and apply *Corrected nearby* — the contradicting data counts as the correction only if it lies within the corrected-nearby distance and refers to the same object; (b) if both statements are non-absolute narrative, rate the claim **Unsubstantiated** and record the contradiction as a qualitative internal inconsistency (M4 if it concerns a headline claim or core topic). Always cite both pages.

**Rounding tolerance (consistency check and M4).** Two published figures are consistent if they differ by no more than half a unit of the last printed digit of the **less precise** figure: tolerance = 0.5 × 10^(−d), where d is the number of decimals printed (12.3 vs 12.34 → tolerance 0.05, consistent; 91% vs 91.7% → tolerance 0.5, difference 0.7, flag; 1,262 vs 1,263 → tolerance 0.5, flag). A total of n rounded addends may differ from the sum of the addends by up to n × 0.5 units of the last digit; percentage breakdowns summing to 99-101% because of rounding are not flagged. Ratios recomputed with an assumed denominator (e.g. year-end vs average headcount) are not inconsistencies: report them as derived values with the assumption.

**Severity of consistency flags** (schema `data_quality_flags.severity`): **high** — a headline or core figure differs by ≥1% beyond rounding, a highlights figure does not match its table, or a qualitative inconsistency concerns a headline claim or core topic (these trigger M4); **medium** — a non-headline, non-core figure differs by ≥1%, or a qualitative inconsistency on a non-core topic; **low** — a difference <1% beyond rounding, a labelling, reference or editorial slip, or a perimeter note (Group vs entity) recorded for transparency.

---

## Report Completeness Checklist

Use this checklist to assess how complete a sustainability report is against best practice:

### Environmental
- [ ] Scope 1, 2, 3 GHG emissions (absolute, with methodology)
- [ ] Energy consumption by source (renewable vs. non-renewable)
- [ ] Science-based targets (SBTi status)
- [ ] Climate transition plan with milestones and capex
- [ ] Water consumption, withdrawal, discharge (with stress context)
- [ ] Waste by type and destination (recycling, landfill, incineration)
- [ ] Pollution data (if material)
- [ ] Biodiversity impacts (if material)
- [ ] LCA data for key products (if relevant)

### Social
- [ ] Workforce composition (gender, age, contract type)
- [ ] Gender pay gap (unadjusted)
- [ ] Health and safety (incident rates, fatalities)
- [ ] Training and development
- [ ] Living wage / adequate wage assessment
- [ ] Supply chain due diligence (human rights, labor)
- [ ] Community engagement

### Governance
- [ ] Board oversight of sustainability
- [ ] Executive compensation tied to ESG targets
- [ ] Anti-corruption policies and incidents
- [ ] Whistleblowing mechanisms
- [ ] Sustainability governance structure

### Process & Methodology
- [ ] Double materiality assessment conducted
- [ ] Reporting framework declared (GRI, ESRS, SASB)
- [ ] External assurance (who, what scope, what level)
- [ ] Stakeholder engagement process
- [ ] Base year and restatement policy
- [ ] Digital taxonomy / machine-readable format
