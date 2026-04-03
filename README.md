# Sustainable Manager - Claude Code Plugin

[![Skill Version](https://img.shields.io/badge/skill-v2.0-blue)](skills/sustainable-manager/SKILL.md)
[![Skills](https://img.shields.io/badge/skills-11-green)](skills/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/format-agentskills.io-purple)](https://agentskills.io/)

Plugin per Claude Code che aggiunge 11 skill di consulenza sulla sostenibilita con approccio science-based.

## Skills

### Core
- **sustainable-manager** - Analisi documenti, report ESG, LCA/EPD, greenwashing detection, consulenza Socratica, visualizzazioni, assessment ESRS, procurement sostenibile

### Tier 1 — Compliance & Reporting
- **eu-regulation-matrix** - Matrice di applicabilita normativa EU (CSRD, CSDDD, CBAM, Taxonomy, PPWR, EUDR, SFDR)
- **eu-taxonomy-checker** - Verifica eligibilita e allineamento EU Taxonomy (NACE, TSC, DNSH)
- **scope3-mapper** - Mapping 15 categorie Scope 3, stima emissioni, template fornitori
- **double-materiality** - Double Materiality Assessment guidata (ESRS 1 post-Omnibus, IRO scoring)

### Tier 2 — Emerging Regulations
- **cbam-compliance** - CBAM fase definitiva: prodotti in scope, emissioni embedded, certificati
- **biodiversity-screener** - Screening rischi biodiversita (TNFD LEAP, ESRS E4, SBTN)
- **circular-economy** - Metriche circolarita (MCI), compliance PPWR, ESRS E5

### Tier 3 — Strategic Tools
- **cross-framework-mapper** - Sovrapposizione data point tra framework (ESRS, GRI, ISSB, Taxonomy, CBAM, SFDR)
- **transition-plan-builder** - Piano di transizione climatica (SBTi, ESRS E1, pathway settoriali)
- **supplier-engagement** - Questionari ESG fornitori modulari (Scope 3, CSDDD, CBAM, Taxonomy)

## Framework supportati

ESRS/CSRD, GRI, SASB/ISSB, TCFD, TNFD, SDGs, SBTi, SBTN, EU Taxonomy, CBAM, CSDDD, PPWR, EUDR, SFDR, ISO 14040/14044, ISO 20400

## Installazione

### Da marketplace

```bash
claude plugin install sustainable-manager@fullo-plugins
```

### Da GitHub

```bash
git clone https://github.com/fullo/sustainable-manager.git
claude plugin add /path/to/sustainable-manager
```

## Uso

Le skill si attivano automaticamente in base al contesto. Puoi anche invocarle esplicitamente:

```
/sustainable-manager:sustainable-manager       # Core: analisi documenti, LCA, greenwashing
/sustainable-manager:eu-regulation-matrix      # Quali regolamenti si applicano?
/sustainable-manager:eu-taxonomy-checker       # Eligibilita/allineamento EU Taxonomy
/sustainable-manager:scope3-mapper             # Mapping Scope 3 + template fornitori
/sustainable-manager:double-materiality        # Assessment doppia materialita
/sustainable-manager:cbam-compliance           # Compliance CBAM importazioni
/sustainable-manager:biodiversity-screener     # Screening rischi biodiversita
/sustainable-manager:circular-economy          # Metriche economia circolare + PPWR
/sustainable-manager:cross-framework-mapper    # Sovrapposizione dati tra framework
/sustainable-manager:transition-plan-builder   # Piano transizione climatica
/sustainable-manager:supplier-engagement       # Questionari ESG fornitori
```

## Struttura

```
sustainable-manager/
├── .claude-plugin/
│   └── plugin.json
├── skills/
│   ├── sustainable-manager/        # Core skill + shared assets
│   │   ├── SKILL.md
│   │   ├── references/             # 6 reference files
│   │   ├── scripts/                # chart_generator.py, esrs_assessment.py
│   │   └── assets/                 # benchmarks + sector templates
│   ├── eu-regulation-matrix/       # + 1 reference
│   ├── eu-taxonomy-checker/        # + 2 references
│   ├── scope3-mapper/              # + 2 references + scope3_calculator.py
│   ├── double-materiality/         # + 2 references
│   ├── cbam-compliance/            # + 2 references
│   ├── biodiversity-screener/      # + 2 references
│   ├── circular-economy/           # + 2 references + circularity_calculator.py
│   ├── cross-framework-mapper/     # + 2 references
│   ├── transition-plan-builder/    # + 2 references
│   └── supplier-engagement/        # + 2 references + supplier_scorer.py
├── docs/superpowers/specs/         # Design documentation
├── package.json
└── README.md
```

## Requisiti

- Claude Code CLI
- Python 3.8+ (per visualizzazioni e calcolatori)
- matplotlib, numpy (per i grafici)

## Licenza

MIT
