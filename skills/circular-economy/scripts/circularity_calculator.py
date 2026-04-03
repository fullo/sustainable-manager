#!/usr/bin/env python3
"""
Circularity Calculator
======================

Calculates Material Circularity Indicator (MCI) using the Ellen MacArthur Foundation
methodology, recycling/waste diversion rates, and PPWR compliance checks.

Usage examples:
    # As a module
    from circularity_calculator import CircularityCalculator
    calc = CircularityCalculator()
    result = calc.calculate_mci(
        virgin_mass=800, recycled_input_mass=200, total_mass=1000,
        waste_to_landfill=150, waste_to_recycling=600,
        product_lifetime_years=5, industry_avg_lifetime_years=4
    )

    # CLI
    python circularity_calculator.py \\
        --virgin 800 --recycled 200 --total 1000 \\
        --landfill 150 --recycling 600 \\
        --lifetime 5 --avg-lifetime 4
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field
from typing import Any


# ---------------------------------------------------------------------------
# PPWR target tables
# ---------------------------------------------------------------------------

PPWR_RECYCLING_TARGETS: dict[str, dict[int, float]] = {
    "paper": {2025: 75.0, 2030: 85.0},
    "cardboard": {2025: 75.0, 2030: 85.0},
    "glass": {2025: 70.0, 2030: 75.0},
    "ferrous_metals": {2025: 70.0, 2030: 80.0},
    "aluminium": {2025: 50.0, 2030: 60.0},
    "plastic": {2025: 50.0, 2030: 55.0},
    "wood": {2025: 25.0, 2030: 30.0},
}

PPWR_RECYCLED_CONTENT_TARGETS: dict[str, dict[int, float]] = {
    "pet_bottles": {2030: 30.0, 2040: 65.0},
    "other_contact_sensitive_plastic": {2030: 10.0, 2040: 50.0},
    "single_use_plastic_bottles_non_pet": {2030: 30.0, 2040: 65.0},
    "other_plastic_packaging": {2030: 35.0, 2040: 65.0},
}


# ---------------------------------------------------------------------------
# Data classes for results
# ---------------------------------------------------------------------------

@dataclass
class MCIResult:
    """Result of an MCI calculation."""
    mci: float
    lfi: float
    utility_factor: float
    interpretation: str
    rating: str
    breakdown: dict[str, float] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "mci": round(self.mci, 4),
            "lfi": round(self.lfi, 4),
            "utility_factor": round(self.utility_factor, 4),
            "interpretation": self.interpretation,
            "rating": self.rating,
            "breakdown": {k: round(v, 4) for k, v in self.breakdown.items()},
        }


@dataclass
class RecyclingResult:
    """Result of recycling / waste diversion calculation."""
    recycling_rate_pct: float
    waste_diversion_rate_pct: float
    total_waste: float
    hierarchy_breakdown: dict[str, float] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "recycling_rate_pct": round(self.recycling_rate_pct, 2),
            "waste_diversion_rate_pct": round(self.waste_diversion_rate_pct, 2),
            "total_waste": round(self.total_waste, 2),
            "hierarchy_breakdown": {
                k: round(v, 2) for k, v in self.hierarchy_breakdown.items()
            },
        }


@dataclass
class PPWRComplianceResult:
    """Result of a PPWR compliance check."""
    material: str
    target_year: int
    recycling_compliant: bool
    recycling_rate_pct: float
    recycling_target_pct: float | None
    recycling_gap_pct: float | None
    recycled_content_compliant: bool | None
    recycled_content_pct: float | None
    recycled_content_target_pct: float | None
    recycled_content_gap_pct: float | None
    recommendations: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        d: dict[str, Any] = {
            "material": self.material,
            "target_year": self.target_year,
            "recycling_compliant": self.recycling_compliant,
            "recycling_rate_pct": self.recycling_rate_pct,
            "recycling_target_pct": self.recycling_target_pct,
            "recycling_gap_pct": self.recycling_gap_pct,
        }
        if self.recycled_content_compliant is not None:
            d["recycled_content_compliant"] = self.recycled_content_compliant
            d["recycled_content_pct"] = self.recycled_content_pct
            d["recycled_content_target_pct"] = self.recycled_content_target_pct
            d["recycled_content_gap_pct"] = self.recycled_content_gap_pct
        d["recommendations"] = self.recommendations
        return d


# ---------------------------------------------------------------------------
# Main calculator class
# ---------------------------------------------------------------------------

class CircularityCalculator:
    """Calculate circularity metrics, recycling rates, and PPWR compliance."""

    # -- MCI ----------------------------------------------------------------

    @staticmethod
    def calculate_mci(
        virgin_mass: float,
        recycled_input_mass: float,
        total_mass: float,
        waste_to_landfill: float,
        waste_to_recycling: float,
        product_lifetime_years: float = 1.0,
        industry_avg_lifetime_years: float = 1.0,
    ) -> MCIResult:
        """Calculate the Material Circularity Indicator (MCI).

        Args:
            virgin_mass: Mass of virgin (primary) material input (kg/tonnes).
            recycled_input_mass: Mass of recycled/secondary material input.
            total_mass: Total mass of the product.
            waste_to_landfill: Waste sent to landfill or incineration without
                energy recovery.
            waste_to_recycling: Waste collected for recycling or reuse.
            product_lifetime_years: Actual product lifetime in years.
            industry_avg_lifetime_years: Industry average lifetime in years.

        Returns:
            MCIResult with score, components, and interpretation.
        """
        if total_mass <= 0:
            raise ValueError("total_mass must be > 0")
        if industry_avg_lifetime_years <= 0:
            raise ValueError("industry_avg_lifetime_years must be > 0")

        # Unrecoverable waste
        w = waste_to_landfill
        v = virgin_mass

        # Linear Flow Index
        denominator = 2 * total_mass + waste_to_landfill - waste_to_recycling
        if denominator <= 0:
            denominator = 1e-9  # avoid division by zero
        lfi = (v + w) / denominator
        lfi = max(0.0, min(1.0, lfi))

        # Utility factor
        x = product_lifetime_years / industry_avg_lifetime_years
        if x >= 1:
            f_x = 0.9 / x
        else:
            f_x = min(0.9, 0.9 * x) if x > 0 else 0.9

        # MCI
        mci = 1.0 - lfi * f_x
        mci = max(0.0, min(1.0, mci))

        # Interpretation
        if mci >= 0.8:
            rating, interpretation = "excellent", "Excellent circularity — industry-leading performance"
        elif mci >= 0.6:
            rating, interpretation = "good", "Good circularity — above-average circular material flows"
        elif mci >= 0.3:
            rating, interpretation = "moderate", "Moderate circularity — improvement opportunities exist"
        else:
            rating, interpretation = "low", "Low circularity — priority intervention needed"

        breakdown = {
            "virgin_mass": virgin_mass,
            "recycled_input_mass": recycled_input_mass,
            "total_mass": total_mass,
            "waste_to_landfill": waste_to_landfill,
            "waste_to_recycling": waste_to_recycling,
            "product_lifetime_years": product_lifetime_years,
            "industry_avg_lifetime_years": industry_avg_lifetime_years,
            "recycled_content_pct": (recycled_input_mass / total_mass * 100)
            if total_mass > 0
            else 0.0,
        }

        return MCIResult(
            mci=mci, lfi=lfi, utility_factor=f_x,
            interpretation=interpretation, rating=rating,
            breakdown=breakdown,
        )

    # -- Recycling / waste diversion ----------------------------------------

    @staticmethod
    def calculate_recycling_rate(waste_by_treatment: dict[str, float]) -> RecyclingResult:
        """Calculate recycling and waste diversion rates.

        Args:
            waste_by_treatment: Dict with keys from
                {recycling, reuse, composting, energy_recovery, landfill}
                and values in tonnes/kg.

        Returns:
            RecyclingResult with rates and hierarchy breakdown.
        """
        recycling = waste_by_treatment.get("recycling", 0.0)
        reuse = waste_by_treatment.get("reuse", 0.0)
        composting = waste_by_treatment.get("composting", 0.0)
        energy_recovery = waste_by_treatment.get("energy_recovery", 0.0)
        landfill = waste_by_treatment.get("landfill", 0.0)

        total = recycling + reuse + composting + energy_recovery + landfill
        if total <= 0:
            raise ValueError("Total waste must be > 0")

        recycling_rate = recycling / total * 100
        diversion_rate = (recycling + reuse + composting) / total * 100

        hierarchy = {
            "reuse_pct": reuse / total * 100,
            "recycling_pct": recycling / total * 100,
            "composting_pct": composting / total * 100,
            "energy_recovery_pct": energy_recovery / total * 100,
            "landfill_pct": landfill / total * 100,
        }

        return RecyclingResult(
            recycling_rate_pct=recycling_rate,
            waste_diversion_rate_pct=diversion_rate,
            total_waste=total,
            hierarchy_breakdown=hierarchy,
        )

    # -- PPWR compliance ----------------------------------------------------

    @staticmethod
    def ppwr_compliance_check(packaging_data: dict[str, Any]) -> PPWRComplianceResult:
        """Check compliance against PPWR targets.

        Args:
            packaging_data: Dict with keys:
                - material (str): e.g. "plastic", "glass", "paper"
                - recycling_rate_pct (float): current recycling rate
                - recycled_content_pct (float, optional): current recycled content
                - packaging_subtype (str, optional): e.g. "pet_bottles"
                - target_year (int): 2025, 2030, or 2040

        Returns:
            PPWRComplianceResult with compliance status and recommendations.
        """
        material = packaging_data["material"].lower().replace("/", "_").replace(" ", "_")
        recycling_rate = packaging_data["recycling_rate_pct"]
        recycled_content = packaging_data.get("recycled_content_pct")
        subtype = packaging_data.get("packaging_subtype", "")
        target_year = packaging_data.get("target_year", 2030)

        recommendations: list[str] = []

        # --- Recycling target ---
        targets = PPWR_RECYCLING_TARGETS.get(material, {})
        recycling_target = targets.get(target_year)
        recycling_gap = None
        recycling_compliant = True

        if recycling_target is not None:
            recycling_gap = recycling_rate - recycling_target
            recycling_compliant = recycling_gap >= 0
            if not recycling_compliant:
                recommendations.append(
                    f"Increase recycling rate by {abs(recycling_gap):.1f}pp "
                    f"to meet {target_year} target of {recycling_target}%"
                )
        else:
            recommendations.append(
                f"No specific PPWR recycling target found for '{material}' "
                f"at year {target_year}. Verify material classification."
            )

        # --- Recycled content target ---
        content_target = None
        content_gap = None
        content_compliant: bool | None = None

        if recycled_content is not None and subtype:
            content_targets = PPWR_RECYCLED_CONTENT_TARGETS.get(subtype, {})
            content_target = content_targets.get(target_year)
            if content_target is not None:
                content_gap = recycled_content - content_target
                content_compliant = content_gap >= 0
                if not content_compliant:
                    recommendations.append(
                        f"Increase recycled content by {abs(content_gap):.1f}pp "
                        f"to meet {target_year} target of {content_target}%"
                    )
        elif recycled_content is not None and material == "plastic":
            recommendations.append(
                "Specify packaging_subtype (e.g. 'pet_bottles', "
                "'other_plastic_packaging') for recycled content target check."
            )

        # General recommendations
        if not recycling_compliant:
            recommendations.append("Review waste collection and sorting infrastructure")
            recommendations.append("Consider design-for-recycling improvements")
        if content_compliant is False:
            recommendations.append("Engage with recycled material suppliers")
            recommendations.append("Evaluate mass-balance certification options")

        return PPWRComplianceResult(
            material=material,
            target_year=target_year,
            recycling_compliant=recycling_compliant,
            recycling_rate_pct=recycling_rate,
            recycling_target_pct=recycling_target,
            recycling_gap_pct=round(recycling_gap, 2) if recycling_gap is not None else None,
            recycled_content_compliant=content_compliant,
            recycled_content_pct=recycled_content,
            recycled_content_target_pct=content_target,
            recycled_content_gap_pct=round(content_gap, 2) if content_gap is not None else None,
            recommendations=recommendations,
        )

    # -- Summary ------------------------------------------------------------

    @staticmethod
    def generate_summary(
        mci_results: MCIResult | None = None,
        recycling_results: RecyclingResult | None = None,
        ppwr_results: PPWRComplianceResult | None = None,
    ) -> str:
        """Generate a markdown summary of all available results.

        Args:
            mci_results: Output from calculate_mci().
            recycling_results: Output from calculate_recycling_rate().
            ppwr_results: Output from ppwr_compliance_check().

        Returns:
            Markdown-formatted summary string.
        """
        sections: list[str] = ["# Circularity Assessment Summary\n"]

        if mci_results is not None:
            sections.append("## Material Circularity Indicator (MCI)\n")
            sections.append(f"| Metric | Value |")
            sections.append(f"|--------|-------|")
            sections.append(f"| **MCI Score** | **{mci_results.mci:.3f}** |")
            sections.append(f"| Rating | {mci_results.rating.capitalize()} |")
            sections.append(f"| Linear Flow Index | {mci_results.lfi:.3f} |")
            sections.append(f"| Utility Factor | {mci_results.utility_factor:.3f} |")
            bd = mci_results.breakdown
            sections.append(f"| Recycled Content | {bd.get('recycled_content_pct', 0):.1f}% |")
            sections.append(f"\n*{mci_results.interpretation}*\n")

        if recycling_results is not None:
            sections.append("## Waste Management Performance\n")
            sections.append(f"| Metric | Value |")
            sections.append(f"|--------|-------|")
            sections.append(f"| Recycling Rate | {recycling_results.recycling_rate_pct:.1f}% |")
            sections.append(
                f"| Waste Diversion Rate | {recycling_results.waste_diversion_rate_pct:.1f}% |"
            )
            sections.append(f"| Total Waste | {recycling_results.total_waste:.1f} tonnes |")
            sections.append(f"\n### Waste Hierarchy Breakdown\n")
            for key, val in recycling_results.hierarchy_breakdown.items():
                label = key.replace("_pct", "").replace("_", " ").capitalize()
                sections.append(f"- {label}: {val:.1f}%")
            sections.append("")

        if ppwr_results is not None:
            status = "COMPLIANT" if ppwr_results.recycling_compliant else "NON-COMPLIANT"
            sections.append("## PPWR Compliance Check\n")
            sections.append(f"| Metric | Value |")
            sections.append(f"|--------|-------|")
            sections.append(f"| Material | {ppwr_results.material} |")
            sections.append(f"| Target Year | {ppwr_results.target_year} |")
            sections.append(f"| Recycling Status | **{status}** |")
            if ppwr_results.recycling_gap_pct is not None:
                sections.append(
                    f"| Recycling Gap | {ppwr_results.recycling_gap_pct:+.1f}pp |"
                )
            if ppwr_results.recycled_content_compliant is not None:
                rc_status = (
                    "COMPLIANT"
                    if ppwr_results.recycled_content_compliant
                    else "NON-COMPLIANT"
                )
                sections.append(f"| Recycled Content Status | **{rc_status}** |")
            if ppwr_results.recommendations:
                sections.append(f"\n### Recommendations\n")
                for rec in ppwr_results.recommendations:
                    sections.append(f"- {rec}")
            sections.append("")

        return "\n".join(sections)


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Calculate Material Circularity Indicator (MCI) and related metrics."
    )
    parser.add_argument("--virgin", type=float, required=True, help="Virgin material mass")
    parser.add_argument("--recycled", type=float, required=True, help="Recycled input mass")
    parser.add_argument("--total", type=float, required=True, help="Total product mass")
    parser.add_argument("--landfill", type=float, required=True, help="Waste to landfill/incineration")
    parser.add_argument("--recycling", type=float, required=True, help="Waste to recycling/reuse")
    parser.add_argument("--lifetime", type=float, default=1.0, help="Product lifetime (years)")
    parser.add_argument("--avg-lifetime", type=float, default=1.0, help="Industry avg lifetime (years)")
    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()
    calc = CircularityCalculator()

    mci_result = calc.calculate_mci(
        virgin_mass=args.virgin,
        recycled_input_mass=args.recycled,
        total_mass=args.total,
        waste_to_landfill=args.landfill,
        waste_to_recycling=args.recycling,
        product_lifetime_years=args.lifetime,
        industry_avg_lifetime_years=args.avg_lifetime,
    )

    # Build a basic waste treatment dict from available data
    waste_data = {
        "recycling": args.recycling,
        "landfill": args.landfill,
        "reuse": 0.0,
        "composting": 0.0,
        "energy_recovery": 0.0,
    }
    recycling_result = calc.calculate_recycling_rate(waste_data)

    if args.json:
        output = {
            "mci": mci_result.to_dict(),
            "recycling": recycling_result.to_dict(),
        }
        print(json.dumps(output, indent=2))
    else:
        summary = calc.generate_summary(
            mci_results=mci_result,
            recycling_results=recycling_result,
        )
        print(summary)


if __name__ == "__main__":
    main()
