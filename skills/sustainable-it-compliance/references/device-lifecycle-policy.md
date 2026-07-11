# Device Lifecycle Policy — Generator Guide

Structure and content blocks for generating a corporate device lifecycle policy (laptops, smartphones, tablets, monitors, peripherals; adaptable to servers). Ask the user for fleet size, current refresh cycle, and procurement channel, then assemble the policy from these blocks. Embodied carbon typically dominates the device footprint, so lifetime extension is the single biggest lever. Last verified: July 2026.

---

## 1. Procurement Criteria

- **Certifications**: require at least one of EPEAT (Gold preferred), TCO Certified, Blauer Engel; for the Italian PA, CAM ICT compliance is mandatory (Codice Appalti)
- **Repairability**: minimum repairability index (EU energy label for smartphones/tablets), availability of spare parts and repair documentation (Right to Repair, Dir. (EU) 2024/1799 — servers included)
- **PCF sheets**: request the manufacturer's Product Carbon Footprint per model; use `assets/benchmarks/device-embodied-carbon.json` when unavailable
- **Refurbished quota**: set a target share of refurbished/remanufactured purchases (suggested starting point: 20-30% of non-critical roles), with certified vendors and warranty ≥ 2 years
- **Right-sizing**: match device tier to role profile (avoid workstation-class laptops for office work)

## 2. Use and Maintenance

- Default power management profiles enforced via MDM (sleep, display timeout)
- **Repair-first rule**: below a repair-cost threshold (suggested: 40-50% of replacement cost), repair instead of replace; track mean time in service
- Battery care policies (charge thresholds where supported) and mid-life battery replacement as default for smartphones/laptops instead of device swap
- Protective equipment (cases) as standard issue — extends life measurably

## 3. Refresh Cycle

- Extend default cycles: laptops 3→4-5 years, smartphones 2→3-4 years, monitors 5→7+ years, servers per capacity planning not calendar
- Replace on **failure/inadequacy, not on schedule**: annual fleet review flags devices that actually need replacement
- Cascade reuse internally: newest devices to demanding roles, cascaded devices to lighter roles

## 4. End-of-Life (reuse cascade → WEEE)

1. Internal redeployment pool
2. Employee purchase program / donation to schools and non-profits (with fiscal notes for Italy)
3. Certified refurbisher buy-back (data sanitization certificate per NIST 800-88 / IEEE 2883 required)
4. Certified WEEE/RAEE channel for the remainder; retain disposal documentation (evidences ESRS E5)
- Never stockpile: drawer-parked devices lose reuse value at ~20-30% per year

## 5. Data Security Integration

- Sanitization standard and certificate mandatory before any device leaves the organization
- Asset register updated at every lifecycle transition (issue, repair, cascade, exit)
- Encryption-by-default makes fast, safe decommissioning possible — note the synergy, it disarms the most common security objection to reuse

## 6. KPIs (feed ESRS E5 and the board dashboard)

| KPI | Target suggestion |
|-----|-------------------|
| Average device lifetime (by category) | +1 year vs current baseline |
| % refurbished on total purchases | 20-30% year 1, growing |
| % devices reused (cascade+donation+refurb) vs recycled | > 60% |
| E-waste through certified channels | 100%, documented |
| Devices per employee | monitor for creep |
| Repair vs replace ratio | growing |

## 7. Governance

- Policy owner: IT/CIO with sustainability co-sign (CSO)
- Review cycle: annual, aligned with the fleet review
- Exceptions: documented, time-boxed, approved by the policy owner
- Link procurement KPIs to supplier scorecards (see supplier-engagement skill)
