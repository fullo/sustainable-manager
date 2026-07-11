# Guida all'uso del plugin Sustainable Manager

Guida pratica per chi usa il plugin per la prima volta. Non serve conoscere Claude Code a fondo: basta sapere **cosa chiedere** e **quale skill risponde**.

## Come funzionano le skill

Le skill si attivano in due modi:

1. **Automaticamente**: scrivi la tua domanda in linguaggio naturale (italiano o inglese) e Claude attiva la skill giusta in base al contesto. Esempio: *"importiamo acciaio dalla Turchia, cosa dobbiamo fare per il CBAM?"* attiva `cbam-compliance`.
2. **Esplicitamente**: invochi la skill con il comando slash, ad esempio `/sustainable-manager:eu-regulation-matrix`.

Tutte le skill:
- rispondono nella tua lingua (se scrivi in italiano, rispondono in italiano con il contesto normativo italiano);
- fanno **una domanda alla volta** — non serve preparare tutti i dati prima, la skill ti guida;
- producono output che sono **bozze da revisionare**, non certificazioni: il giudizio finale resta tuo (e del tuo legale/revisore).

## Quale skill per quale domanda

| La tua domanda | Skill | Comando |
|----------------|-------|---------|
| "Quali normative si applicano alla mia azienda?" | eu-regulation-matrix | `/sustainable-manager:eu-regulation-matrix` |
| "Devo fare l'analisi di doppia materialità" | double-materiality | `/sustainable-manager:double-materiality` |
| "Le nostre attività sono allineate alla Tassonomia?" | eu-taxonomy-checker | `/sustainable-manager:eu-taxonomy-checker` |
| "Da dove parto con lo Scope 3?" | scope3-mapper | `/sustainable-manager:scope3-mapper` |
| "Importiamo cemento/acciaio/alluminio da fuori UE" | cbam-compliance | `/sustainable-manager:cbam-compliance` |
| "Cosa c'entra la biodiversità con noi?" | biodiversity-screener | `/sustainable-manager:biodiversity-screener` |
| "Quanto è circolare il nostro packaging/prodotto?" | circular-economy | `/sustainable-manager:circular-economy` |
| "Quali dati servono per più framework insieme?" | cross-framework-mapper | `/sustainable-manager:cross-framework-mapper` |
| "Dobbiamo costruire il piano di transizione climatica" | transition-plan-builder | `/sustainable-manager:transition-plan-builder` |
| "Come raccolgo i dati ESG dai fornitori?" | supplier-engagement | `/sustainable-manager:supplier-engagement` |
| "Data centre, cloud, device, AI: che obblighi abbiamo?" | sustainable-it-compliance | `/sustainable-manager:sustainable-it-compliance` |
| "Analizza questo report di sostenibilità / costruiamone uno" | sustainable-manager (core) | `/sustainable-manager:sustainable-manager` |

## Scenari realistici (da dove partire)

**«Siamo una PMI e la banca ci ha chiesto i dati ESG»** — Non sei in scope CSRD (dopo l'Omnibus servono 1.000+ dipendenti E 450M€), ma le richieste di banche e clienti sono reali. Parti da `eu-regulation-matrix` per confermare cosa NON ti si applica, poi usa il core `sustainable-manager` citando il VSME: le richieste dei clienti in scope CSRD non possono superare quel perimetro.

**«Il nostro cliente tedesco ci ha mandato un questionario di 80 domande»** — `supplier-engagement` sa leggere e prioritizzare i questionari (e ti dice cosa puoi legittimamente rifiutare se hai meno di 1.000 dipendenti). Se il questionario tocca emissioni, `scope3-mapper` ti aiuta a produrre i numeri con il metodo spend-based come primo passo.

**«Importiamo 120 tonnellate di profilati d'acciaio l'anno dalla Turchia»** — `cbam-compliance`: sei sopra la soglia de minimis (50t cumulative), quindi ti serve lo status di dichiarante autorizzato; la skill ti calcola le emissioni incorporate e stima i certificati (acquisto dal febbraio 2027, dichiarazione entro il 30 settembre).

**«Il CFO vuole sapere quanto ci costa il net-zero»** — `transition-plan-builder`, sei fasi dalla baseline al piano CapEx. Attenzione alla versione SBTi: chi si fa validare dal 1° febbraio 2028 deve usare il Corporate Net-Zero Standard v2.0.

**«Abbiamo un data centre e 1.500 laptop, l'IT ci chiede cosa deve fare»** — `sustainable-it-compliance`: vedi la [guida completa con caso di studio](sustainable-it-compliance.md).

**«Il marketing vuole scrivere "piattaforma carbon neutral" sul sito»** — Fermali e usa `sustainable-it-compliance` (claim IT) o il core (greenwashing detection): dal 27 settembre 2026 la Empowering Consumers Directive vieta i claim di neutralità basati su compensazioni.

## I tre errori più comuni dei principianti

1. **Chiedere "tutto subito"**: le skill lavorano a step. Rispondi alle domande una alla volta; puoi sempre dire "non lo so" — la skill ti dirà come stimare o dove trovare il dato.
2. **Prendere gli output come definitivi**: tabelle, matrici e stime sono bozze di lavoro con fonti e assunzioni esplicite. Verificale prima di metterle in un documento ufficiale.
3. **Usare la skill sbagliata per il livello sbagliato**: questo plugin lavora a livello *manageriale/compliance*. Per l'audit tecnico del codice (green coding, misure di runtime) usa il plugin gemello `sustainable-code` (skill `gc-*`).

## Requisiti tecnici

Gli script Python (calcolatori SCI, Scope 3, circolarità, scoring fornitori, grafici) richiedono Python 3.8+ e, per i grafici, matplotlib/numpy. Claude li esegue per te: non devi lanciarli a mano, ma puoi farlo (ogni script ha `--help` ed esempi nell'header).
