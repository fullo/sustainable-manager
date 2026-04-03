# Supplier ESG Questionnaire — Module Library

Comprehensive question library for supplier engagement. Each question includes ID, text in English and Italian, answer type, weight (1-5), and evidence requirements.

**Answer types**:
- `numeric`: quantitative value with unit
- `yes_no`: binary yes/no
- `yes_no_details`: yes/no with free-text explanation
- `yes_no_certification`: yes/no/certified (with certification name)
- `scale_0_100`: percentage scale
- `text`: free-text response
- `text_list`: comma-separated list
- `yes_no_amount`: yes/no with amount (EUR)
- `multiple_choice`: select from options

---

## Module A: Environmental (Scope 3 / ESRS E1-E5)

### Climate & Energy

| ID | Question (EN) | Question (IT) | Type | Weight | Evidence |
|----|--------------|---------------|------|--------|----------|
| A1 | What are your total GHG Scope 1+2 emissions (tCO2e) for the last reporting year? | Quali sono le vostre emissioni GHG Scope 1+2 totali (tCO2e) per l'ultimo anno di rendicontazione? | numeric | 5 | GHG report or calculation methodology |
| A2 | What is your total energy consumption (MWh)? | Qual e il vostro consumo energetico totale (MWh)? | numeric | 4 | Utility bills or energy audit |
| A3 | What percentage of your energy comes from renewable sources? | Quale percentuale della vostra energia proviene da fonti rinnovabili? | scale_0_100 | 3 | Green certificates, PPA contracts, RECs |
| A4 | Do you have an environmental management system in place? | Avete un sistema di gestione ambientale? | yes_no_certification | 3 | ISO 14001 certificate or equivalent |
| A5 | Have you set GHG reduction targets? If yes, please describe. | Avete fissato obiettivi di riduzione GHG? Se si, descrivete. | yes_no_details | 4 | Public commitment, SBTi validation |
| A6 | Are your targets validated by SBTi or equivalent? | I vostri target sono validati da SBTi o equivalente? | yes_no | 4 | SBTi dashboard listing |
| A7 | Do you have a climate transition plan? | Avete un piano di transizione climatica? | yes_no_details | 3 | Published transition plan |
| A8 | Can you provide product-level carbon footprint data? | Potete fornire dati sull'impronta carbonica a livello di prodotto? | yes_no | 3 | EPD, LCA report, or product carbon footprint |
| A9 | What is the GHG intensity of the products/services supplied to us (tCO2e/unit)? | Qual e l'intensita GHG dei prodotti/servizi forniti a noi (tCO2e/unita)? | numeric | 5 | Product-level calculation |

### Water

| ID | Question (EN) | Question (IT) | Type | Weight | Evidence |
|----|--------------|---------------|------|--------|----------|
| A10 | What is your total water consumption (m3/year)? | Qual e il vostro consumo idrico totale (m3/anno)? | numeric | 2 | Utility records or water meter data |
| A11 | Do any of your operations occur in water-stressed areas? | Qualcuna delle vostre attivita si svolge in aree a stress idrico? | yes_no_details | 3 | WRI Aqueduct assessment or equivalent |
| A12 | What percentage of water is recycled/reused? | Quale percentuale di acqua viene riciclata/riutilizzata? | scale_0_100 | 2 | Water management records |

### Waste & Circular Economy

| ID | Question (EN) | Question (IT) | Type | Weight | Evidence |
|----|--------------|---------------|------|--------|----------|
| A13 | What is the total waste generated (tonnes/year)? | Quanti rifiuti totali vengono generati (tonnellate/anno)? | numeric | 2 | Waste manifests (MUD in Italy) |
| A14 | What is your waste recycling rate (%)? | Qual e il vostro tasso di riciclo dei rifiuti (%)? | scale_0_100 | 3 | Recycling certificates, waste records |
| A15 | What is the total hazardous waste generated (tonnes/year)? | Quanti rifiuti pericolosi vengono generati (tonnellate/anno)? | numeric | 3 | Waste manifests, FIR (Italy) |
| A16 | Do you use substances of concern in your production? If yes, list them. | Utilizzate sostanze preoccupanti nella produzione? Se si, elencarle. | yes_no_list | 3 | REACH compliance documentation |

---

## Module B: Social (CSDDD / ESRS S1-S2)

### Human Rights & Labor

| ID | Question (EN) | Question (IT) | Type | Weight | Evidence |
|----|--------------|---------------|------|--------|----------|
| B1 | Do you have a human rights policy? | Avete una politica sui diritti umani? | yes_no | 5 | Published policy document |
| B2 | Do you conduct human rights due diligence? Describe your process. | Svolgete la due diligence sui diritti umani? Descrivete il processo. | yes_no_details | 5 | Process documentation, reports |
| B3 | Have you assessed child labor risks in your operations and supply chain? | Avete valutato i rischi di lavoro minorile nelle vostre attivita e catena di fornitura? | yes_no | 5 | Risk assessment report |
| B4 | Have you assessed forced labor risks in your operations and supply chain? | Avete valutato i rischi di lavoro forzato nelle vostre attivita e catena di fornitura? | yes_no | 5 | Risk assessment report |
| B5 | Is freedom of association respected for all workers? | La liberta di associazione e rispettata per tutti i lavoratori? | yes_no | 4 | Policy, collective bargaining agreements |
| B6 | Do you pay a living wage to all workers? How do you verify this? | Pagate un salario dignitoso a tutti i lavoratori? Come lo verificate? | yes_no_details | 4 | Payroll benchmarking against living wage |
| B7 | What is your Lost Time Injury Rate (LTIR)? | Qual e il vostro tasso di infortuni con assenza dal lavoro (LTIR)? | numeric | 3 | H&S records, INAIL data (Italy) |

### Health & Safety

| ID | Question (EN) | Question (IT) | Type | Weight | Evidence |
|----|--------------|---------------|------|--------|----------|
| B8 | Do you have a health and safety management system? | Avete un sistema di gestione della salute e sicurezza? | yes_no_certification | 4 | ISO 45001 or equivalent, DVR (Italy) |
| B9 | How many training hours per employee did you provide last year? | Quante ore di formazione per dipendente avete fornito l'ultimo anno? | numeric | 2 | Training records |
| B10 | Do you have a grievance mechanism for workers and external stakeholders? | Avete un meccanismo di reclamo per lavoratori e stakeholder esterni? | yes_no | 4 | Mechanism description, access details |
| B11 | Have you had any work-related fatalities in the last 3 years? | Avete avuto decessi sul lavoro negli ultimi 3 anni? | yes_no_details | 5 | Incident reports |
| B12 | Do you extend social requirements to your own suppliers (Tier 2+)? | Estendete i requisiti sociali ai vostri fornitori (Tier 2+)? | yes_no_details | 3 | Supplier code of conduct, audit records |

---

## Module C: Governance

| ID | Question (EN) | Question (IT) | Type | Weight | Evidence |
|----|--------------|---------------|------|--------|----------|
| C1 | Do you have a code of conduct? | Avete un codice di condotta? | yes_no | 3 | Published code of conduct |
| C2 | Do you have an anti-corruption and anti-bribery policy? | Avete una politica anti-corruzione e anti-concussione? | yes_no | 4 | Published policy |
| C3 | Do you have a whistleblowing channel accessible to internal and external parties? | Avete un canale di segnalazione (whistleblowing) accessibile a parti interne ed esterne? | yes_no | 3 | Channel description, D.Lgs. 24/2023 compliance |
| C4 | Are you GDPR-compliant? Do you have a Data Protection Officer? | Siete conformi al GDPR? Avete un Responsabile della Protezione dei Dati (DPO)? | yes_no | 3 | DPO appointment, privacy policy |
| C5 | Have you been subject to sanctions, fines, or legal proceedings in the last 3 years? | Siete stati soggetti a sanzioni, ammende o procedimenti legali negli ultimi 3 anni? | yes_no_details | 4 | Self-declaration with details |
| C6 | Do you have a Modello Organizzativo 231 (for Italian companies)? | Avete adottato un Modello Organizzativo 231? | yes_no | 3 | MOG 231 documentation |
| C7 | Do you publish a sustainability report? | Pubblicate un report di sostenibilita? | yes_no_details | 2 | Published report (link/copy) |
| C8 | Do you have a conflict minerals policy (if applicable)? | Avete una politica sui minerali di conflitto (se applicabile)? | yes_no | 3 | Published policy, OECD DDG compliance |

---

## Module D: CBAM-Specific (for Importers of Covered Goods)

Applicable to suppliers of: cement, iron & steel, aluminium, fertilizers, electricity, hydrogen.

| ID | Question (EN) | Question (IT) | Type | Weight | Evidence |
|----|--------------|---------------|------|--------|----------|
| D1 | Describe the production method for the goods supplied to us. | Descrivete il metodo di produzione dei beni forniti a noi. | text | 5 | Process description, flow diagram |
| D2 | What are the direct (Scope 1) emissions per tonne of product (tCO2e/t)? | Quali sono le emissioni dirette (Scope 1) per tonnellata di prodotto (tCO2e/t)? | numeric | 5 | Verified calculation per CBAM methodology |
| D3 | What are the indirect (Scope 2) emissions per tonne of product (tCO2e/t)? | Quali sono le emissioni indirette (Scope 2) per tonnellata di prodotto (tCO2e/t)? | numeric | 4 | Grid emission factor x consumption/tonne |
| D4 | List the energy sources used in production (type and share %). | Elencate le fonti energetiche utilizzate nella produzione (tipo e quota %). | text_list | 4 | Energy contracts, fuel purchase records |
| D5 | Do you pay a carbon price in your jurisdiction? If yes, what amount (EUR/tCO2e)? | Pagate un prezzo del carbonio nella vostra giurisdizione? Se si, quale importo (EUR/tCO2e)? | yes_no_amount | 3 | Carbon tax/ETS payment receipts |
| D6 | Can you provide installation-level emission data as required by CBAM regulation? | Potete fornire dati sulle emissioni a livello di impianto come richiesto dal regolamento CBAM? | yes_no | 5 | CBAM communication template |
| D7 | Is your installation covered by an emissions trading system? If yes, which one? | Il vostro impianto e coperto da un sistema di scambio di emissioni? Se si, quale? | yes_no_details | 3 | ETS registration, allowance records |
| D8 | What are the precursor products used and their embedded emissions? | Quali sono i prodotti precursori utilizzati e le loro emissioni incorporate? | text | 4 | Precursor supplier data |

---

## Module E: EU Taxonomy (Value Chain Alignment)

| ID | Question (EN) | Question (IT) | Type | Weight | Evidence |
|----|--------------|---------------|------|--------|----------|
| E1 | What are the NACE codes of your main economic activities? | Quali sono i codici NACE delle vostre principali attivita economiche? | text | 3 | Chamber of commerce registration |
| E2 | Are any of your activities eligible under the EU Taxonomy? | Qualcuna delle vostre attivita e ammissibile (eligible) ai sensi della Tassonomia UE? | yes_no_details | 3 | Self-assessment against Taxonomy activities |
| E3 | For eligible activities: do you meet the Technical Screening Criteria? | Per le attivita ammissibili: soddisfate i Criteri di Screening Tecnici? | yes_no_details | 4 | TSC compliance evidence |
| E4 | Can you demonstrate Do No Significant Harm (DNSH) compliance? | Potete dimostrare la conformita al principio Do No Significant Harm (DNSH)? | yes_no | 3 | DNSH assessment documentation |
| E5 | Can you demonstrate compliance with Minimum Safeguards? | Potete dimostrare la conformita alle Minimum Safeguards? | yes_no | 3 | OECD Guidelines, UNGPs, ILO compliance |
| E6 | What percentage of your revenue/CapEx/OpEx is Taxonomy-aligned? | Quale percentuale del vostro fatturato/CapEx/OpEx e allineata alla Tassonomia? | numeric | 3 | Taxonomy disclosure or self-assessment |

---

## Simplified Version (Micro/Small Suppliers, <50 employees)

For smaller suppliers with limited ESG capacity. 10 essential questions, simple language, yes/no/in-progress format. No evidence required for first assessment.

| # | Question (EN) | Question (IT) | Type |
|---|--------------|---------------|------|
| S1 | Do you measure your energy consumption? | Misurate il vostro consumo energetico? | yes_no_progress |
| S2 | Are you taking any steps to reduce energy use or switch to renewables? | State prendendo misure per ridurre il consumo energetico o passare alle rinnovabili? | yes_no_progress |
| S3 | Do you measure and manage your waste? | Misurate e gestite i vostri rifiuti? | yes_no_progress |
| S4 | Do you comply with all applicable environmental regulations? | Siete conformi a tutte le normative ambientali applicabili? | yes_no |
| S5 | Do you ensure safe working conditions for all employees? | Garantite condizioni di lavoro sicure per tutti i dipendenti? | yes_no |
| S6 | Do you have a process to identify and prevent human rights risks? | Avete un processo per identificare e prevenire rischi sui diritti umani? | yes_no_progress |
| S7 | Do you have a code of conduct or ethics policy? | Avete un codice di condotta o una politica etica? | yes_no |
| S8 | Do you comply with GDPR and data protection regulations? | Siete conformi al GDPR e alle normative sulla protezione dei dati? | yes_no |
| S9 | Are you willing to participate in improvement programs with us? | Siete disponibili a partecipare a programmi di miglioramento con noi? | yes_no |
| S10 | Do you extend any sustainability requirements to your own suppliers? | Estendete requisiti di sostenibilita ai vostri fornitori? | yes_no_progress |

**Answer type `yes_no_progress`**: Yes / In progress / No / Not applicable

**Scoring**: Yes = 100%, In progress = 50%, No = 0%, N/A = excluded from calculation

---

## Sector-Specific Add-On Questions

### Add-On: Food & Agriculture
| ID | Question (EN) | Question (IT) | Type | Weight |
|----|--------------|---------------|------|--------|
| F1 | Do you have a zero-deforestation commitment for commodity sourcing? | Avete un impegno zero-deforestazione per l'approvvigionamento di materie prime? | yes_no | 4 |
| F2 | Are your agricultural commodities certified (e.g., RSPO, Rainforest Alliance, FSC)? | Le vostre materie prime agricole sono certificate (es. RSPO, Rainforest Alliance, FSC)? | yes_no_details | 3 |
| F3 | Do you track food waste in your operations? | Monitorate lo spreco alimentare nelle vostre attivita? | yes_no | 3 |
| F4 | Do you use integrated pest management (IPM) or organic farming practices? | Utilizzate la gestione integrata dei parassiti (IPM) o pratiche di agricoltura biologica? | yes_no_details | 2 |
| F5 | What percentage of your packaging is recyclable or compostable? | Quale percentuale del vostro packaging e riciclabile o compostabile? | scale_0_100 | 3 |

### Add-On: Textiles & Fashion
| ID | Question (EN) | Question (IT) | Type | Weight |
|----|--------------|---------------|------|--------|
| T1 | Do you use restricted substance lists (MRSL/RSL) such as ZDHC? | Utilizzate liste di sostanze soggette a restrizioni (MRSL/RSL) come ZDHC? | yes_no | 4 |
| T2 | What percentage of materials used are recycled or certified sustainable? | Quale percentuale dei materiali utilizzati e riciclata o certificata sostenibile? | scale_0_100 | 3 |
| T3 | Do you have traceability to raw material origin (Tier 3-4)? | Avete tracciabilita fino all'origine della materia prima (Tier 3-4)? | yes_no_details | 4 |
| T4 | Do you conduct social audits of your production facilities? If yes, which standard? | Svolgete audit sociali dei vostri stabilimenti produttivi? Se si, quale standard? | yes_no_details | 4 |
| T5 | What is your water treatment process for dyeing/finishing wastewater? | Qual e il vostro processo di trattamento delle acque reflue di tintura/finissaggio? | text | 3 |

### Add-On: Electronics & Technology
| ID | Question (EN) | Question (IT) | Type | Weight |
|----|--------------|---------------|------|--------|
| EL1 | Do you comply with the EU Conflict Minerals Regulation (2017/821)? | Siete conformi al Regolamento UE sui minerali di conflitto (2017/821)? | yes_no | 4 |
| EL2 | Do you have a Responsible Minerals Initiative (RMI) CMRT/EMRT? | Avete un CMRT/EMRT della Responsible Minerals Initiative (RMI)? | yes_no | 3 |
| EL3 | What is the energy efficiency rating of your products? | Qual e la classe di efficienza energetica dei vostri prodotti? | text | 3 |
| EL4 | Do you offer take-back or recycling programs for end-of-life products? | Offrite programmi di ritiro o riciclo per i prodotti a fine vita? | yes_no | 3 |
| EL5 | Do you comply with RoHS and WEEE directives? | Siete conformi alle direttive RoHS e RAEE? | yes_no | 4 |

### Add-On: Construction & Building Materials
| ID | Question (EN) | Question (IT) | Type | Weight |
|----|--------------|---------------|------|--------|
| CO1 | Do you provide Environmental Product Declarations (EPDs) for your products? | Fornite Dichiarazioni Ambientali di Prodotto (EPD) per i vostri prodotti? | yes_no | 4 |
| CO2 | What is the recycled content percentage of your products? | Qual e la percentuale di contenuto riciclato dei vostri prodotti? | scale_0_100 | 3 |
| CO3 | Do you comply with CAM (Criteri Ambientali Minimi) for public procurement in Italy? | Siete conformi ai CAM (Criteri Ambientali Minimi) per gli appalti pubblici in Italia? | yes_no | 4 |
| CO4 | Do your products have VOC emission certifications? | I vostri prodotti hanno certificazioni sulle emissioni di COV? | yes_no_details | 3 |
| CO5 | Do you track and report the embodied carbon of your products? | Monitorate e rendicontate il carbonio incorporato nei vostri prodotti? | yes_no | 3 |

---

## Questionnaire Design Guidelines

### Response Format Standards
- **Numeric fields**: always specify unit of measurement (tCO2e, MWh, m3, tonnes, EUR, %)
- **Date references**: always specify reporting period (calendar year or fiscal year)
- **Evidence requirements**: specify acceptable formats (PDF, certificate scan, report link)
- **Confidentiality**: mark all data as confidential, shared only for compliance purposes

### Progressive Disclosure
For suppliers completing the questionnaire for the first time:
1. **Year 1**: Simplified version (S1-S10) + Module C basics (C1-C4)
2. **Year 2**: Full Module A (environmental) + Module B (social)
3. **Year 3**: Full questionnaire including sector-specific add-ons and evidence requirements

### Digital Platform Integration
The questionnaire can be deployed via:
- **Excel template**: for suppliers without digital platform access
- **Google Forms / Microsoft Forms**: for basic digital collection
- **EcoVadis / CDP**: accept existing ratings as alternative responses
- **Custom API (JSON)**: for automated data exchange with supplier ERP systems

### JSON Schema for Digital Collection
```json
{
  "supplier_id": "string",
  "supplier_name": "string",
  "date": "YYYY-MM-DD",
  "reporting_period": "YYYY",
  "responses": {
    "A1": {
      "value": "number | string | boolean",
      "unit": "string (optional)",
      "evidence": "boolean",
      "evidence_type": "string (optional)",
      "details": "string (optional)",
      "not_applicable": "boolean (optional)"
    }
  }
}
```

### Scoring Weights Rationale
- **Weight 5 (Critical)**: Data points required by regulation with penalties for non-compliance, or representing severe human rights risks
- **Weight 4 (High)**: Data points required by multiple frameworks or representing significant ESG risks
- **Weight 3 (Medium)**: Important for comprehensive ESG assessment but not individually critical
- **Weight 2 (Standard)**: Useful for benchmarking and improvement tracking
- **Weight 1 (Low)**: Nice-to-have, forward-looking or aspirational metrics
