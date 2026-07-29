from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE_URL = "https://neuro-symbolic-decisions.co.za"
OG_IMAGE = f"{BASE_URL}/assets/nsdm-boundary-monolith-og-1200x630.png"
DATE_MODIFIED = "2026-07-29"

PAGES = {
    "index.html": {
        "url": "/",
        "name": "Neurosymbolic Decision Machines",
        "description": "NSDM stands for Neurosymbolic Decision Machines: AI systems that distinguish capability from evidence-supported, authorised and consequence-aware action.",
        "about": ["Neurosymbolic artificial intelligence", "AI decision assurance", "Justified AI action"],
        "breadcrumb": ["Home"],
    },
    "research.html": {
        "url": "/research.html",
        "name": "NSDM Research",
        "description": "NSDM research on evidence-state, governance-state and action-state boundaries, prospective evaluation, runtime assurance and world-model validity.",
        "about": ["AI research", "Evidence-state decision boundaries", "Runtime assurance"],
        "breadcrumb": ["Home", "Research"],
    },
    "papers.html": {
        "url": "/papers.html",
        "name": "NSDM Papers",
        "description": "Working papers and planned manuscripts from the NSDM Institute on Neurosymbolic Decision Machines, decision boundaries, governance and assurance.",
        "about": ["Research papers", "Neurosymbolic Decision Machines", "AI governance"],
        "breadcrumb": ["Home", "Papers"],
    },
    "neurosymbolic-ai.html": {
        "url": "/neurosymbolic-ai.html",
        "name": "Neuro-Symbolic AI",
        "description": "An accessible explanation of neuro-symbolic AI and how NSDM combines learned perception with explicit evidence, rules, authority and controlled action.",
        "about": ["Neuro-symbolic AI", "Symbolic reasoning", "Machine learning"],
        "breadcrumb": ["Home", "Neuro-Symbolic AI"],
    },
    "use-cases.html": {
        "url": "/use-cases.html",
        "name": "NSDM Use Cases",
        "description": "Role-based NSDM workflows for researchers, AI builders, enterprises, boards and regulators evaluating whether AI decisions are justified.",
        "about": ["AI use cases", "Decision assurance", "Enterprise AI"],
        "breadcrumb": ["Home", "Use Cases"],
    },
    "verticals.html": {
        "url": "/verticals.html",
        "name": "NSDM Industry Verticals",
        "description": "How Neurosymbolic Decision Machines apply evidence, governance and action boundaries across telecoms, finance, retail, industry and public systems.",
        "about": ["Industry AI", "Vertical AI systems", "AI assurance"],
        "breadcrumb": ["Home", "Verticals"],
    },
    "governance.html": {
        "url": "/governance.html",
        "name": "NSDM Governance",
        "description": "NSDM governance methods for evidence sufficiency, authority, consequence, world-state validity, human review and auditable AI action.",
        "about": ["AI governance", "Responsible AI", "Decision accountability"],
        "breadcrumb": ["Home", "Governance"],
    },
    "action-states.html": {
        "url": "/action-states.html",
        "name": "NSDM Action States",
        "description": "NSDM action states define when an AI system should answer, verify, clarify, abstain, refuse, escalate, pause, allow or block.",
        "about": ["AI action states", "Abstention", "Human escalation"],
        "breadcrumb": ["Home", "Action States"],
    },
    "tools.html": {
        "url": "/tools.html",
        "name": "NSDM Tools",
        "description": "Research and assurance tools for NSDM benchmarks, evidence records, deployment gates, decision passports and reproducible AI evaluation.",
        "about": ["AI evaluation tools", "Decision passports", "AI benchmarks"],
        "breadcrumb": ["Home", "Tools"],
    },
}

META_PATTERNS = [
    r'\s*<link rel="canonical"[^>]*>\n?',
    r'\s*<meta property="og:[^"]+"[^>]*>\n?',
    r'\s*<meta name="twitter:[^"]+"[^>]*>\n?',
    r'\s*<meta name="author"[^>]*>\n?',
    r'\s*<meta name="publisher"[^>]*>\n?',
    r'\s*<meta name="robots"[^>]*>\n?',
    r'\s*<script type="application/ld\+json" data-nsdm-seo>.*?</script>\n?',
]


def page_title(html: str, path: str) -> str:
    match = re.search(r"<title>(.*?)</title>", html, flags=re.DOTALL)
    if not match:
        raise RuntimeError(f"Missing title in {path}")
    return re.sub(r"\s+", " ", match.group(1)).strip()


def page_head_description(html: str, fallback: str) -> str:
    match = re.search(r'<meta name="description" content="([^"]*)">', html)
    return match.group(1).strip() if match else fallback


def breadcrumb_items(config: dict[str, object]) -> list[dict[str, object]]:
    labels = config["breadcrumb"]
    assert isinstance(labels, list)
    items = []
    for position, label in enumerate(labels, start=1):
        if position == 1:
            item_url = f"{BASE_URL}/"
        else:
            item_url = f"{BASE_URL}{config['url']}"
        items.append({
            "@type": "ListItem",
            "position": position,
            "name": label,
            "item": item_url,
        })
    return items


def structured_data(config: dict[str, object], title: str, description: str) -> dict[str, object]:
    canonical = f"{BASE_URL}{config['url']}"
    graph: list[dict[str, object]] = [
        {
            "@type": "Organization",
            "@id": f"{BASE_URL}/#organization",
            "name": "MetaForgeX AI (Pty) Ltd",
            "alternateName": "NSDM Institute",
            "url": f"{BASE_URL}/",
            "email": "mailto:rajesh@metaforgexai.co.za",
            "logo": {
                "@type": "ImageObject",
                "url": f"{BASE_URL}/assets/nsdm-boundary-monolith.svg",
            },
            "address": {
                "@type": "PostalAddress",
                "addressLocality": "Johannesburg",
                "addressCountry": "ZA",
            },
            "founder": {"@id": f"{BASE_URL}/#rajesh-singh"},
            "sameAs": [
                "https://www.linkedin.com/in/rajesh-singh-78a419",
                "https://github.com/Rajesh0311",
            ],
        },
        {
            "@type": "Person",
            "@id": f"{BASE_URL}/#rajesh-singh",
            "name": "Rajesh Singh",
            "url": f"{BASE_URL}/",
            "email": "mailto:rajesh@metaforgexai.co.za",
            "jobTitle": "Founder and Research Lead",
            "worksFor": {"@id": f"{BASE_URL}/#organization"},
            "sameAs": [
                "https://www.linkedin.com/in/rajesh-singh-78a419",
                "https://github.com/Rajesh0311",
            ],
        },
        {
            "@type": "WebSite",
            "@id": f"{BASE_URL}/#website",
            "url": f"{BASE_URL}/",
            "name": "NSDM Institute",
            "alternateName": "Neurosymbolic Decision Machines",
            "publisher": {"@id": f"{BASE_URL}/#organization"},
            "inLanguage": "en-ZA",
        },
        {
            "@type": "WebPage",
            "@id": f"{canonical}#webpage",
            "url": canonical,
            "name": title,
            "description": description,
            "isPartOf": {"@id": f"{BASE_URL}/#website"},
            "about": [{"@type": "Thing", "name": item} for item in config["about"]],
            "author": {"@id": f"{BASE_URL}/#rajesh-singh"},
            "publisher": {"@id": f"{BASE_URL}/#organization"},
            "primaryImageOfPage": {"@type": "ImageObject", "url": OG_IMAGE},
            "dateModified": DATE_MODIFIED,
            "inLanguage": "en-ZA",
        },
    ]
    if len(config["breadcrumb"]) > 1:
        graph.append({
            "@type": "BreadcrumbList",
            "@id": f"{canonical}#breadcrumb",
            "itemListElement": breadcrumb_items(config),
        })
        graph[3]["breadcrumb"] = {"@id": f"{canonical}#breadcrumb"}
    return {"@context": "https://schema.org", "@graph": graph}


def metadata_block(config: dict[str, object], title: str, description: str) -> str:
    canonical = f"{BASE_URL}{config['url']}"
    data = structured_data(config, title, description)
    json_ld = json.dumps(data, ensure_ascii=False, indent=2)
    image_alt = "NSDM Institute Boundary Monolith identity"
    return f'''  <link rel="canonical" href="{canonical}">
  <meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
  <meta name="author" content="Rajesh Singh">
  <meta name="publisher" content="MetaForgeX AI (Pty) Ltd · NSDM Institute">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="NSDM Institute">
  <meta property="og:locale" content="en_ZA">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{OG_IMAGE}">
  <meta property="og:image:secure_url" content="{OG_IMAGE}">
  <meta property="og:image:type" content="image/png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="{image_alt}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{description}">
  <meta name="twitter:image" content="{OG_IMAGE}">
  <meta name="twitter:image:alt" content="{image_alt}">
  <script type="application/ld+json" data-nsdm-seo>
{json_ld}
  </script>'''


def clean_existing_authority_tags(html: str) -> str:
    for pattern in META_PATTERNS:
        html = re.sub(pattern, "\n", html, flags=re.DOTALL)
    return html


def apply(path: str, config: dict[str, object]) -> None:
    file_path = ROOT / path
    html = file_path.read_text(encoding="utf-8-sig")
    title = page_title(html, path)
    description = page_head_description(html, str(config["description"]))
    html = clean_existing_authority_tags(html)

    description_tag = re.search(r'  <meta name="description" content="[^"]*">', html)
    if not description_tag:
        raise RuntimeError(f"Missing meta description in {path}")

    block = metadata_block(config, title, description)
    insertion_point = description_tag.end()
    html = html[:insertion_point] + "\n" + block + html[insertion_point:]
    html = re.sub(r"\n{3,}", "\n\n", html)
    file_path.write_text(html, encoding="utf-8", newline="\n")


def validate() -> None:
    errors: list[str] = []
    for path, config in PAGES.items():
        html = (ROOT / path).read_text(encoding="utf-8")
        canonical = f'{BASE_URL}{config["url"]}'
        checks = {
            "canonical": html.count(f'<link rel="canonical" href="{canonical}">') == 1,
            "og_url": html.count(f'<meta property="og:url" content="{canonical}">') == 1,
            "json_ld": html.count('type="application/ld+json" data-nsdm-seo') == 1,
            "organization": '"@type": "Organization"' in html,
            "person": '"@type": "Person"' in html,
            "website": '"@type": "WebSite"' in html,
            "webpage": '"@type": "WebPage"' in html,
        }
        for label, passed in checks.items():
            if not passed:
                errors.append(f"{path}: failed {label}")
        if len(config["breadcrumb"]) > 1 and '"@type": "BreadcrumbList"' not in html:
            errors.append(f"{path}: failed breadcrumb")
    if errors:
        raise RuntimeError("SEO validation failed:\n" + "\n".join(errors))


if __name__ == "__main__":
    for page_path, page_config in PAGES.items():
        apply(page_path, page_config)
    validate()
    print("NSDM SEO authority layer applied and validated across 9 public pages.")
