#!/usr/bin/env python3
"""
Scope 3 Emissions Calculator

Estimates Scope 3 GHG emissions using spend-based (EEIO) and activity-based methods.
Provides per-category breakdown, totals, and data quality ratings.

Usage:
    python scope3_calculator.py --spend spend.json --sector manufacturing
    python scope3_calculator.py --activity activity.json
    python scope3_calculator.py --sector food_beverage --profile-only

Examples:
    # Spend-based estimation from JSON file:
    echo '{"purchased_goods": {"raw_materials": 5000000, "packaging": 1200000}, "business_travel": {"flights": 300000}}' > spend.json
    python scope3_calculator.py --spend spend.json --sector manufacturing_general

    # Activity-based estimation:
    echo '{"electricity_kwh": 2000000, "natural_gas_m3": 500000, "freight_tkm": {"road": 1000000, "rail": 200000}}' > activity.json
    python scope3_calculator.py --activity activity.json

    # View sector profile only:
    python scope3_calculator.py --sector food_beverage --profile-only
"""

import json
import argparse
import sys
from typing import Dict, Optional, Any


# --- Simplified EEIO Emission Factors (tCO2e per EUR spent) ---
# Based on simplified DEFRA supply chain factors and EPA EEIO model.
# These are illustrative averages; real implementations should use
# the full EEIO tables or DEFRA supply chain factors.
SPEND_EMISSION_FACTORS: Dict[str, Dict[str, float]] = {
    "purchased_goods": {
        "raw_materials": 0.00060,         # tCO2e per EUR — metals, minerals, chemicals
        "raw_materials_metals": 0.00085,   # higher for metals specifically
        "raw_materials_chemicals": 0.00070,
        "raw_materials_plastics": 0.00075,
        "agricultural_products": 0.00055,  # crops, livestock inputs
        "food_ingredients": 0.00065,       # processed food inputs
        "packaging": 0.00045,             # paper, cardboard, plastic packaging
        "textiles_fabrics": 0.00050,
        "electronics_components": 0.00040,
        "office_supplies": 0.00025,
        "other_goods": 0.00040,
        "_default": 0.00050,
    },
    "capital_goods": {
        "machinery_equipment": 0.00035,
        "vehicles": 0.00030,
        "buildings_construction": 0.00045,
        "it_equipment": 0.00025,
        "furniture": 0.00020,
        "_default": 0.00035,
    },
    "upstream_transport": {
        "road_freight": 0.00065,
        "rail_freight": 0.00020,
        "sea_freight": 0.00025,
        "air_freight": 0.00130,
        "logistics_services": 0.00055,
        "_default": 0.00055,
    },
    "waste": {
        "waste_management": 0.00030,
        "hazardous_waste": 0.00050,
        "recycling_services": 0.00015,
        "_default": 0.00030,
    },
    "business_travel": {
        "flights": 0.00080,
        "rail": 0.00015,
        "hotels": 0.00025,
        "car_rental": 0.00040,
        "travel_agency": 0.00060,
        "_default": 0.00060,
    },
    "commuting": {
        "employee_transport_subsidy": 0.00035,
        "_default": 0.00035,
    },
    "purchased_services": {
        "professional_services": 0.00015,
        "it_services": 0.00012,
        "cleaning_maintenance": 0.00020,
        "marketing_advertising": 0.00018,
        "financial_services": 0.00008,
        "telecommunications": 0.00010,
        "_default": 0.00015,
    },
    "downstream_transport": {
        "outbound_logistics": 0.00055,
        "_default": 0.00055,
    },
}

# --- Activity-Based Emission Factors ---
ACTIVITY_EMISSION_FACTORS: Dict[str, float] = {
    # Energy (WTT + T&D for Cat 3)
    "electricity_kwh": 0.000023,            # tCO2e per kWh (WTT + T&D, EU avg)
    "natural_gas_m3": 0.00040,              # tCO2e per m3 (WTT)
    "diesel_litres": 0.00060,               # tCO2e per litre (WTT)
    "petrol_litres": 0.00053,               # tCO2e per litre (WTT)

    # Freight transport (tCO2e per tonne-km)
    "freight_road_tkm": 0.000107,           # road freight, average truck
    "freight_rail_tkm": 0.000028,           # rail freight, EU average
    "freight_sea_tkm": 0.000016,            # container ship, average
    "freight_air_tkm": 0.000602,            # air freight, average

    # Passenger transport (tCO2e per passenger-km)
    "flight_short_haul_pkm": 0.000156,      # <1500 km, economy
    "flight_medium_haul_pkm": 0.000131,     # 1500-4000 km, economy
    "flight_long_haul_pkm": 0.000114,       # >4000 km, economy
    "flight_business_class_multiplier": 2.0, # multiply economy factor
    "rail_pkm": 0.000035,                   # rail, EU average
    "car_pkm": 0.000170,                    # average car
    "hotel_night": 0.031,                   # tCO2e per hotel night (EU average)

    # Waste (tCO2e per tonne)
    "waste_landfill_mixed": 0.460,          # mixed waste to landfill
    "waste_incineration_mixed": 0.021,      # mixed waste incineration (net)
    "waste_recycling_mixed": -0.050,        # recycling credit (avoided emissions)
    "waste_composting_organic": 0.010,      # organic waste composting
    "waste_landfill_paper": 1.040,          # paper to landfill
    "waste_landfill_food": 0.580,           # food waste to landfill

    # Commuting (tCO2e per employee per year, average)
    "commuting_avg_per_employee": 0.60,     # EU average, mix of modes
}

# --- Scope 3 Category Mapping ---
CATEGORY_NAMES = {
    "1": "Purchased Goods and Services",
    "2": "Capital Goods",
    "3": "Fuel- and Energy-Related Activities",
    "4": "Upstream Transportation and Distribution",
    "5": "Waste Generated in Operations",
    "6": "Business Travel",
    "7": "Employee Commuting",
    "8": "Upstream Leased Assets",
    "9": "Downstream Transportation and Distribution",
    "10": "Processing of Sold Products",
    "11": "Use of Sold Products",
    "12": "End-of-Life Treatment of Sold Products",
    "13": "Downstream Leased Assets",
    "14": "Franchises",
    "15": "Investments",
}

# --- Sector Profiles (embedded summary) ---
SECTOR_PROFILES: Dict[str, Dict[str, Any]] = {
    "manufacturing_general": {
        "label": "Manufacturing (General)",
        "categories": {
            "1": {"typical_pct": 45, "materiality": "high"},
            "2": {"typical_pct": 8, "materiality": "medium"},
            "3": {"typical_pct": 5, "materiality": "medium"},
            "4": {"typical_pct": 6, "materiality": "medium"},
            "5": {"typical_pct": 3, "materiality": "medium"},
            "6": {"typical_pct": 2, "materiality": "low"},
            "7": {"typical_pct": 2, "materiality": "low"},
            "8": {"typical_pct": 1, "materiality": "low"},
            "9": {"typical_pct": 5, "materiality": "medium"},
            "10": {"typical_pct": 8, "materiality": "medium"},
            "11": {"typical_pct": 10, "materiality": "high"},
            "12": {"typical_pct": 3, "materiality": "low"},
            "13": {"typical_pct": 0, "materiality": "na"},
            "14": {"typical_pct": 0, "materiality": "na"},
            "15": {"typical_pct": 2, "materiality": "low"},
        },
    },
    "food_beverage": {
        "label": "Food & Beverage",
        "categories": {
            "1": {"typical_pct": 55, "materiality": "high"},
            "2": {"typical_pct": 5, "materiality": "low"},
            "3": {"typical_pct": 4, "materiality": "low"},
            "4": {"typical_pct": 8, "materiality": "medium"},
            "5": {"typical_pct": 3, "materiality": "medium"},
            "6": {"typical_pct": 1, "materiality": "low"},
            "7": {"typical_pct": 1, "materiality": "low"},
            "8": {"typical_pct": 1, "materiality": "low"},
            "9": {"typical_pct": 8, "materiality": "medium"},
            "10": {"typical_pct": 3, "materiality": "low"},
            "11": {"typical_pct": 3, "materiality": "low"},
            "12": {"typical_pct": 4, "materiality": "medium"},
            "13": {"typical_pct": 0, "materiality": "na"},
            "14": {"typical_pct": 3, "materiality": "low"},
            "15": {"typical_pct": 1, "materiality": "low"},
        },
    },
    "fashion_textiles": {
        "label": "Fashion & Textiles",
        "categories": {
            "1": {"typical_pct": 60, "materiality": "high"},
            "2": {"typical_pct": 3, "materiality": "low"},
            "3": {"typical_pct": 3, "materiality": "low"},
            "4": {"typical_pct": 6, "materiality": "medium"},
            "5": {"typical_pct": 3, "materiality": "medium"},
            "6": {"typical_pct": 1, "materiality": "low"},
            "7": {"typical_pct": 1, "materiality": "low"},
            "8": {"typical_pct": 1, "materiality": "low"},
            "9": {"typical_pct": 5, "materiality": "medium"},
            "10": {"typical_pct": 2, "materiality": "low"},
            "11": {"typical_pct": 10, "materiality": "medium"},
            "12": {"typical_pct": 4, "materiality": "medium"},
            "13": {"typical_pct": 0, "materiality": "na"},
            "14": {"typical_pct": 1, "materiality": "low"},
            "15": {"typical_pct": 0, "materiality": "na"},
        },
    },
    "financial_services": {
        "label": "Financial Services",
        "categories": {
            "1": {"typical_pct": 5, "materiality": "medium"},
            "2": {"typical_pct": 3, "materiality": "low"},
            "3": {"typical_pct": 1, "materiality": "low"},
            "4": {"typical_pct": 0, "materiality": "na"},
            "5": {"typical_pct": 0, "materiality": "na"},
            "6": {"typical_pct": 5, "materiality": "medium"},
            "7": {"typical_pct": 3, "materiality": "low"},
            "8": {"typical_pct": 3, "materiality": "medium"},
            "9": {"typical_pct": 0, "materiality": "na"},
            "10": {"typical_pct": 0, "materiality": "na"},
            "11": {"typical_pct": 0, "materiality": "na"},
            "12": {"typical_pct": 0, "materiality": "na"},
            "13": {"typical_pct": 5, "materiality": "medium"},
            "14": {"typical_pct": 0, "materiality": "na"},
            "15": {"typical_pct": 75, "materiality": "high"},
        },
    },
    "construction": {
        "label": "Construction",
        "categories": {
            "1": {"typical_pct": 40, "materiality": "high"},
            "2": {"typical_pct": 12, "materiality": "medium"},
            "3": {"typical_pct": 4, "materiality": "low"},
            "4": {"typical_pct": 8, "materiality": "medium"},
            "5": {"typical_pct": 5, "materiality": "medium"},
            "6": {"typical_pct": 2, "materiality": "low"},
            "7": {"typical_pct": 2, "materiality": "low"},
            "8": {"typical_pct": 2, "materiality": "low"},
            "9": {"typical_pct": 3, "materiality": "low"},
            "10": {"typical_pct": 2, "materiality": "low"},
            "11": {"typical_pct": 15, "materiality": "high"},
            "12": {"typical_pct": 3, "materiality": "low"},
            "13": {"typical_pct": 1, "materiality": "low"},
            "14": {"typical_pct": 0, "materiality": "na"},
            "15": {"typical_pct": 1, "materiality": "low"},
        },
    },
    "energy_utilities": {
        "label": "Energy & Utilities",
        "categories": {
            "1": {"typical_pct": 10, "materiality": "medium"},
            "2": {"typical_pct": 15, "materiality": "high"},
            "3": {"typical_pct": 20, "materiality": "high"},
            "4": {"typical_pct": 3, "materiality": "low"},
            "5": {"typical_pct": 2, "materiality": "low"},
            "6": {"typical_pct": 1, "materiality": "low"},
            "7": {"typical_pct": 1, "materiality": "low"},
            "8": {"typical_pct": 1, "materiality": "low"},
            "9": {"typical_pct": 2, "materiality": "low"},
            "10": {"typical_pct": 0, "materiality": "na"},
            "11": {"typical_pct": 40, "materiality": "high"},
            "12": {"typical_pct": 1, "materiality": "low"},
            "13": {"typical_pct": 0, "materiality": "na"},
            "14": {"typical_pct": 0, "materiality": "na"},
            "15": {"typical_pct": 4, "materiality": "low"},
        },
    },
}

# Mapping from spend categories to Scope 3 category numbers
SPEND_TO_CATEGORY: Dict[str, str] = {
    "purchased_goods": "1",
    "capital_goods": "2",
    "upstream_transport": "4",
    "waste": "5",
    "business_travel": "6",
    "commuting": "7",
    "purchased_services": "1",  # Services also fall under Cat 1
    "downstream_transport": "9",
}


class Scope3Calculator:
    """Calculates Scope 3 GHG emissions using spend-based and activity-based methods."""

    def __init__(self) -> None:
        self.spend_factors = SPEND_EMISSION_FACTORS
        self.activity_factors = ACTIVITY_EMISSION_FACTORS
        self.sector_profiles = SECTOR_PROFILES

    def estimate_spend_based(self, spend_data: Dict[str, Dict[str, float]]) -> Dict[str, Any]:
        """
        Estimate Scope 3 emissions using spend-based (EEIO) method.

        Args:
            spend_data: Nested dict of {spend_category: {subcategory: EUR_amount}}.
                        e.g., {"purchased_goods": {"raw_materials": 5000000, "packaging": 1200000}}

        Returns:
            Dict with per-category results, total, and metadata.
        """
        results: Dict[str, Dict[str, Any]] = {}
        total_emissions = 0.0
        total_spend = 0.0

        for category, subcategories in spend_data.items():
            if category not in self.spend_factors:
                continue

            factors = self.spend_factors[category]
            cat_emissions = 0.0
            cat_spend = 0.0
            subcategory_results = {}

            for subcategory, amount in subcategories.items():
                factor = factors.get(subcategory, factors.get("_default", 0.00040))
                emissions = amount * factor
                subcategory_results[subcategory] = {
                    "spend_eur": amount,
                    "factor_tco2e_per_eur": factor,
                    "emissions_tco2e": round(emissions, 2),
                }
                cat_emissions += emissions
                cat_spend += amount

            scope3_cat = SPEND_TO_CATEGORY.get(category, "1")
            cat_name = CATEGORY_NAMES.get(scope3_cat, category)

            if scope3_cat in results:
                # Merge if same Scope 3 category (e.g., purchased_services -> Cat 1)
                results[scope3_cat]["emissions_tco2e"] += round(cat_emissions, 2)
                results[scope3_cat]["spend_eur"] += cat_spend
                results[scope3_cat]["subcategories"].update(subcategory_results)
            else:
                results[scope3_cat] = {
                    "category_name": cat_name,
                    "emissions_tco2e": round(cat_emissions, 2),
                    "spend_eur": cat_spend,
                    "subcategories": subcategory_results,
                    "method": "spend-based (EEIO)",
                    "data_quality": 2,
                }

            total_emissions += cat_emissions
            total_spend += cat_spend

        # Calculate percentages
        for cat_id, cat_data in results.items():
            cat_data["pct_of_total"] = (
                round(cat_data["emissions_tco2e"] / total_emissions * 100, 1)
                if total_emissions > 0
                else 0.0
            )

        return {
            "method": "spend-based",
            "total_emissions_tco2e": round(total_emissions, 2),
            "total_spend_eur": total_spend,
            "avg_intensity_tco2e_per_meur": (
                round(total_emissions / (total_spend / 1_000_000), 2)
                if total_spend > 0
                else 0.0
            ),
            "data_quality_rating": 2,
            "data_quality_label": "Spend-based (lowest quality — use as screening baseline)",
            "categories": results,
        }

    def estimate_activity_based(self, activity_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Estimate Scope 3 emissions using activity-based method.

        Args:
            activity_data: Dict of physical activity data.
                Keys match ACTIVITY_EMISSION_FACTORS (e.g., "electricity_kwh", "freight_road_tkm").
                Special key "freight_tkm" can be a dict of {mode: tkm} for convenience.
                Special key "flights" can be a dict of {haul_type: pkm}.
                Special key "waste_tonnes" can be a dict of {type_treatment: tonnes}.

        Returns:
            Dict with per-activity results and total.
        """
        results: Dict[str, Dict[str, Any]] = {}
        total_emissions = 0.0

        # Handle nested freight data
        if "freight_tkm" in activity_data:
            freight = activity_data.pop("freight_tkm")
            for mode, tkm in freight.items():
                key = f"freight_{mode}_tkm"
                activity_data[key] = tkm

        # Handle nested flight data
        if "flights" in activity_data:
            flights = activity_data.pop("flights")
            for haul, pkm in flights.items():
                key = f"flight_{haul}_pkm"
                activity_data[key] = pkm

        for activity, quantity in activity_data.items():
            if activity not in self.activity_factors:
                results[activity] = {
                    "quantity": quantity,
                    "emissions_tco2e": 0.0,
                    "note": "No emission factor available for this activity",
                }
                continue

            factor = self.activity_factors[activity]
            emissions = quantity * factor

            results[activity] = {
                "quantity": quantity,
                "factor": factor,
                "emissions_tco2e": round(emissions, 2),
            }
            total_emissions += emissions

        return {
            "method": "activity-based",
            "total_emissions_tco2e": round(total_emissions, 2),
            "data_quality_rating": 4,
            "data_quality_label": "Activity-based (good quality)",
            "activities": results,
        }

    def get_sector_profile(self, sector: str) -> Optional[Dict[str, Any]]:
        """
        Get typical Scope 3 emissions profile for a sector.

        Args:
            sector: Sector key (e.g., "manufacturing_general", "food_beverage").

        Returns:
            Sector profile dict or None if sector not found.
        """
        profile = self.sector_profiles.get(sector)
        if profile is None:
            return None

        enriched = {
            "sector": sector,
            "label": profile["label"],
            "categories": {},
        }

        for cat_id, data in profile["categories"].items():
            enriched["categories"][cat_id] = {
                "name": CATEGORY_NAMES[cat_id],
                "typical_pct": data["typical_pct"],
                "materiality": data["materiality"],
            }

        return enriched

    def generate_summary(self, results: Dict[str, Any]) -> str:
        """
        Generate a markdown summary table from estimation results.

        Args:
            results: Output from estimate_spend_based() or estimate_activity_based().

        Returns:
            Markdown-formatted summary string.
        """
        lines = []
        method = results.get("method", "unknown")
        total = results.get("total_emissions_tco2e", 0.0)
        quality = results.get("data_quality_rating", 0)
        quality_label = results.get("data_quality_label", "")

        lines.append(f"# Scope 3 Emissions Estimate ({method})")
        lines.append("")
        lines.append(f"**Total Scope 3 Emissions:** {total:,.2f} tCO2e")
        lines.append(f"**Data Quality:** {quality}/5 — {quality_label}")
        lines.append("")

        if method == "spend-based":
            total_spend = results.get("total_spend_eur", 0)
            intensity = results.get("avg_intensity_tco2e_per_meur", 0)
            lines.append(f"**Total Spend Analyzed:** EUR {total_spend:,.0f}")
            lines.append(f"**Average Intensity:** {intensity:,.2f} tCO2e / M EUR")
            lines.append("")
            lines.append("| Cat # | Category | Emissions (tCO2e) | % of Total | Spend (EUR) | Quality |")
            lines.append("|-------|----------|-------------------|------------|-------------|---------|")

            categories = results.get("categories", {})
            for cat_id in sorted(categories.keys(), key=lambda x: int(x)):
                cat = categories[cat_id]
                lines.append(
                    f"| {cat_id} | {cat['category_name']} | "
                    f"{cat['emissions_tco2e']:,.2f} | "
                    f"{cat['pct_of_total']:.1f}% | "
                    f"{cat['spend_eur']:,.0f} | "
                    f"{cat.get('data_quality', 2)}/5 |"
                )

        elif method == "activity-based":
            lines.append("| Activity | Quantity | Factor | Emissions (tCO2e) |")
            lines.append("|----------|----------|--------|-------------------|")

            activities = results.get("activities", {})
            for activity, data in activities.items():
                factor_str = f"{data.get('factor', 'N/A')}"
                lines.append(
                    f"| {activity} | {data['quantity']:,.2f} | "
                    f"{factor_str} | {data['emissions_tco2e']:,.2f} |"
                )

        lines.append("")
        lines.append("---")
        lines.append("*Note: Emission factors are simplified averages for estimation purposes.*")
        lines.append("*For regulatory reporting (CSRD/ESRS E1), use verified factors from DEFRA, ecoinvent, or national databases.*")

        return "\n".join(lines)


def load_json_file(path: str) -> Dict:
    """Load and parse a JSON file."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main() -> None:
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Scope 3 GHG Emissions Calculator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--spend",
        type=str,
        help="Path to JSON file with spend data: {category: {subcategory: EUR_amount}}",
    )
    parser.add_argument(
        "--activity",
        type=str,
        help="Path to JSON file with activity data: {activity_key: quantity}",
    )
    parser.add_argument(
        "--sector",
        type=str,
        choices=list(SECTOR_PROFILES.keys()),
        help="Sector for profile lookup and benchmarking",
    )
    parser.add_argument(
        "--profile-only",
        action="store_true",
        help="Only display the sector profile (no estimation)",
    )
    parser.add_argument(
        "--output",
        type=str,
        help="Output file path (default: stdout)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output raw JSON instead of markdown summary",
    )

    args = parser.parse_args()

    if not args.spend and not args.activity and not args.sector:
        parser.print_help()
        sys.exit(1)

    calc = Scope3Calculator()
    output_parts = []

    # Sector profile
    if args.sector:
        profile = calc.get_sector_profile(args.sector)
        if profile is None:
            print(f"Error: Unknown sector '{args.sector}'", file=sys.stderr)
            sys.exit(1)

        if args.json:
            output_parts.append(json.dumps(profile, indent=2))
        else:
            output_parts.append(f"## Sector Profile: {profile['label']}\n")
            output_parts.append("| Cat # | Category | Typical % | Materiality |")
            output_parts.append("|-------|----------|-----------|-------------|")
            for cat_id in sorted(profile["categories"].keys(), key=lambda x: int(x)):
                cat = profile["categories"][cat_id]
                output_parts.append(
                    f"| {cat_id} | {cat['name']} | {cat['typical_pct']}% | {cat['materiality']} |"
                )
            output_parts.append("")

        if args.profile_only:
            output_text = "\n".join(output_parts)
            if args.output:
                with open(args.output, "w", encoding="utf-8") as f:
                    f.write(output_text)
            else:
                print(output_text)
            return

    # Spend-based estimation
    if args.spend:
        spend_data = load_json_file(args.spend)
        results = calc.estimate_spend_based(spend_data)

        if args.json:
            output_parts.append(json.dumps(results, indent=2))
        else:
            output_parts.append(calc.generate_summary(results))

    # Activity-based estimation
    if args.activity:
        activity_data = load_json_file(args.activity)
        results = calc.estimate_activity_based(activity_data)

        if args.json:
            output_parts.append(json.dumps(results, indent=2))
        else:
            output_parts.append(calc.generate_summary(results))

    output_text = "\n\n".join(output_parts)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(output_text)
        print(f"Results written to {args.output}")
    else:
        print(output_text)


if __name__ == "__main__":
    main()
