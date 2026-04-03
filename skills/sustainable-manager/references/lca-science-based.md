# Life Cycle Assessment (LCA) & Science-Based Approach — Reference Guide

## Table of Contents
1. [Life Cycle Assessment (LCA)](#life-cycle-assessment)
2. [Science Based Targets initiative (SBTi)](#science-based-targets)
3. [Planetary Boundaries](#planetary-boundaries)
4. [Reading and Interpreting LCA Reports](#reading-lca-reports)
5. [Integrating LCA with Sustainability Reporting](#lca-and-reporting)

---

## Life Cycle Assessment

### What is LCA?
Life Cycle Assessment is a systematic methodology for evaluating the environmental impacts of a product, process, or service throughout its entire life cycle — from raw material extraction ("cradle") through manufacturing, distribution, use, and end-of-life disposal or recycling ("grave" or "cradle" if circular).

### ISO Standards
- **ISO 14040:2006** — Principles and framework
- **ISO 14044:2006** — Requirements and guidelines
- **ISO 14067:2018** — Carbon footprint of products (CFP)
- **ISO 14046:2014** — Water footprint

### LCA Phases (ISO 14040)

#### 1. Goal and Scope Definition
- **Functional unit**: The quantified function of the product system (e.g., "1 kg of packaged product delivered to consumer", "1 kWh of electricity generated")
- **System boundaries**: What's included/excluded (cradle-to-gate, cradle-to-grave, cradle-to-cradle)
- **Cut-off criteria**: Materiality thresholds for excluding minor flows
- **Allocation procedures**: How to handle co-products (mass, economic, or system expansion)

#### 2. Life Cycle Inventory (LCI)
Quantification of all inputs and outputs across the life cycle:
- **Inputs**: Raw materials, energy, water, land use
- **Outputs**: Products, co-products, emissions to air/water/soil, waste
- **Data sources**: Primary data (measured), secondary data (databases like ecoinvent, GaBi, ELCD)

#### 3. Life Cycle Impact Assessment (LCIA)
Translation of LCI data into environmental impact categories:

**Midpoint indicators** (cause-oriented):
- **Climate change / GWP** (Global Warming Potential) — kg CO2 eq
- **Ozone depletion** — kg CFC-11 eq
- **Acidification** — kg SO2 eq or mol H+ eq
- **Eutrophication** (freshwater, marine, terrestrial) — kg P eq, kg N eq
- **Photochemical ozone formation** — kg NMVOC eq
- **Resource depletion** (mineral, fossil) — kg Sb eq, MJ
- **Water use** — m3 eq (water scarcity weighted)
- **Land use** — dimensionless (soil quality index)
- **Ecotoxicity** (freshwater) — CTUe
- **Human toxicity** (cancer, non-cancer) — CTUh
- **Particulate matter** — disease incidence

**Endpoint indicators** (damage-oriented):
- **Human health** — DALY (Disability-Adjusted Life Years)
- **Ecosystems** — species.yr (species potentially disappeared)
- **Resources** — surplus cost ($)

**Common LCIA methods:**
- **EF 3.1 (Environmental Footprint)** — EU PEF recommended method
- **ReCiPe 2016** — Both midpoint and endpoint
- **CML-IA** — Midpoint focused, widely used in EU
- **TRACI** — US EPA method
- **IMPACT World+** — Global scope

#### 4. Interpretation
- **Contribution analysis**: Which life cycle stages and processes dominate each impact?
- **Sensitivity analysis**: How do results change with different assumptions?
- **Uncertainty analysis**: Monte Carlo simulation for confidence intervals
- **Normalization and weighting**: Optional steps for comparing across impact categories

### System Boundary Types
- **Cradle-to-gate**: Raw materials → factory gate (excludes use and end-of-life)
- **Cradle-to-grave**: Full life cycle including disposal
- **Cradle-to-cradle**: Full cycle with recycling/reuse loop
- **Gate-to-gate**: Single production step only
- **Well-to-wheel**: Specific to fuels/energy (extraction → combustion)

### Environmental Product Declarations (EPD)
- Standardized LCA results following **ISO 14025** and **EN 15804** (construction products)
- Published through Programme Operators (EPD International, IBU, INIES, etc.)
- Third-party verified
- Basis for green procurement and building certification (LEED, BREEAM)

---

## Science Based Targets

### SBTi (Science Based Targets initiative)
A partnership between CDP, UNGC, WRI, and WWF that helps companies set emission reduction targets aligned with climate science.

### Key Concepts

**1.5C alignment**: Targets must be consistent with limiting warming to 1.5C above pre-industrial levels (Paris Agreement).

**Near-term targets** (5-10 years):
- Scope 1+2: At least 4.2% linear annual reduction (1.5C pathway)
- Scope 3: Required if Scope 3 is >40% of total emissions. At least 2.5% annual reduction.

**Long-term / Net-Zero targets** (by 2050 or sooner):
- Reduce Scope 1+2 by at least 90% vs. base year
- Reduce Scope 3 by at least 90% vs. base year
- Neutralize residual emissions (max 10%) through permanent carbon removals

### SBTi Methods
- **Absolute contraction approach (ACA)**: Reduce absolute emissions regardless of growth
- **Sectoral decarbonization approach (SDA)**: Sector-specific intensity pathways (for homogeneous sectors)
- **SBTi for Financial Institutions**: Portfolio alignment and engagement targets
- **FLAG (Forest, Land and Agriculture)**: Sector-specific for land-intensive sectors

### SBTi and ESRS
ESRS E1 explicitly asks:
- Whether the company has set science-based targets (E1-4)
- Alignment with the 1.5C / well-below 2C pathway
- GHG reduction targets with base year, target year, and methodology

### Carbon Budget Approach
The global carbon budget for 1.5C is approximately 400 GtCO2 remaining (from 2023). Science-based targets distribute this budget equitably across sectors and companies.

---

## Planetary Boundaries

The Stockholm Resilience Centre's framework identifies 9 planetary boundaries that define a "safe operating space" for humanity:

1. **Climate change** — CO2 concentration, radiative forcing (EXCEEDED)
2. **Biosphere integrity** — Genetic diversity, functional diversity (EXCEEDED)
3. **Land-system change** — % forest cover remaining (EXCEEDED)
4. **Biogeochemical flows** — N and P cycles (EXCEEDED)
5. **Freshwater change** — Blue and green water (EXCEEDED)
6. **Ocean acidification** — Aragonite saturation state
7. **Atmospheric aerosol loading** — Aerosol optical depth
8. **Stratospheric ozone depletion** — O3 concentration
9. **Novel entities** — Chemical pollution, plastics, etc. (EXCEEDED)

### Relevance to Sustainability Reporting
- Planetary boundaries provide the scientific foundation for understanding environmental limits
- The Science Based Targets Network (SBTN) extends the SBTi concept to all planetary boundaries (not just climate)
- ESRS E1-E5 map roughly to the environmental planetary boundaries
- Useful framing for materiality: impacts that push against exceeded boundaries are inherently material

---

## Reading LCA Reports

When a user provides an LCA report, extract and analyze:

### Key Data Points to Extract
1. **Functional unit** — What exactly is being assessed, and in what quantity?
2. **System boundaries** — What's included? Any notable exclusions?
3. **Impact results table** — The core quantitative results per impact category
4. **Hotspot identification** — Which life cycle stage dominates which impact?
5. **Normalization** — If provided, which impacts are most significant in relative terms?
6. **Sensitivity results** — How robust are the conclusions?
7. **Data quality** — Primary vs. secondary data mix, data age, geographic representativeness

### Red Flags to Watch For
- **Narrow system boundaries** without justification (e.g., cradle-to-gate when use phase is significant)
- **Outdated data** (LCI databases older than 5-10 years)
- **Missing impact categories** (e.g., only GWP when toxicity or water use may be critical)
- **No sensitivity analysis** — results may not be robust
- **Allocation choices** that favor the assessed product without transparency
- **Comparison without equal functional units** — apples to oranges
- **Cut-off criteria** that exclude significant flows (>5% of any impact category)

### Interpretation Framework
When presenting LCA findings:
1. Start with the **functional unit** — anchor all discussions to what's being measured
2. Present **top 3-5 impact categories** most relevant to the product/sector
3. Show **contribution analysis** — where do the impacts come from?
4. Highlight **trade-offs** between impact categories (e.g., lighter packaging reduces GWP but may increase land use)
5. Connect to **improvement opportunities** — what can actually be changed?
6. Frame in terms of **planetary boundaries** — which boundaries are most affected?

---

## LCA and Reporting

### ESRS Integration
- **ESRS E1**: GWP results from LCA directly feed Scope 1/2/3 reporting
- **ESRS E2**: LCA toxicity and pollution indicators support pollution disclosures
- **ESRS E3**: LCA water footprint supports water and marine resource disclosures
- **ESRS E5**: LCA material flow data supports circular economy disclosures
- **Product Environmental Footprint (PEF)**: EU method for product-level LCA, uses EF 3.1 impact method

### GRI Integration
- **GRI 301** (Materials): LCA material input data
- **GRI 302** (Energy): LCA energy inventory
- **GRI 305** (Emissions): LCA GWP results
- **GRI 306** (Waste): LCA waste generation data

### From LCA to Strategy
LCA results inform science-based decision-making:
1. **Eco-design**: Reduce impacts at the design stage (material selection, weight reduction, durability)
2. **Supplier engagement**: Target hotspots in the supply chain
3. **Circular strategies**: Identify end-of-life improvements (recyclability, biodegradability)
4. **Communication**: EPDs, green claims, comparative assertions (ISO 14044 critical review required)
5. **Target setting**: LCA baselines inform science-based reduction pathways

---

## Life Cycle Costing (LCC)

### What is LCC?
Life Cycle Costing extends the LCA perspective to economic costs, evaluating the total cost of ownership across a product's or asset's entire life cycle — not just the purchase price.

### Relationship to LCA
- **LCA** measures environmental impacts across the life cycle
- **LCC** measures economic costs across the life cycle
- **Together** they enable integrated decision-making: choosing options that minimize both environmental impact and total cost

### ISO and EU Standards
- **ISO 15686-5:2017** — Buildings and constructed assets, service life planning, life-cycle costing
- **IEC 60300-3-3** — Dependability management, life cycle costing (general application)
- **EU Green Public Procurement (GPP)** — Recommends LCC in public tenders
- **ISO 20400:2017** — Sustainable procurement guidance, emphasizes lifecycle costing over upfront cost

### LCC Components

| Phase | Cost Elements |
|-------|--------------|
| **Acquisition** | Purchase price, installation, commissioning, training |
| **Operation** | Energy, water, consumables, labor, maintenance, insurance |
| **End-of-life** | Decommissioning, disposal, recycling, residual value |
| **Externalities** (optional) | Carbon cost (shadow pricing), pollution remediation, health costs |

### When to Apply LCC
- **Procurement decisions**: ISO 20400 recommends evaluating suppliers on total lifecycle cost, not just upfront price. A cheaper product that consumes more energy or requires frequent replacement may cost more over its lifetime.
- **Eco-design trade-offs**: A more durable or recyclable product may have higher production costs but lower total lifecycle cost.
- **Investment decisions**: Capital expenditure for efficiency upgrades (e.g., LED lighting, heat recovery) justified through LCC analysis.
- **Public tenders**: EU GPP criteria increasingly require or reward LCC-based evaluation.

### LCC and Sustainability Reporting
- **ESRS E1**: Transition plan investments evaluated through LCC lens (cost of inaction vs. cost of transition)
- **ESRS E5**: Circular economy strategies justified through total lifecycle economic analysis
- **TCFD**: Financial impact of climate risks quantified using lifecycle cost projections

### Practical LCC Calculation
1. Define the analysis period (product lifetime, contract period, or building lifespan)
2. Identify all cost categories across acquisition, operation, and end-of-life
3. Apply a discount rate to future costs (Net Present Value — NPV)
4. Include externalities if required (e.g., EU ETS carbon price, social cost of carbon)
5. Compare alternatives on NPV basis
6. Conduct sensitivity analysis on key assumptions (energy price, discount rate, lifetime)
