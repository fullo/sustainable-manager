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

### Green Claims Directive (Proposed)
The EU Green Claims Directive (2023/0085) aims to regulate environmental claims by requiring:
- **Substantiation**: Claims must be supported by widely recognized scientific evidence
- **LCA-based methodology**: Environmental claims about products require lifecycle assessment
- **Specific, not generic**: "Eco-friendly", "green", "sustainable" without qualification will be prohibited
- **Third-party verification**: Claims must be verified by an independent body
- **Transparency**: Methodology and underlying data must be accessible

### Unfair Commercial Practices Directive (Updated)
Directive 2024/825 already bans:
- Generic environmental claims without recognized excellent performance
- Claims based solely on carbon offsets (e.g., "carbon neutral" based on offset purchases)
- Sustainability labels not based on approved certification schemes

### CSRD/ESRS Anti-Greenwashing
ESRS reporting itself acts as an anti-greenwashing mechanism:
- Mandatory double materiality assessment prevents cherry-picking topics
- Standardized metrics enable comparison
- External assurance requirement (limited, moving to reasonable)
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
- Has the data been externally assured? By whom?

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
