#!/usr/bin/env python3
"""Automated quote check for a report analysis.

Checks that every quote in `key_metrics` and `greenwashing.flagged_claims`
of a report-analysis JSON (assets/schemas/report-analysis-schema.json) is
found, after normalization, on the cited page(s) of the source PDF.
Both `pdftotext -layout` and plain `pdftotext` text are tried.

This is NOT an adversarial verification: it only proves that the quote
exists on the page, not that the value or the judgement is right.

Statuses (one line per item):
  OK         quote found in the text layer of the cited page
  IMAGE      quote marked `"quote_source": "image"`, not in the text layer, and
             the cited page contains images (or, with an `image_note`, has no
             raster image: vector chart): image-sourced, manual check (not a
             failure). The script cannot read images: it prints the
             `image_note` (where the quote was read) so a reviewer can check it.
  NOT FOUND  quote not on the cited page(s) (or page out of range) - failure
  NO QUOTE   KPI without a quote - failure
Warnings (do not fail unless --strict):
  VALUE?     no number of the KPI `value` appears in its quote
  SHORT      quote under 12 characters, or found more than once on the page
  NO IMAGE_NOTE  image-sourced quote without `image_note`; with --strict it is a
             failure, status NO NOTE (an invented "image" quote cannot pass silently)
  NO RASTER  image-sourced quote with `image_note` on a page without raster images

Normalization: NFKC, ligatures, curly quotes and guillemets, dash variants,
soft hyphens; line-end hyphenation is joined only between letters (so table
cells such as "- - -" are kept); a leading/trailing ellipsis or trailing dash
in the quote is ignored and an inner ellipsis ("..." or "…") is a gap: the
parts must appear in order on the page.

Usage:
    python quote_check.py report.pdf analysis.json [--window 1] [--flags] [--strict]

Requires poppler's `pdftotext` (and `pdfimages` for image-sourced quotes).
Exit codes: 0 all quotes found (warnings and IMAGE items listed);
1 at least one NOT FOUND / NO QUOTE / page out of range (or NO NOTE with --strict);
2 usage, input or tool error; 3 only with --strict: no failure but warnings
(with --strict an image-sourced quote without `image_note` is a failure: exit 1).
"""
import argparse
import json
import re
import shutil
import subprocess
import sys
import unicodedata

LIGATURES = {"ﬀ": "ff", "ﬁ": "fi", "ﬂ": "fl", "ﬃ": "ffi", "ﬄ": "ffl"}
QUOTES = {"’": "'", "‘": "'", "ʼ": "'", "´": "'", "`": "'",
          "“": '"', "”": '"', "„": '"', "«": '"', "»": '"'}
DASHES = "‐‑‒–—―−"  # hyphen, nb-hyphen, figure dash, en, em, bar, minus
ELLIPSIS = re.compile(r"\s*(?:…|\.\.\.+)\s*")
LETTER = r"[^\W\d_]"
MIN_IMAGE_PIXELS = 10000  # ignore tiny decorations (e.g. 100x100 icons and below)


def _base(text):
    text = unicodedata.normalize("NFKC", text)
    for k, v in LIGATURES.items():
        text = text.replace(k, v)
    for k, v in QUOTES.items():
        text = text.replace(k, v)
    for d in DASHES:
        text = text.replace(d, "-")
    return text.replace("­", "")  # soft hyphen


def _squash(text):
    return re.sub(r"\s+", " ", text).strip().lower()


def page_variants(text):
    """Two normalized versions of a page: hyphenation joined (word-\\nword ->
    wordword) and kept (word-\\nword -> word-word). Only between letters."""
    text = _base(text)
    joined = re.sub(rf"(?<={LETTER})-[ \t]*\n\s*(?={LETTER})", "", text)
    kept = re.sub(rf"(?<={LETTER})-[ \t]*\n\s*(?={LETTER})", "-", text)
    return [_squash(joined), _squash(kept)]


def quote_parts(quote):
    """Normalized quote split on inner ellipses; outer ellipses and trailing
    dashes are dropped."""
    q = _squash(_base(quote))
    q = ELLIPSIS.sub("…", q).strip("… ")
    q = re.sub(r"[\s-]+$", "", q)
    return [p.strip() for p in q.split("…") if p.strip()]


def find_in(parts, text):
    """Index of the first part if all parts appear in order, else -1."""
    pos, first = 0, -1
    for p in parts:
        i = text.find(p, pos)
        if i < 0:
            return -1
        first = i if first < 0 else first
        pos = i + len(p)
    return first


def count_in(parts, text):
    if len(parts) != 1:
        return 1 if find_in(parts, text) >= 0 else 0
    return text.count(parts[0])


def run(args):
    return subprocess.run(args, capture_output=True, text=True, check=True).stdout


def page_texts(pdf, layout):
    out = run(["pdftotext"] + (["-layout"] if layout else []) + [pdf, "-"])
    return out.split("\f")


def pages_with_images(pdf):
    """Pages holding at least one non-trivial image (pdfimages -list)."""
    if not shutil.which("pdfimages"):
        return None
    pages = set()
    for line in run(["pdfimages", "-list", pdf]).splitlines()[2:]:
        cols = line.split()
        if len(cols) > 4 and cols[0].isdigit() and cols[3].isdigit() and cols[4].isdigit():
            if int(cols[3]) * int(cols[4]) >= MIN_IMAGE_PIXELS:
                pages.add(int(cols[0]))
    return pages


def pages_of(item, key="page"):
    page = item.get(key)
    pages = page if isinstance(page, list) else [page]
    return [p for p in pages if isinstance(p, int)]  # missing/invalid page -> NOT FOUND


NUM = re.compile(r"\d{1,3}(?:[   ]\d{3})+(?:[.,]\d+)?|\d[\d.,']*\d|\d")


def num_readings(token):
    """Possible numeric readings of a token (IT/EN separators are ambiguous)."""
    t = re.sub(r"[   ']", "", token)
    out = set()
    seps = [c for c in t if c in ".,"]
    if not seps:
        out.add(float(t))
    elif len(set(seps)) == 2:  # both: the last one is the decimal separator
        dec = t[max(t.rfind("."), t.rfind(","))]
        th = "," if dec == "." else "."
        out.add(float(t.replace(th, "").replace(dec, ".")))
    elif len(seps) > 1:  # same separator repeated: thousands
        out.add(float(t.replace(seps[0], "")))
    else:
        head, tail = t.split(seps[0])
        out.add(float(f"{head}.{tail}"))
        if len(tail) == 3:  # 1.396 / 1,249: could be thousands
            out.add(float(head + tail))
    return {round(x, 6) for x in out}


def numbers(text):
    vals = set()
    for tok in NUM.findall(_base(text or "")):
        # "1 262" may be one number (space as thousands separator) or two
        # table cells ("240 233"): keep both readings
        for t in [tok] + (re.split(r"[   ]", tok) if re.search(r"[   ]", tok) else []):
            try:
                vals |= num_readings(t)
            except ValueError:
                continue
    return vals


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pdf")
    ap.add_argument("analysis")
    ap.add_argument("--window", type=int, default=0, help="also accept the quote N pages before/after (default 0)")
    ap.add_argument("--flags", action="store_true",
                    help="also check that pages cited in data_quality_flags and derived_values exist")
    ap.add_argument("--strict", action="store_true", help="exit 3 when there are warnings but no failure")
    a = ap.parse_args()

    try:
        with open(a.analysis, encoding="utf-8") as fh:
            data = json.load(fh)
        raw = [page_texts(a.pdf, True), page_texts(a.pdf, False)]
    except FileNotFoundError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(2)
    except (json.JSONDecodeError, subprocess.CalledProcessError) as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(2)
    n_pages = len(raw[0]) - (1 if raw[0][-1] == "" else 0)  # pdftotext ends each page with \f
    texts = [[v for t in (raw[0][i], raw[1][i]) for v in page_variants(t)] for i in range(n_pages)]
    has_text = [bool(raw[0][i].strip()) for i in range(n_pages)]
    img_pages = None

    items = [("kpi", m.get("name", ""), m) for m in data.get("key_metrics", [])]
    items += [("claim", c.get("claim", ""), c) for c in data.get("greenwashing", {}).get("flagged_claims", [])]

    failed = checked = found = images = warnings = 0
    for kind, label, item in items:
        parts = quote_parts(item.get("quote", "") or "")
        if not parts:
            if kind == "kpi":
                print(f"NO QUOTE  [{kind}] {label}")
                failed += 1
                checked += 1
            continue
        checked += 1
        pages = pages_of(item)
        found_on = None
        for p in pages:
            for q in range(p - a.window, p + a.window + 1):
                if 1 <= q <= n_pages and any(find_in(parts, t) >= 0 for t in texts[q - 1]):
                    found_on = q
                    break
            if found_on:
                break
        notes, warn_img = [], []
        if found_on:
            status = "OK       "
            found += 1
        elif item.get("quote_source") == "image":
            if img_pages is None:
                img_pages = pages_with_images(a.pdf)
            in_range = [p for p in pages if 1 <= p <= n_pages]
            with_img = [p for p in in_range if img_pages is None or p in img_pages]
            note = str(item.get("image_note") or "").strip()
            if with_img or (in_range and note):
                status = "IMAGE    "
                notes.append("image-sourced, manual check" + ("" if img_pages is not None else " (pdfimages not found)"))
                images += 1
                if not with_img:
                    warn_img.append("NO RASTER (no embedded image on the page: vector chart? check the render)")
                if note:
                    notes.append(f"image_note: {note[:120]}")
                elif a.strict:
                    status = "NO NOTE  "
                    notes.append("image-sourced quote without image_note (--strict failure): describe where it was read")
                    images -= 1
                    failed += 1
                else:
                    warn_img.append("NO IMAGE_NOTE (say where in the image the quote was read)")
            else:
                status = "NOT FOUND"
                notes.append("marked image-sourced but no image on the cited page(s) and no image_note")
                failed += 1
        else:
            status = "NOT FOUND"
            failed += 1
            out = [p for p in pages if not 1 <= p <= n_pages]
            empty = [p for p in pages if 1 <= p <= n_pages and not has_text[p - 1]]
            if out:
                notes.append(f"page(s) {out} out of range (document has {n_pages})")
            if empty:
                notes.append(f"page(s) {empty} have no text layer: read visually and mark quote_source 'image'")
            if not pages:
                notes.append("no valid page")
        warn = list(warn_img)
        qlen = len(" ".join(parts))
        if found_on and (qlen < 12 or max(count_in(parts, t) for t in texts[found_on - 1]) > 1):
            warn.append("SHORT" if qlen < 12 else "SHORT (appears more than once on the page)")
        if kind == "kpi":
            vnums = numbers(str(item.get("value", "")))
            if vnums and not (vnums & numbers(item.get("quote", ""))):
                warn.append("VALUE? (value not in quote)")
        warnings += len(warn)
        extra = " - " + "; ".join(notes) if notes else ""
        wtxt = "  [" + ", ".join(warn) + "]" if warn else ""
        print(f"{status} [{kind}] {label} (p.{found_on or item.get('page')}){extra}{wtxt}")

    if a.flags:
        for key, label_key in (("data_quality_flags", "issue"), ("derived_values", "name")):
            for it in data.get(key, []) or []:
                for p in pages_of(it, "pages"):
                    if not 1 <= p <= n_pages:
                        print(f"BAD PAGE  [{key}] {str(it.get(label_key, ''))[:60]} (p.{p} out of range, document has {n_pages})")
                        failed += 1
                    elif not has_text[p - 1]:
                        print(f"NOTE      [{key}] {str(it.get(label_key, ''))[:60]} (p.{p} has no text layer: check visually)")

    print(f"\n{found}/{checked} quotes found in the text layer; {images} image-sourced (manual check); "
          f"{failed} failed; {warnings} warning(s) ({len(items) - checked} claims without a quote skipped). "
          "Automated quote check only - not an adversarial verification.")
    if failed:
        sys.exit(1)
    sys.exit(3 if a.strict and warnings else 0)


if __name__ == "__main__":
    main()
