# Circular Economy Metrics Reference

## Material Circularity Indicator (MCI)

### Overview
The Material Circularity Indicator (MCI) was developed by the Ellen MacArthur Foundation
in collaboration with Granta Design. It measures how restorative the material flows of a
product or company are, providing a score between 0 (fully linear) and 1 (fully circular).

### Formula

```
MCI = 1 - LFI x F(X)
```

Where:

- **LFI** = Linear Flow Index
- **F(X)** = Utility factor (adjusts for product lifetime and intensity of use)

### Linear Flow Index (LFI)

```
LFI = (V + W) / (2M + Wf - Wc)
```

Where:

| Symbol | Description | Unit |
|--------|-------------|------|
| V | Virgin material input | kg or tonnes |
| W | Unrecoverable waste produced | kg or tonnes |
| M | Total mass of the product | kg or tonnes |
| Wf | Waste sent to landfill or incineration | kg or tonnes |
| Wc | Waste collected for recycling or reuse | kg or tonnes |

### Utility Factor F(X)

The utility factor adjusts the MCI based on the product's actual utility compared to
the industry average. It accounts for both product lifetime and functional units of use.

```
X = (L / Lav) x (U / Uav)
```

Where:

| Symbol | Description |
|--------|-------------|
| L | Actual product lifetime (years) |
| Lav | Industry average product lifetime (years) |
| U | Functional units of use |
| Uav | Industry average functional units of use |

```
F(X) = 0.9 / X    (for X >= 1)
F(X) = 0.9 x X    (for X < 1, capped at 0.9)
```

### MCI Interpretation Scale

| MCI Range | Rating | Description |
|-----------|--------|-------------|
| 0.0 - 0.1 | Very low | Almost entirely linear; no meaningful circularity |
| 0.1 - 0.3 | Low | Minimal circular practices; heavy reliance on virgin inputs |
| 0.3 - 0.5 | Moderate-low | Some recycled inputs or end-of-life recovery |
| 0.5 - 0.6 | Moderate | Balanced mix of linear and circular flows |
| 0.6 - 0.7 | Moderate-good | Significant circular material flows |
| 0.7 - 0.8 | Good | Strong circularity; majority of flows are restorative |
| 0.8 - 0.9 | Very good | Near-circular; minimal virgin input and waste |
| 0.9 - 1.0 | Excellent | Approaching full circularity |

### Practical Thresholds for Benchmarking

- **< 0.3**: Low circularity - priority intervention needed
- **0.3 - 0.6**: Moderate circularity - improvement opportunities exist
- **0.6 - 0.8**: Good circularity - above average performance
- **> 0.8**: Excellent circularity - industry leading

---

## ESRS E5 — Resource Use and Circular Economy

### Disclosure Requirements

#### E5-1: Policies on resource use and circular economy
- Policies addressing resource efficiency, waste prevention, circular design
- Integration with procurement, product development, operations
- Board-level oversight and governance

#### E5-2: Actions and resources related to resource use and circular economy
- Concrete actions taken or planned
- Resources allocated (financial, human)
- Timeline for implementation
- Expected outcomes and KPIs

#### E5-3: Targets related to resource use and circular economy
- Measurable targets with base year and target year
- Scope: company-wide or specific business units/products
- Alignment with EU Circular Economy Action Plan
- Progress tracking methodology

#### E5-4: Resource inflows
- Total weight of materials used (tonnes)
- Percentage of recycled or reused input materials
- Percentage of renewable input materials
- Percentage of secondary (recovered) materials
- Breakdown by material type
- Critical raw materials used (as per EU Critical Raw Materials Act)

#### E5-5: Resource outflows
**Products and packaging:**
- Total weight of products placed on market
- Designed for durability, reuse, repair, refurbishment, remanufacturing, recycling
- Packaging weight and recyclability rate

**Waste generation:**
- Total waste generated (tonnes)
- Breakdown by type: hazardous vs non-hazardous
- Breakdown by treatment method:
  - Recycling
  - Reuse
  - Composting/anaerobic digestion
  - Energy recovery (incineration with energy recovery)
  - Incineration without energy recovery
  - Landfill
  - Other disposal
- Waste diversion rate from landfill
- Food waste (if applicable)

#### E5-6: Anticipated financial effects
- Financial effects of resource use and circular economy risks/opportunities
- Potential cost savings from circular practices
- Revenue from secondary materials or circular business models
- Stranded asset risks from linear dependencies

### ESRS E5 Reporting Checklist

| Disclosure | Key Data Points | Status |
|------------|----------------|--------|
| E5-1 | Circular economy policy document | |
| E5-2 | Action plan with budget | |
| E5-3 | Targets with baselines | |
| E5-4 | Material input data by type | |
| E5-5 | Waste output data by treatment | |
| E5-6 | Financial impact assessment | |

---

## PPWR Targets (Regulation on Packaging and Packaging Waste)

### Context
The EU Packaging and Packaging Waste Regulation (PPWR) replaces the previous Directive
94/62/EC. It was adopted in 2024 and enters into force progressively starting August 2026.

### Recycling Targets by Material

| Material | Target 2025 | Target 2030 | Target 2035 |
|----------|-------------|-------------|-------------|
| Paper and cardboard | 75% | 85% | 85% |
| Glass | 70% | 75% | 75% |
| Ferrous metals | 70% | 80% | 80% |
| Aluminium | 50% | 60% | 60% |
| Plastic | 50% | 55% | 55% |
| Wood | 25% | 30% | 30% |
| Overall packaging | 65% | 70% | 70% |

### Minimum Recycled Content Requirements

| Packaging Type | Target 2030 | Target 2040 |
|----------------|-------------|-------------|
| PET contact-sensitive (bottles) | 30% | 65% |
| Other contact-sensitive plastic | 10% | 50% |
| Single-use plastic bottles (non-PET) | 30% | 65% |
| Other plastic packaging | 35% | 65% |

### Reuse Targets

| Packaging Category | Target 2030 | Target 2040 |
|-------------------|-------------|-------------|
| Transport packaging (pallets, crates) | 40% | 70% |
| E-commerce packaging | 10% | 50% |
| Grouped packaging (multipacks) | 10% | 40% |
| Beverage packaging (HoReCa) | 10% | 40% |

### Additional PPWR Requirements

**Compostable packaging mandates:**
- Tea bags and coffee pods: must be compostable
- Fruit and vegetable sticker labels: must be compostable
- Very lightweight plastic carrier bags: must be compostable

**Deposit return schemes (DRS):**
- Mandatory for plastic bottles up to 3 litres
- Mandatory for aluminium cans up to 3 litres
- Member states must achieve 90% separate collection by 2029
- Exemptions possible if already achieving >90% collection

**Restrictions on single-use formats:**
- Ban on certain single-use plastic packaging formats from 2030
- Includes: single-use grouped packaging for cans/bottles, single-use HoReCa packaging for dine-in, single-use hotel miniatures, single-use packaging for fresh fruit and vegetables under 1.5 kg

**Labelling and digital product passport:**
- Harmonised labelling for sorting instructions
- QR code linking to recycling information
- Digital product passport for packaging by 2030

---

## Waste Hierarchy (EU Directive 2008/98/EC)

### Priority Order (Most to Least Preferred)

1. **Prevention**
   - Reduce material use at source
   - Design out waste
   - Extend product lifetime
   - Examples: lightweighting, dematerialisation, product-as-a-service

2. **Preparing for re-use**
   - Check, clean, repair, refurbish products/components
   - No reprocessing required
   - Examples: refurbished electronics, reusable packaging, second-hand markets

3. **Recycling**
   - Reprocess waste into new materials or substances
   - Includes composting and anaerobic digestion of bio-waste
   - Excludes energy recovery
   - Examples: PET recycling, metal recycling, paper recycling

4. **Other recovery**
   - Use waste to generate energy or other benefit
   - Includes incineration with energy recovery (waste-to-energy)
   - Includes backfilling operations
   - Examples: waste-to-energy plants, cement kilns co-processing

5. **Disposal**
   - Landfill or incineration without energy recovery
   - Least preferred option
   - Subject to landfill taxes and restrictions across EU

### Hierarchy Application Principle
Member states must apply the waste hierarchy as a priority order in waste prevention and
management policy. Departures are permitted for specific waste streams where justified by
life-cycle assessment demonstrating better overall environmental outcomes.

---

## Circular Economy Act (Expected Late 2026)

### Key Pillars

**Extended Producer Responsibility (EPR):**
- Producers financially responsible for end-of-life management
- Fee modulation based on durability, reparability, recyclability
- Expanded to new product categories (textiles, furniture, tyres)

**Eco-design Requirements:**
- Minimum durability standards
- Repairability requirements (availability of spare parts, repair manuals)
- Recyclability design criteria
- Use of recycled content mandates
- Restrictions on substances hindering recycling

**Right to Repair:**
- Manufacturers must provide spare parts for minimum period
- Access to repair information and tools
- Prohibition of practices preventing independent repair
- Repair scoring/index for consumers

**Digital Product Passport (DPP):**
- Mandatory for batteries (already in force), textiles, electronics
- Contains: material composition, recycled content, repairability score, disassembly instructions
- QR code or RFID-based access
- Interoperable EU-wide registry

**Material Efficiency Targets:**
- Sector-specific material productivity targets
- Critical raw materials recovery rates
- Secondary raw materials market development

---

## Key Circularity Metrics Beyond MCI

### Recycled Content Percentage
```
Recycled Content (%) = (Mass of recycled input / Total mass of input) x 100
```
- Measures how much secondary material is used in production
- Relevant for PPWR compliance (packaging) and eco-design regulations
- Chain of custody: mass balance vs physical segregation

### Recycling Rate
```
Recycling Rate (%) = (Mass sent to recycling / Total waste generated) x 100
```
- Measures the proportion of waste diverted to recycling
- Calculation point matters: at collection vs at output of recycling facility
- EU standard: output-based measurement (actual recycled material)

### Waste Diversion Rate
```
Waste Diversion Rate (%) = (Recycling + Reuse + Composting) / Total waste x 100
```
- Broader than recycling rate: includes reuse and biological treatment
- Does NOT include energy recovery (waste-to-energy)
- Key metric for ESRS E5-5 reporting

### Resource Productivity
```
Resource Productivity = Revenue (EUR) / Material Consumption (tonnes)
```
- Measures economic value generated per unit of material
- EU uses GDP/Domestic Material Consumption (DMC)
- Useful for benchmarking across sectors and over time
- Target: decouple economic growth from material consumption

### Product Lifetime Extension
```
Lifetime Extension Factor = Actual Lifetime / Design Lifetime
```
- Measures whether products last longer than designed
- Relevant for durability claims and eco-design compliance
- Consider: repair frequency, refurbishment cycles, second-life use

### Circular Material Use Rate (CMUR)
```
CMUR = Recycled Material Use / (Total Material Use + Recycled Material Use - Recycled Material Output)
```
- EU headline indicator for circular economy monitoring
- National-level metric tracked by Eurostat
- EU average ~11.5% (2022), target to increase significantly
