#!/usr/bin/env python3
"""
ESRS Readiness Self-Assessment Tool
====================================
A questionnaire-based tool to evaluate an organization's readiness for ESRS
(European Sustainability Reporting Standards) compliance under the CSRD directive.

Usage as CLI:
    python esrs_assessment.py --interactive
    python esrs_assessment.py --load responses.json --report
    python esrs_assessment.py --load responses.json --radar output_radar.png

Usage as module:
    from esrs_assessment import load_questionnaire, score_responses, generate_report

    questionnaire = load_questionnaire()
    # ... collect responses ...
    scores = score_responses(responses, questionnaire)
    report = generate_report(scores, responses, questionnaire)
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

# ---------------------------------------------------------------------------
# Questionnaire definition
# ---------------------------------------------------------------------------

QUESTIONNAIRE: list[dict[str, Any]] = [
    # ── ESRS 2 — General Disclosures ──────────────────────────────────────
    {
        "id": "ESRS2_01",
        "esrs_standard": "ESRS 2",
        "pillar": "General",
        "question": "Has the organization conducted a double materiality assessment?",
        "question_it": "L'organizzazione ha condotto un'analisi di doppia materialita?",
        "answer_type": "yes_no",
        "weight": 3,
        "requirement": "ESRS 2 IRO-1 requires identification and assessment of material impacts, risks and opportunities through double materiality.",
    },
    {
        "id": "ESRS2_02",
        "esrs_standard": "ESRS 2",
        "pillar": "General",
        "question": "Is there a formal governance body or committee responsible for sustainability matters?",
        "question_it": "Esiste un organo di governance o comitato formalmente responsabile delle questioni di sostenibilita?",
        "answer_type": "yes_no",
        "weight": 2,
        "requirement": "ESRS 2 GOV-1 requires disclosure of governance bodies' role in sustainability.",
    },
    {
        "id": "ESRS2_03",
        "esrs_standard": "ESRS 2",
        "pillar": "General",
        "question": "How integrated is sustainability into the overall business strategy? (1=not at all, 5=fully embedded)",
        "question_it": "Quanto e integrata la sostenibilita nella strategia aziendale complessiva? (1=per niente, 5=completamente integrata)",
        "answer_type": "scale_1_5",
        "weight": 2,
        "requirement": "ESRS 2 SBM-1 requires description of strategy and business model in relation to sustainability.",
    },
    {
        "id": "ESRS2_04",
        "esrs_standard": "ESRS 2",
        "pillar": "General",
        "question": "Does the organization have a stakeholder engagement process for sustainability topics?",
        "question_it": "L'organizzazione ha un processo di coinvolgimento degli stakeholder sulle tematiche di sostenibilita?",
        "answer_type": "yes_no",
        "weight": 2,
        "requirement": "ESRS 2 SBM-2 requires disclosure on interests and views of stakeholders.",
    },
    # ── ESRS E1 — Climate Change ─────────────────────────────────────────
    {
        "id": "E1_01",
        "esrs_standard": "ESRS E1",
        "pillar": "Environment",
        "question": "Does the organization measure and report Scope 1 and Scope 2 GHG emissions?",
        "question_it": "L'organizzazione misura e rendiconta le emissioni GHG Scope 1 e Scope 2?",
        "answer_type": "yes_no",
        "weight": 3,
        "requirement": "ESRS E1-6 requires disclosure of Scope 1, 2 and 3 GHG emissions.",
    },
    {
        "id": "E1_02",
        "esrs_standard": "ESRS E1",
        "pillar": "Environment",
        "question": "Does the organization measure Scope 3 GHG emissions (at least key categories)?",
        "question_it": "L'organizzazione misura le emissioni GHG Scope 3 (almeno le categorie principali)?",
        "answer_type": "yes_no",
        "weight": 3,
        "requirement": "ESRS E1-6 requires Scope 3 disclosure for material categories.",
    },
    {
        "id": "E1_03",
        "esrs_standard": "ESRS E1",
        "pillar": "Environment",
        "question": "Has the organization set science-based or Paris-aligned emission reduction targets?",
        "question_it": "L'organizzazione ha fissato obiettivi di riduzione delle emissioni science-based o allineati a Parigi?",
        "answer_type": "yes_no",
        "weight": 3,
        "requirement": "ESRS E1-4 requires climate-related targets aligned with limiting warming to 1.5C.",
    },
    {
        "id": "E1_04",
        "esrs_standard": "ESRS E1",
        "pillar": "Environment",
        "question": "Is there a documented climate transition plan?",
        "question_it": "Esiste un piano di transizione climatica documentato?",
        "answer_type": "yes_no",
        "weight": 2,
        "requirement": "ESRS E1-1 requires a transition plan for climate change mitigation.",
    },
    # ── ESRS E2 — Pollution ──────────────────────────────────────────────
    {
        "id": "E2_01",
        "esrs_standard": "ESRS E2",
        "pillar": "Environment",
        "question": "Does the organization monitor and report air, water, and soil pollution levels?",
        "question_it": "L'organizzazione monitora e rendiconta i livelli di inquinamento di aria, acqua e suolo?",
        "answer_type": "scale_1_5",
        "weight": 2,
        "requirement": "ESRS E2-4 requires disclosure of pollutant emissions to air, water and soil.",
    },
    {
        "id": "E2_02",
        "esrs_standard": "ESRS E2",
        "pillar": "Environment",
        "question": "Are there policies and actions in place to prevent and control pollution?",
        "question_it": "Esistono politiche e azioni per prevenire e controllare l'inquinamento?",
        "answer_type": "yes_no",
        "weight": 2,
        "requirement": "ESRS E2-1 requires disclosure of policies related to pollution.",
    },
    # ── ESRS E3 — Water and Marine Resources ────────────────────────────
    {
        "id": "E3_01",
        "esrs_standard": "ESRS E3",
        "pillar": "Environment",
        "question": "Does the organization track water withdrawal, consumption and discharge by source?",
        "question_it": "L'organizzazione traccia prelievo, consumo e scarico idrico per fonte?",
        "answer_type": "yes_no",
        "weight": 2,
        "requirement": "ESRS E3-4 requires disclosure of water consumption.",
    },
    {
        "id": "E3_02",
        "esrs_standard": "ESRS E3",
        "pillar": "Environment",
        "question": "Are operations in water-stressed areas identified and managed?",
        "question_it": "Le operazioni in aree con stress idrico sono identificate e gestite?",
        "answer_type": "yes_no",
        "weight": 2,
        "requirement": "ESRS E3-1 requires policies related to water and marine resources.",
    },
    # ── ESRS E4 — Biodiversity and Ecosystems ───────────────────────────
    {
        "id": "E4_01",
        "esrs_standard": "ESRS E4",
        "pillar": "Environment",
        "question": "Has the organization assessed its impact on biodiversity and ecosystems?",
        "question_it": "L'organizzazione ha valutato il proprio impatto sulla biodiversita e gli ecosistemi?",
        "answer_type": "scale_1_5",
        "weight": 2,
        "requirement": "ESRS E4-4 requires disclosure on biodiversity and ecosystem impacts.",
    },
    # ── ESRS E5 — Resource Use and Circular Economy ─────────────────────
    {
        "id": "E5_01",
        "esrs_standard": "ESRS E5",
        "pillar": "Environment",
        "question": "Does the organization track resource inflows (materials) and waste outflows by type?",
        "question_it": "L'organizzazione traccia i flussi di risorse in ingresso (materiali) e i rifiuti in uscita per tipologia?",
        "answer_type": "yes_no",
        "weight": 2,
        "requirement": "ESRS E5-4 requires disclosure of resource inflows and E5-5 of resource outflows.",
    },
    {
        "id": "E5_02",
        "esrs_standard": "ESRS E5",
        "pillar": "Environment",
        "question": "What percentage of waste is recycled or recovered? (enter numeric %)",
        "question_it": "Quale percentuale di rifiuti viene riciclata o recuperata? (inserire % numerico)",
        "answer_type": "numeric",
        "weight": 1,
        "requirement": "ESRS E5-5 requires waste-related metrics.",
    },
    # ── ESRS S1 — Own Workforce ──────────────────────────────────────────
    {
        "id": "S1_01",
        "esrs_standard": "ESRS S1",
        "pillar": "Social",
        "question": "Does the organization have policies on fair wages, working conditions and social dialogue?",
        "question_it": "L'organizzazione ha politiche su retribuzione equa, condizioni di lavoro e dialogo sociale?",
        "answer_type": "yes_no",
        "weight": 2,
        "requirement": "ESRS S1-1 requires policies related to own workforce.",
    },
    {
        "id": "S1_02",
        "esrs_standard": "ESRS S1",
        "pillar": "Social",
        "question": "Does the organization track and disclose diversity metrics (gender, age, disability)?",
        "question_it": "L'organizzazione traccia e divulga metriche di diversita (genere, eta, disabilita)?",
        "answer_type": "yes_no",
        "weight": 2,
        "requirement": "ESRS S1-9 requires diversity metrics disclosure.",
    },
    {
        "id": "S1_03",
        "esrs_standard": "ESRS S1",
        "pillar": "Social",
        "question": "Is there a health and safety management system in place (e.g., ISO 45001)?",
        "question_it": "E presente un sistema di gestione della salute e sicurezza (es. ISO 45001)?",
        "answer_type": "yes_no",
        "weight": 2,
        "requirement": "ESRS S1-14 requires disclosure of health and safety indicators.",
    },
    {
        "id": "S1_04",
        "esrs_standard": "ESRS S1",
        "pillar": "Social",
        "question": "How many training hours per employee were provided last year?",
        "question_it": "Quante ore di formazione per dipendente sono state erogate nell'ultimo anno?",
        "answer_type": "numeric",
        "weight": 1,
        "requirement": "ESRS S1-13 requires disclosure of training and skills development metrics.",
    },
    {
        "id": "S1_05",
        "esrs_standard": "ESRS S1",
        "pillar": "Social",
        "question": "Is there a formal grievance mechanism or whistleblowing channel for employees?",
        "question_it": "Esiste un meccanismo formale di reclamo o un canale di segnalazione (whistleblowing) per i dipendenti?",
        "answer_type": "yes_no",
        "weight": 2,
        "requirement": "ESRS S1-3 requires disclosure of remediation processes.",
    },
    # ── ESRS S2 — Workers in the Value Chain ─────────────────────────────
    {
        "id": "S2_01",
        "esrs_standard": "ESRS S2",
        "pillar": "Social",
        "question": "Does the organization assess human rights risks in its supply chain?",
        "question_it": "L'organizzazione valuta i rischi per i diritti umani nella propria catena di fornitura?",
        "answer_type": "scale_1_5",
        "weight": 2,
        "requirement": "ESRS S2-1 requires policies related to value chain workers.",
    },
    {
        "id": "S2_02",
        "esrs_standard": "ESRS S2",
        "pillar": "Social",
        "question": "Is there a supplier code of conduct covering labour rights and working conditions?",
        "question_it": "Esiste un codice di condotta fornitori che copra diritti del lavoro e condizioni lavorative?",
        "answer_type": "yes_no",
        "weight": 2,
        "requirement": "ESRS S2-1 requires policies for value chain workers' rights.",
    },
    # ── ESRS S3 — Affected Communities ───────────────────────────────────
    {
        "id": "S3_01",
        "esrs_standard": "ESRS S3",
        "pillar": "Social",
        "question": "Does the organization engage with local communities affected by its operations?",
        "question_it": "L'organizzazione coinvolge le comunita locali interessate dalle proprie attivita?",
        "answer_type": "scale_1_5",
        "weight": 1,
        "requirement": "ESRS S3-1 requires policies related to affected communities.",
    },
    # ── ESRS S4 — Consumers and End-Users ────────────────────────────────
    {
        "id": "S4_01",
        "esrs_standard": "ESRS S4",
        "pillar": "Social",
        "question": "Are there processes to ensure product safety and responsible marketing?",
        "question_it": "Esistono processi per garantire la sicurezza dei prodotti e un marketing responsabile?",
        "answer_type": "yes_no",
        "weight": 1,
        "requirement": "ESRS S4-1 requires policies related to consumers and end-users.",
    },
    # ── ESRS G1 — Business Conduct ──────────────────────────────────────
    {
        "id": "G1_01",
        "esrs_standard": "ESRS G1",
        "pillar": "Governance",
        "question": "Does the organization have a formal anti-corruption and anti-bribery policy?",
        "question_it": "L'organizzazione ha una politica formale anti-corruzione e anti-concussione?",
        "answer_type": "yes_no",
        "weight": 2,
        "requirement": "ESRS G1-3 requires disclosure of prevention and detection of corruption and bribery.",
    },
    {
        "id": "G1_02",
        "esrs_standard": "ESRS G1",
        "pillar": "Governance",
        "question": "Is there a documented corporate sustainability due diligence process?",
        "question_it": "Esiste un processo documentato di due diligence di sostenibilita aziendale?",
        "answer_type": "yes_no",
        "weight": 2,
        "requirement": "ESRS G1-1 requires disclosure of business conduct policies.",
    },
    {
        "id": "G1_03",
        "esrs_standard": "ESRS G1",
        "pillar": "Governance",
        "question": "How mature is the organization's sustainability data collection and reporting system? (1=manual/ad-hoc, 5=automated/audited)",
        "question_it": "Quanto e maturo il sistema di raccolta dati e rendicontazione di sostenibilita? (1=manuale/ad-hoc, 5=automatizzato/verificato)",
        "answer_type": "scale_1_5",
        "weight": 3,
        "requirement": "ESRS 2 BP-2 requires disclosure of preparation basis including data quality.",
    },
    {
        "id": "G1_04",
        "esrs_standard": "ESRS G1",
        "pillar": "Governance",
        "question": "Does the organization disclose its tax transparency practices and approach?",
        "question_it": "L'organizzazione divulga le proprie pratiche e il proprio approccio alla trasparenza fiscale?",
        "answer_type": "yes_no",
        "weight": 1,
        "requirement": "ESRS G1-4 requires disclosure on confirmed incidents of corruption or bribery.",
    },
    {
        "id": "G1_05",
        "esrs_standard": "ESRS G1",
        "pillar": "Governance",
        "question": "Are sustainability KPIs linked to executive or management remuneration?",
        "question_it": "I KPI di sostenibilita sono collegati alla remunerazione dei dirigenti?",
        "answer_type": "yes_no",
        "weight": 2,
        "requirement": "ESRS 2 GOV-3 requires disclosure on incentive schemes linked to sustainability.",
    },
]

# Maximum possible scores per answer type (used for normalisation)
_MAX_SCORE = {
    "yes_no": 1.0,
    "scale_1_5": 1.0,
    "numeric": 1.0,
    "text": 1.0,
}


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def load_questionnaire() -> list[dict[str, Any]]:
    """Return the full ESRS questionnaire."""
    return QUESTIONNAIRE


def _normalise_answer(question: dict, answer: Any) -> float:
    """Convert a raw answer to a 0-1 score."""
    atype = question["answer_type"]
    if answer is None:
        return 0.0
    if atype == "yes_no":
        if isinstance(answer, str):
            return 1.0 if answer.strip().lower() in ("yes", "y", "si", "true", "1") else 0.0
        return 1.0 if answer else 0.0
    if atype == "scale_1_5":
        try:
            v = float(answer)
            return max(0.0, min((v - 1) / 4.0, 1.0))
        except (ValueError, TypeError):
            return 0.0
    if atype == "numeric":
        # Numeric questions score 1.0 if a value is provided (data availability)
        try:
            v = float(answer)
            return 1.0 if v > 0 else 0.0
        except (ValueError, TypeError):
            return 0.0
    if atype == "text":
        return 1.0 if answer and str(answer).strip() else 0.0
    return 0.0


def score_responses(
    responses: dict[str, Any],
    questionnaire: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    """
    Score a set of responses against the questionnaire.

    Parameters
    ----------
    responses : dict
        Mapping of question id -> answer value.
    questionnaire : list[dict], optional
        Override questionnaire; defaults to the built-in QUESTIONNAIRE.

    Returns
    -------
    dict with keys:
        - overall_pct : float (0-100)
        - by_standard : dict[str, float]   (0-100 per ESRS standard)
        - by_pillar   : dict[str, float]   (0-100 per pillar)
        - details     : list[dict]          per-question breakdown
        - gaps        : list[dict]          questions scoring below 50%
    """
    q = questionnaire or QUESTIONNAIRE

    details: list[dict] = []
    standard_scores: dict[str, list[tuple[float, float]]] = {}
    pillar_scores: dict[str, list[tuple[float, float]]] = {}
    total_weighted = 0.0
    total_max = 0.0

    for item in q:
        qid = item["id"]
        answer = responses.get(qid)
        norm = _normalise_answer(item, answer)
        weight = item.get("weight", 1)
        weighted = norm * weight
        max_w = weight

        total_weighted += weighted
        total_max += max_w

        std = item["esrs_standard"]
        standard_scores.setdefault(std, []).append((weighted, max_w))
        pil = item["pillar"]
        pillar_scores.setdefault(pil, []).append((weighted, max_w))

        details.append({
            "id": qid,
            "esrs_standard": std,
            "pillar": pil,
            "question": item["question"],
            "answer": answer,
            "score_pct": round(norm * 100, 1),
            "weight": weight,
            "gap": norm < 0.5,
        })

    def _aggregate(bucket: dict[str, list[tuple[float, float]]]) -> dict[str, float]:
        out = {}
        for key, pairs in bucket.items():
            s = sum(p[0] for p in pairs)
            m = sum(p[1] for p in pairs)
            out[key] = round((s / m) * 100, 1) if m else 0.0
        return out

    overall_pct = round((total_weighted / total_max) * 100, 1) if total_max else 0.0

    gaps = [d for d in details if d["gap"]]
    # Sort gaps by weight descending (most important first)
    gaps.sort(key=lambda g: g["weight"], reverse=True)

    return {
        "overall_pct": overall_pct,
        "by_standard": _aggregate(standard_scores),
        "by_pillar": _aggregate(pillar_scores),
        "details": details,
        "gaps": gaps,
    }


def generate_report(
    scores: dict[str, Any],
    responses: dict[str, Any],
    questionnaire: list[dict[str, Any]] | None = None,
) -> str:
    """
    Generate a human-readable gap analysis report.

    Returns a formatted text report string.
    """
    q = questionnaire or QUESTIONNAIRE
    q_map = {item["id"]: item for item in q}

    lines: list[str] = []
    lines.append("=" * 70)
    lines.append("ESRS READINESS ASSESSMENT REPORT")
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("=" * 70)
    lines.append("")

    # Overall score
    overall = scores["overall_pct"]
    if overall >= 75:
        level = "ADVANCED"
        desc = "Strong foundation for ESRS compliance. Focus on refinement and assurance readiness."
    elif overall >= 50:
        level = "INTERMEDIATE"
        desc = "Moderate readiness. Key gaps remain that require structured action plans."
    elif overall >= 25:
        level = "EARLY STAGE"
        desc = "Significant gaps exist. Prioritize foundational elements: governance, data collection, materiality assessment."
    else:
        level = "INITIAL"
        desc = "ESRS compliance journey is just beginning. Immediate action needed on all fronts."

    lines.append(f"OVERALL READINESS: {overall:.1f}% ({level})")
    lines.append(desc)
    lines.append("")

    # Pillar scores
    lines.append("-" * 40)
    lines.append("SCORES BY ESRS PILLAR")
    lines.append("-" * 40)
    for pillar in ["General", "Environment", "Social", "Governance"]:
        pct = scores["by_pillar"].get(pillar, 0.0)
        bar_len = int(pct / 5)
        bar = "█" * bar_len + "░" * (20 - bar_len)
        lines.append(f"  {pillar:<14s} {bar} {pct:5.1f}%")
    lines.append("")

    # Standard-level scores
    lines.append("-" * 40)
    lines.append("SCORES BY ESRS STANDARD")
    lines.append("-" * 40)
    std_order = ["ESRS 2", "ESRS E1", "ESRS E2", "ESRS E3", "ESRS E4", "ESRS E5",
                 "ESRS S1", "ESRS S2", "ESRS S3", "ESRS S4", "ESRS G1"]
    for std in std_order:
        pct = scores["by_standard"].get(std, 0.0)
        bar_len = int(pct / 5)
        bar = "█" * bar_len + "░" * (20 - bar_len)
        lines.append(f"  {std:<10s} {bar} {pct:5.1f}%")
    lines.append("")

    # Prioritised gap list
    gaps = scores["gaps"]
    if gaps:
        lines.append("-" * 40)
        lines.append("PRIORITISED ACTION LIST (gaps)")
        lines.append("-" * 40)
        for i, gap in enumerate(gaps, 1):
            priority = "HIGH" if gap["weight"] >= 3 else ("MEDIUM" if gap["weight"] >= 2 else "LOW")
            lines.append(f"  {i:2d}. [{priority:6s}] [{gap['esrs_standard']}] {gap['question']}")
            req = q_map.get(gap["id"], {}).get("requirement", "")
            if req:
                lines.append(f"      Requirement: {req}")
            if gap["answer"] is not None:
                lines.append(f"      Current answer: {gap['answer']}")
            else:
                lines.append(f"      Status: NOT ANSWERED")
            lines.append("")
    else:
        lines.append("No critical gaps identified. Well done!")
        lines.append("")

    lines.append("=" * 70)
    lines.append("END OF REPORT")
    lines.append("=" * 70)

    return "\n".join(lines)


def generate_radar(
    scores: dict[str, Any],
    output_path: str | Path = "esrs_readiness_radar.png",
) -> str:
    """
    Generate a radar chart of readiness by ESRS pillar using chart_generator.py.

    Parameters
    ----------
    scores : dict
        Output from score_responses().
    output_path : str or Path
        Where to save the PNG.

    Returns
    -------
    str : path to the saved chart.
    """
    # Import chart_generator from the same directory
    script_dir = Path(__file__).resolve().parent
    if str(script_dir) not in sys.path:
        sys.path.insert(0, str(script_dir))
    from chart_generator import SustainabilityCharts

    charts = SustainabilityCharts(figsize=(8, 8), dpi=150)

    pillar_order = ["General", "Environment", "Social", "Governance"]
    values = [scores["by_pillar"].get(p, 0.0) for p in pillar_order]

    path = charts.radar_chart(
        categories=pillar_order,
        values=values,
        title="ESRS Readiness by Pillar",
        output_path=str(output_path),
        max_value=100,
        source="ESRS Self-Assessment",
    )
    return path


def generate_standard_radar(
    scores: dict[str, Any],
    output_path: str | Path = "esrs_standard_radar.png",
) -> str:
    """
    Generate a detailed radar chart with each ESRS standard as an axis.

    Parameters
    ----------
    scores : dict
        Output from score_responses().
    output_path : str or Path
        Where to save the PNG.

    Returns
    -------
    str : path to the saved chart.
    """
    script_dir = Path(__file__).resolve().parent
    if str(script_dir) not in sys.path:
        sys.path.insert(0, str(script_dir))
    from chart_generator import SustainabilityCharts

    charts = SustainabilityCharts(figsize=(10, 10), dpi=150)

    std_order = ["ESRS 2", "ESRS E1", "ESRS E2", "ESRS E3", "ESRS E4", "ESRS E5",
                 "ESRS S1", "ESRS S2", "ESRS S3", "ESRS S4", "ESRS G1"]
    # Use shorter labels for the chart
    labels = ["General\n(ESRS 2)", "Climate\n(E1)", "Pollution\n(E2)",
              "Water\n(E3)", "Biodiversity\n(E4)", "Circular\n(E5)",
              "Workforce\n(S1)", "Value Chain\n(S2)", "Communities\n(S3)",
              "Consumers\n(S4)", "Governance\n(G1)"]
    values = [scores["by_standard"].get(s, 0.0) for s in std_order]

    path = charts.radar_chart(
        categories=labels,
        values=values,
        title="ESRS Readiness by Standard",
        output_path=str(output_path),
        max_value=100,
        source="ESRS Self-Assessment",
    )
    return path


# ---------------------------------------------------------------------------
# Persistence helpers
# ---------------------------------------------------------------------------

def save_responses(responses: dict[str, Any], path: str | Path) -> None:
    """Save responses to a JSON file."""
    data = {
        "timestamp": datetime.now().isoformat(),
        "tool": "esrs_assessment",
        "version": "1.0",
        "responses": responses,
    }
    Path(path).write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


def load_responses(path: str | Path) -> dict[str, Any]:
    """Load responses from a JSON file."""
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if "responses" in data:
        return data["responses"]
    # If the file is just a flat dict of responses
    return data


# ---------------------------------------------------------------------------
# Interactive CLI
# ---------------------------------------------------------------------------

def _run_interactive() -> None:
    """Run the questionnaire interactively in the terminal."""
    print()
    print("=" * 60)
    print("  ESRS READINESS SELF-ASSESSMENT")
    print("  European Sustainability Reporting Standards")
    print("=" * 60)
    print()
    print("Answer each question. Press Enter to skip.")
    print("For yes/no questions, type 'y' or 'n'.")
    print("For scale questions, enter a number from 1 to 5.")
    print("For numeric questions, enter the value.")
    print()

    responses: dict[str, Any] = {}
    current_std = ""

    for item in QUESTIONNAIRE:
        if item["esrs_standard"] != current_std:
            current_std = item["esrs_standard"]
            print(f"\n--- {current_std} ---")

        prompt_type = {
            "yes_no": "[y/n]",
            "scale_1_5": "[1-5]",
            "numeric": "[number]",
            "text": "[text]",
        }.get(item["answer_type"], "")

        print(f"\n  {item['id']}: {item['question']}")
        print(f"         (IT: {item['question_it']})")
        raw = input(f"  {prompt_type} > ").strip()

        if raw == "":
            responses[item["id"]] = None
        elif item["answer_type"] == "yes_no":
            responses[item["id"]] = raw.lower() in ("y", "yes", "si", "true", "1")
        elif item["answer_type"] in ("scale_1_5", "numeric"):
            try:
                responses[item["id"]] = float(raw)
            except ValueError:
                print("  (Invalid number, recording as skipped)")
                responses[item["id"]] = None
        else:
            responses[item["id"]] = raw

    # Score and report
    scores = score_responses(responses)
    report = generate_report(scores, responses)
    print("\n")
    print(report)

    # Save
    save_path = input("\nSave responses to file? (enter path or press Enter to skip): ").strip()
    if save_path:
        save_responses(responses, save_path)
        print(f"Responses saved to {save_path}")

    # Radar chart
    radar_path = input("Generate radar chart? (enter path or press Enter to skip): ").strip()
    if radar_path:
        try:
            generate_radar(scores, radar_path)
            print(f"Radar chart saved to {radar_path}")
        except ImportError:
            print("Could not generate chart (matplotlib or chart_generator not available).")


def main():
    parser = argparse.ArgumentParser(
        description="ESRS Readiness Self-Assessment Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python esrs_assessment.py --interactive
  python esrs_assessment.py --load responses.json --report
  python esrs_assessment.py --load responses.json --radar readiness.png
  python esrs_assessment.py --load responses.json --radar-detailed standards.png
  python esrs_assessment.py --load responses.json --report --radar readiness.png
  python esrs_assessment.py --questionnaire   (dump questionnaire as JSON)
        """,
    )
    parser.add_argument("--interactive", action="store_true",
                        help="Run interactive questionnaire in the terminal")
    parser.add_argument("--load", type=str, metavar="FILE",
                        help="Load responses from a JSON file")
    parser.add_argument("--report", action="store_true",
                        help="Generate and print a gap analysis report")
    parser.add_argument("--radar", type=str, metavar="FILE",
                        help="Generate a pillar-level radar chart PNG")
    parser.add_argument("--radar-detailed", type=str, metavar="FILE",
                        help="Generate a standard-level radar chart PNG")
    parser.add_argument("--save", type=str, metavar="FILE",
                        help="Save scored results to JSON")
    parser.add_argument("--questionnaire", action="store_true",
                        help="Dump the full questionnaire as JSON to stdout")

    args = parser.parse_args()

    if args.questionnaire:
        print(json.dumps(QUESTIONNAIRE, indent=2, ensure_ascii=False))
        return

    if args.interactive:
        _run_interactive()
        return

    if not args.load:
        parser.print_help()
        print("\nError: Provide --interactive or --load FILE")
        sys.exit(1)

    responses = load_responses(args.load)
    scores = score_responses(responses)

    if args.report:
        print(generate_report(scores, responses))

    if args.radar:
        path = generate_radar(scores, args.radar)
        print(f"Pillar radar chart saved to: {path}")

    if args.radar_detailed:
        path = generate_standard_radar(scores, args.radar_detailed)
        print(f"Standard radar chart saved to: {path}")

    if args.save:
        out = {
            "timestamp": datetime.now().isoformat(),
            "overall_readiness_pct": scores["overall_pct"],
            "by_pillar": scores["by_pillar"],
            "by_standard": scores["by_standard"],
            "gaps_count": len(scores["gaps"]),
            "gaps": scores["gaps"],
        }
        Path(args.save).write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"Results saved to: {args.save}")

    if not any([args.report, args.radar, args.radar_detailed, args.save]):
        # Default: print a summary
        print(f"Overall ESRS Readiness: {scores['overall_pct']:.1f}%")
        print(f"Gaps identified: {len(scores['gaps'])}")
        print("Use --report for full analysis or --radar FILE for a chart.")


if __name__ == "__main__":
    main()
