"""Check new links and the design/publication preservation contract."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import subprocess
import json
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
BASE = 'c89ce28e537fab0678bc8e4e9f232fd4720c3271'
CHANGED = ['index.html', 'papers.html', 'research.html', 'use-cases.html',
           'verticals.html', 'governance.html', 'tools.html']
NEW = ['architecture.html', 'evidence.html', 'frontier.html']

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.links, self.ids, self.downloads = [], set(), []
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            assert attrs['id'] not in self.ids, 'duplicate ID'
            self.ids.add(attrs['id'])
        for key in ('href', 'src'):
            if key in attrs:
                self.links.append(attrs[key])
        if tag == 'a' and 'download' in attrs:
            self.downloads.append(attrs.get('href'))

def original(name):
    return subprocess.check_output(['git', 'show', f'{BASE}:{name}'], cwd=ROOT).decode()

def fragment(text, tag):
    return re.search(rf'<{tag}\b[\s\S]*?</{tag}>', text).group()

errors = []
for name in CHANGED + NEW:
    text = (ROOT / name).read_text()
    page = Page(text)
    before = Page(original(name)) if name in CHANGED else Page('')
    # Existing links can predate this change. Check additions and all new routes.
    links = page.links if name in NEW else [x for x in page.links if x not in before.links]
    for link in links:
        u = urlsplit(link)
        if u.scheme or u.netloc or not u.path and not u.fragment:
            continue
        target = ROOT / unquote(u.path.lstrip('/')) if u.path.startswith('/') else (ROOT / name).parent / unquote(u.path)
        if not u.path:
            target = ROOT / name
        if not target.exists():
            errors.append(f'{name}: missing {link}')
        elif u.fragment and target.suffix == '.html' and u.fragment not in Page(target.read_text()).ids:
            errors.append(f'{name}: missing fragment {link}')
    for raw in re.findall(r'<script type="application/ld\+json"[^>]*>([\s\S]*?)</script>', text):
        json.loads(raw)
    if name in CHANGED:
        old = original(name)
        assert fragment(text, 'header') == fragment(old, 'header'), f'{name}: header changed'
        assert re.findall(r'<style[^>]*>[\s\S]*?</style>', text) == re.findall(r'<style[^>]*>[\s\S]*?</style>', old), f'{name}: inline styles changed'
        assert page.downloads == before.downloads, f'{name}: downloads changed'
    else:
        assert len(re.findall(r'<main>', text)) == 1
        assert fragment(text, 'header') == fragment(original('papers.html'), 'header').replace('class="active" href="/papers.html"', 'href="/papers.html"')

# Append-only research change: original body and measured results remain verbatim.
old_body = original('research.html').split('<main>')[1].split('</main>')[0]
assert old_body in (ROOT / 'research.html').read_text()
for p in ['assets/site.css', 'assets/styles.css', 'assets/main.js']:
    assert (ROOT / p).read_bytes() == subprocess.check_output(['git', 'show', f'{BASE}:{p}'], cwd=ROOT)
protected = subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', BASE, 'publications', 'papers', 'assets'], cwd=ROOT).decode().splitlines()
for p in protected:
    assert (ROOT / p).read_bytes() == subprocess.check_output(['git', 'show', f'{BASE}:{p}'], cwd=ROOT), f'Protected asset changed: {p}'
for p in ['assets/accountable-intelligence-architecture.svg', 'assets/optimization-admissibility.svg', 'sitemap.xml']:
    ET.parse(ROOT / p)
assert not errors, '\n'.join(errors)
print('PASS: new links/fragments, JSON-LD, SVG/XML, unchanged navigation/styles/downloads, original research body and all existing assets/manuscripts.')
