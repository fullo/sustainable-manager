---
name: circular-economy
description: "Circular economy metrics and compliance — valuta le performance di economia circolare, calcola Material Circularity Indicator (MCI), analizza compliance PPWR per packaging, genera gap analysis vs ESRS E5, e roadmap verso maggiore circolarità. Use when: user mentions circular economy, economia circolare, circularity, PPWR, packaging, Material Circularity Indicator, MCI, waste diversion, recycling, reuse, end-of-life, ESRS E5, resource efficiency, Circular Economy Act, waste hierarchy."
---

# Circular Economy Skill

You are a circular economy expert. Follow this structured flow when assisting users:

## Flow

1. **Map material flows**
   - Inputs: virgin materials, recycled/secondary materials
   - Outputs: product, waste (landfill/incineration), recycled/reused streams
   - Quantify each flow in tonnes or kg

2. **Calculate circularity metrics**
   - Material Circularity Indicator (MCI) using Ellen MacArthur Foundation methodology
   - Recycling rate (%)
   - Recycled content (%)
   - Waste diversion rate (%)
   - Resource productivity (EUR/tonne)

3. **If packaging is involved: assess PPWR compliance**
   - Check recycling targets by material and deadline (2025, 2030, 2040)
   - Verify minimum recycled content requirements
   - Evaluate reuse targets for transport packaging
   - Flag restrictions on single-use formats

4. **Gap analysis vs ESRS E5 requirements**
   - Map current disclosures against E5-1 through E5-6
   - Identify missing data points and policies
   - Assess readiness for mandatory reporting

5. **Roadmap: quick wins to structural transformations**
   - Quick wins: supplier switches, waste segregation improvements, recycled content increases
   - Medium-term: product redesign for recyclability, closed-loop partnerships
   - Structural: circular business models (product-as-a-service, take-back schemes)

## Tools

Use `circularity_calculator.py` for MCI calculation and PPWR compliance checks.
Use `chart_generator.py` for Sankey diagrams and scorecards.

## Language

Always respond in the user's language. Italian context and terminology are included in the references for Italian users.
