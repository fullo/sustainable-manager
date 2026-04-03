#!/usr/bin/env python3
"""
Supplier ESG Scorer

Scores supplier ESG questionnaire responses, classifies suppliers into tiers,
identifies gaps and strengths, and generates reports and heatmap data.

Usage:
    # Score a single supplier
    python supplier_scorer.py --responses supplier1.json --modules environmental,social

    # Score multiple suppliers from a directory
    python supplier_scorer.py --responses-dir ./suppliers/ --modules all

    # Generate markdown report
    python supplier_scorer.py --responses supplier1.json --modules all --report

Example response JSON format:
{
    "supplier_name": "Acme S.r.l.",
    "supplier_id": "SUP-001",
    "date": "2026-03-15",
    "responses": {
        "A1": {"value": 1250, "evidence": true},
        "A2": {"value": 8500, "evidence": true},
        "A3": {"value": 35, "evidence": false},
        "B1": {"value": true, "evidence": true},
        "B2": {"value": true, "evidence": true, "details": "Annual HRDD process"},
        "C1": {"value": true, "evidence": true},
        "S1": {"value": "yes"}
    }
}
"""

import json
import os
import sys
import argparse
from pathlib import Path
from typing import Optional


# --- Module and question definitions ---

MODULES = {
    "environmental": {
        "label": "Environmental",
        "questions": {
            "A1":  {"text": "GHG Scope 1+2 emissions (tCO2e)", "type": "numeric", "weight": 5, "score_if_provided": True},
            "A2":  {"text": "Total energy consumption (MWh)", "type": "numeric", "weight": 4, "score_if_provided": True},
            "A3":  {"text": "Renewable energy share (%)", "type": "scale_0_100", "weight": 3, "thresholds": [20, 40, 60, 80]},
            "A4":  {"text": "Environmental management system", "type": "yes_no_certification", "weight": 3},
            "A5":  {"text": "GHG reduction targets set", "type": "yes_no_details", "weight": 4},
            "A6":  {"text": "SBTi-validated targets", "type": "yes_no", "weight": 4},
            "A7":  {"text": "Climate transition plan", "type": "yes_no_details", "weight": 3},
            "A8":  {"text": "Product-level carbon footprint", "type": "yes_no", "weight": 3},
            "A9":  {"text": "GHG intensity of supplied products", "type": "numeric", "weight": 5, "score_if_provided": True},
            "A10": {"text": "Water consumption (m3)", "type": "numeric", "weight": 2, "score_if_provided": True},
            "A11": {"text": "Operations in water-stressed areas", "type": "yes_no_details", "weight": 3},
            "A12": {"text": "Water recycled/reused (%)", "type": "scale_0_100", "weight": 2, "thresholds": [10, 25, 50, 75]},
            "A13": {"text": "Total waste generated (tonnes)", "type": "numeric", "weight": 2, "score_if_provided": True},
            "A14": {"text": "Waste recycling rate (%)", "type": "scale_0_100", "weight": 3, "thresholds": [20, 40, 60, 80]},
            "A15": {"text": "Hazardous waste (tonnes)", "type": "numeric", "weight": 3, "score_if_provided": True},
            "A16": {"text": "Substances of concern", "type": "yes_no_list", "weight": 3},
        },
    },
    "social": {
        "label": "Social",
        "questions": {
            "B1":  {"text": "Human rights policy", "type": "yes_no", "weight": 5},
            "B2":  {"text": "Human rights due diligence", "type": "yes_no_details", "weight": 5},
            "B3":  {"text": "Child labor risk assessment", "type": "yes_no", "weight": 5},
            "B4":  {"text": "Forced labor risk assessment", "type": "yes_no", "weight": 5},
            "B5":  {"text": "Freedom of association", "type": "yes_no", "weight": 4},
            "B6":  {"text": "Living wage", "type": "yes_no_details", "weight": 4},
            "B7":  {"text": "Lost Time Injury Rate (LTIR)", "type": "numeric", "weight": 3, "score_if_provided": True, "lower_is_better": True},
            "B8":  {"text": "H&S management system", "type": "yes_no_certification", "weight": 4},
            "B9":  {"text": "Training hours per employee", "type": "numeric", "weight": 2, "score_if_provided": True, "thresholds": [8, 16, 24, 40]},
            "B10": {"text": "Grievance mechanism", "type": "yes_no", "weight": 4},
            "B11": {"text": "Work-related fatalities (last 3 years)", "type": "yes_no_details", "weight": 5, "negative": True},
            "B12": {"text": "Social requirements extended to Tier 2+", "type": "yes_no_details", "weight": 3},
        },
    },
    "governance": {
        "label": "Governance",
        "questions": {
            "C1": {"text": "Code of conduct", "type": "yes_no", "weight": 3},
            "C2": {"text": "Anti-corruption policy", "type": "yes_no", "weight": 4},
            "C3": {"text": "Whistleblowing channel", "type": "yes_no", "weight": 3},
            "C4": {"text": "GDPR compliance / DPO", "type": "yes_no", "weight": 3},
            "C5": {"text": "Sanctions/fines (last 3 years)", "type": "yes_no_details", "weight": 4, "negative": True},
            "C6": {"text": "MOG 231 adopted", "type": "yes_no", "weight": 3},
            "C7": {"text": "Sustainability report published", "type": "yes_no_details", "weight": 2},
            "C8": {"text": "Conflict minerals policy", "type": "yes_no", "weight": 3},
        },
    },
    "cbam": {
        "label": "CBAM",
        "questions": {
            "D1": {"text": "Production method described", "type": "text", "weight": 5, "score_if_provided": True},
            "D2": {"text": "Direct emissions per tonne (tCO2e/t)", "type": "numeric", "weight": 5, "score_if_provided": True},
            "D3": {"text": "Indirect emissions per tonne (tCO2e/t)", "type": "numeric", "weight": 4, "score_if_provided": True},
            "D4": {"text": "Energy sources listed", "type": "text_list", "weight": 4, "score_if_provided": True},
            "D5": {"text": "Carbon price paid locally", "type": "yes_no_amount", "weight": 3},
            "D6": {"text": "Installation-level data available", "type": "yes_no", "weight": 5},
            "D7": {"text": "Covered by ETS", "type": "yes_no_details", "weight": 3},
            "D8": {"text": "Precursor embedded emissions", "type": "text", "weight": 4, "score_if_provided": True},
        },
    },
    "taxonomy": {
        "label": "EU Taxonomy",
        "questions": {
            "E1": {"text": "NACE codes provided", "type": "text", "weight": 3, "score_if_provided": True},
            "E2": {"text": "Taxonomy-eligible activities", "type": "yes_no_details", "weight": 3},
            "E3": {"text": "Technical Screening Criteria met", "type": "yes_no_details", "weight": 4},
            "E4": {"text": "DNSH compliance", "type": "yes_no", "weight": 3},
            "E5": {"text": "Minimum Safeguards compliance", "type": "yes_no", "weight": 3},
            "E6": {"text": "Taxonomy-aligned revenue/CapEx/OpEx %", "type": "numeric", "weight": 3, "score_if_provided": True},
        },
    },
}

# Tier classification thresholds
TIERS = {
    "leader":    {"min": 80, "label": "Leader", "description": "Strong ESG performance, role model"},
    "compliant": {"min": 60, "label": "Compliant", "description": "Meets basic expectations, some gaps"},
    "at-risk":   {"min": 40, "label": "At-Risk", "description": "Significant gaps, improvement needed"},
    "critical":  {"min": 0,  "label": "Critical", "description": "Major deficiencies, urgent action required"},
}


class SupplierScorer:
    """Scores supplier ESG questionnaire responses and generates reports."""

    def load_responses(self, file_path: str) -> dict:
        """Load supplier responses from a JSON file.

        Args:
            file_path: Path to the JSON file containing supplier responses.

        Returns:
            Dictionary with supplier metadata and responses.

        Raises:
            FileNotFoundError: If the file does not exist.
            json.JSONDecodeError: If the file is not valid JSON.
        """
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"Response file not found: {file_path}")
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if "responses" not in data:
            raise ValueError("JSON must contain a 'responses' key with question_id -> answer mappings")
        return data

    def _score_question(self, question_id: str, question_def: dict, answer: dict) -> float:
        """Score a single question response. Returns 0.0 to 1.0."""
        if answer is None:
            return 0.0

        q_type = question_def["type"]
        is_negative = question_def.get("negative", False)
        value = answer.get("value") if isinstance(answer, dict) else answer
        has_evidence = answer.get("evidence", False) if isinstance(answer, dict) else False

        # Handle not-answered
        if value is None or value == "" or value == "N/A":
            return 0.0

        score = 0.0

        if q_type == "yes_no":
            if is_negative:
                score = 0.0 if value is True or value == "yes" else 1.0
            else:
                score = 1.0 if value is True or value == "yes" else 0.0

        elif q_type == "yes_no_details":
            if is_negative:
                score = 0.0 if value is True or value == "yes" else 1.0
            else:
                has_details = bool(answer.get("details", "")) if isinstance(answer, dict) else False
                if value is True or value == "yes":
                    score = 1.0 if has_details else 0.7
                else:
                    score = 0.0

        elif q_type == "yes_no_certification":
            if isinstance(value, str) and value.lower() == "certified":
                score = 1.0
            elif value is True or value == "yes":
                score = 0.7
            else:
                score = 0.0

        elif q_type == "yes_no_amount":
            if value is True or value == "yes":
                score = 1.0
            else:
                score = 0.0

        elif q_type == "yes_no_list":
            # For substances of concern: having them is negative
            if value is True or value == "yes":
                score = 0.3  # Has substances but disclosed them
            elif value is False or value == "no":
                score = 1.0  # No substances of concern
            else:
                score = 0.5  # Partial disclosure

        elif q_type == "scale_0_100":
            thresholds = question_def.get("thresholds", [25, 50, 75, 90])
            if isinstance(value, (int, float)):
                if value >= thresholds[3]:
                    score = 1.0
                elif value >= thresholds[2]:
                    score = 0.75
                elif value >= thresholds[1]:
                    score = 0.5
                elif value >= thresholds[0]:
                    score = 0.25
                else:
                    score = 0.1  # At least provided data

        elif q_type == "numeric":
            if question_def.get("score_if_provided", False):
                # For numeric data: providing the data is the main value
                score = 0.7 if value is not None and value != "" else 0.0
                if has_evidence:
                    score = 1.0
            elif "thresholds" in question_def:
                thresholds = question_def["thresholds"]
                lower_is_better = question_def.get("lower_is_better", False)
                if isinstance(value, (int, float)):
                    if lower_is_better:
                        if value <= thresholds[0]:
                            score = 1.0
                        elif value <= thresholds[1]:
                            score = 0.75
                        elif value <= thresholds[2]:
                            score = 0.5
                        elif value <= thresholds[3]:
                            score = 0.25
                        else:
                            score = 0.1
                    else:
                        if value >= thresholds[3]:
                            score = 1.0
                        elif value >= thresholds[2]:
                            score = 0.75
                        elif value >= thresholds[1]:
                            score = 0.5
                        elif value >= thresholds[0]:
                            score = 0.25
                        else:
                            score = 0.1

        elif q_type in ("text", "text_list"):
            if question_def.get("score_if_provided", False):
                if value and str(value).strip():
                    score = 0.7
                    if has_evidence:
                        score = 1.0
                else:
                    score = 0.0

        elif q_type == "yes_no_progress":
            # Simplified questionnaire
            if value == "yes":
                score = 1.0
            elif value == "in_progress":
                score = 0.5
            elif value == "no":
                score = 0.0
            else:
                score = 0.0  # N/A

        # Evidence bonus for non-numeric types
        if has_evidence and q_type not in ("numeric", "text", "text_list") and score > 0:
            score = min(1.0, score * 1.1)

        return round(score, 2)

    def score_supplier(self, responses: dict, modules: Optional[list] = None) -> dict:
        """Score a single supplier's responses.

        Args:
            responses: Dictionary with supplier data including 'responses' key.
            modules: List of module names to score (default: all modules with responses).

        Returns:
            Dictionary with overall_score, by_module scores, tier, gaps, and strengths.
        """
        supplier_responses = responses.get("responses", {})
        supplier_name = responses.get("supplier_name", "Unknown")

        if modules is None or "all" in modules:
            modules = list(MODULES.keys())

        by_module = {}
        all_gaps = []
        all_strengths = []
        total_weighted_score = 0.0
        total_weight = 0.0

        for module_name in modules:
            if module_name not in MODULES:
                continue

            module = MODULES[module_name]
            module_score = 0.0
            module_weight = 0.0
            module_questions_answered = 0

            for q_id, q_def in module["questions"].items():
                answer = supplier_responses.get(q_id)
                weight = q_def["weight"]

                if answer is not None:
                    q_score = self._score_question(q_id, q_def, answer)
                    module_score += q_score * weight
                    module_weight += weight
                    module_questions_answered += 1

                    if q_score >= 0.8:
                        all_strengths.append({
                            "question_id": q_id,
                            "module": module_name,
                            "text": q_def["text"],
                            "score": q_score,
                        })
                    elif q_score <= 0.3:
                        priority = "high" if weight >= 4 else "medium" if weight >= 3 else "low"
                        all_gaps.append({
                            "question_id": q_id,
                            "module": module_name,
                            "text": q_def["text"],
                            "issue": f"Low score ({q_score}) on: {q_def['text']}",
                            "priority": priority,
                        })
                else:
                    # Not answered — counts as gap if weight is high
                    module_weight += weight
                    if weight >= 4:
                        all_gaps.append({
                            "question_id": q_id,
                            "module": module_name,
                            "text": q_def["text"],
                            "issue": f"No data provided for: {q_def['text']}",
                            "priority": "high",
                        })
                    elif weight >= 3:
                        all_gaps.append({
                            "question_id": q_id,
                            "module": module_name,
                            "text": q_def["text"],
                            "issue": f"No data provided for: {q_def['text']}",
                            "priority": "medium",
                        })

            if module_weight > 0:
                normalized = (module_score / module_weight) * 100
            else:
                normalized = 0.0

            by_module[module_name] = {
                "score": round(normalized, 1),
                "label": module["label"],
                "questions_answered": module_questions_answered,
                "questions_total": len(module["questions"]),
            }

            total_weighted_score += module_score
            total_weight += module_weight

        # Overall score
        overall = round((total_weighted_score / total_weight) * 100, 1) if total_weight > 0 else 0.0

        # Tier classification
        if overall >= 80:
            tier = "leader"
        elif overall >= 60:
            tier = "compliant"
        elif overall >= 40:
            tier = "at-risk"
        else:
            tier = "critical"

        # Sort gaps by priority
        priority_order = {"high": 0, "medium": 1, "low": 2}
        all_gaps.sort(key=lambda g: priority_order.get(g["priority"], 3))

        return {
            "supplier_name": supplier_name,
            "supplier_id": responses.get("supplier_id", ""),
            "overall_score": overall,
            "by_module": by_module,
            "tier": tier,
            "tier_label": TIERS[tier]["label"],
            "tier_description": TIERS[tier]["description"],
            "gaps": all_gaps,
            "strengths": all_strengths,
        }

    def score_multiple(self, suppliers_dir: str, modules: Optional[list] = None) -> list:
        """Score multiple suppliers from JSON files in a directory.

        Args:
            suppliers_dir: Path to directory containing supplier JSON files.
            modules: List of module names to score.

        Returns:
            List of score dictionaries, sorted by overall_score descending.
        """
        results = []
        dir_path = Path(suppliers_dir)

        if not dir_path.is_dir():
            raise NotADirectoryError(f"Not a directory: {suppliers_dir}")

        for json_file in sorted(dir_path.glob("*.json")):
            try:
                data = self.load_responses(str(json_file))
                score = self.score_supplier(data, modules)
                score["file"] = str(json_file)
                results.append(score)
            except (json.JSONDecodeError, ValueError, KeyError) as e:
                print(f"Warning: Could not score {json_file.name}: {e}", file=sys.stderr)

        results.sort(key=lambda r: r["overall_score"], reverse=True)
        return results

    def generate_report(self, scores: dict, supplier_name: Optional[str] = None) -> str:
        """Generate a markdown report for a single supplier.

        Args:
            scores: Score dictionary from score_supplier().
            supplier_name: Override supplier name (optional).

        Returns:
            Markdown-formatted report string.
        """
        name = supplier_name or scores.get("supplier_name", "Unknown Supplier")

        lines = [
            f"# ESG Supplier Scorecard: {name}",
            "",
            f"**Overall Score**: {scores['overall_score']}/100",
            f"**Tier**: {scores['tier_label']} — {scores['tier_description']}",
            "",
            "## Module Scores",
            "",
            "| Module | Score | Answered | Total |",
            "|--------|-------|----------|-------|",
        ]

        for mod_name, mod_data in scores["by_module"].items():
            lines.append(
                f"| {mod_data['label']} | {mod_data['score']}/100 | "
                f"{mod_data['questions_answered']} | {mod_data['questions_total']} |"
            )

        if scores["gaps"]:
            lines.extend(["", "## Priority Gaps", ""])
            for gap in scores["gaps"]:
                icon = "!!!" if gap["priority"] == "high" else "!!" if gap["priority"] == "medium" else "!"
                lines.append(f"- [{icon}] **{gap['question_id']}** ({gap['module']}): {gap['issue']}")

        if scores["strengths"]:
            lines.extend(["", "## Strengths", ""])
            for s in scores["strengths"]:
                lines.append(f"- **{s['question_id']}** ({s['module']}): {s['text']} (score: {s['score']})")

        lines.extend(["", "## Recommended Actions", ""])
        if scores["tier"] == "critical":
            lines.append("- **Urgent**: Engage supplier immediately to address critical gaps")
            lines.append("- Require corrective action plan within 30 days")
            lines.append("- Consider alternative suppliers if no improvement within 6 months")
        elif scores["tier"] == "at-risk":
            lines.append("- Develop joint improvement plan with 12-month timeline")
            lines.append("- Provide training and support on priority gap areas")
            lines.append("- Schedule quarterly progress reviews")
        elif scores["tier"] == "compliant":
            lines.append("- Encourage improvement on identified gaps")
            lines.append("- Share best practices from leader-tier suppliers")
            lines.append("- Annual reassessment")
        else:
            lines.append("- Recognize as ESG leader in supplier portfolio")
            lines.append("- Consider for strategic partnership and joint sustainability initiatives")
            lines.append("- Use as benchmark/mentor for other suppliers")

        return "\n".join(lines)

    def generate_heatmap_data(self, all_scores: list) -> dict:
        """Generate data structure for heatmap visualization.

        Args:
            all_scores: List of score dictionaries from score_multiple().

        Returns:
            Dictionary with suppliers, modules, and score matrix for chart_generator.py.
        """
        suppliers = []
        modules = []
        matrix = []

        # Collect all module names from results
        module_set = set()
        for s in all_scores:
            for mod_name in s.get("by_module", {}):
                module_set.add(mod_name)
        modules = sorted(module_set)

        for s in all_scores:
            supplier_name = s.get("supplier_name", s.get("supplier_id", "Unknown"))
            suppliers.append(supplier_name)
            row = []
            for mod_name in modules:
                mod_data = s.get("by_module", {}).get(mod_name, {})
                row.append(mod_data.get("score", 0.0))
            matrix.append(row)

        module_labels = []
        for mod_name in modules:
            if mod_name in MODULES:
                module_labels.append(MODULES[mod_name]["label"])
            else:
                module_labels.append(mod_name.title())

        return {
            "type": "heatmap",
            "title": "Supplier ESG Performance Heatmap",
            "suppliers": suppliers,
            "modules": module_labels,
            "matrix": matrix,
            "tiers": [s.get("tier", "unknown") for s in all_scores],
            "overall_scores": [s.get("overall_score", 0.0) for s in all_scores],
        }


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Score supplier ESG questionnaire responses",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Score a single supplier (all modules)
  python supplier_scorer.py --responses supplier1.json --modules all

  # Score specific modules only
  python supplier_scorer.py --responses supplier1.json --modules environmental,social

  # Score all suppliers in a directory and generate reports
  python supplier_scorer.py --responses-dir ./suppliers/ --modules all --report

  # Output heatmap data as JSON
  python supplier_scorer.py --responses-dir ./suppliers/ --modules all --heatmap
        """,
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--responses", type=str, help="Path to single supplier response JSON file")
    group.add_argument("--responses-dir", type=str, help="Path to directory of supplier JSON files")

    parser.add_argument(
        "--modules",
        type=str,
        default="all",
        help="Comma-separated list of modules to score: environmental,social,governance,cbam,taxonomy,all (default: all)",
    )
    parser.add_argument("--report", action="store_true", help="Generate markdown report(s)")
    parser.add_argument("--heatmap", action="store_true", help="Output heatmap data as JSON")
    parser.add_argument("--output", type=str, help="Output file path (default: stdout)")

    args = parser.parse_args()

    modules = args.modules.split(",") if args.modules != "all" else ["all"]
    scorer = SupplierScorer()
    output_lines = []

    if args.responses:
        data = scorer.load_responses(args.responses)
        scores = scorer.score_supplier(data, modules)

        if args.report:
            output_lines.append(scorer.generate_report(scores))
        else:
            output_lines.append(json.dumps(scores, indent=2, ensure_ascii=False))

    elif args.responses_dir:
        all_scores = scorer.score_multiple(args.responses_dir, modules)

        if args.heatmap:
            heatmap = scorer.generate_heatmap_data(all_scores)
            output_lines.append(json.dumps(heatmap, indent=2, ensure_ascii=False))
        elif args.report:
            for s in all_scores:
                output_lines.append(scorer.generate_report(s))
                output_lines.append("\n---\n")
        else:
            summary = []
            for s in all_scores:
                summary.append({
                    "supplier_name": s["supplier_name"],
                    "overall_score": s["overall_score"],
                    "tier": s["tier_label"],
                    "modules": {k: v["score"] for k, v in s["by_module"].items()},
                })
            output_lines.append(json.dumps(summary, indent=2, ensure_ascii=False))

    result = "\n".join(output_lines)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(result)
        print(f"Output written to {args.output}", file=sys.stderr)
    else:
        print(result)


if __name__ == "__main__":
    main()
