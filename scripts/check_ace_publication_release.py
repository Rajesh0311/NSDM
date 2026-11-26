"""Validate this publication increment and preserve pre-existing research/assets."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import subprocess,re,json,hashlib,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
BASE='d4ee1f7f0106e5c4fd731899331a1dcfb5f8bf17'
CHANGED=['index.html','programme.html','evidence.html','papers.html','research.html']
NEW=['observation-cost.html','preserving-unknown.html','machine-earns-speed.html','cheapest-answer-open.html','unknown-scored-103.html']
class Page(HTMLParser):
 def __init__(self,text):
  super().__init__();self.ids=set();self.links=[];self.main=0;self.feed(text)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id'in a:
   assert a['id']not in self.ids,'duplicate ID '+a['id'];self.ids.add(a['id'])
  if tag=='main':self.main+=1
  for k in ['href','src']:
   if k in a:self.links.append(a[k])
def original(p):return subprocess.check_output(['git','show',BASE+':'+p],cwd=ROOT)
def header(t):return re.search(r'<header>[\s\S]*?</header>',t).group()
errors=[]
for name in CHANGED+NEW:
 text=(ROOT/name).read_text();page=Page(text);assert page.main==1
 before=original(name).decode()if name in CHANGED else None
 if before:
  assert header(text)==header(before),name+' header changed'
  assert re.findall(r'<style[^>]*>[\s\S]*?</style>',text)==re.findall(r'<style[^>]*>[\s\S]*?</style>',before)
 for link in page.links:
  u=urlsplit(link)
  if u.scheme or u.netloc:continue
  p=ROOT/unquote(u.path.lstrip('/'))if u.path else ROOT/name
  if not p.exists():errors.append(name+': missing '+link)
  elif u.fragment and p.suffix=='.html'and u.fragment not in Page(p.read_text()).ids:errors.append(name+': missing anchor '+link)
 for raw in re.findall(r'<script type="application/ld\+json"[^>]*>([\s\S]*?)</script>',text):json.loads(raw)
 # Check preserved existing research paragraphs as whole text, including null results.
 if name=='research.html':
  assert before.split('<main>')[1].split('</main>')[0]in text,'original research body changed'
for p in ['assets/site.css','assets/styles.css','assets/main.js']:
 assert (ROOT/p).read_bytes()==original(p),p+' changed'
protected=subprocess.check_output(['git','ls-tree','-r','--name-only',BASE,'assets','papers','publications'],cwd=ROOT).decode().splitlines()
for p in protected:assert (ROOT/p).read_bytes()==original(p),'existing artifact changed '+p
ET.parse(ROOT/'sitemap.xml')
cat=json.loads((ROOT/'publications/ace-2026-11-26/catalogue.json').read_text());assert len(cat['items'])==5
for r in cat['items']:
 assert (ROOT/r['manuscript']).is_file()
 if r['pdf']:assert (ROOT/r['pdf']).read_bytes().startswith(b'%PDF')
assert not errors,'\n'.join(errors)
print('PASS: all reader/local links and anchors, metadata, PDF signatures, XML, five catalogue records; original headers/styles/research body and all existing assets/manuscripts preserved.')
print('Scope: static validation; no browser layout or assistive-technology execution.')
