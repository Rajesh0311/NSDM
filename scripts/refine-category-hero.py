from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "what-is-a-neurosymbolic-decision-machine.html"

STYLE_BLOCK = '''  <style data-nsdm-category-hero>
    .definition-hero {
      max-width: var(--max);
      margin: 0 auto;
      padding: 76px 24px 54px;
    }

    .definition-hero > * {
      max-width: 980px;
    }

    .definition-hero h1 {
      max-width: 15ch;
      font-size: clamp(44px, 6vw, 68px);
      line-height: 1.01;
      letter-spacing: -.055em;
      text-wrap: balance;
    }

    .definition-hero .lead {
      max-width: 760px;
    }

    .definition-hero .button-row {
      max-width: 900px;
    }

    @media (max-width: 620px) {
      .definition-hero {
        padding: 48px 18px 34px;
      }

      .definition-hero h1 {
        max-width: none;
        font-size: clamp(34px, 10vw, 44px);
      }
    }
  </style>'''


def main() -> None:
    html = PAGE.read_text(encoding="utf-8-sig")

    if '<section class="hero definition-hero">' not in html:
        if '<section class="hero">' not in html:
            raise RuntimeError("Category hero section was not found.")
        html = html.replace(
            '<section class="hero">',
            '<section class="hero definition-hero">',
            1,
        )

    if 'data-nsdm-category-hero' not in html:
        anchor = '  <link rel="stylesheet" href="/assets/site.css">'
        if anchor not in html:
            raise RuntimeError("Stylesheet anchor was not found.")
        html = html.replace(anchor, anchor + "\n" + STYLE_BLOCK, 1)

    PAGE.write_text(html, encoding="utf-8", newline="\n")

    result = PAGE.read_text(encoding="utf-8")
    checks = {
        "hero class": '<section class="hero definition-hero">' in result,
        "scoped style": 'data-nsdm-category-hero' in result,
        "headline width": 'max-width: 15ch;' in result,
        "lead width": 'max-width: 760px;' in result,
        "mobile rule": '@media (max-width: 620px)' in result,
    }
    failed = [name for name, passed in checks.items() if not passed]
    if failed:
        raise RuntimeError("Category hero validation failed: " + ", ".join(failed))

    print("NSDM category hero alignment refined and validated.")


if __name__ == "__main__":
    main()
