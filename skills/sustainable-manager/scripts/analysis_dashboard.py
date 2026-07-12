#!/usr/bin/env python3
"""
analysis_dashboard.py — build a self-contained comparative HTML dashboard from
one or more sustainability-report analyses produced by the sustainable-manager
skill (Document Analysis / Greenwashing Detection).

Each input JSON must conform to assets/schemas/report-analysis-schema.json.
Pass several files (one analysis each) or a single file containing a JSON array.

Usage:
    python3 analysis_dashboard.py report1.json report2.json -o dashboard.html
    python3 analysis_dashboard.py all_reports.json                # array input
    python3 analysis_dashboard.py *.json --title "Peer benchmark 2025"

Output: a standalone .html (no external assets) with a quality KPI row, a
completeness x greenwashing quadrant, a comparable red-flag matrix, and one card
per report. Theme-aware (light/dark). Colors use a CVD-validated status palette.

The dashboard is a working draft for review, not a certified assessment.
"""
import argparse
import json
import sys
from pathlib import Path


def load_records(paths):
    records = []
    for p in paths:
        data = json.loads(Path(p).read_text(encoding="utf-8"))
        items = data if isinstance(data, list) else [data]
        for it in items:
            if not isinstance(it, dict) or "company" not in it:
                print(f"warning: skipping non-analysis object in {p}", file=sys.stderr)
                continue
            it.setdefault("_source", Path(p).name)
            records.append(it)
    return records


def normalize_risk(v):
    m = {"basso": "low", "medio": "medium", "alto": "high",
         "low": "low", "medium": "medium", "high": "high"}
    return m.get(str(v).lower().strip(), "medium")


def build_payload(records):
    """Map schema objects to the flat shape the embedded JS renderer expects."""
    out = []
    for r in records:
        fw = r.get("framework", {}) or {}
        status_lbl = {"in_accordance": "in accordance", "with_reference": "with reference",
                      "inspired_by": "inspired by", "none": "no standard"}.get(fw.get("status", ""), "")
        standards = fw.get("standards", []) or []
        frameworks = ([f"{standards[0]} ({status_lbl})"] if standards else [status_lbl or "n/d"]) + standards[1:]
        assur = r.get("assurance", {}) or {}
        assurance = ("absent" if not assur.get("present", False)
                     else (assur.get("type") or "external assurance"))
        gw = r.get("greenwashing", {}) or {}
        ver = r.get("verification") or None
        out.append({
            "company": r.get("company", "—"),
            "sector": r.get("sector", ""),
            "period": r.get("reporting_period", ""),
            "frameworks": frameworks,
            "assurance": assurance,
            "metrics": r.get("key_metrics", []) or [],
            "present": (r.get("completeness", {}) or {}).get("present", []) or [],
            "missing": (r.get("completeness", {}) or {}).get("missing", []) or [],
            "gw_risk": normalize_risk(gw.get("overall_risk", "medium")),
            "flagged": gw.get("flagged_claims", []) or [],
            "strengths": r.get("strengths", []) or [],
            "weaknesses": r.get("weaknesses", []) or [],
            "recommendations": r.get("recommendations", []) or [],
            "verification": ver if (ver and ver.get("performed")) else None,
        })
    return out


HTML = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__</title>
<style>
:root{--surface:#fcfcfb;--plane:#f4f4f1;--card:#fff;--ink:#0b0b0b;--ink2:#52514e;--muted:#6b6963;
--grid:#e1e0d9;--line:#e6e5df;--good:#0ca30c;--warning:#e0951a;--serious:#e0663a;--critical:#d03b3b;
--good-ink:#087508;--warn-ink:#8a6000;--serious-ink:#b8501f;--crit-ink:#b3322a;--accent-ink:#1f66c0;
--accent:#2a78d6;--accent-soft:#eef4fc;--shadow:0 1px 2px rgba(0,0,0,.05),0 4px 16px rgba(0,0,0,.04);}
@media(prefers-color-scheme:dark){:root{--surface:#1a1a19;--plane:#0d0d0d;--card:#1f1f1e;--ink:#fff;
--ink2:#c3c2b7;--muted:#a3a199;--grid:#2c2c2a;--line:#2c2c2a;--good:#22b422;--warning:#fab219;
--serious:#ef8a5e;--critical:#e05454;--good-ink:#43c743;--warn-ink:#f5b53a;--serious-ink:#f0956a;
--crit-ink:#f07a7a;--accent-ink:#63a4ee;--accent:#3987e5;--accent-soft:#182636;--shadow:0 1px 2px rgba(0,0,0,.3),0 4px 16px rgba(0,0,0,.25);}}
:root[data-theme="dark"]{--surface:#1a1a19;--plane:#0d0d0d;--card:#1f1f1e;--ink:#fff;--ink2:#c3c2b7;
--muted:#a3a199;--grid:#2c2c2a;--line:#2c2c2a;--good:#22b422;--warning:#fab219;--serious:#ef8a5e;
--critical:#e05454;--good-ink:#43c743;--warn-ink:#f5b53a;--serious-ink:#f0956a;--crit-ink:#f07a7a;
--accent-ink:#63a4ee;--accent:#3987e5;--accent-soft:#182636;--shadow:0 1px 2px rgba(0,0,0,.3),0 4px 16px rgba(0,0,0,.25);}
:root[data-theme="light"]{--surface:#fcfcfb;--plane:#f4f4f1;--card:#fff;--ink:#0b0b0b;--ink2:#52514e;
--muted:#6b6963;--grid:#e1e0d9;--line:#e6e5df;--good:#0ca30c;--warning:#e0951a;--serious:#e0663a;
--critical:#d03b3b;--good-ink:#087508;--warn-ink:#8a6000;--serious-ink:#b8501f;--crit-ink:#b3322a;
--accent-ink:#1f66c0;--accent:#2a78d6;--accent-soft:#eef4fc;--shadow:0 1px 2px rgba(0,0,0,.05),0 4px 16px rgba(0,0,0,.04);}
*{box-sizing:border-box}
body{margin:0;background:var(--plane);color:var(--ink);font:15px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;-webkit-font-smoothing:antialiased}
a:focus-visible,button:focus-visible,summary:focus-visible{outline:2px solid var(--accent);outline-offset:2px;border-radius:4px}
.wrap{max-width:1180px;margin:0 auto;padding:28px 20px 80px}
h1{font-size:25px;letter-spacing:-.02em;margin:0 0 4px}
.sub{color:var(--ink2);font-size:14px;max-width:680px}
.tag{display:inline-block;font-size:12px;font-weight:600;padding:3px 9px;border-radius:20px;background:var(--accent-soft);color:var(--accent-ink)}
h2{font-size:13px;text-transform:uppercase;letter-spacing:.08em;color:var(--muted);font-weight:700;margin:38px 0 14px}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px}
.kpi{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:16px 18px;box-shadow:var(--shadow)}
.kpi .n{font-size:29px;font-weight:750;letter-spacing:-.02em;line-height:1}
.kpi .l{font-size:12.5px;color:var(--ink2);margin-top:6px}
.kpi .n.good{color:var(--good-ink)}.kpi .n.acc{color:var(--accent-ink)}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:14px}
.card{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:18px;box-shadow:var(--shadow)}
.card h3{margin:0 0 2px;font-size:16.5px;letter-spacing:-.01em}
.card .meta{font-size:12.5px;color:var(--muted);margin-bottom:12px}
.rowflex{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.chip{font-size:11.5px;font-weight:600;padding:2px 8px;border-radius:6px;border:1px solid var(--line);color:var(--ink2)}
.risk{font-size:11.5px;font-weight:700;padding:3px 9px;border-radius:6px}
.risk.low{background:color-mix(in srgb,var(--good) 16%,transparent);color:var(--good-ink)}
.risk.medium{background:color-mix(in srgb,var(--warning) 22%,transparent);color:var(--warn-ink)}
.risk.high{background:color-mix(in srgb,var(--critical) 16%,transparent);color:var(--crit-ink)}
.bar{display:flex;height:22px;border-radius:6px;overflow:hidden;margin:10px 0 6px;background:var(--grid)}
.bar span{display:block;box-shadow:2px 0 0 var(--card)}
.seg-good{background:var(--good)}.seg-partial{background:var(--warning)}.seg-uns{background:var(--serious)}.seg-mis{background:var(--critical)}
.legend{display:flex;flex-wrap:wrap;gap:12px;font-size:12px;color:var(--ink2);margin:6px 0 2px}
.legend i{display:inline-block;width:12px;height:12px;border-radius:3px;margin-right:5px;vertical-align:-2px}
.gapbar{height:8px;border-radius:5px;background:var(--grid);overflow:hidden;margin-top:4px}
.gapbar i{display:block;height:100%;background:var(--critical);border-radius:5px}
.mini{font-size:12px;color:var(--ink2)}
.verif{margin-top:14px;border-top:1px solid var(--line);padding-top:12px}
.vbox{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:10px 12px}
.vbox .c{font-size:22px;font-weight:750;letter-spacing:-.02em}
.vbox .c small{font-size:12px;color:var(--muted);font-weight:600}
.vbox .d{font-size:11.5px;color:var(--ink2);margin-top:2px}
.badge{display:inline-block;font-size:10.5px;font-weight:700;padding:1px 6px;border-radius:5px;background:color-mix(in srgb,var(--good) 18%,transparent);color:var(--good-ink)}
details{margin-top:12px}
summary{cursor:pointer;font-size:12.5px;font-weight:600;color:var(--accent-ink);list-style:none}
summary::-webkit-details-marker{display:none}
summary::before{content:"\25B8 "}details[open] summary::before{content:"\25BE "}
.detail{font-size:12.5px;color:var(--ink2);margin-top:8px}
.detail ul{margin:4px 0 10px;padding-left:18px}
table.metrics{width:100%;border-collapse:collapse;font-size:12px;margin-top:6px}
table.metrics th,table.metrics td{text-align:left;padding:5px 8px;border-bottom:1px solid var(--line);vertical-align:top}
table.metrics th{color:var(--muted);font-weight:600;font-size:11px;text-transform:uppercase}
table.metrics td.v{font-variant-numeric:tabular-nums;font-weight:650;white-space:nowrap}
.scrollx{overflow-x:auto}
.scrollhint{font-size:11.5px;color:var(--muted);margin:0 0 6px}
table.matrix{border-collapse:separate;border-spacing:0;width:100%;min-width:700px;font-size:12.5px}
table.matrix caption{caption-side:top;text-align:left;font-size:12px;color:var(--ink2);padding:0 0 10px}
table.matrix th,table.matrix td{padding:7px 4px;text-align:center}
table.matrix thead th{vertical-align:bottom;color:var(--ink2);font-weight:600;font-size:11px;line-height:1.15;border-bottom:2px solid var(--line)}
table.matrix thead th span{display:inline-block;max-width:74px}
table.matrix th.rname{width:180px}
table.matrix th[scope="row"]{text-align:left;font-weight:650;color:var(--ink);white-space:nowrap;padding-left:6px;border-bottom:1px solid var(--line)}
table.matrix td.c{border-bottom:1px solid var(--line);font-size:14px;width:70px}
table.matrix td.c.flag{color:var(--crit-ink);background:color-mix(in srgb,var(--critical) 12%,transparent);cursor:help}
table.matrix td.c.none{color:var(--muted);opacity:.7}
table.matrix th.tot,table.matrix td.tot{width:78px;border-bottom:1px solid var(--line)}
.totn{display:block;font-weight:750;font-size:14px;font-variant-numeric:tabular-nums}
.totn small{font-weight:600;color:var(--muted);font-size:11px}
.totbar{display:block;height:5px;border-radius:4px;background:var(--grid);margin-top:3px;overflow:hidden}
.totbar i{display:block;height:100%;border-radius:4px}
.mlegend{display:flex;gap:16px;flex-wrap:wrap;font-size:12px;color:var(--ink2);padding:12px 6px 2px}
.mlegend .dot.flag{color:var(--crit-ink)}.mlegend .dot.none{color:var(--muted)}
.toggle{position:fixed;top:14px;right:14px;background:var(--card);border:1px solid var(--line);border-radius:20px;padding:6px 12px;font-size:12px;cursor:pointer;color:var(--ink2);box-shadow:var(--shadow);z-index:10}
.foot{margin-top:40px;font-size:12px;color:var(--muted);border-top:1px solid var(--line);padding-top:16px}
</style>
</head>
<body>
<button class="toggle" id="themeBtn" aria-pressed="false" aria-label="Toggle light/dark theme">&#9680; theme</button>
<div class="wrap">
<span class="tag">sustainable-manager &middot; report analysis</span>
<h1>__TITLE__</h1>
<div class="sub">Comparative view of sustainability-report analyses produced with the <b>sustainable-manager</b> skill. Each figure is source-anchored (page + quote) per the anti-fabrication rule. Working draft for review, not a certified assessment.</div>

<h2>Overview</h2>
<div class="kpis" id="kpis"></div>

<h2 id="quadTitle">Completeness &times; greenwashing severity</h2>
<div class="card" style="padding:20px 16px 8px"><div id="quadrant"></div>
<div class="mini" style="padding:6px 6px 10px">X: disclosure completeness (reported / total). Y: <b>mean greenwashing severity</b> of flagged claims (0 = substantiated &rarr; 3 = misleading). <b>Colour = the same severity as the Y axis</b> (green/amber/red), so position and colour agree. <b>Red ring</b> = contains at least one <i>misleading</i> claim (which the mean alone would hide). <b>Dashed outline</b> = no quantitative KPI extracted. Bottom-right = stronger. A report with zero flagged claims sits at 0 and is not necessarily virtuous.</div></div>

<h2>Red flags beyond greenwashing</h2>
<div class="card" style="padding:18px 14px 10px"><div id="redflags"></div></div>

<h2>Per-report detail</h2>
<div class="grid" id="cards"></div>
<div class="foot" id="foot"></div>
</div>
<script>
const DATA = __PAYLOAD__;
const RISK_ORDER={low:0,medium:1,high:2};
const RAT={substantiated:{c:'seg-good',l:'Substantiated'},partially_substantiated:{c:'seg-partial',l:'Partial'},
unsubstantiated:{c:'seg-uns',l:'Unsupported'},misleading:{c:'seg-mis',l:'Misleading'}};
const RW={substantiated:0,partially_substantiated:1,unsubstantiated:2,misleading:3};
const esc=s=>(s==null?'':String(s)).replace(/[&<>"]/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[m]));
const DIMS=[
{s:'External assurance',re:/assurance|terza parte|third[- ]party|independent verification/i},
{s:'Scope 3',re:/scope 3/i},
{s:'Scope 2 mkt/loc',re:/market-based|location-based/i},
{s:'Target/baseline',re:/sbti|science-based|baseline|reduction target|target.*ridu/i},
{s:'Transition plan',re:/transition plan|piano di transizione/i},
{s:'Double materiality',re:/double materiality|doppia materialit/i},
{s:'Data inconsistency',re:/inconsist|incoerenz|not reconcil|non riconcil|contradict|contraddizione/i},
{s:'Social / pay gap',re:/pay gap|remunerat|retribuzion|board diversity|turnover/i},
{s:'Methodology',re:/methodolog|metodolog|not verifiable|non verificabil|emission factor|fattori di emissione/i},
{s:'Offset-heavy',re:/offset|compensa|neutralit.*(without|senza)|not science-based|on\/off/i}];
function redflags(d){const miss=d.missing||[],weak=d.weaknesses||[];
 const cells=DIMS.map(dim=>{let hit=miss.find(t=>dim.re.test(t)),src='Missing';
  if(!hit){hit=weak.find(t=>dim.re.test(t));src='Weakness';}
  return hit?{state:'flag',ev:hit,src,label:dim.s}:{state:'none',label:dim.s};});
 return {cells,total:DIMS.length,flags:cells.filter(c=>c.state==='flag').length};}
function severity(d){return d.flagged.length?d.flagged.reduce((s,f)=>s+(RW[f.rating]??0),0)/d.flagged.length:0;}
function hasMisleading(d){return d.flagged.some(f=>f.rating==='misleading');}

let reports=DATA.length, verified=DATA.filter(d=>d.verification).length;
let totFlags=DATA.reduce((a,d)=>a+d.flagged.length,0);
let mis=DATA.reduce((a,d)=>a+d.flagged.filter(f=>f.rating==='misleading').length,0);
let noAssur=DATA.filter(d=>/absent|assente|nessun/i.test(d.assurance)).length;
let confs=DATA.filter(d=>d.verification&&typeof d.verification.confidence==='number').map(d=>d.verification.confidence);
let avgConf=confs.length?Math.round(confs.reduce((a,b)=>a+b,0)/confs.length):null;
const kpis=[{n:reports,l:'reports analyzed'},
{n:totFlags,l:'greenwashing claims flagged'},
{n:mis,l:'misleading claims',cls:mis?'':'good'},
{n:noAssur+'/'+reports,l:'without external assurance'},
{n:verified+'/'+reports,l:'independently verified',cls:'acc'}];
if(avgConf!=null)kpis.push({n:avgConf,l:'mean verification confidence /100',cls:'acc'});
document.getElementById('kpis').innerHTML=kpis.map(k=>`<div class="kpi"><div class="n ${k.cls||''}">${esc(k.n)}</div><div class="l">${esc(k.l)}</div></div>`).join('');

(function(){
 const pts=DATA.map(d=>({name:d.company.split(/[—(]/)[0].trim(),
  comp:100*d.present.length/((d.present.length+d.missing.length)||1),sev:severity(d),
  kpi:d.metrics.length,mis:hasMisleading(d)}));
 const W=720,H=440,m={t:26,r:26,b:54,l:60},pw=W-m.l-m.r,ph=H-m.t-m.b,xd=[30,70],yd=[0,3];
 const X=v=>m.l+(Math.max(xd[0],Math.min(xd[1],v))-xd[0])/(xd[1]-xd[0])*pw;
 const Y=v=>m.t+(1-(v-yd[0])/(yd[1]-yd[0]))*ph;
 const sevCol=s=>s<1?'var(--good)':s<2?'var(--warning)':'var(--critical)';
 const xmid=X(50),ymid=Y(1.5),R=11;
 let s=`<svg viewBox="0 0 ${W} ${H}" width="100%" role="img" aria-label="Completeness (X) by mean greenwashing severity (Y); colour and vertical position encode the same severity" style="max-width:100%;height:auto;font-family:inherit">`;
 s+=`<rect x="${m.l}" y="${ymid}" width="${xmid-m.l}" height="${m.t+ph-ymid}" fill="var(--critical)" opacity="0.05"/>`;
 s+=`<rect x="${xmid}" y="${m.t}" width="${m.l+pw-xmid}" height="${ymid-m.t}" fill="var(--good)" opacity="0.06"/>`;
 for(const g of[0,1,2,3]){const gy=Y(g);s+=`<line x1="${m.l}" y1="${gy}" x2="${m.l+pw}" y2="${gy}" stroke="var(--grid)"/>`;s+=`<text x="${m.l-10}" y="${gy+4}" text-anchor="end" font-size="11" fill="var(--muted)">${g}</text>`;}
 for(const g of[40,50,60]){const gx=X(g);s+=`<line x1="${gx}" y1="${m.t}" x2="${gx}" y2="${m.t+ph}" stroke="var(--grid)"/>`;s+=`<text x="${gx}" y="${m.t+ph+18}" text-anchor="middle" font-size="11" fill="var(--muted)">${g}%</text>`;}
 s+=`<text x="${m.l+pw/2}" y="${H-10}" text-anchor="middle" font-size="12" fill="var(--ink2)" font-weight="600">Completeness &#8594;</text>`;
 s+=`<text transform="translate(16 ${m.t+ph/2}) rotate(-90)" text-anchor="middle" font-size="12" fill="var(--ink2)" font-weight="600">&#8592; Mean greenwashing severity (0-3)</text>`;
 s+=`<text x="${m.l+pw-6}" y="${m.t+14}" text-anchor="end" font-size="10.5" fill="var(--crit-ink)" font-weight="700">more critical</text>`;
 s+=`<text x="${m.l+pw-6}" y="${m.t+ph-8}" text-anchor="end" font-size="10.5" fill="var(--good-ink)" font-weight="700">stronger &#10003;</text>`;
 const order=[...pts].sort((a,b)=>a.comp-b.comp);
 order.forEach((p,i)=>{const cx=X(p.comp),cy=Y(p.sev);
  if(p.mis)s+=`<circle cx="${cx}" cy="${cy}" r="${R+4}" fill="none" stroke="var(--critical)" stroke-width="1.5"/>`;
  s+=`<circle cx="${cx}" cy="${cy}" r="${R}" fill="${sevCol(p.sev)}" fill-opacity="0.85" stroke="var(--card)" stroke-width="2"${p.kpi===0?' stroke-dasharray="3 2"':''}><title>${esc(p.name)}: completeness ${p.comp.toFixed(0)}%, severity ${p.sev.toFixed(2)}/3, ${p.kpi} KPI${p.mis?', contains a misleading claim':''}${p.kpi===0?', no KPI extracted':''}</title></circle>`;
  const ly=(i%2===0)?cy-R-7:cy+R+15;
  s+=`<text x="${cx}" y="${ly}" text-anchor="middle" font-size="11.5" font-weight="650" fill="var(--ink)">${esc(p.name.slice(0,22))}</text>`;});
 let tbl=`<details><summary>Chart data (table)</summary><div class="detail"><table class="metrics"><thead><tr><th>Company</th><th>Completeness</th><th>Severity</th><th>KPI</th><th>Misleading claim</th></tr></thead><tbody>`;
 pts.forEach(p=>{tbl+=`<tr><td>${esc(p.name)}</td><td class="v">${p.comp.toFixed(0)}%</td><td class="v">${p.sev.toFixed(2)}/3</td><td class="v">${p.kpi}</td><td>${p.mis?'yes':'no'}</td></tr>`;});
 tbl+=`</tbody></table></div></details>`;
 document.getElementById('quadrant').innerHTML=s+`</svg>`+tbl;
 if(DATA.length<2){document.getElementById('quadTitle').style.display='none';document.getElementById('quadrant').parentNode.style.display='none';}
})();

(function(){
 const rows=DATA.map(d=>{const rf=redflags(d);return {name:d.company.split(/[—(]/)[0].trim(),cells:rf.cells,flags:rf.flags,total:rf.total};})
  .sort((a,b)=>b.flags-a.flags);
 const N=DIMS.length;
 let h=`<div class="scrollhint">Scroll horizontally to see all categories &rarr;</div><div class="scrollx"><table class="matrix">`;
 h+=`<caption>Concerns detected in each analysis text. <b>&#9679;</b> detected &middot; <b>&middot;</b> not flagged (not a compliance check) &middot; more concerns = more issues.</caption>`;
 h+=`<thead><tr><th class="rname" scope="col"><span>Company</span></th>`;
 DIMS.forEach(dim=>h+=`<th scope="col"><span>${esc(dim.s)}</span></th>`);h+=`<th class="tot" scope="col">Concerns</th></tr></thead><tbody>`;
 rows.forEach(r=>{h+=`<tr><th scope="row">${esc(r.name.slice(0,26))}</th>`;
  r.cells.forEach(c=>{h+=c.state==='flag'?`<td class="c flag" title="${esc(c.label)} — ${c.src}: ${esc(c.ev).replace(/"/g,'&quot;').slice(0,180)}">&#9679;</td>`:`<td class="c none" title="${esc(c.label)}: not flagged in the analysis (not a compliance check)">&middot;</td>`;});
  const pct=r.flags/N,bc=pct>=0.6?'var(--critical)':pct>=0.35?'var(--warning)':'var(--good)';
  h+=`<td class="tot"><span class="totn">${r.flags}<small> of ${N}</small></span><span class="totbar"><i style="width:${Math.round(pct*100)}%;background:${bc}"></i></span></td></tr>`;});
 h+=`</tbody></table></div><div class="mlegend"><span><b class="dot flag">&#9679;</b> concern detected</span><span><b class="dot none">&middot;</b> not flagged (not = compliant)</span></div>`;
 h+=`<details><summary>Detected concern evidence</summary><div class="detail">`;
 h+=`<p class="mini" style="margin:0 0 6px">Each item shows the <b>missing disclosure</b> or <b>weakness</b> that triggered the concern — not something present in the report.</p>`;
 rows.forEach(r=>{const fl=r.cells.filter(c=>c.state==='flag');if(!fl.length)return;
  h+=`<div style="margin:8px 0"><b>${esc(r.name)}</b> — ${r.flags} of ${N}<ul>${fl.map(c=>`<li><b>${esc(c.label)}</b> — <i>${c.src}</i>: ${esc(c.ev).slice(0,200)}</li>`).join('')}</ul></div>`;});
 h+=`</div></details>`;
 document.getElementById('redflags').innerHTML=h;
})();

const sorted=[...DATA].sort((a,b)=>(RISK_ORDER[b.gw_risk]-RISK_ORDER[a.gw_risk])||(b.missing.length-a.missing.length));
function stack(flagged){const c={substantiated:0,partially_substantiated:0,unsubstantiated:0,misleading:0};
 flagged.forEach(f=>{if(c[f.rating]!=null)c[f.rating]++});const tot=flagged.length||1;
 const ord=['substantiated','partially_substantiated','unsubstantiated','misleading'];
 return `<div class="bar" role="img" aria-label="Claim breakdown by rating">${ord.filter(k=>c[k]>0).map(k=>`<span class="${RAT[k].c}" style="width:${100*c[k]/tot}%" title="${RAT[k].l}: ${c[k]}"></span>`).join('')}</div>`;}
function vbox(v){if(!v)return '';const conf=(typeof v.confidence==='number')?v.confidence:'—';
 const iss=(v.issues||[]).filter(i=>['imprecise','refuted','unverifiable'].includes(i.verdict));
 return `<div class="verif"><div class="mini" style="margin-bottom:6px"><b>Independent verification</b></div>
 <div class="vbox"><div class="c">${conf}<small>/100</small></div>
 <div class="d">${esc(v.summary||'').slice(0,180)} <span class="badge">${v.hallucinations??0} halluc.</span></div></div>
 ${iss.length?`<details><summary>Verifier issues (${iss.length})</summary><div class="detail">${iss.map(i=>`<div>&bull; <b>${esc(i.verdict)}</b> — ${esc(i.claim).slice(0,90)}: ${esc(i.evidence).slice(0,150)}</div>`).join('')}</div></details>`:''}</div>`;}
function mtable(m){if(!m.length)return '<div class="mini" style="margin-top:6px">No quantitative KPI extracted.</div>';
 return `<table class="metrics"><thead><tr><th>Metric</th><th>Value</th><th>Pg.</th></tr></thead><tbody>${m.map(x=>`<tr><td>${esc(x.name)}</td><td class="v">${esc(x.value)} ${esc(x.unit)}</td><td class="v">${esc(x.page)}</td></tr>`).join('')}</tbody></table>`;}
document.getElementById('cards').innerHTML=sorted.map(d=>{
 const rf=redflags(d);
 const fw=d.frameworks[0]?d.frameworks[0].slice(0,42):'n/d';
 return `<div class="card"><div class="rowflex" style="justify-content:space-between">
 <h3>${esc(d.company.split(/[—(]/)[0].trim().slice(0,40))}</h3>
 <span class="risk ${d.gw_risk}">GW ${esc(d.gw_risk)}</span></div>
 <div class="meta">${esc((d.period||d.sector||'').slice(0,66))}</div>
 <div class="rowflex"><span class="chip">${esc(fw)}</span>
 <span class="chip">${/absent|assente|nessun/i.test(d.assurance)?'No assurance':'Assured'}</span>
 <span class="chip">${d.metrics.length} KPI</span></div>
 <div style="margin-top:14px"><div class="mini"><b>Greenwashing claims</b> &middot; ${d.flagged.length} flagged</div>${stack(d.flagged)}
 <div class="legend"><span><i style="background:var(--good)"></i>Subst.</span><span><i style="background:var(--warning)"></i>Partial</span><span><i style="background:var(--serious)"></i>Unsup.</span><span><i style="background:var(--critical)"></i>Mislead.</span></div>
 <details><summary>Breakdown of ${d.flagged.length} claims</summary><div class="detail">${d.flagged.map(f=>`<div>&bull; <b>${RAT[f.rating].l}</b> (p.${esc(f.page)}) — ${esc(f.claim).slice(0,120)}</div>`).join('')}</div></details></div>
 <div style="margin-top:12px">
 <div class="mini"><b>Disclosures</b> — ${d.present.length} reported &middot; ${d.missing.length} gaps</div>
 <div class="mini" style="margin-top:6px"><b>Material concerns</b> — ${rf.flags} of ${rf.total} key categories <span style="color:var(--muted)">(comparable subset of the gaps)</span></div>
 <div class="gapbar" role="img" aria-label="Material concerns: ${rf.flags} of ${rf.total}"><i style="width:${Math.round(100*rf.flags/rf.total)}%"></i></div></div>
 ${vbox(d.verification)}
 <details><summary>KPIs, strengths &amp; weaknesses</summary><div class="detail">${mtable(d.metrics)}
 <div style="margin-top:10px"><b>Strengths</b><ul>${d.strengths.map(s=>`<li>${esc(s)}</li>`).join('')}</ul>
 <b>Weaknesses</b><ul>${d.weaknesses.map(s=>`<li>${esc(s)}</li>`).join('')}</ul>
 ${d.recommendations.length?`<b>Recommendations</b><ul>${d.recommendations.map(s=>`<li>${esc(s)}</li>`).join('')}</ul>`:''}</div></div></details>
 </div>`;}).join('');

document.getElementById('foot').innerHTML=`${reports} report(s) &middot; ${totFlags} greenwashing claims flagged (${mis} misleading) &middot; ${noAssur} without external assurance. Produced with the sustainable-manager skill.`;
const b=document.getElementById('themeBtn');b.onclick=()=>{const r=document.documentElement;
 const cur=r.getAttribute('data-theme')||(matchMedia('(prefers-color-scheme:dark)').matches?'dark':'light');
 const next=cur==='dark'?'light':'dark';r.setAttribute('data-theme',next);
 b.setAttribute('aria-pressed',next==='dark'?'true':'false');};
</script>
</body>
</html>"""


def render(records, title):
    payload = json.dumps(build_payload(records), ensure_ascii=False)
    return HTML.replace("__PAYLOAD__", payload).replace("__TITLE__", title)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Build a comparative HTML dashboard from report-analysis JSON files.")
    ap.add_argument("inputs", nargs="+", help="One or more analysis JSON files (schema: report-analysis-schema.json). A file may hold one object or an array.")
    ap.add_argument("-o", "--output", default="analysis-dashboard.html", help="Output HTML path (default: analysis-dashboard.html).")
    ap.add_argument("--title", default="Sustainability report analysis", help="Dashboard title.")
    args = ap.parse_args(argv)

    records = load_records(args.inputs)
    if not records:
        print("error: no valid analysis objects found in inputs", file=sys.stderr)
        return 1
    Path(args.output).write_text(render(records, args.title), encoding="utf-8")
    print(f"Wrote {args.output} ({len(records)} report(s)).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
