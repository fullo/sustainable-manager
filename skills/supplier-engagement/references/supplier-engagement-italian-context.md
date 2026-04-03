# Supplier Engagement — Contesto Italiano

Riferimenti specifici per il coinvolgimento dei fornitori nel contesto imprenditoriale italiano: tessuto di PMI, normativa nazionale, piattaforme di assessment, e approcci pratici.

---

## 1. Contesto PMI Italiane

### Struttura del tessuto produttivo
- Il 95% delle imprese italiane sono micro/piccole (meno di 50 dipendenti)
- Il 99,9% delle imprese ha meno di 250 dipendenti (PMI)
- Capacita ESG limitata: poche risorse dedicate, conoscenza frammentaria delle normative
- Forte dipendenza da relazioni personali e fiducia nel rapporto cliente-fornitore

### Modello distrettuale e consortile
- I distretti industriali italiani offrono opportunita di engagement collettivo:
  - **Confindustria Ceramica**: engagement ambientale per il distretto di Sassuolo
  - **Sistema Moda Italia (SMI)**: linee guida sostenibilita per la filiera tessile/moda
  - **Federalimentare**: standard di sostenibilita per la filiera alimentare
  - **ANCE**: impegni ambientali per il settore costruzioni
- I consorzi possono fungere da intermediari per raccolta dati ESG aggregati
- L'approccio collettivo riduce i costi per singola PMI e aumenta il tasso di risposta

### Approccio collaborativo vs. compliance-only
- In Italia, l'approccio puramente prescrittivo (compliance demands) e meno efficace che in contesti anglosassoni
- **Raccomandato**: combinare requisiti chiari con offerta di supporto
- Elementi di un engagement efficace nel contesto italiano:
  1. Comunicazione personale (non solo email automatiche)
  2. Workshop formativi (anche in collaborazione con associazioni di categoria)
  3. Helpdesk dedicato per domande e supporto alla compilazione
  4. Tempistiche realistiche (almeno 4-6 settimane per il primo questionario)
  5. Feedback sui risultati (non solo raccolta dati one-way)
  6. Riconoscimento dei fornitori virtuosi (premialita, non solo penalita)

---

## 2. D.Lgs. 231/2001 — Responsabilita Amministrativa degli Enti

### Rilevanza per la supply chain
- Il D.Lgs. 231/2001 prevede la responsabilita amministrativa dell'ente per reati commessi nell'interesse o a vantaggio dell'organizzazione
- La responsabilita puo estendersi a reati commessi lungo la catena di fornitura
- Reati rilevanti per l'ESG dei fornitori:
  - **Ambientali** (Art. 25-undecies): inquinamento, rifiuti, emissioni
  - **Sicurezza sul lavoro** (Art. 25-septies): omicidio colposo, lesioni gravi
  - **Corruzione** (Art. 25): corruzione attiva/passiva, induzione indebita
  - **Riciclaggio** (Art. 25-octies): riciclaggio, impiego di beni illeciti
  - **Sfruttamento lavorativo** (Art. 25-quinquies): riduzione in schiavitu, caporalato

### Modello Organizzativo (MOG 231)
- Le aziende con MOG 231 adottato dovrebbero estendere i controlli ai fornitori critici
- Elementi tipici nella gestione fornitori secondo 231:
  - Qualificazione iniziale con verifica requisiti etici/legali
  - Clausole contrattuali di compliance (clausole 231)
  - Monitoraggio periodico
  - Diritto di audit
  - Meccanismo di segnalazione

### Implicazioni per il questionario fornitori
- Includere domanda C6 (MOG 231) per fornitori italiani
- Verificare l'esistenza di clausole 231 nei contratti
- La domanda C2 (anti-corruzione) e particolarmente rilevante per il 231

---

## 3. D.Lgs. 24/2023 — Whistleblowing

### Requisiti
- Recepimento della Direttiva UE 2019/1937
- Obbligo di canali di segnalazione interni per:
  - Imprese con >50 dipendenti
  - Imprese con MOG 231 (indipendentemente dalla dimensione)
- Canale deve essere accessibile anche a terzi (fornitori, consulenti, collaboratori)

### Rilevanza per il questionario
- La domanda C3 (canale whistleblowing) verifica la conformita al D.Lgs. 24/2023
- I fornitori devono poter segnalare irregolarita sia nel proprio canale sia in quello del committente
- Il canale ANAC e disponibile come canale esterno di segnalazione

---

## 4. EcoVadis e CDP Supply Chain in Italia

### EcoVadis
- Piattaforma di rating ESG dei fornitori piu diffusa in Europa
- **Adozione in Italia**: in crescita tra le grandi aziende
  - ENEL: richiede EcoVadis a fornitori strategici
  - ENI: programma di qualificazione fornitori include EcoVadis
  - Generali: EcoVadis per fornitori Tier 1
  - Intesa Sanpaolo: assessment ESG fornitori via EcoVadis
  - Barilla: programma Good4Growth con EcoVadis
- **Pro**: standardizzazione, comparabilita, piattaforma digitale
- **Contro**: costo per i fornitori (soprattutto PMI), possibile assessment fatigue

### CDP Supply Chain
- Programma CDP per raccolta dati climatici dalla supply chain
- **Aziende italiane partecipanti** (come member): ENEL, Pirelli, Prysmian, A2A
- Focalizzato su emissioni GHG e gestione del rischio climatico
- Complementare al questionario ESG generico (piu profondo sul clima)

### Integrazione con questionario proprio
- Se il fornitore ha gia un rating EcoVadis o disclosure CDP, valorizzare i dati esistenti
- Evitare duplicazione: mappare le domande del proprio questionario a EcoVadis/CDP
- Accettare lo scorecard EcoVadis come risposta alternativa per fornitori gia valutati

---

## 5. Guida Pratica per l'Engagement

### Step 1: Segmentazione fornitori
- **Top 20 fornitori** (per spesa/rischio): questionario completo, engagement diretto
- **Fornitori 21-100**: questionario standard, comunicazione digitale
- **Fornitori >100**: questionario semplificato o solo codice di condotta
- Criteri di prioritizzazione: valore contrattuale, rischio settoriale, rischio geografico, criticita della fornitura

### Step 2: Comunicazione e lancio
- Lettera di presentazione firmata dal top management
- Webinar introduttivo (in italiano, con Q&A)
- FAQ e guida alla compilazione
- Helpdesk (email + telefono) con orari definiti

### Step 3: Raccolta e follow-up
- Piattaforma digitale (o almeno formato strutturato Excel/Forms)
- Reminder a 2 settimane dalla scadenza
- Supporto telefonico per fornitori in difficolta
- Tasso di risposta atteso al primo anno: 50-70% (top suppliers), 30-50% (general)

### Step 4: Scoring e feedback
- Scoring con `supplier_scorer.py`
- Restituzione individuale dei risultati (scorecard per fornitore)
- Evidenziare punti di forza e aree di miglioramento
- Non usare il punteggio solo come strumento punitivo

### Step 5: Piani di miglioramento
- Per fornitori "At-Risk" e "Critical": piano di miglioramento concordato
- Timeline: 12-18 mesi per miglioramenti significativi
- Supporto: formazione, condivisione best practice, mentoring da fornitori leader
- Monitoraggio: verifica progressi a 6 e 12 mesi

### Template lettera di accompagnamento (stile business formale italiano)

> Oggetto: Richiesta di compilazione questionario ESG fornitori
>
> Gentile Fornitore,
>
> nell'ambito del nostro impegno verso la sostenibilita e in ottemperanza ai nuovi obblighi normativi europei (CSRD/ESRS, CSDDD), stiamo avviando un programma di raccolta dati ESG dalla nostra catena di fornitura.
>
> La invitiamo a compilare il questionario allegato entro [DATA]. Le informazioni raccolte ci consentiranno di mappare le performance di sostenibilita della nostra filiera e di identificare opportunita di miglioramento condivise.
>
> Siamo consapevoli che questo rappresenta un impegno aggiuntivo. Per questo motivo, mettiamo a disposizione: [helpdesk, webinar, guida alla compilazione].
>
> Consideriamo questa iniziativa come un percorso collaborativo e non come un mero adempimento. I risultati saranno condivisi con Lei in forma riservata.
>
> Restiamo a disposizione per qualsiasi chiarimento.
>
> Cordiali saluti,
> [Nome, Titolo]
