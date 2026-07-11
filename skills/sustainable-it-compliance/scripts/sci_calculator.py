#!/usr/bin/env python3
"""
SCI Calculator — Software Carbon Intensity (ISO/IEC 21031:2024)

Computes SCI = ((E * I) + M) / R for one or more software boundaries.
E = energy consumed (kWh), I = grid carbon intensity (gCO2e/kWh),
M = embodied emissions share (gCO2e), R = functional unit count.

SCI is a RATE (gCO2e per functional unit), not a total: it cannot be
summed into a corporate GHG inventory. Use it to track software
improvement over time against a consistent boundary and functional unit.

Usage:
    python sci_calculator.py --input sci_input.json
    python sci_calculator.py --energy-kwh 120 --intensity 280 --embodied 45000 \
        --functional-units 1000000 --unit-name "API request"
    python sci_calculator.py --list-intensities

Input JSON format (single boundary or list under "boundaries"):
    {
      "name": "checkout-service",
      "functional_unit": "order processed",
      "energy_kwh": 120.0,             # E over the measurement window
      "grid_intensity_gco2e_kwh": 280, # I — or use "region" (see --list-intensities)
      "embodied_gco2e": 45000,         # M — hardware share for the window (see below)
      "functional_units": 1000000      # R over the same window
    }

Embodied share helper (per ISO 21031): M = TE * (TiR/EL) * (RS/TR)
    TE  = total embodied emissions of the hardware (gCO2e)
    TiR = time reserved / EL = expected lifespan (same time unit)
    RS  = resources reserved / TR = total resources of the host
Pass the four values under "embodied_detail" instead of "embodied_gco2e"
and the script computes M:
    "embodied_detail": {"te_gco2e": 250000000, "tir_hours": 720,
                        "el_hours": 35040, "rs_share": 0.25}
"""

import json
import argparse
import sys
from typing import Any, Dict, List, Optional

# --- Illustrative grid carbon intensities (gCO2e/kWh, location-based) ---
# Yearly averages, rounded; use current data (e.g., Ember, national TSO,
# provider region data / Real Time Cloud) for real assessments.
GRID_INTENSITIES: Dict[str, float] = {
    "eu_average": 210.0,
    "italy": 260.0,
    "france": 55.0,
    "germany": 350.0,
    "spain": 150.0,
    "poland": 620.0,
    "nordics": 45.0,
    "uk": 200.0,
    "us_average": 370.0,
    "world_average": 480.0,
}


def compute_embodied(detail: Dict[str, float]) -> float:
    """M = TE * (TiR/EL) * (RS/TR) per ISO/IEC 21031."""
    te = float(detail["te_gco2e"])
    time_share = float(detail["tir_hours"]) / float(detail["el_hours"])
    rs_share = float(detail.get("rs_share", 1.0))
    return te * time_share * rs_share


def resolve_intensity(boundary: Dict[str, Any]) -> float:
    if "grid_intensity_gco2e_kwh" in boundary:
        return float(boundary["grid_intensity_gco2e_kwh"])
    region = boundary.get("region")
    if region:
        key = str(region).lower()
        if key not in GRID_INTENSITIES:
            raise ValueError(
                f"Unknown region '{region}'. Known: {', '.join(sorted(GRID_INTENSITIES))}"
            )
        return GRID_INTENSITIES[key]
    raise ValueError("Provide 'grid_intensity_gco2e_kwh' or 'region'")


def compute_sci(boundary: Dict[str, Any]) -> Dict[str, Any]:
    name = boundary.get("name", "unnamed boundary")
    e_kwh = float(boundary["energy_kwh"])
    intensity = resolve_intensity(boundary)
    if "embodied_detail" in boundary:
        m = compute_embodied(boundary["embodied_detail"])
        m_source = "computed from embodied_detail (TE * TiR/EL * RS/TR)"
    else:
        m = float(boundary.get("embodied_gco2e", 0.0))
        m_source = "provided" if m else "not provided (M=0 — flag as incomplete)"
    r = float(boundary["functional_units"])
    if r <= 0:
        raise ValueError(f"{name}: functional_units must be > 0")

    operational = e_kwh * intensity
    sci = (operational + m) / r
    return {
        "name": name,
        "functional_unit": boundary.get("functional_unit", "functional unit"),
        "E_kwh": e_kwh,
        "I_gco2e_per_kwh": intensity,
        "operational_gco2e": operational,
        "M_gco2e": m,
        "M_source": m_source,
        "R": r,
        "sci_gco2e_per_unit": sci,
        "operational_share_pct": 100.0 * operational / (operational + m) if (operational + m) else 0.0,
    }


def format_result(res: Dict[str, Any]) -> str:
    lines = [
        f"Boundary: {res['name']}",
        f"  E (energy):            {res['E_kwh']:,.2f} kWh",
        f"  I (grid intensity):    {res['I_gco2e_per_kwh']:,.0f} gCO2e/kWh",
        f"  E x I (operational):   {res['operational_gco2e']:,.0f} gCO2e",
        f"  M (embodied):          {res['M_gco2e']:,.0f} gCO2e ({res['M_source']})",
        f"  R (functional units):  {res['R']:,.0f} ({res['functional_unit']})",
        f"  SCI = ((E x I) + M)/R: {res['sci_gco2e_per_unit']:.4f} gCO2e per {res['functional_unit']}",
        f"  Operational share:     {res['operational_share_pct']:.1f}%",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="SCI (ISO/IEC 21031) calculator")
    parser.add_argument("--input", help="JSON file with one boundary or {'boundaries': [...]}")
    parser.add_argument("--energy-kwh", type=float, help="E: energy consumed (kWh)")
    parser.add_argument("--intensity", type=float, help="I: grid intensity (gCO2e/kWh)")
    parser.add_argument("--region", help="I from built-in region table (see --list-intensities)")
    parser.add_argument("--embodied", type=float, default=0.0, help="M: embodied share (gCO2e)")
    parser.add_argument("--functional-units", type=float, help="R: functional unit count")
    parser.add_argument("--unit-name", default="functional unit", help="Functional unit label")
    parser.add_argument("--name", default="cli boundary", help="Boundary label")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of text")
    parser.add_argument("--list-intensities", action="store_true",
                        help="List built-in illustrative grid intensities")
    args = parser.parse_args()

    if args.list_intensities:
        for k, v in sorted(GRID_INTENSITIES.items()):
            print(f"{k:15s} {v:7.0f} gCO2e/kWh")
        return 0

    boundaries: List[Dict[str, Any]] = []
    if args.input:
        with open(args.input, encoding="utf-8") as fh:
            data = json.load(fh)
        boundaries = data["boundaries"] if isinstance(data, dict) and "boundaries" in data else [data]
    elif args.energy_kwh is not None and args.functional_units is not None:
        b: Dict[str, Any] = {
            "name": args.name,
            "functional_unit": args.unit_name,
            "energy_kwh": args.energy_kwh,
            "embodied_gco2e": args.embodied,
            "functional_units": args.functional_units,
        }
        if args.intensity is not None:
            b["grid_intensity_gco2e_kwh"] = args.intensity
        elif args.region:
            b["region"] = args.region
        else:
            parser.error("provide --intensity or --region")
        boundaries = [b]
    else:
        parser.error("provide --input FILE or (--energy-kwh, --functional-units, --intensity/--region)")

    results = [compute_sci(b) for b in boundaries]
    if args.json:
        print(json.dumps(results, indent=2))
    else:
        for res in results:
            print(format_result(res))
            print()
        print("Note: SCI is a rate per functional unit — do not sum across boundaries")
        print("or report it as a corporate total (use GHG Protocol for inventories).")
        print("Built-in grid intensities are illustrative yearly averages: use current")
        print("regional data (Ember, TSO, cloud provider / Real Time Cloud) for real work.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
