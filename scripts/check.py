"""Check the pilot's public asset contract without third-party dependencies."""
from pathlib import Path
from html.parser import HTMLParser
import re
import json
import hashlib
import xml.etree.ElementTree as ET
ROOT = Path(__file__).resolve().parents[1]
catalog=json.loads((ROOT/'catalog.json').read_text())
expected={i['name'] for i in catalog}
core=json.loads((ROOT/'scripts/core-icons.json').read_text())
N=len(catalog)
assert len(core)==40 and set(core)<=expected, 'Core icons missing'
assert N==len(expected)>=40
assert all(re.fullmatch(r'[a-z]+(?:-[a-z]+)*',name) for name in expected)
for file,digest in json.loads((ROOT/'scripts/pilot-sha256.json').read_text()).items():
 assert hashlib.sha256((ROOT/file).read_bytes()).hexdigest()==digest, f'Pilot modified: {file}'
styles={i['name']: i.get('styles',['outline','heraldic']) for i in catalog}
assert all(s and set(s)<={'outline','heraldic'} for s in styles.values())
assert all(len(styles[n])==2 for n in core), 'Core icons keep both styles'
for i in catalog:
 if 'credit' in i:
  c=i['credit']; assert c['url'].startswith('https://') and c['author'] and c['license'], i['name']
  assert c['author'] in (ROOT/'icons/heraldic'/(i['name']+'.svg')).read_text(), i['name']
V=sum(len(s) for s in styles.values())
for style in ('outline', 'heraldic'):
 paths=list((ROOT/'icons'/style).glob('*.svg'))
 assert {p.stem for p in paths} == {n for n,s in styles.items() if style in s}, style
 for p in paths:
  assert 'lannitacodes.tumblr.com' in p.read_text(), f'Missing credit comment: {p}'
  svg=ET.fromstring(p.read_text())
  assert svg.get('viewBox') == '0 0 64 64', p
  ids={el.get('id') for el in svg.iter() if el.get('id')}
  for el in svg.iter():
   assert el.tag.split('}')[-1] not in ('script','image','foreignObject'), p
   for value in el.attrib.values():
    for ref in re.findall(r'url\(#([^)]*)\)', value): assert ref in ids, (p,ref)
class Gallery(HTMLParser):
 def __init__(self): super().__init__(); self.variants=0; self.downloads=0; self.ids=[]
 def handle_starttag(self, tag, attrs):
  attrs=dict(attrs)
  if tag=='svg': self.variants+=1
  if 'id' in attrs: self.ids.append(attrs['id'])
  if 'download' in attrs: self.downloads+=1
  for attr in ('src','href'):
   value=attrs.get(attr)
   if value and not value.startswith(('#','https://')):
    assert (ROOT/value.split('#')[0]).is_file(), value
gallery=Gallery(); gallery.feed((ROOT/'index.html').read_text())
assert gallery.variants==gallery.downloads==V
assert len(gallery.ids)==len(set(gallery.ids))
css=ROOT/'css/lannita-icons.css'
for url in re.findall(r'url\("([^"]*)"\)',css.read_text()): assert (css.parent/url).is_file(),url
print(f'OK: {N} icons (40 core), {V} valid SVGs, mask IDs, {V} previews/downloads and local HTML/CSS paths.')

comparison=Gallery(); comparison.feed((ROOT/'comparison.html').read_text())
assert (ROOT/'assets/brand/og-image.png').is_file(), 'Missing social preview image'
assert comparison.variants==4*V
assert len(comparison.ids)==len(set(comparison.ids))
assert len(re.findall(r'--li-icon:url',css.read_text()))==V
print(f'OK: approved pilot baseline verified; comparison includes {4*V} renders with unique IDs.')
