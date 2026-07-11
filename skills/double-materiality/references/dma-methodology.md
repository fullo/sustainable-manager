# Double Materiality Assessment — Methodology Reference

## Legal Basis

### ESRS 1 Chapter 3: Materiality of Information

The Double Materiality Assessment is mandated by ESRS 1 (General Requirements), Chapter 3. It requires companies subject to the Corporate Sustainability Reporting Directive (CSRD) to assess sustainability matters from two perspectives simultaneously:

1. **Impact materiality**: How the company's activities affect people and the environment (inside-out perspective)
2. **Financial materiality**: How sustainability matters create risks and opportunities that affect the company's financial position, performance, and cash flows (outside-in perspective)

A sustainability matter is material if it is material from either or both perspectives. This is the "double" in double materiality.

### Regulatory References

- **CSRD** (Directive 2022/2464): Establishes the reporting obligation
- **ESRS 1** (Delegated Regulation 2023/2772): Defines the materiality assessment process
- **ESRS 2 IRO-1**: Requires description of the process to identify and assess material IROs
- **ESRS 2 IRO-2**: Requires disclosure of material matters and related ESRS standards
- **ESRS 2 SBM-3**: Requires description of material impacts, risks, and opportunities and their interaction with strategy and business model

### Post-Omnibus Simplification — Now in Force

The Omnibus simplification is no longer a proposal: the Omnibus I Directive (EU) 2026/470 entered into force on 18 March 2026, and the **revised ESRS (2026) were adopted as a delegated act on 3 July 2026** (applicable FY2027, voluntary early use FY2026). Key changes for the DMA:

- **Top-down approach permitted**: Companies no longer need to start from an exhaustive analysis of all sub-sub-topics
- **Information Materiality Filter**: Companies may omit data points within material topics if not decision-relevant (omissions documented)
- **Fair presentation principle**: Replaces the checklist mentality — the report must fairly present material IROs
- **Wider use of estimates** without "undue cost or effort", especially for value chain data
- **Value chain cap**: Data requests to value chain partners below 1,000 employees are capped at VSME content
- **61% fewer mandatory datapoints** overall in the revised ESRS; all voluntary datapoints removed

---

## Top-down vs Bottom-up Approach

### Bottom-up Approach (Original ESRS)

The original ESRS framework implicitly assumed an exhaustive bottom-up process:

1. List all ESRS topics and sub-topics (approximately 90+ sub-sub-topics)
2. For each sub-sub-topic, identify all possible IROs
3. Score each IRO on both materiality dimensions
4. Apply threshold to determine materiality
5. Aggregate sub-topic scores to topic level

**Pros**: Comprehensive, leaves no blind spots, produces detailed documentation
**Cons**: Extremely time-consuming (200-400 hours for a first assessment), resource-intensive, may produce analysis paralysis

### Top-down Approach (Post-Omnibus)

The simplified top-down approach:

1. Start from sector-level materiality indications (ESRS sector standards, SASB, GRI sector guidance)
2. Identify the 3-5 ESRS topics most likely material for the sector
3. Within those topics, assess IROs at the topic level first
4. Only drill into sub-topics where topic-level analysis indicates potential materiality
5. For topics clearly not material at sector level, document the exclusion rationale without detailed analysis

**Pros**: Faster (80-150 hours), focused on what matters, pragmatic
**Cons**: Risk of missing emerging or company-specific issues not captured in sector profiles

### When to Use Which

| Situation | Recommended Approach |
|---|---|
| First-time DMA | Top-down |
| SME or simplified reporting | Top-down |
| Mature reporter refining prior DMA | Bottom-up |
| High-controversy sector (oil & gas, mining) | Bottom-up |
| Company with complex, multi-sector operations | Hybrid: top-down per segment, then consolidate |
| Significant M&A or business model change | Bottom-up for new activities, top-down for legacy |

---

## Information Materiality Filter (Post-Omnibus)

### Concept

Even when a sustainability topic is determined to be material (i.e., it crosses the materiality threshold), not every data point required by the corresponding ESRS standard may be "information material." A data point is information material only if its disclosure would reasonably be expected to influence the decisions of primary users of sustainability reports.

### Application

1. Assess at the **data point level**, not at the topic or sub-topic level
2. Consider whether omitting the data point would change a reader's assessment of the company's sustainability performance
3. Consider the **cost-benefit** of collecting and reporting the data point
4. This filter does NOT allow skipping entire topics — only specific data points within material topics

### Documentation Requirement

For each omitted data point, document:
- Which data point is being omitted (specific ESRS reference)
- Why it is not information material for this company
- What alternative information, if any, is provided instead
- Confirmation that the omission does not render the remaining disclosures misleading

### Examples

- A service company with E1 (Climate Change) as material may omit detailed Scope 3 Category 1 (purchased goods) breakdown if its purchased goods are standard office supplies with immaterial emissions
- A manufacturing company with S1 (Own Workforce) as material may omit detailed contractor workforce data if contractors represent less than 2% of its labor force
- A software company with E2 (Pollution) as material due to data center operations may omit water pollution data points if its operations produce no liquid effluents

### Limitations

The filter cannot be used to:
- Skip entire ESRS topics determined to be material
- Avoid disclosures that are explicitly mandatory regardless of materiality (ESRS 2 general disclosures)
- Circumvent disclosures where the company has specific impacts that stakeholders have raised

---

## Impact Materiality Scoring

### Actual Negative Impacts

Severity is assessed on three dimensions:

**Scale** (1-5): How grave is the impact?
| Score | Definition | Example |
|---|---|---|
| 1 | Negligible | Minor, temporary nuisance with no measurable harm |
| 2 | Minor | Noticeable but limited harm, easily addressed |
| 3 | Moderate | Significant harm requiring remediation effort |
| 4 | Serious | Substantial harm to health, environment, or rights |
| 5 | Very serious | Severe, potentially catastrophic harm |

**Scope** (1-5): How widespread is the impact?
| Score | Definition | Example |
|---|---|---|
| 1 | Isolated | Single site or handful of individuals |
| 2 | Limited | One community or specific worker group |
| 3 | Moderate | Multiple sites/communities or a significant population segment |
| 4 | Widespread | Regional scale or large population group |
| 5 | Global/systemic | National/global scale or affecting fundamental systems |

**Irremediability** (1-5): How difficult is it to reverse or remedy?
| Score | Definition | Example |
|---|---|---|
| 1 | Fully reversible | Can be restored to original state quickly and completely |
| 2 | Mostly reversible | Restorable with moderate effort and time |
| 3 | Partially reversible | Some lasting effects even after remediation |
| 4 | Difficult to reverse | Long-term or permanent damage to some aspects |
| 5 | Irreversible | Permanent loss (e.g., species extinction, fatality, cultural heritage destruction) |

**Composite severity**: (Scale + Scope + Irremediability) / 3, rounded to nearest integer, yielding 1-5.

For actual impacts, the score IS the severity (1-5 scale), as the impact is already occurring (likelihood = certain).

### Potential Negative Impacts

Score = Composite Severity (1-5) x Likelihood (1-5)

**Likelihood** (1-5):
| Score | Definition | Probability |
|---|---|---|
| 1 | Rare | < 5% probability in assessment period |
| 2 | Unlikely | 5-20% probability |
| 3 | Possible | 20-50% probability |
| 4 | Likely | 50-80% probability |
| 5 | Almost certain | > 80% probability |

Score range: 1-25. Threshold default: >= 10.

### Actual Positive Impacts

Assessed on Scale (1-5) and Scope (1-5) only (irremediability not applicable to positive impacts).

Score = Scale x Scope (range 1-25).

### Potential Positive Impacts

Score = (Scale x Scope composite, 1-5) x Likelihood (1-5)

Range: 1-25. Positive impacts are scored to identify opportunities the company is creating for people and environment.

---

## Financial Materiality Scoring

### Risks

**Magnitude of financial effect** (1-5):
| Score | Definition | Indicative range |
|---|---|---|
| 1 | Insignificant | < 1% of annual revenue or < 0.5% of total assets |
| 2 | Minor | 1-5% of revenue or 0.5-2% of assets |
| 3 | Moderate | 5-10% of revenue or 2-5% of assets |
| 4 | Significant | 10-25% of revenue or 5-15% of assets |
| 5 | Severe | > 25% of revenue or > 15% of assets |

Score = Magnitude (1-5) x Likelihood (1-5). Range: 1-25.

### Opportunities

Same framework as risks. Magnitude reflects the potential positive financial effect:
- Revenue increase from green products or services
- Cost reduction from resource efficiency
- Access to green finance at favorable rates
- New market access or competitive advantage
- Avoided future costs (e.g., carbon pricing avoided through early decarbonization)

### Time Horizons

Each IRO must be assessed across three time horizons:

- **Short-term** (< 1 year): Current reporting period and immediate future
- **Medium-term** (1-5 years): Strategic planning horizon
- **Long-term** (> 5 years): Structural and systemic changes, climate scenarios

The **final score** for an IRO is the **maximum** across all three time horizons. This is critical because:
- Climate risks may score 2 short-term but 20 long-term
- Regulatory risks may be 5 today but 15 in medium-term as regulations tighten
- Transition opportunities may be 3 now but 18 in medium-term

Document the time horizon that drives the maximum score, as auditors will ask for this justification.

---

## Thresholds and Materiality Determination

### Recommended Threshold

**Default threshold: composite score >= 10 out of 25**

This corresponds roughly to a "moderate magnitude, possible likelihood" combination or equivalent.

### Threshold Calibration

Companies may adjust the threshold based on:
- **Sector risk profile**: Higher-risk sectors may use a lower threshold (8) to be more conservative
- **Stakeholder expectations**: Companies with ESG-sensitive investor base may lower the threshold
- **Regulatory scrutiny**: Sectors under specific EU regulation (e.g., EU ETS participants) may lower for climate topics
- **Maturity**: First-time reporters may start with 10 and refine in subsequent years

Common range in practice: 8-12.

### Topic-Level Materiality

A topic is material if **any** of its IROs exceeds the threshold on **either** the impact or financial dimension. This means:
- A topic can be material from impact perspective only
- A topic can be material from financial perspective only
- A topic can be material from both perspectives (most common for high-materiality topics)

### Documentation Requirements

The DMA documentation must include:
1. **Methodology description**: Top-down or bottom-up, rationale for choice
2. **Stakeholder engagement**: Who was consulted, how, when, key findings
3. **Scoring criteria**: Exact definitions used for each scale level
4. **Threshold justification**: Why this threshold was chosen
5. **IRO register**: Complete list of identified IROs with scores
6. **Results summary**: Material topics, non-material topics with exclusion rationale
7. **Information Materiality Filter**: Applications and justifications (if used)
8. **Date and responsible persons**: When the DMA was performed and by whom

### Auditor Expectations

Limited assurance auditors will check:
- Evidence of a **structured process** (not just management judgment)
- **Stakeholder engagement** documentation (meeting minutes, survey results, workshop outputs)
- **Traceable scoring**: Ability to follow from raw input to final score
- **Consistency**: Similar IROs scored similarly across topics
- **Completeness**: All ESRS topics considered (even if quickly excluded)
- **Independence**: Scoring not solely by management with vested interests
- **Year-on-year consistency**: Changes from prior year DMA are explained

---

## Common Pitfalls

### 1. Confusing Impact and Financial Materiality

Impact materiality asks: "How does the company affect the world?"
Financial materiality asks: "How does the world affect the company?"

Example: A company's GHG emissions (impact) may be high even if carbon pricing risk (financial) is currently low because the company operates outside the EU ETS. Both must be assessed independently.

### 2. Ignoring Time Horizons

Climate-related risks often score low on short-term financial materiality but very high on long-term. Using only the current-year perspective will miss these. Always assess all three horizons and use the maximum.

### 3. Neglecting Positive Impacts and Opportunities

Many first-time DMAs focus exclusively on negative impacts and risks. ESRS explicitly requires assessment of positive impacts and opportunities. These are important for:
- Balanced reporting
- Strategic insight (where the company creates value)
- Investor interest in growth opportunities

### 4. Insufficient Stakeholder Engagement

Common failures:
- Only consulting management (internal bias)
- Survey with 5 responses (insufficient sample)
- No engagement with affected communities
- Workshop with stakeholders but no documentation

Best practice: Minimum 2-3 engagement methods, include both internal and external stakeholders, document everything.

### 5. Generic IROs Not Tailored to the Company

Using boilerplate IRO lists without adapting them to the specific company context. The DMA must reflect the company's actual value chain, geographic context, and business model.

### 6. Treating the DMA as a One-Time Exercise

The DMA should be reviewed annually and updated when:
- Significant business changes occur (M&A, new products, geographic expansion)
- New regulations are introduced
- Stakeholder expectations shift materially
- Prior-year scoring proves inaccurate based on actual events

### 7. Inconsistent Scoring Across Topics

Using different interpretations of the severity scale for different topics. Establish clear, written scoring guidelines before beginning and apply them consistently. Consider using calibration sessions where a cross-functional team scores a few IROs together first.

### 8. Not Considering the Full Value Chain

ESRS requires consideration of impacts across the entire value chain (upstream, own operations, downstream). Companies often under-assess upstream supply chain impacts and downstream product use/end-of-life impacts.
