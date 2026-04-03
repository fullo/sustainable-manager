# GHG Protocol Scope 3 Categories — Comprehensive Reference

This reference covers all 15 Scope 3 categories as defined by the GHG Protocol Corporate Value Chain (Scope 3) Accounting and Reporting Standard.

---

## Upstream Categories (1-8)

---

### Category 1: Purchased Goods and Services

**Description:** Extraction, production, and transportation of goods and services purchased or acquired by the reporting company in the reporting year, not otherwise included in Categories 2-8.

**Typical % of total Scope 3:** 30-70% (varies by sector; highest in manufacturing, retail, food & beverage)

**Materiality by sector:**
| Sector | Materiality |
|--------|------------|
| Manufacturing | High (40-60%) |
| Food & Beverage | High (50-70%) |
| Fashion/Textiles | High (55-70%) |
| Construction | High (35-55%) |
| Financial Services | Medium (10-20%) |
| Energy/Utilities | Medium (15-25%) |

**Calculation methods:**

1. **Supplier-specific method** (Quality: 5/5)
   - Uses supplier-provided cradle-to-gate GHG data per unit purchased
   - Data needed: supplier emission factors per product/service
   - Best for: key suppliers with mature carbon reporting

2. **Hybrid method** (Quality: 4/5)
   - Combines supplier-specific data with secondary data for gaps
   - Data needed: mix of supplier data + industry averages

3. **Average-data method** (Quality: 3/5)
   - Uses industry-average emission factors per unit of good/service
   - Data needed: mass, volume, or units purchased per type
   - Sources: ecoinvent, DEFRA, industry-specific databases

4. **Spend-based method** (Quality: 2/5)
   - Uses economic input-output (EEIO) emission factors per EUR/USD spent
   - Data needed: procurement spend by category
   - Sources: EPA EEIO, EXIOBASE, Eurostat environmentally-extended IO tables
   - Fastest to implement but least accurate

**Emission factor sources:**
- DEFRA: "Indirect emissions from the supply chain" factors (UK, updated annually)
- ecoinvent: cradle-to-gate LCA data (global, paid license)
- EPA EEIO: US supply chain factors by NAICS sector (free)
- EXIOBASE: multi-regional IO model (academic, free)
- ADEME Base Empreinte: French factors (free)

**Key considerations:**
- Typically the largest Scope 3 category — prioritize early
- Spend-based is a good starting point but plan migration to activity/supplier data
- Under CSRD, companies must disclose calculation methodology and data quality

---

### Category 2: Capital Goods

**Description:** Extraction, production, and transportation of capital goods purchased or acquired by the reporting company in the reporting year (e.g., equipment, machinery, buildings, vehicles).

**Typical % of total Scope 3:** 3-15%

**Materiality by sector:**
| Sector | Materiality |
|--------|------------|
| Manufacturing | Medium (5-15%) |
| Food & Beverage | Low (3-8%) |
| Fashion/Textiles | Low (2-5%) |
| Construction | Medium (8-15%) |
| Financial Services | Low (3-8%) |
| Energy/Utilities | High (10-20%) |

**Calculation methods:**

1. **Supplier-specific method** (Quality: 5/5)
   - Cradle-to-gate emissions from capital good manufacturer
   - Data needed: supplier-provided carbon footprint per asset

2. **Average-data method** (Quality: 3/5)
   - Industry-average factors per type of capital good
   - Data needed: type, weight, or value of each capital purchase

3. **Spend-based method** (Quality: 2/5)
   - EEIO factors applied to CAPEX spending
   - Data needed: CAPEX by asset category

**Accounting note:** Report in the year of purchase (do not amortize unless justified by company policy and disclosed). Lumpy year-over-year due to large purchases.

**Emission factor sources:** ecoinvent (machinery, vehicles), DEFRA (construction materials), EPA EEIO (by spending category)

---

### Category 3: Fuel- and Energy-Related Activities (not in Scope 1 or 2)

**Description:** Emissions related to the production of fuels and energy purchased and consumed that are not already accounted for in Scope 1 (direct combustion) or Scope 2 (purchased electricity). Includes:
- Upstream emissions of purchased fuels (well-to-tank, WTT)
- Upstream emissions of purchased electricity (WTT of fuel used in generation)
- Transmission and distribution (T&D) losses
- Generation of purchased electricity sold to end users (for utilities)

**Typical % of total Scope 3:** 3-10%

**Materiality by sector:**
| Sector | Materiality |
|--------|------------|
| Manufacturing | Medium (5-10%) |
| Food & Beverage | Low (3-6%) |
| Fashion/Textiles | Low (2-5%) |
| Construction | Low (3-6%) |
| Financial Services | Low (1-3%) |
| Energy/Utilities | High (15-30%) |

**Calculation methods:**

1. **Activity-based method** (Quality: 4/5)
   - Uses fuel/energy consumption data (already collected for Scope 1/2) with WTT and T&D factors
   - Data needed: kWh electricity, litres/m3 fuel consumed (from Scope 1/2 inventory)
   - Sources: DEFRA WTT factors, IEA T&D loss factors by country

**Emission factor sources:**
- DEFRA: WTT factors by fuel type, T&D loss factors (UK grid)
- IEA: country-specific T&D loss percentages
- National grid operators: country-specific T&D loss data

**Key considerations:**
- Relatively straightforward because it reuses Scope 1/2 data
- Often overlooked but required for completeness

---

### Category 4: Upstream Transportation and Distribution

**Description:** Transportation and distribution of products purchased by the reporting company in the reporting year between a company's tier 1 suppliers and its own operations (inbound logistics), in vehicles and facilities not owned or controlled by the reporting company.

**Typical % of total Scope 3:** 2-10%

**Materiality by sector:**
| Sector | Materiality |
|--------|------------|
| Manufacturing | Medium (4-8%) |
| Food & Beverage | Medium (5-10%) |
| Fashion/Textiles | Medium (3-8%) |
| Construction | Medium (5-10%) |
| Financial Services | NA (<1%) |
| Energy/Utilities | Low (2-5%) |

**Calculation methods:**

1. **Distance-based method** (Quality: 4/5)
   - Data needed: mass of goods (tonnes), distance (km), transport mode (road/rail/sea/air)
   - Factor: tCO2e per tonne-km by mode
   - Sources: DEFRA freight factors, GLEC Framework

2. **Spend-based method** (Quality: 2/5)
   - Data needed: logistics spend by mode
   - Source: EEIO factors for transport services

3. **Fuel-based method** (Quality: 4/5)
   - Data needed: fuel consumption by transport provider
   - Source: DEFRA fuel combustion factors

**Emission factor sources:**
- DEFRA: freight transport factors by mode and vehicle type
- GLEC Framework: Global Logistics Emissions Council standardized factors
- EcoTransIT: online calculator for freight emissions
- Clean Cargo Working Group: container shipping factors

---

### Category 5: Waste Generated in Operations

**Description:** Disposal and treatment of waste generated in the reporting company's operations in the reporting year, in facilities not owned or controlled by the reporting company.

**Typical % of total Scope 3:** 1-5%

**Materiality by sector:**
| Sector | Materiality |
|--------|------------|
| Manufacturing | Medium (2-5%) |
| Food & Beverage | Medium (3-5%) |
| Fashion/Textiles | Medium (2-5%) |
| Construction | Medium (3-8%) |
| Financial Services | Low (<1%) |
| Energy/Utilities | Low (1-3%) |

**Calculation methods:**

1. **Waste-type-specific method** (Quality: 4/5)
   - Data needed: mass of waste by type (paper, plastic, organic, metal, etc.) and treatment method (landfill, incineration, recycling, composting)
   - Factor: tCO2e per tonne by waste type and treatment
   - Sources: DEFRA waste disposal factors

2. **Average-data method** (Quality: 3/5)
   - Data needed: total waste mass + average treatment split
   - Source: national waste statistics for treatment mix

**Emission factor sources:**
- DEFRA: waste disposal emission factors by waste type and treatment method (updated annually)
- EPA WARM model: US waste reduction model
- ADEME: French waste factors

---

### Category 6: Business Travel

**Description:** Transportation of employees for business-related activities in vehicles not owned or operated by the reporting company (air, rail, rental cars, hotels).

**Typical % of total Scope 3:** 1-8%

**Materiality by sector:**
| Sector | Materiality |
|--------|------------|
| Manufacturing | Low (1-3%) |
| Food & Beverage | Low (1-3%) |
| Fashion/Textiles | Low (1-3%) |
| Construction | Low (1-3%) |
| Financial Services | Medium (3-8%) |
| Energy/Utilities | Low (1-3%) |

**Calculation methods:**

1. **Distance-based method** (Quality: 4/5)
   - Data needed: distance travelled by mode (air short/medium/long haul, rail, car), cabin class for flights
   - Factor: tCO2e per passenger-km by mode
   - Sources: DEFRA business travel factors
   - Include radiative forcing multiplier for aviation (typically 1.9x)

2. **Spend-based method** (Quality: 2/5)
   - Data needed: travel agency spend or expense claims by category
   - Source: EEIO factors for travel services

3. **Hotel nights** (Quality: 3/5)
   - Data needed: number of hotel nights by country
   - Factor: tCO2e per hotel night by country
   - Source: DEFRA hotel stay factors, Cornell Hotel Sustainability Benchmarking Index

**Emission factor sources:**
- DEFRA: passenger transport factors (air by haul/class, rail, car), hotel stays
- ICAO Carbon Emissions Calculator: flight-specific factors
- UIC: rail emission factors by country

---

### Category 7: Employee Commuting

**Description:** Transportation of employees between their homes and their worksites in vehicles not owned or operated by the reporting company.

**Typical % of total Scope 3:** 1-5%

**Materiality by sector:**
| Sector | Materiality |
|--------|------------|
| Manufacturing | Low (1-3%) |
| Food & Beverage | Low (1-3%) |
| Fashion/Textiles | Low (1-3%) |
| Construction | Low (1-3%) |
| Financial Services | Low (2-5%) |
| Energy/Utilities | Low (1-3%) |

**Calculation methods:**

1. **Survey-based + distance method** (Quality: 4/5)
   - Data needed: employee commuting survey (mode, distance, frequency)
   - Factor: tCO2e per passenger-km by mode
   - Sources: DEFRA passenger transport factors

2. **Average-data method** (Quality: 2/5)
   - Data needed: number of employees, average commuting distance by country
   - Factor: national average commuting emission per employee
   - Sources: national transport statistics, DEFRA

3. **Remote work adjustment**
   - Account for home office energy use (if material)
   - Factor: kWh per home-working day × grid factor

**Emission factor sources:**
- DEFRA: passenger transport factors by vehicle type
- National transport surveys: average commuting patterns by country
- EcoAct: homeworking emission factors

---

### Category 8: Upstream Leased Assets

**Description:** Emissions from the operation of assets leased by the reporting company (lessee) not included in Scope 1 and Scope 2, reported by the lessee.

**Typical % of total Scope 3:** 0-5%

**Materiality by sector:**
| Sector | Materiality |
|--------|------------|
| Manufacturing | Low (0-2%) |
| Food & Beverage | Low (0-2%) |
| Fashion/Textiles | Low (0-3%) |
| Construction | Low (1-3%) |
| Financial Services | Medium (2-5%) |
| Energy/Utilities | Low (0-2%) |

**Calculation methods:**

1. **Asset-specific method** (Quality: 4/5)
   - Data needed: energy use data for each leased asset (building, vehicle, equipment)
   - Factor: Scope 1/2 factors applied to asset energy use
   - Note: Depends on consolidation approach (operational vs financial control)

2. **Average-data method** (Quality: 2/5)
   - Data needed: floor area of leased buildings, type/number of leased vehicles
   - Factor: average energy intensity per m2 or per vehicle type

**Key considerations:**
- Relevance depends heavily on consolidation approach
- If the company uses operational control, leased assets where the company is the operator are in Scope 1/2
- Often low materiality unless the company leases significant real estate or fleet

---

## Downstream Categories (9-15)

---

### Category 9: Downstream Transportation and Distribution

**Description:** Transportation and distribution of products sold by the reporting company between the reporting company's operations and the end consumer (outbound logistics), in vehicles and facilities not owned or controlled by the reporting company.

**Typical % of total Scope 3:** 2-10%

**Materiality by sector:**
| Sector | Materiality |
|--------|------------|
| Manufacturing | Medium (3-8%) |
| Food & Beverage | Medium (5-10%) |
| Fashion/Textiles | Medium (3-8%) |
| Construction | Low (2-5%) |
| Financial Services | NA (<1%) |
| Energy/Utilities | Low (1-3%) |

**Calculation methods:** Same as Category 4 (distance-based, spend-based, fuel-based), applied to outbound logistics.

**Key considerations:**
- Distinguish from Cat 4: Cat 9 = outbound (to customer), Cat 4 = inbound (from supplier)
- Include warehousing and distribution center emissions if third-party operated
- E-commerce companies: last-mile delivery can be significant

---

### Category 10: Processing of Sold Products

**Description:** Processing of intermediate products sold by the reporting company by downstream companies (e.g., manufacturers) in the reporting year.

**Typical % of total Scope 3:** 0-15%

**Materiality by sector:**
| Sector | Materiality |
|--------|------------|
| Manufacturing | Medium (5-15%) |
| Food & Beverage | Low (2-8%) |
| Fashion/Textiles | Low (1-5%) |
| Construction | Low (2-5%) |
| Financial Services | NA |
| Energy/Utilities | NA |

**Calculation methods:**

1. **Average processing energy method** (Quality: 3/5)
   - Data needed: mass of intermediate products sold, type of downstream processing
   - Factor: average energy consumption per tonne of processing by type
   - Apply appropriate electricity grid factor for processing location

2. **Site-specific method** (Quality: 4/5)
   - Data needed: actual energy use data from downstream processors
   - Requires customer engagement

**Key considerations:**
- Only relevant if the company sells intermediate products
- NA for companies that sell finished consumer products or services

---

### Category 11: Use of Sold Products

**Description:** Emissions from the use of goods and services sold by the reporting company in the reporting year over their expected lifetime.

**Typical % of total Scope 3:** 0-80% (highly variable)

**Materiality by sector:**
| Sector | Materiality |
|--------|------------|
| Manufacturing | High (10-50%) — depends on product type |
| Food & Beverage | Low (1-5%) |
| Fashion/Textiles | Medium (5-15%) — washing/drying |
| Construction | High (20-40%) — building operational energy |
| Financial Services | NA |
| Energy/Utilities | High (50-80%) — combustion of sold fuels |

**Calculation methods:**

1. **Direct use-phase method** (Quality: 4/5)
   - For energy-using products: units sold × product lifetime × energy/fuel consumed per use × use frequency × emission factor
   - For fuels/feedstocks: quantity sold × emission factor upon combustion
   - Data needed: product specifications, expected lifetime, usage patterns

2. **Indirect use-phase method** (Quality: 3/5)
   - For products that indirectly consume energy (e.g., clothing requiring washing)
   - Data needed: estimated energy use per wash cycle × expected washes over lifetime

**Key considerations:**
- Can be the largest category for automotive, appliance, and fossil fuel companies
- Requires assumptions about product lifetime and user behavior — document clearly
- GHG Protocol requires separate reporting of direct and indirect use-phase emissions

---

### Category 12: End-of-Life Treatment of Sold Products

**Description:** Waste disposal and treatment of products sold by the reporting company (in the reporting year) at the end of their life.

**Typical % of total Scope 3:** 1-5%

**Materiality by sector:**
| Sector | Materiality |
|--------|------------|
| Manufacturing | Low (1-5%) |
| Food & Beverage | Medium (2-5%) — packaging waste |
| Fashion/Textiles | Medium (2-5%) — textile waste |
| Construction | Low (1-3%) |
| Financial Services | NA |
| Energy/Utilities | Low (<1%) |

**Calculation methods:**

1. **Waste-type-specific method** (Quality: 4/5)
   - Data needed: mass of products sold × material composition × expected end-of-life treatment (landfill %, recycling %, incineration %, composting %)
   - Factor: tCO2e per tonne by material and treatment
   - Sources: DEFRA waste disposal factors, national waste statistics for treatment split

**Emission factor sources:**
- DEFRA: end-of-life treatment factors
- National waste management statistics for treatment mix assumptions
- Ellen MacArthur Foundation: circularity metrics

---

### Category 13: Downstream Leased Assets

**Description:** Emissions from the operation of assets owned by the reporting company (as lessor) and leased to other entities not already included in Scope 1 and Scope 2, reported by the lessor.

**Typical % of total Scope 3:** 0-15%

**Materiality by sector:**
| Sector | Materiality |
|--------|------------|
| Manufacturing | NA |
| Food & Beverage | NA |
| Fashion/Textiles | NA |
| Construction | Low (0-5%) |
| Financial Services | Medium (5-15%) — leased real estate |
| Energy/Utilities | NA |

**Calculation methods:**

1. **Asset-specific method** (Quality: 4/5)
   - Data needed: energy use data for each leased-out asset
   - Factor: Scope 1/2 methodology applied to tenant energy use

2. **Average-data method** (Quality: 2/5)
   - Data needed: floor area of leased-out buildings, asset type
   - Factor: average energy intensity benchmarks

**Key considerations:**
- Primarily relevant for real estate companies and lessors
- Depends on consolidation approach (financial vs operational control)

---

### Category 14: Franchises

**Description:** Emissions from the operation of franchises not included in Scope 1 and Scope 2, reported by the franchisor.

**Typical % of total Scope 3:** 0-50%

**Materiality by sector:**
| Sector | Materiality |
|--------|------------|
| Manufacturing | NA |
| Food & Beverage | High (20-50%) — if franchise model |
| Fashion/Textiles | Medium (5-20%) — if franchise model |
| Construction | NA |
| Financial Services | NA |
| Energy/Utilities | NA |

**Calculation methods:**

1. **Franchise-specific method** (Quality: 4/5)
   - Data needed: energy use, fuel consumption, refrigerant data from each franchise location
   - Apply Scope 1/2 methodology to each franchise

2. **Average-data method** (Quality: 2/5)
   - Data needed: number of franchise locations, average floor area
   - Factor: average energy intensity per location type

**Key considerations:**
- Only applies to franchisors
- Franchisees report these as their own Scope 1/2

---

### Category 15: Investments

**Description:** Emissions associated with the reporting company's investments in the reporting year, not already included in Scope 1 or Scope 2. Relevant for investors and companies that provide financial services.

**Typical % of total Scope 3:** 0-95%

**Materiality by sector:**
| Sector | Materiality |
|--------|------------|
| Manufacturing | NA (unless significant investments) |
| Food & Beverage | NA |
| Fashion/Textiles | NA |
| Construction | NA |
| Financial Services | High (70-95%) |
| Energy/Utilities | Low (0-5%) |

**Calculation methods:**

1. **PCAF Standard** (Quality: varies 1-5)
   - Partnership for Carbon Accounting Financials methodology
   - Asset classes: listed equity, corporate bonds, business loans, project finance, commercial real estate, mortgages, sovereign debt
   - Data needed: investment amount, borrower/investee emissions, attribution factor
   - Quality score per PCAF data quality matrix

2. **Investment-specific method** (Quality: 4/5)
   - Data needed: Scope 1+2 (and ideally Scope 3) of each investee × ownership/attribution share
   - Source: investee sustainability reports, CDP responses

**Emission factor sources:**
- PCAF: Global GHG Accounting and Reporting Standard for the Financial Industry
- CDP: company-reported emissions data
- MSCI, ISS, Bloomberg: estimated emissions for listed companies

---

## Emission Factor Source Summary

| Source | Coverage | Cost | Update Frequency | Quality |
|--------|----------|------|-----------------|---------|
| DEFRA (UK Government) | UK-centric, widely applicable | Free | Annual (June) | High |
| ecoinvent | Global, 18,000+ datasets | Paid license | Regular | Very High |
| ADEME Base Empreinte | France-centric | Free | Regular | High |
| EPA EEIO (USEEIO) | US economy, 400+ sectors | Free | Periodic | Medium |
| EXIOBASE | Multi-regional, 49 countries | Free (academic) | Periodic | Medium-High |
| GHG Protocol tools | Global, sector-specific | Free | Varies | Medium |
| GLEC Framework | Global logistics | Free | Regular | High |
| PCAF | Financial sector | Free | Regular | High |

---

## Data Quality Hierarchy

The GHG Protocol and CSRD both emphasize data quality improvement over time:

| Level | Method | Description | Quality Score |
|-------|--------|-------------|--------------|
| 1 | Supplier-specific | Primary data from supplier, verified/audited | 5/5 |
| 2 | Activity-based (verified) | Physical data (kWh, km, tonnes) from verified sources | 4/5 |
| 3 | Activity-based (unverified) | Physical data from unverified or estimated sources | 3/5 |
| 4 | Average-data | Industry-average emission factors per unit | 3/5 |
| 5 | Spend-based | Financial spend × EEIO emission factors | 2/5 |
| 6 | Extrapolated/proxy | Scaled from partial data or proxy indicators | 1/5 |

**Improvement path:**
- Year 1: Spend-based for all categories (establish baseline)
- Year 2: Activity-based for top 3-5 material categories
- Year 3+: Supplier-specific for top 20 suppliers by emissions contribution

---

## CSRD / ESRS E1 Requirements for Scope 3

Under ESRS E1 (Climate Change), companies subject to CSRD must:
- Report Scope 3 GHG emissions by significant category
- Disclose methodology, emission factors, and data quality per category
- Explain exclusions (any excluded category must be justified as immaterial)
- Set Scope 3 reduction targets aligned with a 1.5C pathway
- Report progress against targets annually
- Phase-in: Scope 3 reporting may be delayed to the second year of CSRD reporting for companies with fewer than 750 employees
