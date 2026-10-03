# Sustainable Manager - Claude Code Plugin

[![Skill Version](https://img.shields.io/badge/skill-v2.7-blue)](skills/sustainable-manager/SKILL.md)
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

- **[Landing](https://fullo.github.io/sustainable-manager/)** — le 12 skill, copertura normativa (stato ottobre 2026), installazione e uso
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
│   │   ├── scripts/                # chart_generator.py, esrs_assessment.py, analysis_dashboard.py, quote_check.py
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

## Igiene dei test

I sei report reali usati per i test di regressione (v2.7.2, v2.7.3) sono stati usati anche per sviluppare le correzioni: sono un **set di sviluppo**, non una prova cieca. I miglioramenti misurati su questi documenti vanno quindi confermati su documenti non visti. **TODO**: costruire un set di controllo (held-out) di 3-6 report di settori, formati e committenti diversi, da non usare per scrivere i fix; i riferimenti della skill non devono nominare i soggetti dei documenti di test.

## Changelog

### v2.7.4 (ottobre 2026) — Fix P1 da regressione 2.7.3

Correzioni di priorità P1 emerse dalla regressione 2.7.3. La modifica normativa è verificata sul testo in Cellar (Reg. (UE) 2023/1115, Reg. (UE) 2025/2650, Dir. 2013/34/UE, Dir. delegata (UE) 2023/2775); la composizione del Tavolo UNI/PdR 179 sulla scheda UNI.

- **Rubrica del rischio greenwashing deterministica**: definizioni di claim *headline*, tema *core* (GHG sempre; top-3 temi materiali del report), claim quantitativi e narrativi (i claim assoluti come "zero sprechi" contano come quantitativi), "corretto nelle vicinanze" (stessa pagina/tabella o entro 2 pagine nella stessa sezione); regole numerate R1-R3 (🔴) e M1-M5 (🟡), soglia del 10% delle emissioni per i claim di compensazione, ordine di applicazione e obbligo di indicare il fatto che cambierebbe il livello; *Substantiated* non richiede l'assurance se il dato è pienamente tracciabile — greenwashing-detection, template
- **EUDR, micro e piccole imprese**: rimossa la definizione errata "meno di 50 dipendenti e fatturato di prodotto sotto 10 M€"; ora rinvio all'art. 3(1)-(2), primo comma, Dir. 2013/34/UE (piccola: 2 su 3 tra 5 M€ di attivo, 10 M€ di ricavi, 50 dipendenti, come adeguati dalla Dir. delegata 2023/2775), definizione di "micro or small primary operator" (art. 2(15a)) e data del 30/6/2027 solo per chi era tale al 31/12/2024 — `regulation-thresholds.md` §6
- **`verification.performed`**: `true` solo dopo una rilettura indipendente (`/adversarial-verify` o autoverifica che riapre ogni pagina citata); il solo `quote_check.py` è `performed: false`, `method_type: "automated_quote_check"`; la sezione 8 del template va sempre compilata con lo stato reale — SKILL.md, template, schema
- **Schema 1.2** (retrocompatibile: i 12 JSON delle regressioni 2.7.2 e 2.7.3 restano validi): `quote_source` (`text`/`image`) su KPI e claim, `verification.method_type` con vincolo su `performed`
- **`quote_check.py`**: citazioni da immagine segnalate come `IMAGE` (controllo manuale) invece che come errore; sillabazione unita solo tra lettere (le celle "-" delle tabelle restano); puntini di sospensione iniziali/finali e trattini finali ignorati, puntini interni come salto; avvisi `VALUE?` (valore del KPI assente nella citazione) e `SHORT`; opzioni `--flags` (pagine di flag e valori derivati) e `--strict`; codici di uscita 0/1/2/3 documentati
- **Riferimenti ripuliti dai documenti di test**: rimossi gli esempi e i nomi tratti dai sei report (operatore e provincia nel contesto italiano dell'economia circolare, nome del project leader della UNI/PdR 179, "UNI/PdR XX:2024", "PA" su scala 0-40, "pollinator nesting", "sponsor", blocchi di settore telecomunicazioni, utility/rifiuti, bevande, stampa/foto, Società Benefit); al loro posto controlli trasversali generici, mantenendo le regole verificate (EmpCo, soglie CSRD, EUDR, L. 208/2015, ISO 14064-1, diagnosi energetica)
- **Screenshot**: estrarre l'immagine originale (`pdfimages -png`) o renderizzare a ≥200 dpi (`pdftoppm -r 200`) e leggerla a piena risoluzione — SKILL.md, biodiversity-screener
- **Igiene dei test**: nota sul set di sviluppo e TODO per un set di controllo

### v2.7.3 (ottobre 2026) — Fix da test di regressione

Correzioni emerse dal test di regressione su sei report reali (analisi v2.7.2 confrontate con le precedenti). Le correzioni normative sono verificate sul testo in GUUE/Cellar (Dir. 2026/470, Reg. 2025/2650, Reg. delegati 2026/2102, 2026/1560 e 2026/1563, Dir. 2024/825, Dir. delegata 2023/2775, Reg. 2025/40), sul sito della Commissione, di EFRAG, GRI, ISPRA e su Normattiva.

- **EUDR**: i prodotti stampati (ex cap. 49) non sono più nell'Allegato I (Reg. 2025/2650, art. 1(26)); carta e cartone (cap. 47-48) restano in ambito; i materiali di imballaggio sono esclusi solo quando sostengono, proteggono o trasportano un altro prodotto (Reg. delegato 2026/2102, considerando 16); nota per stampatori e "downstream operator" — `regulation-thresholds.md`, eu-regulation-matrix, greenwashing-detection
- **Soglie CSRD/CSDDD**: "più di 1.000 dipendenti e più di 450 M€" (non "1.000+"), CSDDD "più di 5.000 e più di 1,5 mld"; value chain cap per le imprese "non superiori a 1.000 dipendenti"; soglie originali aggiornate a 50 M€ / 25 M€ (Dir. delegata 2023/2775); Wave 1 sotto le nuove soglie esentabile dagli Stati membri già per FY2025-2026; perimetro entità/gruppo, esenzione della controllata (art. 19a(9)/29a(8)) e MTF ≠ mercato regolamentato — SKILL.md, eu-regulation-matrix, efrag-updates, glossary, eu-taxonomy-checker, sustainable-it-compliance, supplier-engagement, docs
- **EmpCo**: elenco completo dei divieti (claim generici con esempi del considerando 9, compensazione GHG riferita al prodotto, marchi non certificati, intero prodotto, **prestazioni future** senza piano verificato da esperto terzo) e nota sull'ambito B2C e sui crediti di biodiversità — greenwashing-detection, SKILL.md, circular-economy, sustainable-it-compliance, biodiversity-screener, glossary, docs
- **Workflow di analisi**: lettura visiva delle pagine immagine prima di dichiarare un'assenza; estrazione PDF (layout/raw, doppie pagine); controllo di coerenza interna come passo standard; contesto normativo come passo; rubrica per il rischio complessivo 🟢/🟡/🔴; esecuzione non interattiva; passaggio al biodiversity-screener per piani e crediti di biodiversità
- **Template e schema 1.1** (retrocompatibile, i sei JSON del test restano validi): sezione "Contesto normativo", coerenza interna, valori derivati, colonne fisse della tabella claim con citazione, riga Scope 3 senza "absent"; nello schema `page` intero o array, `printed_page`, `perimeter`, `basis`, `scope_note`, `regulatory_context`, `derived_values`, `data_quality_flags`, `overall_risk_rule`, `verification.method`, `recommendations` max 6
- **Nuovo `scripts/quote_check.py`**: controllo automatico che ogni citazione sia sulla pagina indicata (non è una verifica avversariale)
- **Guide di settore**: telecomunicazioni, utility/rifiuti, bevande, stampa, Società Benefit/B Corp, corrispondenza ISO 14064-1 ↔ Scope, diagnosi energetica D.Lgs. 102/2014 — greenwashing-detection, glossary
- **Biodiversità**: scala MSA 0-1 vs 0-100, "bare area", indici non definiti (es. "PA"), bozze di prassi, conflitto d'interessi, decorrenza della retroattività indicata come ipotesi (clausole UNI/PdR 179 non verificate su fonte UNI)
- **ESRS e VSME**: versione ESRS per FY2024-2025 (2023/2772 come modificato dal 2025/1416); due atti con date di entrata in vigore diverse (2026/1563 il 10/11/2026, 2026/1560 il 24/09/2026); il VSME sostituisce la Raccomandazione 2025/1710 ed è aperto a qualsiasi impresa fuori dall'obbligo; "−61%" attribuito al parere EFRAG (dicembre 2025), la Commissione indica "oltre il 60%" obbligatori e "oltre il 70%" totali
- **Altro**: GRI 102/103 legati alla data di pubblicazione; PPWR con date scaglionate; rifiuti urbani: raccolta differenziata ≠ riciclo (ISPRA: 67,7% vs 52,3% nel 2024; 65,2% vs 49,2% nel 2022) e nota su Contarina; versione della skill in SKILL.md
- **Verifica avversariale** (fonti primarie, 2/10/2026): 86 affermazioni controllate, 78 confermate (10 con precisazioni: PPWR "o più tardi" se gli atti attuativi tardano, voci EUDR ex 47/ex 48 del Reg. 2026/2102, art. 4 del Reg. 2026/1560, ISPRA aggiornata ai dati 2024 — RD 67,7%, riciclo 52,3% —, GRI 305-1…305-5 ritirati, CPE telco, D.Lgs. 102/2014 art. 8), 2 corrette (l'esenzione delle controllate EIP esisteva già: la Dir. 2026/470 sostituisce l'art. 19a(10)/29a(9) togliendo l'eccezione per le quotate; terreni agricoli abbandonati: curva di recupero GLOBIO, non classe cropland), 6 con riserva o riformulate (contenuti UNI/PdR 179, claim di biodiversità, utility pubbliche); `quote_check.py` non va più in errore se manca la pagina

### v2.7.2 (ottobre 2026) — Verifica avversariale su fonti primarie

Verifica avversariale delle modifiche v2.7.0-v2.7.1 solo su fonti primarie (EUR-Lex/GUUE, Commissione, Consiglio, OEIL, EFRAG, IFRS, SBTi, GHG Protocol, GRI, senato.it, camera.it, governo.it, Gazzetta Ufficiale): 89 affermazioni controllate, 62 confermate, 19 corrette, 8 riformulate con riserva o rimosse perché non confermate.

- **CSDDD**: l'art. 29 (responsabilità civile) è modificato, non soppresso — eliminato il regime UE armonizzato, la responsabilità segue il diritto nazionale e resta il diritto al pieno risarcimento
- **Legge di delegazione europea 2026**: A.S. 2025 assegnato alla 4ª Commissione del Senato (sede referente), in esame senza voti al 30/09/2026; l'art. 6 contiene la delega per la Dir. (UE) 2026/470 (tolta la riserva "da verificare") e il suo contenuto è stato riscritto secondo il testo; il 1/10/2026 la Conferenza Stato-Regioni ha reso il parere. Stop-the-clock attribuito al D.L. 95/2025 come convertito dalla L. 118/2025
- **Clima**: il Reg. (UE) 2026/667 è in vigore dal 7/04/2026 (GUUE 18/03); il "pilota" 2031-2035 sui crediti internazionali è solo un elemento per future proposte
- **CBAM**: 97,5% → 2034 è il fattore CBAM applicato all'allocazione gratuita; ~457 prodotti è la cifra della commissione ENVI; avvio dei triloghi non confermato; aggiunto il prezzo Q2 2026 (75,28 €)
- **EUDR**: i pneumatici ricostruiti sono solo ristretti (i battistrada restano nell'Allegato I); Reg. di esecuzione 2026/1565 in GUUE il 14/07, art. 1(2)(c) dal 15/10/2026
- **Sustainable IT**: AI Omnibus — l'obbligo di marcatura dell'art. 50(2) per i sistemi generativi immessi prima del 2/08/2026 slitta al 2/12/2026, e i nuovi divieti dell'art. 5 si applicano dal 2/12/2026; EED — primo report entro il 15/09/2024, poi 15 maggio dal 2025; passaporto batterie per batterie LMT, industriali >2 kWh e per veicoli elettrici; ESPR — nessun gruppo di prodotti ICT dedicato, solo misure orizzontali (2027/2029)
- **Standard globali**: ISSB adottato o in introduzione in più di 40 giurisdizioni (non 28); la consultazione TNFD "State of Nature" si è chiusa il 4/06/2026; 733 aderenti TNFD datati a novembre 2025; rimozioni SBTi dall'1% nel 2035, poi lineari fino al 100%; GRI 102/103 si applicano ai report pubblicati dal 1/01/2027; monitoraggio TCFD passato alla IFRS Foundation
- **Con riserva o rimossi**: bozze dei criteri tecnici della Tassonomia (data di applicazione non verificata), annuncio in plenaria SFDR, tempi di accreditamento dei verificatori CBAM, "nessun regime transitorio per le scorte" EmpCo (ora: nessuna clausola transitoria nei testi), MSA "obbligatoria" nella UNI/PdR 179 (testo non pubblico), pubblicazione in GU del decreto sul diritto alla riparazione (verificata fino al 1/10/2026), data di chiusura di SBTi v1 (documenti SBTi incoerenti); Green Claims descritta come proposta pendente, non ritirata
- Tassonomia: −64% riferito alle sole imprese non finanziarie; differimento per le imprese finanziarie solo senza claim di allineamento. Value chain cap: esercizi dal 1/01/2027, dipendenti medi dell'esercizio precedente. Cross-Skill References di eu-regulation-matrix puntate alle 12 skill esistenti

### v2.7.1 (ottobre 2026) — Delegazione europea, glossario sigle, revisione

- **Legge di delegazione europea 2026**: corretto lo stato — è un disegno di legge (A.S. 2025) approvato dal CdM il 4/08/2026 e all'esame del Senato, non risulta approvato in via definitiva al 2/10/2026 — eu-regulation-matrix, cross-framework-mapper, supplier-engagement, sustainable-it-compliance
- **Glossario sigle**: nuovo `skills/sustainable-manager/references/glossary.md` (forma estesa, atto e stato di CSRD, ESRS, VSME, CSDDD, SFDR, EmpCo, EUDR, CBAM, ETS/ETS2, PPWR, ESPR/DPP, EED, PUE/WUE/ERF/REF, DMA, IRO, DNSH, TSC, ISSB, TNFD, SBTi, CAM, CER, AGCM ecc.), richiamato dalle skill; EmpCo usata al posto della "Green Claims Directive" dove la Dir. 2024/825 era citata come tale (core, template moda, `dma-sector-iro.md`, eval)
- **Diritto alla riparazione**: lo schema AG 426 è stato approvato in via definitiva dal CdM il 16/09/2026 (in attesa di GU) — circular-economy, sustainable-it-compliance
- **Fix di revisione**: value chain cap riferito alle imprese "fino a 1.000 dipendenti" (non "meno di 1.000"); EUDR: Reg. di esecuzione (UE) 2026/1565 sul sistema informativo (adottato 13/07, GUUE 14/07, in vigore 17/07/2026); SBTi v2.0: il sostegno alle rimozioni dal 2035 per le imprese di Categoria A è segnalato come requisito futuro progressivo, non come obbligo di acquisto; timeline 2027 riordinata

### v2.7.0 (ottobre 2026) — Aggiornamento normativo luglio-ottobre 2026

Allineamento di tutte le skill allo stato normativo al 2 ottobre 2026:

- **ESRS rivisti e VSME in Gazzetta**: Reg. delegato (UE) 2026/1563 (GUUE 21/09/2026, in vigore 10/11/2026, obbligatori dal FY2027; per il FY2026 scelta tra ESRS vigenti, vigenti con esenzioni o rivisti) e Reg. delegato (UE) 2026/1560 per il VSME (in vigore 24/09/2026); value chain cap dal FY2027 limitato ai datapoint dell'Allegato II — sustainable-manager (`efrag-updates.md`, `frameworks.md`), double-materiality, cross-framework-mapper, scope3-mapper, supplier-engagement
- **CSRD/CSDDD post-Omnibus**: limited assurance permanente (standard entro 1/07/2027); CSDDD con data unica 26/07/2029, rendicontazione dal FY2030, sanzioni massime al 3%, eliminato il piano di transizione (art. 22), responsabilità civile (art. 29) modificata e rinviata al diritto nazionale, approccio basato sul rischio non limitato al primo livello; corrette le soglie "originali" CSDDD (1.000 dipendenti / 450 M€) — eu-regulation-matrix, supplier-engagement
- **Italia**: delega per recepire la Direttiva 2026/470 nel disegno di legge di delegazione europea 2026 (A.S. 2025, approvato dal CdM il 4/8/2026, all'esame del Senato); EmpCo recepita con D.Lgs. 30/2026 (Codice del consumo), applicabile dal 27/09/2026; diritto alla riparazione in ritardo (AG 426)
- **EUDR**: dal 30/12/2026 per grandi e medie imprese (non "tutti gli operatori"); Reg. delegato (UE) 2026/2102 (GUUE 17/09/2026) toglie pelli e cuoio dall'Allegato I e aggiunge caffè solubile e alcuni derivati della palma dal 30/12/2027 — eu-regulation-matrix, biodiversity-screener
- **CBAM**: guidance per operatori extra-UE (14/08) e per verificatori (24/08), prezzo Q1 2026, estensione downstream COM(2025) 989 con posizione del Parlamento del 15/09/2026 (ancora proposta), revisione ETS COM(2026) 616 sull'uscita dalle quote gratuite — cbam-compliance, eu-regulation-matrix
- **Clima e standard**: Legge europea sul clima modificata dal Reg. (UE) 2026/667 (−90% al 2040), ETS2 al 2028; consolidamento GHG Protocol + ISO annunciato il 29/07/2026; SBTi Net-Zero v2.0 (target setting da febbraio 2027); emendamenti IFRS S2 (esercizi dal 1/01/2027) e GRI 102/103 (report pubblicati dal 1/01/2027); bozza ISSB sulla natura (Practice Statement) attesa alla COP17 — transition-plan-builder, scope3-mapper, biodiversity-screener, `lca-science-based.md`
- **Tassonomia**: Reg. delegato 2026/73 applicabile dai report FY2025, opex valutabile solo se rilevante; bozze di modifica dei criteri tecnici segnalate come non ancora adottate — eu-taxonomy-checker
- **Sustainable IT e circolarità**: Digital Omnibus sull'AI (Reg. (UE) 2026/1744, in vigore 27/07/2026), rating scheme data centre C(2026) 3472 adottato il 21/09/2026 (in scrutinio), registro DPP attivo dal 20/07/2026 (Reg. di esecuzione 2026/1778), divieto di distruzione dell'invenduto tessile per le grandi imprese — sustainable-it-compliance, circular-economy
- **Fix**: SFDR 2.0 non è ancora in trilogo (mandato del Consiglio giugno, voto ECON settembre 2026); la Green Claims Directive è una proposta bloccata, non ritirata (`greenwashing-detection.md` la presentava come in arrivo); la limited assurance non passa più a reasonable
- **Sito**: landing e case study aggiornati allo stato di ottobre 2026

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
- core (frameworks.md) e cross-framework-mapper: GRI 102 Climate Change / GRI 103 Energy in vigore dal 1/01/2027, adozione ISSB a 28 giurisdizioni (apr 2026) [correzione in v2.7.2: l'IFRS Foundation indica più di 40 giurisdizioni], targeted amendments IFRS S2 (dic 2025)

### v2.3.0 (luglio 2026) — Sustainable IT compliance

- **Nuova skill `sustainable-it-compliance`** (12ª): mappa gli obblighi EU sulla sostenibilità digitale — reporting data centre EED art. 12 (soglia 500 kW, scadenza 15 maggio, KPI PUE/WUE/ERF/REF), aspetti energetici AI Act post-Digital Omnibus (documentazione energia GPAI in vigore, high-risk rinviati a 2027/2028), standard di misura (SCI ISO/IEC 21031, SCI for AI ratificata dic 2025, Real Time Cloud, Tech Carbon Standard), Right to Repair (server inclusi), battery passport, ESPR/DPP, green claims IT sotto EmpCo. Include reference normativa e contesto italiano (CAM ICT, RAEE, CER). Nata dall'allineamento con il libro "Sustainable IT the Right Way"

### v2.2.0 (luglio 2026) — Allineamento normativo

Aggiornamento legislativo completo di tutte le skill al quadro in vigore a luglio 2026:

- **Omnibus I è legge**: Direttiva (EU) 2026/470 (GU 26/02/2026, in vigore 18/03/2026) — soglie CSRD più di 1.000 dipendenti e più di 450M€, listed SME fuori dallo scope obbligatorio, non-UE a 450M€ di fatturato UE, CSDDD recepimento 26/07/2028 / applicazione 26/07/2029
- **ESRS rivisti adottati** (atto delegato 3/07/2026, insieme al VSME): −61% datapoint obbligatori (stima del parere EFRAG di dicembre 2025; la Commissione indica "oltre il 60%"), applicazione FY2027 con early adoption FY2026 — aggiornati `efrag-updates.md`, double-materiality, cross-framework-mapper
- **CBAM**: integrato il Reg. (EU) 2025/2083 — de minimis 50t cumulative (esclusi H2/elettricità), vendita certificati dal 1/02/2027, dichiarazione annuale al 30 settembre, holding trimestrale al 50%; corretta la de minimis erroneamente descritta come "per tipo di prodotto"
- **EU Taxonomy**: integrato il Reg. Delegato (EU) 2026/73 — soglia di materialità 10% (nuovo Step 0), template semplificati, deferral opzionale per le imprese finanziarie
- **EUDR**: nuove date post-revisione dicembre 2025 (30/12/2026 tutti gli operatori, 30/06/2027 micro/piccole)
- **PPWR**: applicazione fasata chiarita (12/08/2026 solo restrizioni sostanze e PFAS; etichettatura 2028; riciclabilità e recycled content 2030)
- **SBTi Corporate Net-Zero Standard v2.0** (giugno 2026): doppio binario di validazione v1.3.1/v2.0 nel transition-plan-builder, obbligo v2.0 dal 1/02/2028
- **Fix**: la EU 2024/825 era etichettata "Green Claims Directive" — è la Empowering Consumers Directive (EmpCo, dal 27/09/2026); la Green Claims Directive resta una proposta congelata
- **Note aggiunte**: SFDR 2.0 in trilogo [correzione in v2.7.0: a ottobre 2026 i triloghi non sono ancora iniziati — mandato del Consiglio giugno 2026, voto ECON settembre 2026], revisione GHG Protocol in corso, value chain cap VSME per fornitori <1.000 dipendenti

### v2.1.0 (aprile 2026)

- Integrazione UNI/PdR 179:2025 nella biodiversity-screener (MSA, crediti di biodiversità, contesto italiano)

### v2.0.0 (aprile 2026)

- 10 nuove skill oltre alla core; gotchas, evals e LICENSE secondo le best practice agentskills.io

## Licenza

MIT
