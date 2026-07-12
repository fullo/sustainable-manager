# Sustainable Manager - Claude Code Plugin

[![Skill Version](https://img.shields.io/badge/skill-v2.6-blue)](skills/sustainable-manager/SKILL.md)
[![Skills](https://img.shields.io/badge/skills-12-green)](skills/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/format-agentskills.io-purple)](https://agentskills.io/)

Plugin per Claude Code che aggiunge 12 skill di consulenza sulla sostenibilita con approccio science-based.

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
- **sustainable-it-compliance** - Compliance IT sostenibile (EED art. 12 data centre, AI Act/Digital Omnibus, SCI/ISO 21031, Right to Repair, DPP, green claims IT)

## Framework supportati

ESRS/CSRD, GRI, SASB/ISSB, TCFD, TNFD, SDGs, SBTi, SBTN, EU Taxonomy, CBAM, CSDDD, PPWR, EUDR, SFDR, ISO 14040/14044, ISO 20400, EED art. 12, AI Act, SCI (ISO/IEC 21031), Tech Carbon Standard

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

## Aggiornamento

```bash
claude plugin update sustainable-manager@fullo-plugins
```

Il sistema plugin usa gli hash dei commit git come versione. Non c'e notifica automatica di nuove versioni: esegui il comando sopra periodicamente per restare aggiornato.

## Documentazione

Sito e manuale (in inglese) su **[fullo.github.io/sustainable-manager](https://fullo.github.io/sustainable-manager/)**:

- **[Landing](https://fullo.github.io/sustainable-manager/)** — le 12 skill, copertura normativa (stato luglio 2026), installazione e uso
- **[Manual](https://fullo.github.io/sustainable-manager/manual.html)** — quale skill per quale domanda, scenari realistici, caso di studio end-to-end (data centre EED, SCI, cloud, device policy, KPI board), reference degli strumenti

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
/sustainable-manager:sustainable-it-compliance # Compliance IT sostenibile (EED, AI Act, SCI)
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
│   │   ├── scripts/                # chart_generator.py, esrs_assessment.py, analysis_dashboard.py
│   │   └── assets/                 # benchmarks, sector templates, report-analysis template + schema
│   ├── eu-regulation-matrix/       # + 1 reference
│   ├── eu-taxonomy-checker/        # + 2 references
│   ├── scope3-mapper/              # + 2 references + scope3_calculator.py
│   ├── double-materiality/         # + 2 references
│   ├── cbam-compliance/            # + 2 references
│   ├── biodiversity-screener/      # + 2 references
│   ├── circular-economy/           # + 2 references + circularity_calculator.py
│   ├── cross-framework-mapper/     # + 2 references
│   ├── transition-plan-builder/    # + 2 references
│   ├── supplier-engagement/        # + 2 references + supplier_scorer.py
│   └── sustainable-it-compliance/  # + 5 references + sci_calculator.py + benchmarks
├── docs/                           # Sito GitHub Pages (landing + manuale, EN)
│   ├── index.html
│   ├── manual.html
│   ├── style.css
│   └── superpowers/specs/          # Design documentation
├── package.json
└── README.md
```

## Requisiti

- Claude Code CLI
- Python 3.8+ (per visualizzazioni e calcolatori)
- matplotlib, numpy (per i grafici)

## Changelog

### v2.6.2 (luglio 2026) — Copertina del libro

- Il box "The Book" sulla landing mostra la copertina del libro (ospitata localmente in `docs/assets/`, layout responsive con alt text)

### v2.6.1 (luglio 2026) — Il libro sul sito

- La landing promuove il libro **[Sustainable IT — Il metodo pratico per la sostenibilità digitale](https://sustainableit.it)** (sezione dedicata "The Book" con link in nav), il caso di studio IT dichiara di seguirne il metodo, e sustainableit.it è nel footer di tutte le pagine

### v2.6.0 (luglio 2026) — Analisi report: template, schema e dashboard comparativa

- **Output standardizzato dell'analisi**: nuovo [`report-analysis-template.md`](skills/sustainable-manager/assets/templates/report-analysis-template.md) (formato di output per analizzare un report *esistente* — distinto dai `template-<settore>.md` che servono a *costruirlo* — con regola anti-fabbricazione: ogni KPI riporta pagina + citazione) e [`report-analysis-schema.json`](skills/sustainable-manager/assets/schemas/report-analysis-schema.json) (contratto machine-readable)
- **Dashboard comparativa**: [`analysis_dashboard.py`](skills/sustainable-manager/scripts/analysis_dashboard.py) genera una dashboard HTML self-contained da uno o piu report (quadrante completezza x severita greenwashing, matrice criticita, card per report), theme-aware e accessibile (WCAG AA: fallback `<details>` agli hover, contrasti verificati, colore = severita coerente con l'asse, evidenze etichettate come "mancante/debolezza")
- **Verifica adversariale consigliata**: `SKILL.md` e il template suggeriscono, per i report ad alto impatto, di confermare l'analisi con `/adversarial-verify` (plugin `adversarial-verify@fullo-plugins`), con nota esplicita sul consumo di token

### v2.5.4 (luglio 2026) — Comandi nei case study

- I case study mostrano ora il **comando da digitare a ogni step** (blocchi `pre` con prompt naturali e slash command) e i riferimenti a skill esterne linkano il loro sito (es. [/adversarial-verify](https://fullo.github.io/claude-adversarial-skill/))

### v2.5.3 (luglio 2026) — Architettura dell'informazione e accessibilità

- **Nuova IA del sito** (da PR): guida step-by-step "Analyzing a sustainability report" nel manuale (6 step con gotchas e rating greenwashing) e casi di studio scorporati in pagine dedicate — manufacturing ([case-manufacturing.html](docs/case-manufacturing.html), Ceramica Valdenza: EPD, Scope 2 market vs location, claim "carbon neutral") e IT ([case-it.html](docs/case-it.html), Bottega Digitale)
- **Accessibilità WCAG 2.2 AA**: landmark `main` con skip-link funzionante su tutte le pagine, `nav` etichettate e breadcrumb, gerarchia heading corretta (card h4 sotto i tier), focus visibile da tastiera, `prefers-reduced-motion`, `scope="col"` sulle tabelle, `lang="it"` sulle parti in italiano, contrasti verificati programmaticamente (rimossi i due casi sotto 4.5:1)

### v2.5.2 (luglio 2026) — Sito GitHub Pages

- **docs/** ora è un sito GitHub Pages in inglese ([fullo.github.io/sustainable-manager](https://fullo.github.io/sustainable-manager/)): landing con le 12 skill e la copertura normativa a luglio 2026, più il **manuale** (quale skill per quale domanda, scenari, caso di studio end-to-end, reference strumenti). Le guide markdown in italiano della v2.5.1 sono confluite (tradotte) nel manuale

### v2.5.1 (luglio 2026) — Guide utente

- **docs/guide/**: guida all'uso per principianti (quale skill per quale domanda, scenari realistici, errori comuni) e walkthrough completo di sustainable-it-compliance con caso di studio end-to-end (Bottega Digitale S.p.A.: report EED, calcolo SCI con output reali, questionario cloud, device policy, KPI board)

### v2.5.0 (luglio 2026) — Sustainable IT: cloud, device, governance

- **Questionario cloud provider** (`cloud-provider-questionnaire.md`, EN+IT): PUE/WUE/CFE per regione, evidenze claim rinnovabili, carbon reporting cliente, EED art. 12, red flags — agganciato a supplier-engagement come Modulo F
- **Device lifecycle policy generator** (`device-lifecycle-policy.md`): criteri d'acquisto (EPEAT/TCO/CAM), repair-first, estensione cicli di refresh, cascata di riuso, integrazione data security, KPI
- **Benchmark embodied carbon device** (`assets/benchmarks/device-embodied-carbon.json`): valori illustrativi da PCF dei produttori per 9 categorie, con vita utile tipica
- **Step 5 Governance & Board KPIs**: set di KPI per il board mappati su ESRS, ownership, GreenOps×FinOps
- **F-gas 2024/573** (raffrescamento DC), **EU Taxonomy attività 8.1** (riuso del dataset EED) e **flusso operativo WEEE/RAEE** aggiunti a mappatura obblighi e reference

### v2.4.0 (luglio 2026) — Sustainable IT: maturity, SCI calculator, EED checklist, EAA

- **Step 0 Maturity Snapshot** nella sustainable-it-compliance: posizionamento sui 4 pilastri SOFT (GSF) con scala a 5 livelli, che calibra profondità e tono della consulenza
- **`sci_calculator.py`**: calcolo SCI (ISO/IEC 21031) da CLI o JSON, con formula embodied M = TE × TiR/EL × RS/TR e tabella intensità di rete illustrative
- **`eed-reporting-checklist.md`**: checklist compilabile dei datapoint DR (EU) 2024/1364 per il report annuale data centre (scadenza 15 maggio), con gap comuni e workaround
- **European Accessibility Act** (Dir. 2019/882, applicabile da giu 2025) aggiunto alla mappatura obblighi: il pilastro sociale dell'IT sostenibile (EN 301 549/WCAG, ESRS S4, D.Lgs. 82/2022)

### v2.3.1 (luglio 2026) — Note TNFD/ISSB/GRI

- biodiversity-screener: adozione TNFD (733 organizzazioni, nov 2025), exposure draft ISSB sulla natura atteso alla COP17 (ott 2026), consultazione TNFD "State of Nature"
- core (frameworks.md) e cross-framework-mapper: GRI 102 Climate Change / GRI 103 Energy in vigore dal 1/01/2027, adozione ISSB a 28 giurisdizioni (apr 2026), targeted amendments IFRS S2 (dic 2025)

### v2.3.0 (luglio 2026) — Sustainable IT compliance

- **Nuova skill `sustainable-it-compliance`** (12ª): mappa gli obblighi EU sulla sostenibilità digitale — reporting data centre EED art. 12 (soglia 500 kW, scadenza 15 maggio, KPI PUE/WUE/ERF/REF), aspetti energetici AI Act post-Digital Omnibus (documentazione energia GPAI in vigore, high-risk rinviati a 2027/2028), standard di misura (SCI ISO/IEC 21031, SCI for AI ratificata dic 2025, Real Time Cloud, Tech Carbon Standard), Right to Repair (server inclusi), battery passport, ESPR/DPP, green claims IT sotto EmpCo. Include reference normativa e contesto italiano (CAM ICT, RAEE, CER). Nata dall'allineamento con il libro "Sustainable IT the Right Way"

### v2.2.0 (luglio 2026) — Allineamento normativo

Aggiornamento legislativo completo di tutte le skill al quadro in vigore a luglio 2026:

- **Omnibus I è legge**: Direttiva (EU) 2026/470 (GU 26/02/2026, in vigore 18/03/2026) — soglie CSRD 1.000 dipendenti + 450M€, listed SME fuori dallo scope obbligatorio, non-UE a 450M€ di fatturato UE, CSDDD recepimento 26/07/2028 / applicazione 26/07/2029
- **ESRS rivisti adottati** (atto delegato 3/07/2026, insieme al VSME): −61% datapoint obbligatori, applicazione FY2027 con early adoption FY2026 — aggiornati `efrag-updates.md`, double-materiality, cross-framework-mapper
- **CBAM**: integrato il Reg. (EU) 2025/2083 — de minimis 50t cumulative (esclusi H2/elettricità), vendita certificati dal 1/02/2027, dichiarazione annuale al 30 settembre, holding trimestrale al 50%; corretta la de minimis erroneamente descritta come "per tipo di prodotto"
- **EU Taxonomy**: integrato il Reg. Delegato (EU) 2026/73 — soglia di materialità 10% (nuovo Step 0), template semplificati, deferral opzionale per le imprese finanziarie
- **EUDR**: nuove date post-revisione dicembre 2025 (30/12/2026 tutti gli operatori, 30/06/2027 micro/piccole)
- **PPWR**: applicazione fasata chiarita (12/08/2026 solo restrizioni sostanze e PFAS; etichettatura 2028; riciclabilità e recycled content 2030)
- **SBTi Corporate Net-Zero Standard v2.0** (giugno 2026): doppio binario di validazione v1.3.1/v2.0 nel transition-plan-builder, obbligo v2.0 dal 1/02/2028
- **Fix**: la EU 2024/825 era etichettata "Green Claims Directive" — è la Empowering Consumers Directive (EmpCo, dal 27/09/2026); la Green Claims Directive resta una proposta congelata
- **Note aggiunte**: SFDR 2.0 in trilogo, revisione GHG Protocol in corso, value chain cap VSME per fornitori <1.000 dipendenti

### v2.1.0 (aprile 2026)

- Integrazione UNI/PdR 179:2025 nella biodiversity-screener (MSA, crediti di biodiversità, contesto italiano)

### v2.0.0 (aprile 2026)

- 10 nuove skill oltre alla core; gotchas, evals e LICENSE secondo le best practice agentskills.io

## Licenza

MIT
