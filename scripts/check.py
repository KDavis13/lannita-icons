"""Check the pilot's public asset contract without third-party dependencies."""
from pathlib import Path
from html.parser import HTMLParser
import re
import xml.etree.ElementTree as ET
ROOT = Path(__file__).resolve().parents[1]
expected=set('crown shield swords raven scroll castle coins key quill dice'.split())
for style in ('outline', 'heraldic'):
 paths=list((ROOT/'icons'/style).glob('*.svg'))
 assert {p.stem for p in paths} == expected
 for p in paths:
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
   if attr in attrs: assert (ROOT/attrs[attr]).is_file(), attrs[attr]
gallery=Gallery(); gallery.feed((ROOT/'index.html').read_text())
assert gallery.variants==gallery.downloads==20
assert len(gallery.ids)==len(set(gallery.ids))
css=ROOT/'css/lannita-icons.css'
for url in re.findall(r'url\("([^"]*)"\)',css.read_text()): assert (css.parent/url).is_file(),url
print('OK: 10 pairs, 20 valid SVGs, mask IDs, 20 previews/downloads and local HTML/CSS paths.')
