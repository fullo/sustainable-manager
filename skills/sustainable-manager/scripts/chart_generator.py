"""
Sustainability Chart Generator
Provides consistent styling and common chart types for sustainability data visualization.

Usage:
    import sys
    sys.path.insert(0, "<path-to-this-script's-directory>")
    from chart_generator import SustainabilityCharts

    charts = SustainabilityCharts()
    charts.emissions_bar(data, output_path="emissions.png")
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
from pathlib import Path

# --- Color Palette ---
# Professional sustainability palette: earth tones, greens, blues
COLORS = {
    "primary": "#2D6A4F",      # Deep forest green
    "secondary": "#40916C",    # Medium green
    "tertiary": "#52B788",     # Light green
    "accent1": "#1B4965",      # Deep blue
    "accent2": "#5FA8D3",      # Sky blue
    "accent3": "#62B6CB",      # Teal
    "warning": "#E07A5F",      # Terracotta
    "neutral": "#6C757D",      # Gray
    "light": "#B7E4C7",        # Pale green
    "bg": "#FAFAFA",           # Background
}

PALETTE = [
    COLORS["primary"], COLORS["accent1"], COLORS["tertiary"],
    COLORS["accent2"], COLORS["warning"], COLORS["accent3"],
    COLORS["secondary"], COLORS["neutral"], COLORS["light"],
]

# Scope-specific colors for GHG emissions
SCOPE_COLORS = {
    "Scope 1": "#E07A5F",   # Direct - warm
    "Scope 2": "#5FA8D3",   # Indirect energy - blue
    "Scope 3": "#2D6A4F",   # Value chain - green
}


def _apply_style(fig, ax, title, source=None):
    """Apply consistent styling to a chart."""
    fig.patch.set_facecolor(COLORS["bg"])
    ax.set_facecolor(COLORS["bg"])
    ax.set_title(title, fontsize=14, fontweight="bold", color="#333333", pad=15)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#CCCCCC")
    ax.spines["bottom"].set_color("#CCCCCC")
    ax.tick_params(colors="#666666", labelsize=10)
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{x:,.0f}"))
    if source:
        fig.text(0.99, 0.01, f"Source: {source}", ha="right", va="bottom",
                 fontsize=8, color="#999999", style="italic")
    fig.tight_layout()


class SustainabilityCharts:
    """Generate sustainability-themed charts with consistent styling."""

    def __init__(self, figsize=(10, 6), dpi=150):
        self.figsize = figsize
        self.dpi = dpi

    def _create_fig(self, figsize=None):
        return plt.subplots(figsize=figsize or self.figsize)

    # --- Bar Charts ---

    def bar_chart(self, categories, values, title, ylabel, output_path,
                  colors=None, source=None, horizontal=False):
        """Generic bar chart."""
        fig, ax = self._create_fig()
        c = colors or [PALETTE[i % len(PALETTE)] for i in range(len(categories))]
        if horizontal:
            ax.barh(categories, values, color=c, height=0.6)
            ax.set_xlabel(ylabel)
        else:
            ax.bar(categories, values, color=c, width=0.6)
            ax.set_ylabel(ylabel)
        _apply_style(fig, ax, title, source)
        fig.savefig(output_path, dpi=self.dpi, bbox_inches="tight")
        plt.close(fig)
        return output_path

    def emissions_by_scope(self, scope1, scope2, scope3, years, output_path, source=None):
        """Stacked bar chart of GHG emissions by scope over years."""
        fig, ax = self._create_fig()
        x = np.arange(len(years))
        w = 0.5
        ax.bar(x, scope1, w, label="Scope 1", color=SCOPE_COLORS["Scope 1"])
        ax.bar(x, scope2, w, bottom=scope1, label="Scope 2", color=SCOPE_COLORS["Scope 2"])
        ax.bar(x, scope3, w, bottom=np.array(scope1)+np.array(scope2),
               label="Scope 3", color=SCOPE_COLORS["Scope 3"])
        ax.set_xticks(x)
        ax.set_xticklabels(years)
        ax.set_ylabel("tCO2e")
        ax.legend(frameon=False)
        _apply_style(fig, ax, "GHG Emissions by Scope", source)
        fig.savefig(output_path, dpi=self.dpi, bbox_inches="tight")
        plt.close(fig)
        return output_path

    # --- Line Charts ---

    def trend_line(self, x_values, y_series, title, ylabel, output_path,
                   labels=None, target_line=None, source=None):
        """Line chart for trends over time. y_series can be a list of lists for multiple lines."""
        fig, ax = self._create_fig()
        if not isinstance(y_series[0], (list, np.ndarray)):
            y_series = [y_series]
            labels = labels or [""]
        else:
            labels = labels or [f"Series {i+1}" for i in range(len(y_series))]

        for i, (ys, label) in enumerate(zip(y_series, labels)):
            ax.plot(x_values, ys, color=PALETTE[i % len(PALETTE)],
                    marker="o", markersize=5, linewidth=2, label=label)
        if target_line is not None:
            ax.axhline(y=target_line, color=COLORS["warning"], linestyle="--",
                       linewidth=1.5, label="Target")
        if len(y_series) > 1 or target_line is not None:
            ax.legend(frameon=False)
        ax.set_ylabel(ylabel)
        _apply_style(fig, ax, title, source)
        fig.savefig(output_path, dpi=self.dpi, bbox_inches="tight")
        plt.close(fig)
        return output_path

    # --- Pie / Donut Charts ---

    def donut_chart(self, labels, values, title, output_path, source=None):
        """Donut chart for composition breakdowns (max 6 categories recommended)."""
        fig, ax = self._create_fig(figsize=(8, 8))
        colors = [PALETTE[i % len(PALETTE)] for i in range(len(labels))]
        wedges, texts, autotexts = ax.pie(
            values, labels=labels, colors=colors, autopct="%1.1f%%",
            startangle=90, pctdistance=0.75,
            wedgeprops=dict(width=0.4, edgecolor="white", linewidth=2)
        )
        for t in autotexts:
            t.set_fontsize(10)
            t.set_color("#333333")
        ax.set_title(title, fontsize=14, fontweight="bold", color="#333333", pad=15)
        fig.patch.set_facecolor(COLORS["bg"])
        if source:
            fig.text(0.99, 0.01, f"Source: {source}", ha="right", va="bottom",
                     fontsize=8, color="#999999", style="italic")
        fig.tight_layout()
        fig.savefig(output_path, dpi=self.dpi, bbox_inches="tight")
        plt.close(fig)
        return output_path

    # --- Radar / Spider Charts ---

    def radar_chart(self, categories, values, title, output_path,
                    max_value=100, source=None):
        """Radar chart for multi-dimensional scoring (e.g., ESG pillar comparison)."""
        N = len(categories)
        angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
        values_plot = values + [values[0]]
        angles += [angles[0]]

        fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
        fig.patch.set_facecolor(COLORS["bg"])
        ax.set_facecolor(COLORS["bg"])
        ax.plot(angles, values_plot, "o-", color=COLORS["primary"], linewidth=2)
        ax.fill(angles, values_plot, alpha=0.2, color=COLORS["tertiary"])
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(categories, fontsize=11, color="#333333")
        ax.set_ylim(0, max_value)
        ax.set_title(title, fontsize=14, fontweight="bold", color="#333333", pad=20)
        ax.grid(color="#CCCCCC", linewidth=0.5)
        if source:
            fig.text(0.99, 0.01, f"Source: {source}", ha="right", va="bottom",
                     fontsize=8, color="#999999", style="italic")
        fig.tight_layout()
        fig.savefig(output_path, dpi=self.dpi, bbox_inches="tight")
        plt.close(fig)
        return output_path

    # --- Heatmap ---

    def heatmap(self, data, row_labels, col_labels, title, output_path,
                cmap="YlGn", source=None):
        """Heatmap for materiality matrices or risk grids."""
        fig, ax = self._create_fig(figsize=(max(8, len(col_labels)*1.5), max(6, len(row_labels)*0.8)))
        im = ax.imshow(data, cmap=cmap, aspect="auto")
        ax.set_xticks(np.arange(len(col_labels)))
        ax.set_yticks(np.arange(len(row_labels)))
        ax.set_xticklabels(col_labels, fontsize=10)
        ax.set_yticklabels(row_labels, fontsize=10)
        plt.setp(ax.get_xticklabels(), rotation=45, ha="right")
        # Add text annotations
        for i in range(len(row_labels)):
            for j in range(len(col_labels)):
                val = data[i][j] if isinstance(data[i], list) else data[i, j]
                ax.text(j, i, f"{val:.1f}", ha="center", va="center",
                        color="white" if val > np.max(data)*0.6 else "#333333", fontsize=9)
        fig.colorbar(im, ax=ax, shrink=0.8)
        ax.set_title(title, fontsize=14, fontweight="bold", color="#333333", pad=15)
        fig.patch.set_facecolor(COLORS["bg"])
        if source:
            fig.text(0.99, 0.01, f"Source: {source}", ha="right", va="bottom",
                     fontsize=8, color="#999999", style="italic")
        fig.tight_layout()
        fig.savefig(output_path, dpi=self.dpi, bbox_inches="tight")
        plt.close(fig)
        return output_path

    # --- Gauge Chart ---

    def gauge(self, value, max_value, title, output_path, unit="%",
              thresholds=None, source=None):
        """Gauge chart for progress toward targets."""
        fig, ax = plt.subplots(figsize=(6, 4), subplot_kw=dict(polar=False))
        fig.patch.set_facecolor(COLORS["bg"])

        # Create a half-circle gauge
        theta = np.linspace(np.pi, 0, 100)
        # Background arc
        ax.plot(np.cos(theta), np.sin(theta), color="#E0E0E0", linewidth=20,
                solid_capstyle="round")
        # Value arc
        ratio = min(value / max_value, 1.0)
        theta_val = np.linspace(np.pi, np.pi - (np.pi * ratio), max(int(100 * ratio), 2))
        color = COLORS["primary"] if ratio >= 0.7 else (COLORS["warning"] if ratio >= 0.4 else "#DC3545")
        ax.plot(np.cos(theta_val), np.sin(theta_val), color=color, linewidth=20,
                solid_capstyle="round")

        ax.text(0, -0.1, f"{value:,.0f}{unit}", ha="center", va="center",
                fontsize=28, fontweight="bold", color="#333333")
        ax.text(0, -0.35, f"of {max_value:,.0f}{unit} target", ha="center", va="center",
                fontsize=11, color="#999999")
        ax.set_xlim(-1.3, 1.3)
        ax.set_ylim(-0.5, 1.2)
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set_title(title, fontsize=14, fontweight="bold", color="#333333", pad=5)
        if source:
            fig.text(0.99, 0.01, f"Source: {source}", ha="right", va="bottom",
                     fontsize=8, color="#999999", style="italic")
        fig.tight_layout()
        fig.savefig(output_path, dpi=self.dpi, bbox_inches="tight")
        plt.close(fig)
        return output_path

    # --- Materiality Matrix ---

    def materiality_matrix(self, topics, impact_scores, financial_scores, output_path,
                           title="Double Materiality Matrix", source=None, labels_fontsize=9):
        """
        Double materiality matrix — the core visualization for ESRS/CSRD reporting.

        topics: list of str — topic names (e.g., "Climate Change", "Water Use")
        impact_scores: list of float — impact materiality scores (0-10, y-axis)
        financial_scores: list of float — financial materiality scores (0-10, x-axis)
        """
        fig, ax = self._create_fig(figsize=(10, 10))

        # Quadrant backgrounds
        ax.axhspan(5, 10, xmin=0.5, xmax=1.0, alpha=0.08, color=COLORS["primary"])   # top-right: doubly material
        ax.axhspan(5, 10, xmin=0, xmax=0.5, alpha=0.05, color=COLORS["accent2"])      # top-left: impact only
        ax.axhspan(0, 5, xmin=0.5, xmax=1.0, alpha=0.05, color=COLORS["accent3"])     # bottom-right: financial only
        ax.axhspan(0, 5, xmin=0, xmax=0.5, alpha=0.03, color=COLORS["neutral"])       # bottom-left: not material

        # Threshold lines
        ax.axhline(y=5, color="#CCCCCC", linestyle="--", linewidth=1, zorder=1)
        ax.axvline(x=5, color="#CCCCCC", linestyle="--", linewidth=1, zorder=1)

        # Quadrant labels
        ax.text(7.5, 9.5, "DOUBLY MATERIAL", ha="center", va="top",
                fontsize=11, fontweight="bold", color=COLORS["primary"], alpha=0.6)
        ax.text(2.5, 9.5, "IMPACT\nMATERIALITY", ha="center", va="top",
                fontsize=10, color=COLORS["accent2"], alpha=0.6)
        ax.text(7.5, 0.5, "FINANCIAL\nMATERIALITY", ha="center", va="bottom",
                fontsize=10, color=COLORS["accent3"], alpha=0.6)
        ax.text(2.5, 0.5, "NOT MATERIAL", ha="center", va="bottom",
                fontsize=10, color=COLORS["neutral"], alpha=0.5)

        # Plot topics
        colors = []
        for imp, fin in zip(impact_scores, financial_scores):
            if imp >= 5 and fin >= 5:
                colors.append(COLORS["primary"])
            elif imp >= 5:
                colors.append(COLORS["accent2"])
            elif fin >= 5:
                colors.append(COLORS["accent3"])
            else:
                colors.append(COLORS["neutral"])

        ax.scatter(financial_scores, impact_scores, c=colors, s=200, zorder=3,
                   edgecolors="white", linewidths=1.5)

        # Label each point
        for i, topic in enumerate(topics):
            offset_y = 0.25 if impact_scores[i] < 9 else -0.35
            ax.annotate(topic, (financial_scores[i], impact_scores[i]),
                        textcoords="offset points", xytext=(0, 12),
                        ha="center", va="bottom", fontsize=labels_fontsize,
                        color="#333333", fontweight="bold",
                        bbox=dict(boxstyle="round,pad=0.2", facecolor="white",
                                  edgecolor="#DDDDDD", alpha=0.85))

        ax.set_xlabel("Financial Materiality →", fontsize=12, color="#555555", labelpad=10)
        ax.set_ylabel("Impact Materiality →", fontsize=12, color="#555555", labelpad=10)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        _apply_style(fig, ax, title, source)
        fig.savefig(output_path, dpi=self.dpi, bbox_inches="tight")
        plt.close(fig)
        return output_path

    # --- Infographic HTML ---

    def html_infographic(self, title, sections, output_path):
        """
        Generate a self-contained HTML infographic.

        sections: list of dicts with keys:
            - "title": section heading
            - "value": big number or key metric
            - "unit": unit label
            - "description": brief text
            - "color": optional hex color (defaults to palette)
            - "chart_img": optional path to a chart image to embed (base64)
        """
        import base64

        cards_html = ""
        for i, s in enumerate(sections):
            color = s.get("color", PALETTE[i % len(PALETTE)])
            img_html = ""
            if s.get("chart_img"):
                img_path = Path(s["chart_img"])
                if img_path.exists():
                    b64 = base64.b64encode(img_path.read_bytes()).decode()
                    ext = img_path.suffix.lstrip(".")
                    img_html = f'<img src="data:image/{ext};base64,{b64}" style="max-width:100%;margin-top:12px;border-radius:8px;">'

            cards_html += f"""
            <div class="card" style="border-left:4px solid {color}">
                <h3 style="color:{color}">{s['title']}</h3>
                <div class="big-number" style="color:{color}">{s['value']}<span class="unit">{s.get('unit','')}</span></div>
                <p>{s.get('description','')}</p>
                {img_html}
            </div>
            """

        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{ font-family:'Segoe UI',system-ui,-apple-system,sans-serif; background:{COLORS['bg']}; color:#333; padding:40px 20px; }}
  .container {{ max-width:1000px; margin:0 auto; }}
  h1 {{ font-size:28px; color:{COLORS['primary']}; margin-bottom:8px; }}
  .subtitle {{ font-size:14px; color:#999; margin-bottom:32px; }}
  .grid {{ display:grid; grid-template-columns:repeat(auto-fit, minmax(280px,1fr)); gap:20px; }}
  .card {{ background:white; border-radius:12px; padding:24px; box-shadow:0 2px 8px rgba(0,0,0,0.06); }}
  .card h3 {{ font-size:14px; text-transform:uppercase; letter-spacing:1px; margin-bottom:12px; }}
  .big-number {{ font-size:42px; font-weight:700; line-height:1; margin-bottom:8px; }}
  .unit {{ font-size:18px; font-weight:400; margin-left:4px; }}
  .card p {{ font-size:13px; color:#666; line-height:1.5; }}
</style>
</head>
<body>
<div class="container">
  <h1>{title}</h1>
  <p class="subtitle">Generated by Sustainability Manager</p>
  <div class="grid">
    {cards_html}
  </div>
</div>
</body>
</html>"""
        Path(output_path).write_text(html, encoding="utf-8")
        return output_path


# --- Convenience: Interactive HTML with Plotly.js ---

def interactive_chart_html(chart_config, output_path):
    """
    Generate a self-contained HTML file with an interactive Plotly.js chart.

    chart_config: dict with keys:
        - "data": list of Plotly trace dicts
        - "layout": Plotly layout dict
        - "title": page title
    """
    import json
    data_json = json.dumps(chart_config["data"])
    layout = chart_config.get("layout", {})
    layout.setdefault("paper_bgcolor", COLORS["bg"])
    layout.setdefault("plot_bgcolor", COLORS["bg"])
    layout.setdefault("font", {"family": "Segoe UI, system-ui, sans-serif", "color": "#333"})
    layout_json = json.dumps(layout)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{chart_config.get('title', 'Chart')}</title>
<script src="https://cdn.plot.ly/plotly-2.27.0.min.js"></script>
<style>body{{margin:0;padding:20px;background:{COLORS['bg']};font-family:system-ui,sans-serif;}}</style>
</head>
<body>
<div id="chart" style="width:100%;max-width:1000px;margin:0 auto;"></div>
<script>
Plotly.newPlot('chart', {data_json}, {layout_json}, {{responsive:true}});
</script>
</body>
</html>"""
    Path(output_path).write_text(html, encoding="utf-8")
    return output_path
