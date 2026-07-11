# EED Art. 12 — Data Centre Reporting Checklist

Compilable checklist of the information required by Delegated Regulation (EU) 2024/1364 for the annual data centre report (deadline: **15 May**, covering the previous calendar year). One checklist per data centre with installed IT power demand ≥ 500 kW. Last verified: July 2026.

Use it in three passes: (1) mark what is already measured, (2) mark what is derivable from existing meters/BMS/DCIM, (3) what remains is the instrumentation gap.

---

## A. Identification and General Information

- [ ] Data centre name and location (address, Member State)
- [ ] Operator identity and contact
- [ ] Type: enterprise / colocation / co-hosting
- [ ] Year of establishment / major refurbishment
- [ ] Floor area (total, and computer room floor area in m2)
- [ ] Installed IT power demand (kW) — the ≥ 500 kW scope trigger
- [ ] Rated/design capacity vs. capacity in use

## B. Energy

- [ ] Total energy consumption (kWh/year)
- [ ] IT equipment energy consumption (kWh/year)
- [ ] **PUE** (derived: total / IT)
- [ ] Energy from renewable sources (kWh/year), split by:
  - [ ] Renewables with Guarantees of Origin / PPAs (market-based)
  - [ ] On-site generation
- [ ] **REF** — Renewable Energy Factor
- [ ] Waste heat generated and reused (kWh/year), destination of reuse
- [ ] **ERF** — Energy Reuse Factor
- [ ] Backup generation: fuel type and consumption

## C. Cooling and Water

- [ ] Cooling system type(s) (air, liquid, free cooling, district cooling)
- [ ] Temperature set points (supply air / return air)
- [ ] Total water input (m3/year), split potable / non-potable
- [ ] **WUE** — Water Usage Effectiveness
- [ ] Refrigerants in use (type, GWP) — cross-check F-gas Regulation (EU) 2024/573 phase-down

## D. IT Load and Traffic

- [ ] Installed server capacity / utilization where available
- [ ] Data storage capacity (installed, used)
- [ ] Incoming and outgoing data traffic (where measurable)

## E. Governance and Submission

- [ ] Reporting channel identified (national submission channel to the European database)
- [ ] Data owner assigned per section (facility, IT ops, procurement)
- [ ] Evidence retained (meter readings, invoices, BMS/DCIM exports)
- [ ] Colocation: contractual clarity on who reports what (operator reports the facility; customers may need shares for their own Scope 3)
- [ ] Internal deadline set ahead of 15 May
- [ ] Delta check vs. previous year's submission (large variances need explanation)

---

## Common Gaps (from field experience)

| Gap | Workaround while instrumenting |
|-----|-------------------------------|
| No separate IT-load metering (no PUE) | Temporary sub-metering campaign; UPS output as IT-load proxy (flag as estimate) |
| No water metering on cooling towers | Utility invoices at facility level, allocated; flag data quality |
| Waste heat not measured | If no reuse exists, ERF = 0 — state it, don't omit |
| Colocation customer asks for "their" PUE | Provide facility PUE + customer's IT kWh share; per-customer PUE is not a defined KPI |

## Cross-references

- KPI definitions: ISO/IEC 30134 series, EN 50600-4
- Voluntary best practice: EU Code of Conduct for Data Centre Energy Efficiency
- EU Taxonomy activity 8.1 (data processing/hosting): alignment criteria reference the Code of Conduct practices — the same data serves the Taxonomy assessment (see eu-taxonomy-checker skill)
- ESRS: E1 (energy/GHG), E3 (water in water-stressed locations)
