from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGE = "what-is-a-neurosymbolic-decision-machine.html"
PAGE_URL = f"https://neuro-symbolic-decisions.co.za/{PAGE}"


def update_homepage() -> None:
    path = ROOT / "index.html"
    html = path.read_text(encoding="utf-8-sig")
    link = '<a class="button secondary" href="/what-is-a-neurosymbolic-decision-machine.html">What is an NSDM?</a>'
    if link in html:
        return

    anchor = '<a class="button secondary" href="/papers.html">View papers</a>'
    if anchor not in html:
        raise RuntimeError("Homepage button anchor not found")
    html = html.replace(anchor, anchor + "\n        " + link, 1)
    path.write_text(html, encoding="utf-8", newline="\n")


def update_neurosymbolic_page() -> None:
    path = ROOT / "neurosymbolic-ai.html"
    html = path.read_text(encoding="utf-8-sig")
    link = '<a class="button secondary" href="/what-is-a-neurosymbolic-decision-machine.html">Read the NSDM definition</a>'
    if link in html:
        return

    anchor = '<a class="button secondary" href="/research.html">View the research programme</a>'
    if anchor not in html:
        raise RuntimeError("Neuro-symbolic AI button anchor not found")
    html = html.replace(anchor, anchor + "\n    " + link, 1)
    path.write_text(html, encoding="utf-8", newline="\n")


def update_sitemap() -> None:
    path = ROOT / "sitemap.xml"
    xml = path.read_text(encoding="utf-8-sig")
    if PAGE_URL in xml:
        return

    entry = f'''  <url>
    <loc>{PAGE_URL}</loc>
    <lastmod>2026-07-29</lastmod>
    <changefreq>monthly</changefreq>
    <priority>1.0</priority>
  </url>
'''
    closing = "</urlset>"
    if closing not in xml:
        raise RuntimeError("Sitemap closing tag not found")
    xml = xml.replace(closing, entry + closing, 1)
    path.write_text(xml, encoding="utf-8", newline="\n")


def validate() -> None:
    errors: list[str] = []
    category = (ROOT / PAGE).read_text(encoding="utf-8")
    homepage = (ROOT / "index.html").read_text(encoding="utf-8")
    neuro = (ROOT / "neurosymbolic-ai.html").read_text(encoding="utf-8")
    sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")

    checks = {
        "category canonical": f'<link rel="canonical" href="{PAGE_URL}">' in category,
        "defined term schema": '"@type": "DefinedTerm"' in category,
        "article schema": '"@type": "Article"' in category,
        "FAQ schema": '"@type": "FAQPage"' in category,
        "homepage link": '/what-is-a-neurosymbolic-decision-machine.html' in homepage,
        "neuro-symbolic page link": '/what-is-a-neurosymbolic-decision-machine.html' in neuro,
        "sitemap registration": sitemap.count(PAGE_URL) == 1,
        "single H1": len(re.findall(r"<h1(?:\s[^>]*)?>", category)) == 1,
    }
    for label, passed in checks.items():
        if not passed:
            errors.append(label)

    if errors:
        raise RuntimeError("Category-page validation failed:\n" + "\n".join(errors))


if __name__ == "__main__":
    update_homepage()
    update_neurosymbolic_page()
    update_sitemap()
    validate()
    print("NSDM category page registered, internally linked and validated.")
