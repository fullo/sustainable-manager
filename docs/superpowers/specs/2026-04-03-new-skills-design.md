# Sustainable Manager Plugin — 10 New Skills Design

**Date**: 2026-04-03
**Status**: Approved
**Architecture**: Approach A — Skill separate leggere, reference condivisi nella skill principale

## Decisions

- **10 skill separate**, ognuna con il proprio `SKILL.md` in `skills/<skill-name>/`
- **Contesto italiano + EU** mantenuto come pattern esistente
- **Reference condivisi** restano in `skills/sustainable-manager/references/`; ogni nuova skill aggiunge solo i propri reference specifici
- **Script Python** nuovi solo dove serve calcolo strutturato (scope3, circularity, supplier scoring)
- **Visualizzazioni** usano `chart_generator.py` esistente via path relativo

## Skill Overview

| # | Tier | Skill ID | Scopo | Script | Reference nuovi |
|---|------|----------|-------|--------|-----------------|
| 1 | 1 | `eu-regulation-matrix` | Matrice applicabilita normativa EU | — | regulation-thresholds.md |
| 2 | 1 | `eu-taxonomy-checker` | Eligibilita e allineamento EU Taxonomy | — | taxonomy-criteria.md, taxonomy-italian-context.md |
| 3 | 1 | `scope3-mapper` | Mapping 15 categorie Scope 3 + template fornitori | scope3_calculator.py | scope3-categories.md, scope3-supplier-templates.md |
| 4 | 1 | `double-materiality` | DMA guidata ESRS post-Omnibus | — | dma-methodology.md, dma-sector-iro.md |
| 5 | 2 | `cbam-compliance` | Compliance CBAM fase definitiva | — | cbam-product-scope.md, cbam-italian-context.md |
| 6 | 2 | `biodiversity-screener` | Screening rischi biodiversita TNFD/ESRS E4 | — | biodiversity-methodology.md, biodiversity-italian-context.md |
| 7 | 2 | `circular-economy` | Metriche circolarita + compliance PPWR | circularity_calculator.py | circular-metrics.md, circular-italian-context.md |
| 8 | 3 | `cross-framework-mapper` | Sovrapposizione data point tra framework | — | framework-overlap-matrix.md, framework-overlap-italian.md |
| 9 | 3 | `transition-plan-builder` | Climate transition plan SBTi/ESRS E1 | — | transition-plan-guide.md, transition-plan-italian-context.md |
| 10 | 3 | `supplier-engagement` | Questionari fornitori ESG modulari | supplier_scorer.py | supplier-questionnaire-modules.md, supplier-engagement-italian-context.md |

## Benchmarks / Assets nuovi

- `assets/benchmarks/scope3-sector-profiles.json` — % Scope 3 per categoria e settore

## Tier 1 — Design dettagliato

### 1. eu-regulation-matrix

**Trigger**: "Quali regolamenti si applicano?", CSRD scope, CSDDD, CBAM, PPWR, EUDR, Omnibus, "devo reportare?"

**Flusso**: Domande progressive (dimensione, fatturato, settore, geografia, attivita) → matching regolamenti → matrice output.

**Reference `regulation-thresholds.md`**: Tabella soglie per ogni regolamento:
- CSRD originale (250+ dip, 40M+ rev, 20M+ assets — 2 su 3) + post-Omnibus (1000+ dip, 450M+ rev)
- CSDDD (5000+ dip, 1.5B+ rev, da mid-2029)
- CBAM (importatori dei 6 settori, soglia de minimis 50t)
- EU Taxonomy Art. 8 (chi rientra in CSRD)
- PPWR (produttori/importatori packaging, da agosto 2026)
- EUDR (7 commodity: soia, olio di palma, cacao, caffe, gomma, legno, bovini)
- SFDR (partecipanti mercati finanziari)

**Output**: Matrice markdown + flag urgenze + link a skill specifiche per approfondimento.

### 2. eu-taxonomy-checker

**Trigger**: EU Taxonomy, tassonomia, eligibilita, allineamento, NACE, technical screening criteria, DNSH, CapEx/OpEx taxonomy-aligned

**Flusso 3 step**:
1. Eligibilita: codice NACE → attivita elencate nel Regolamento Delegato?
2. Contributo sostanziale: quale obiettivo ambientale? Technical screening criteria soddisfatti?
3. DNSH + minimum safeguards: verifica non-danno agli altri 5 obiettivi + OECD/UNGP

**Reference `taxonomy-criteria.md`**: 6 obiettivi ambientali, criteri screening per settori principali (energia, manifattura, edilizia, trasporti, ICT), soglie quantitative, criteri DNSH.

**Reference `taxonomy-italian-context.md`**: Consob disclosure, Banca d'Italia requisiti, settori italiani ad alta eligibilita.

**Output**: Per attivita: eligibile/allineata + % CapEx/OpEx/Revenue + heatmap + checklist DNSH.

### 3. scope3-mapper

**Trigger**: Scope 3, emissioni indirette, supply chain emissions, 15 categorie GHG Protocol, fornitori

**Flusso**: Settore → categorie materiali → metodo calcolo → stima → template fornitori.

**Reference `scope3-categories.md`**: 15 categorie, metodi (spend-based, activity-based, average-data, supplier-specific), emission factor sources (DEFRA, ecoinvent, ADEME), materialita per settore.

**Reference `scope3-supplier-templates.md`**: Questionario fornitori EN + IT, spiegazioni semplificate.

**Asset `scope3-sector-profiles.json`**: Breakdown % per categoria per settore.

**Script `scope3_calculator.py`**: Input spesa per categoria → emission factor → output tCO2e. Include fattori DEFRA aggiornati per le categorie principali.

**Output**: Tabella categorie + bar chart breakdown + template fornitori + roadmap miglioramento qualita dati.

### 4. double-materiality

**Trigger**: doppia materialita, DMA, IRO, materialita d'impatto/finanziaria, ESRS 1

**Flusso 5 fasi Socratiche**:
1. Contesto aziendale (settore, dimensione, value chain)
2. Identificazione stakeholder (interni + esterni)
3. Long-list IRO per topic ESRS (con pre-mapping settoriale)
4. Scoring (severity × likelihood per impatti; magnitude × likelihood per rischi finanziari)
5. Matrice + lista ESRS materiali

**Reference `dma-methodology.md`**: Approccio top-down post-Omnibus, Information Materiality Filter, scale di scoring, soglie, documentazione richiesta da auditor.

**Reference `dma-sector-iro.md`**: IRO pre-mappati per 5 settori. Per ogni topic ESRS: impatti, rischi, opportunita tipiche.

**Output**: Scatter plot materialita + tabella topic materiali + lista ESRS da reportare + documentazione processo.

## Tier 2 — Design dettagliato

### 5. cbam-compliance

**Trigger**: CBAM, emissioni embedded, importazioni extra-UE, certificati CBAM, cemento/acciaio/alluminio/fertilizzanti/idrogeno/elettricita

**Flusso**: Prodotti importati → codici CN → in scope? → emissioni embedded (dirette + indirette) → certificati necessari → scadenze.

**Reference `cbam-product-scope.md`**: Prodotti coperti + codici CN, metodi calcolo (dati reali / default UE / default paese), soglia de minimis, fasi transitoria vs definitiva.

**Reference `cbam-italian-context.md`**: Agenzia Dogane, procedura dichiarante autorizzato, interazione EU ETS.

**Output**: Checklist prodotti + stima certificati (tCO2e × prezzo ETS) + timeline + gap list dati + template richiesta fornitori extra-UE.

### 6. biodiversity-screener

**Trigger**: biodiversita, TNFD, SBTN, ESRS E4, habitat, ecosistemi, deforestazione, EUDR, Natura 2000

**Flusso LEAP semplificato**: Locate (dove opera) → Evaluate (dipendenze/impatti) → Assess (rischi/opportunita) → Prepare (azioni/disclosure).

**Reference `biodiversity-methodology.md`**: TNFD, SBTN 5 step, driver perdita biodiversita per settore, strumenti (IBAT, ENCORE, STAR), ESRS E4 requirements.

**Reference `biodiversity-italian-context.md`**: Rete Natura 2000 Italia (2600+ siti, 19% territorio), Strategia Nazionale 2030, ISPRA, settori ad alta esposizione.

**Output**: Matrice esposizione + mappa dipendenze natura + gap vs ESRS E4 + top 3 azioni + radar chart.

### 7. circular-economy

**Trigger**: economia circolare, PPWR, packaging, MCI, riciclo, riuso, ESRS E5, Circular Economy Act

**Flusso**: Mappatura flussi materiali → metriche circolarita → assessment PPWR → gap ESRS E5 → roadmap.

**Reference `circular-metrics.md`**: MCI formula (Ellen MacArthur), metriche ESRS E5, target PPWR per materiale e scadenza, gerarchia rifiuti EU.

**Reference `circular-italian-context.md`**: CONAI e consorzi filiera, codici CER, target nazionali, distretti simbiosi industriale, incentivi fiscali.

**Script `circularity_calculator.py`**: Input massa vergine/riciclata/waste → MCI score 0-1 + breakdown.

**Output**: Sankey diagram flussi + scorecard circolarita + compliance matrix PPWR + roadmap prioritizzata.

## Tier 3 — Design dettagliato

### 8. cross-framework-mapper

**Trigger**: mappatura framework, sovrapposizione dati, evitare duplicazione, data point condivisi

**Flusso**: Seleziona regolamenti applicabili → matrice sovrapposizione per topic → mapping data point specifici.

**Reference `framework-overlap-matrix.md`**: ~80 data point principali mappati su ESRS, GRI, ISSB/SASB, EU Taxonomy, CBAM, SFDR.

**Reference `framework-overlap-italian.md`**: Mapping con D.Lgs. 254/2016, Consob, OIC, Banca d'Italia.

**Output**: Heatmap data point × framework + efficienza report ("30 data point coprono 85% di 4 framework") + priorita raccolta dati.

### 9. transition-plan-builder

**Trigger**: piano transizione, decarbonizzazione, net-zero, SBTi, roadmap climatica, ESRS E1 transition plan

**Flusso 6 fasi**: Baseline emissioni → benchmark settoriale SBTi → leve riduzione → target setting → milestones + CapEx → governance.

**Reference `transition-plan-guide.md`**: Struttura TPT Framework + ESRS E1-1, pathway settoriali SBTi, leve decarbonizzazione, criteri credibilita.

**Reference `transition-plan-italian-context.md`**: PNIEC target Italia, incentivi (comunita energetiche, certificati bianchi), settori hard-to-abate italiani.

**Output**: Executive summary + waterfall chart riduzione + timeline milestones + gap vs SBTi + template documento completo.

### 10. supplier-engagement

**Trigger**: coinvolgimento fornitori, questionario fornitori, due diligence, CSDDD, value chain data, codice condotta

**Flusso**: Scopo raccolta dati → selezione moduli → personalizzazione → genera template → scoring risposte.

**Reference `supplier-questionnaire-modules.md`**: Moduli componibili (Ambientale, Sociale, Governance, CBAM, Taxonomy). Domande EN + IT, scala, peso, evidenza richiesta.

**Reference `supplier-engagement-italian-context.md`**: Contesto PMI italiane, semplificazione micro-imprese, Ecovadis/CDP, consorzi/distretti, D.Lgs. 231/2001.

**Script `supplier_scorer.py`**: Risposte JSON → score pesati per area → classificazione fornitori (leader/compliant/at-risk/critical).

**Output**: Questionario personalizzato EN+IT + lettera accompagnamento + scoring matrix + radar per fornitore + risk heatmap.

## Directory Structure finale

```
skills/
├── sustainable-manager/           # ESISTENTE — invariata
│   ├── SKILL.md
│   ├── references/
│   ├── scripts/
│   └── assets/
├── eu-regulation-matrix/          # TIER 1
│   ├── SKILL.md
│   └── references/
│       └── regulation-thresholds.md
├── eu-taxonomy-checker/           # TIER 1
│   ├── SKILL.md
│   └── references/
│       ├── taxonomy-criteria.md
│       └── taxonomy-italian-context.md
├── scope3-mapper/                 # TIER 1
│   ├── SKILL.md
│   ├── references/
│   │   ├── scope3-categories.md
│   │   └── scope3-supplier-templates.md
│   └── scripts/
│       └── scope3_calculator.py
├── double-materiality/            # TIER 1
│   ├── SKILL.md
│   └── references/
│       ├── dma-methodology.md
│       └── dma-sector-iro.md
├── cbam-compliance/               # TIER 2
│   ├── SKILL.md
│   └── references/
│       ├── cbam-product-scope.md
│       └── cbam-italian-context.md
├── biodiversity-screener/         # TIER 2
│   ├── SKILL.md
│   └── references/
│       ├── biodiversity-methodology.md
│       └── biodiversity-italian-context.md
├── circular-economy/              # TIER 2
│   ├── SKILL.md
│   ├── references/
│   │   ├── circular-metrics.md
│   │   └── circular-italian-context.md
│   └── scripts/
│       └── circularity_calculator.py
├── cross-framework-mapper/        # TIER 3
│   ├── SKILL.md
│   └── references/
│       ├── framework-overlap-matrix.md
│       └── framework-overlap-italian.md
├── transition-plan-builder/       # TIER 3
│   ├── SKILL.md
│   └── references/
│       ├── transition-plan-guide.md
│       └── transition-plan-italian-context.md
└── supplier-engagement/           # TIER 3
    ├── SKILL.md
    ├── references/
    │   ├── supplier-questionnaire-modules.md
    │   └── supplier-engagement-italian-context.md
    └── scripts/
        └── supplier_scorer.py
```

## Implementation Order

1. Tier 1: eu-regulation-matrix, eu-taxonomy-checker, scope3-mapper, double-materiality
2. Tier 2: cbam-compliance, biodiversity-screener, circular-economy
3. Tier 3: cross-framework-mapper, transition-plan-builder, supplier-engagement
4. Update plugin.json (version bump to 2.0.0), package.json, README.md
5. Aggiornare scope3-sector-profiles.json in assets/benchmarks/
6. Commit e push
