# Sustainable IT Regulations — Technical Reference

Thresholds, dates, and KPI definitions for EU digital sustainability obligations. Last verified: October 2026.

---

## 1. EED Art. 12 — Data Centre Reporting

**Legal basis**: Energy Efficiency Directive (recast) (EU) 2023/1791, Art. 12 + Delegated Regulation (EU) 2024/1364 (reporting scheme).

### Scope

| Element | Detail |
|---------|--------|
| Threshold | Data centres with **installed IT power demand ≥ 500 kW** |
| Who reports | The data centre operator (owner/colocation provider) |
| Deadline | **15 May each year** (from 2025; the first report was due 15 September 2024), covering the previous calendar year |
| Where | European database on data centres (national channel per Member State) |

### Key KPIs

| KPI | Meaning |
|-----|---------|
| PUE | Power Usage Effectiveness — total facility energy / IT equipment energy |
| WUE | Water Usage Effectiveness — water use / IT equipment energy |
| ERF | Energy Reuse Factor — share of energy reused (e.g., heat recovery) |
| REF | Renewable Energy Factor — share of renewable energy |

Plus: total energy consumption, IT equipment energy, temperature set points, waste heat, water volumes, installed/used capacity, data traffic and storage (per DR 2024/1364 annex).

### Status of the EU rating scheme

The Commission adopted on **21 September 2026** a delegated regulation (C(2026) 3472) establishing the **data centre sustainability rating scheme** (data centres with at least 500 kW IT power demand): A-G classes for PUE and WUE plus indicators on energy sourcing, grid flexibility and waste-heat reuse; first electronic labels due by **15 August 2027**. It is in the two-month Parliament/Council scrutiny period (not yet in force at 2 October 2026), so cite it as adopted-but-pending. In parallel, a public consultation on **minimum performance standards** for data centres runs until 14 December 2026, with the Commission planning to adopt a proposal in Q2 2027.

### Reference standards
- EN 50600 series (data centre facilities)
- ISO/IEC 30134 series (KPIs: PUE, WUE, ERF, REF)
- EU Code of Conduct for Data Centre Energy Efficiency (voluntary)

### F-gas Regulation (EU) 2024/573 — cooling side

Directly relevant to any data centre or server room with mechanical cooling:
- Progressive **HFC quota phase-down** to full phase-out by 2050; refrigerant prices rising as quotas shrink
- **GWP limits on new equipment** phased in from 2027 onward for AC/chiller categories — check before any cooling CapEx
- **Mandatory leak checks and record keeping** for equipment above CO2e thresholds; certified technicians required
- Practical advice: new cooling investments should target low-GWP refrigerants (R-32 transitional, natural refrigerants preferred) or the equipment risks early obsolescence and costly service

### EU Taxonomy — activity 8.1 (Data processing, hosting and related activities)

For companies assessing Taxonomy alignment (see eu-taxonomy-checker skill):
- Listed in the Climate Delegated Act as contributing to **climate change mitigation**
- Substantial contribution criteria reference the implementation of the **EU Code of Conduct for Data Centre Energy Efficiency** expected practices (verified by third party)
- DNSH includes refrigerant GWP conditions and waste/WEEE handling
- The same data collected for EED Art. 12 reporting largely serves the Taxonomy assessment

---

## 2. AI Act — Energy and Sustainability Aspects (as amended by the Digital Omnibus)

**Legal basis**: Regulation (EU) 2024/1689 (AI Act), amended by the Digital Omnibus on AI, Regulation (EU) 2026/1744 (OJ 24 July 2026, in force since 27 July 2026). Article 50 transparency obligations keep their 2 August 2026 date, but providers of generative AI systems placed on the market before 2 August 2026 have until **2 December 2026** to comply with the Art. 50(2) marking obligation; the new Art. 5 prohibitions added by the Omnibus apply from 2 December 2026.

### Timeline (post Digital Omnibus)

| Obligation | Date |
|-----------|------|
| GPAI model obligations, incl. **technical documentation with training compute and energy consumption** | In force since **2 August 2025** (unchanged) |
| High-risk AI obligations — standalone systems (Annex III) | Postponed to **2 December 2027** |
| High-risk AI obligations — AI embedded in regulated products | Postponed to **2 August 2028** |

### Energy-relevant points
- GPAI = models above the indicative **10^23 FLOP** training-compute threshold (per Commission GPAI guidelines)
- Providers must document training resources, including energy consumption (Annex XI documentation)
- Systemic-risk GPAI (≥10^25 FLOP) has additional obligations
- Deployers: no direct energy-reporting duty, but AI energy/water use feeds ESRS E1/E3 where material

---

## 3. Software & Cloud Measurement Standards (voluntary)

| Standard | Status (last verified July 2026) | Notes |
|----------|--------------------|-------|
| **SCI** — Software Carbon Intensity | **ISO/IEC 21031:2024** | `SCI = ((E × I) + M) / R` — rate per functional unit; not summable into inventories |
| **SCI for AI** | **Ratified by GSF, December 2025** | Provider scope and Consumer scope; covers training and inference |
| **SCI for Web** | Draft — first version expected Q4 2026 | Until release, use SWD model / CO2.js and label as estimate |
| **SWI** — Software Water Intensity | Pre-draft (2026) | Links to ESRS E3; do not cite as available |
| **Real Time Cloud** (GSF) | Ratified 2025 | Region-level PUE/WUE/carbon-free-energy metadata from cloud providers |
| **Tech Carbon Standard** | Updated Sept 2025 | Upstream/Direct/Indirect/Downstream; new Upstream "Content" subcategory (AI models, data) |
| **W3C Web Sustainability Guidelines** | W3C **Group Note (draft)** | ~90+ recommendations by role; best practice, NOT a standard |
| **GHG Protocol ICT Sector Guidance** | Current; core GHGP standards under revision | Use for corporate inventory totals |

---

## 4. Devices — Ecodesign, Labelling, Repair

| Instrument | Key dates | Content |
|-----------|-----------|---------|
| **Energy label smartphones/tablets** (Reg. 2023/1669 + ecodesign Reg. 2023/1670) | Applicable since **20 June 2025** | Energy class, battery endurance, **repairability index**, EPREL registration |
| **Right to Repair Directive (EU) 2024/1799** | Transposition deadline **31 July 2026** (missed by several Member States, Italy included: draft decree AG 426 transmitted to Parliament on 9 July 2026, final Council of Ministers approval 16 September 2026, not in the Gazzetta Ufficiale up to 1 October 2026) | Repair obligation beyond legal guarantee at reasonable price/time; covered categories include smartphones, tablets, displays and **servers** (Annex II; Delegated Directive (EU) 2026/74 added domestic local space heaters); repair information access |
| **Battery Regulation (EU) 2023/1542** | **Battery passport from 18 February 2027** for LMT batteries, industrial batteries > 2 kWh and EV batteries (Art. 77); battery due diligence obligations postponed to **18 August 2027** (Reg. (EU) 2025/1561) | QR code, carbon footprint, recycled content — relevant for UPS and e-mobility fleets |
| **ESPR (EU) 2024/1781 + Digital Product Passport** | DPP registry (Implementing Reg. (EU) 2026/1778, OJ 17 July 2026) live since **20 July 2026** (rules in force 6 August 2026); no dedicated ICT product group in the working plan 2025-2030 (COM(2025) 187): ICT is covered by horizontal measures on repairability (**2027**) and recycled content/recyclability of electronics (**2029**) | Plan procurement data flows now; no immediate ICT obligation |
| **WEEE Directive 2012/19/EU** | In force | E-waste collection/recovery; national registers for producers |

### WEEE / e-waste — operational flow

For the IT estate (not just producers placing equipment on the market):
1. **Inventory before disposal**: model, age, condition, data-bearing components
2. **Reuse cascade first**: internal redeployment → employee purchase/donation programs → certified refurbisher (with data sanitization certificate, e.g. per IEEE 2883 / NIST 800-88)
3. **Certified WEEE channel** for what remains: collection through the producer take-back scheme or authorized treatment facility; keep the disposal documentation (formulari) — it evidences ESRS E5 resource outflows
4. **KPIs**: % devices reused vs recycled, e-waste diverted from landfill, average device lifetime
5. **Producers/importers of equipment**: registration in the national WEEE register, financing of collection/treatment, marking obligations (crossed-out bin symbol)

---

## 5. European Accessibility Act (EAA)

**Legal basis**: Directive (EU) 2019/882, applicable since **28 June 2025** (products placed on the market / services provided from that date; transitional window for pre-existing service contracts up to 2030).

| Element | Detail |
|---------|--------|
| Products in scope | Consumer computing hardware and OS, self-service terminals (ATM, ticketing), smartphones, e-readers |
| Services in scope | E-commerce, consumer banking, electronic communications, e-books, transport information services |
| Technical reference | EN 301 549 (which incorporates WCAG 2.1 AA for web/apps) |
| Exemptions | Microenterprises providing services (<10 employees and <EUR 2M turnover); disproportionate burden clause with documentation |
| ESRS linkage | S4 (consumers and end-users) — accessibility is the social pillar of sustainable IT |
| Italy | Recepimento D.Lgs. 82/2022; AgID supervisory role; integrates the pre-existing Legge Stanca (L. 4/2004) regime |

---

## 6. Green Claims on IT Products and Services

| Instrument | Status | Effect |
|-----------|--------|--------|
| **Empowering Consumers Directive (EU) 2024/825 (EmpCo)** | **Applicable since 27 September 2026** (neither the directive nor Italy's D.Lgs. 30/2026 contains a transitional clause for stock) | Bans generic environmental claims ("green", "eco-friendly", "energy efficient") without recognized excellent performance; **claims based on GHG offsetting that a product has a neutral, reduced or positive GHG impact** ("climate neutral", "CO2 neutral"); uncertified sustainability labels; whole-product claims covering only one aspect; and **future-performance claims** ("net zero by 2030") without a detailed, realistic implementation plan verified by an independent third-party expert. Applies to "green cloud", "carbon-neutral app/website" marketing toward consumers |
| **Green Claims Directive** | **Proposal COM(2023) 166 pending (stalled in Council), not withdrawn** — not adopted | Do not cite as upcoming law; EmpCo is the operative reference |

Typical IT claims to audit: "100% green energy" (check market-based evidence quality), "carbon-neutral hosting" (offset-based → banned wording), "most sustainable laptop" (comparative claims need substantiation).

---

## 7. CSRD/ESRS Linkage for IT Data

| IT data | ESRS datapoint |
|---------|----------------|
| Data centre / office IT energy consumption | E1 energy consumption and mix |
| Cloud emissions | E1 Scope 3 (GHG Protocol cat. 1 or 8 depending on control model) |
| Device fleet embodied carbon | E1 Scope 3 cat. 1/2 (purchased/capital goods) |
| E-waste, device reuse/refurbishment | E5 resource outflows |
| Data centre water use | E3 (water), especially in water-stressed locations |
| AI training energy/water | E1/E3 where material; AI Act documentation as source |

Note: revised ESRS (Delegated Reg. (EU) 2026/1563, OJ 21 Sept 2026; mandatory from FY2027, FY2026 optional) reduced datapoints — verify each mapping against the current set. For financial years beginning on or after 1 January 2027, suppliers with up to 1,000 employees can be asked only for VSME Annex II essential datapoints (Delegated Reg. (EU) 2026/1560), limited to the requester's own CSRD needs.
