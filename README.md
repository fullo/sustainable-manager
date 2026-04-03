# Sustainable Manager - Claude Code Plugin

Plugin per Claude Code che aggiunge competenze di consulenza sulla sostenibilita con approccio science-based.

## Cosa fa

- **Analisi documenti** - Legge e analizza report di sostenibilita, bilanci ESG, dati Excel/CSV
- **Analisi LCA** - Interpreta Life Cycle Assessment ed EPD con focus su hotspot e trade-off
- **Rilevamento greenwashing** - Valuta criticamente claim ambientali separando dati da dichiarazioni
- **Consulenza Socratica** - Guida l'utente nella raccolta dati per costruire un report da zero
- **Visualizzazioni** - Genera grafici professionali con matplotlib/plotly (bar, radar, heatmap, sankey)
- **Supporto report** - Struttura report allineati a ESRS, GRI, SASB, TCFD
- **Assessment ESRS** - Questionario di autovalutazione per la readiness CSRD/ESRS
- **Procurement sostenibile** - Guida ISO 20400, valutazione fornitori, life cycle costing

## Framework supportati

ESRS/CSRD, GRI, SASB, TCFD, SDGs, SBTi, ISO 14040/14044, ISO 20400

## Installazione

### Da npm

```bash
claude plugin install sustainable-manager@<marketplace-name>
```

### Da GitHub

```bash
# Clona il repository
git clone https://github.com/fullo/sustainable-manager.git

# Installa come plugin locale (dalla directory del tuo progetto)
claude plugin add /path/to/sustainable-manager
```

## Uso

Una volta installato, il plugin si attiva automaticamente quando menzioni temi di sostenibilita. Puoi anche invocarlo esplicitamente:

```
/sustainable-manager:sustainable-manager
```

## Struttura

```
sustainable-manager/
├── .claude-plugin/
│   └── plugin.json              # Manifesto del plugin
├── skills/
│   └── sustainable-manager/
│       ├── SKILL.md             # Definizione della skill
│       ├── references/          # Documentazione di riferimento
│       │   ├── frameworks.md
│       │   ├── lca-science-based.md
│       │   ├── greenwashing-detection.md
│       │   ├── procurement.md
│       │   ├── socratic-interview.md
│       │   └── efrag-updates.md
│       ├── scripts/             # Helper Python
│       │   ├── chart_generator.py
│       │   └── esrs_assessment.py
│       └── assets/
│           ├── benchmarks/      # Benchmark settoriali
│           └── templates/       # Template per settore
├── package.json
└── README.md
```

## Requisiti

- Claude Code CLI
- Python 3.8+ (per le visualizzazioni)
- matplotlib, numpy (per i grafici)

## Licenza

MIT
