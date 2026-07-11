# Sustainable IT Regulations — Technical Reference

Thresholds, dates, and KPI definitions for EU digital sustainability obligations. Last verified: July 2026.

---

## 1. EED Art. 12 — Data Centre Reporting

**Legal basis**: Energy Efficiency Directive (recast) (EU) 2023/1791, Art. 12 + Delegated Regulation (EU) 2024/1364 (reporting scheme).

### Scope

| Element | Detail |
|---------|--------|
| Threshold | Data centres with **installed IT power demand ≥ 500 kW** |
| Who reports | The data centre operator (owner/colocation provider) |
| Deadline | **15 May each year**, covering the previous calendar year |
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

A Commission delegated act establishing a **data centre sustainability rating scheme** was under consultation in spring 2026 (consultation closed April 2026); adoption was expected Q2 2026 but is **not yet final as of July 2026**. Track before advising on rating-based procurement criteria.

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

**Legal basis**: Regulation (EU) 2024/1689 (AI Act), amended by the Digital Omnibus on AI (adopted June 2026).

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

| Standard | Status (July 2026) | Notes |
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
| **Right to Repair Directive (EU) 2024/1799** | Transposition by **31 July 2026** | Repair obligation beyond legal guarantee at reasonable price/time; covered categories include smartphones, tablets, displays and **servers**; repair information access |
| **Battery Regulation (EU) 2023/1542** | **Battery passport from 18 February 2027** for batteries > 2 kWh | QR code, carbon footprint, recycled content — relevant for UPS and e-mobility fleets |
| **ESPR (EU) 2024/1781 + Digital Product Passport** | DPP registry operational since **19 July 2026**; ICT product groups expected toward **2029** (working plan 2025-2030) | Plan procurement data flows now; no immediate ICT obligation |
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
| **Empowering Consumers Directive (EU) 2024/825 (EmpCo)** | Applicable from **27 September 2026** | Bans generic environmental claims ("green", "eco-friendly", "climate neutral") without recognized excellent performance, and **offset-based neutrality claims**. Applies to "green cloud", "carbon-neutral app/website" marketing |
| **Green Claims Directive** | **Proposal frozen (June 2025)** — not adopted | Do not cite as upcoming law; EmpCo is the operative reference |

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

Note: revised ESRS (2026, applicable FY2027) reduced datapoints — verify each mapping against the current set. Companies below CSRD thresholds meet these data through customer requests capped at VSME content.
