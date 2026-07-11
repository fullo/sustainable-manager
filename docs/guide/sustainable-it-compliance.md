# Guida: sustainable-it-compliance con caso di studio

Walkthrough completo della skill più ricca del plugin, seguendo un'azienda realistica dall'inizio alla fine. Ogni sezione mostra **cosa scrivere a Claude**, cosa risponde la skill, e come usare gli strumenti (script, checklist, questionari).

## Il caso di studio: Bottega Digitale S.p.A.

Azienda italiana di e-commerce e software, profilo volutamente "completo" per attivare tutti gli step:

| Caratteristica | Valore |
|----------------|--------|
| Dipendenti / fatturato | 1.200 / 520M€ → **in scope CSRD** (post-Omnibus) dal FY2027 |
| Data centre proprio (Milano) | Potenza IT installata **750 kW** → in scope EED art. 12 |
| Cloud | AWS (eu-south-1 Milano, eu-west-1 Irlanda) |
| Device | 1.500 laptop (refresh a 3 anni), 1.300 smartphone |
| Prodotto | Piattaforma e-commerce SaaS + feature AI (GPAI di terzi via API) |
| Marketing | Sul sito: "la piattaforma carbon neutral" |

## Come si parte

Scrivi semplicemente:

> Siamo un'azienda e-commerce con 1.200 dipendenti, un data centre a Milano e workload su AWS. Che obblighi di sostenibilità IT abbiamo?

La skill si attiva da sola (o invocala con `/sustainable-manager:sustainable-it-compliance`).

---

## Step 0 — Maturity Snapshot

La skill NON parte dagli obblighi: prima ti posiziona. Ti farà 4-8 domande sui pilastri SOFT (Strategy, Implementation, Operations, Compliance), tipo:

> *"La sostenibilità IT è nella strategia IT o nel piano ESG, con un owner e un budget?"*

Per Bottega Digitale la risposta onesta è: misuriamo poco, nessun owner → livello **Developing**. Effetto pratico: la skill non ti seppellisce sotto 11 obblighi, ma parte dai 2-3 che scattano subito e da una misura da attivare per prima (di solito il dashboard carbonio del cloud provider).

## Step 1-2 — Profilo e mappatura obblighi

La skill raccoglie il profilo (una domanda alla volta) e produce la matrice di applicabilità. Per Bottega Digitale:

| Area | Si applica? | Perché | Urgenza |
|------|-------------|--------|---------|
| EED art. 12 | **SÌ** | DC da 750 kW ≥ soglia 500 kW | [URGENT] report annuale, scadenza 15 maggio |
| EAA accessibilità | **SÌ** | e-commerce = servizio in scope, applicabile da giu 2025 | [URGENT] già in vigore |
| Green claims (EmpCo) | **SÌ** | "carbon neutral" sul sito | [ATTENTION] vietato dal 27/09/2026 |
| CSRD/ESRS | SÌ | 1.200 dip. + 520M€ | FY2027, primo report 2028 |
| F-gas (raffrescamento DC) | SÌ | chiller di proprietà | al prossimo CapEx cooling |
| WEEE / device | SÌ | 2.800 device in fleet | policy da scrivere |
| AI Act (energia) | Parziale | usa GPAI di terzi → nessun obbligo da provider, ma il consumo entra nello Scope 3 | monitoraggio |
| Right to Repair | Indiretto | rilevante nei criteri d'acquisto device e server | procurement |
| DPP/ESPR | Non ancora | obblighi ICT attesi verso il 2029 | pianificazione |

Nota il pattern: **la skill distingue sempre "in vigore" / "adottato ma non applicabile" / "in arrivo"** — è la sua funzione principale, perché nel sustainable IT circolano molte date sbagliate.

## Step 3 — Standard di misura + strumenti

### sci_calculator.py — misurare il software

Il servizio checkout di Bottega Digitale consuma 120 kWh/mese, gira su hardware con quota embodied di 45.000 gCO2e/mese, e processa 1M di richieste. Comando:

```bash
python3 skills/sustainable-it-compliance/scripts/sci_calculator.py \
  --energy-kwh 120 --region italy --embodied 45000 \
  --functional-units 1000000 --unit-name "API request"
```

Output (reale):

```
Boundary: cli boundary
  E (energy):            120.00 kWh
  I (grid intensity):    260 gCO2e/kWh
  E x I (operational):   31,200 gCO2e
  M (embodied):          45,000 gCO2e (provided)
  R (functional units):  1,000,000 (API request)
  SCI = ((E x I) + M)/R: 0.0762 gCO2e per API request
  Operational share:     40.9%
```

Tre cose da capire:
1. **0,0762 gCO2e/richiesta è un tasso, non un totale**: serve a verificare se il refactoring del prossimo trimestre migliora le cose, NON va sommato nell'inventario aziendale (per quello c'è il GHG Protocol).
2. L'**operational share del 40,9%** dice che qui l'embodied pesa più dell'energia: ottimizzare il codice aiuta, ma allungare la vita dell'hardware aiuta di più.
3. Se non conosci la quota embodied, passa i 4 parametri della formula ISO (`embodied_detail`: TE, TiR, EL, RS) e lo script la calcola — vedi `--help`.

### Checklist EED — il report del data centre

Apri `references/eed-reporting-checklist.md` e falla compilare a facility + IT ops in tre passate: *già misurato / derivabile / gap*. Per Bottega Digitale emerge il quadro tipico:

- Energia totale: 5,2 GWh ✓ (contatore) — energia IT: 3,7 GWh ✓ (uscita UPS) → **PUE 1,41**
- Acqua: **non misurata** → gap; workaround temporaneo: bollette allocate, flag "stima"
- Calore riutilizzato: zero → **ERF = 0, va dichiarato, non omesso**
- Rinnovabili: 35% con GO → REF 0,35

Il report scade il **15 maggio**: la checklist serve proprio a scoprire i gap di strumentazione mesi prima, non la settimana prima.

### Questionario cloud — i dati che AWS deve darti

Per la parte cloud, `references/cloud-provider-questionnaire.md` (15 domande EN+IT). Le tre che contano di più per Bottega Digitale:

- PUE/WUE **per regione** (non media globale) → serve per scegliere tra eu-south-1 e eu-west-1
- Il dashboard carbonio copre l'**embodied hardware** o solo lo Scope 2 allocato?
- I claim rinnovabili sono market-based con disclosure anche location-based?

Se il fornitore risponde solo con medie globali e claim da brochure: è un red flag da mettere nero su bianco nella valutazione fornitori (la skill supplier-engagement lo usa come Modulo F).

## Step 4 — Gap analysis e device policy

Per la flotta device il numero chiave viene dal benchmark (`assets/benchmarks/device-embodied-carbon.json`): un laptop business ≈ 250 kgCO2e embodied. Con 1.500 laptop:

- refresh a 3 anni → 250/3 = **83 kgCO2e/anno per laptop**
- refresh a 5 anni → 250/5 = **50 kgCO2e/anno per laptop**
- differenza × 1.500 laptop ≈ **50 tCO2e/anno risparmiate** solo allungando il ciclo

È l'argomento che convince il CFO (il refresh a 5 anni costa anche meno). La policy completa si genera da `references/device-lifecycle-policy.md`: chiedi a Claude *"generami la device lifecycle policy per la nostra flotta"* e rispondi alle domande sui blocchi (procurement, repair-first, cascata di riuso, WEEE).

## Step 5 — Governance e KPI per il board

Chiusura: la skill propone 5-7 KPI da portare in board. Per Bottega Digitale:

| KPI | Baseline | Target anno 1 |
|-----|----------|---------------|
| PUE data centre | 1,41 | ≤ 1,35 |
| Emissioni cloud (market-based) | da dashboard | -10% |
| SCI checkout | 0,0762 g/req | -20% |
| Vita media laptop | 3 anni | 4 anni |
| % acquisti refurbished | 0% | 20% |
| E-waste in canale certificato | non tracciato | 100% documentato |

Regola d'oro della skill: **GreenOps rides FinOps** — la colonna carbonio entra nella riunione FinOps che esiste già; anomalia di costo e anomalia di carbonio di solito sono la stessa anomalia.

## E il claim "carbon neutral"?

Va rimosso o riformulato entro il 27 settembre 2026 (EmpCo). La skill suggerisce la riformulazione sostanziabile, ad esempio: *"PUE 1,41 in miglioramento, 35% energia rinnovabile certificata GO, SCI del checkout pubblicato e in riduzione"* — dati misurati, metodologia dichiarata, zero parole vietate.

---

## Riepilogo: cosa chiedere, in ordine

1. *"Che obblighi di sostenibilità IT abbiamo?"* → maturity + matrice obblighi
2. *"Prepariamo il report EED del data centre"* → checklist e gap
3. *"Calcola la SCI del nostro servizio X"* → script con i tuoi numeri
4. *"Cosa chiedo al mio cloud provider?"* → questionario Modulo F
5. *"Generami la device lifecycle policy"* → policy pronta da revisionare
6. *"Quali KPI porto in board?"* → set governance

Per l'audit tecnico del codice (pattern green, misure runtime, mobile) usa il plugin `sustainable-code` (skill `gc-*`): questa skill si ferma dove inizia l'IDE.
