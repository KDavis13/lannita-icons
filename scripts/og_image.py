"""Render assets/brand/og-image.png (1200x630), the preview shown when the gallery link is shared.

Optional helper: needs Python Playwright with Chromium. Run after adding icons:
    python3 scripts/og_image.py
"""
from pathlib import Path
import json
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
catalog = json.loads((ROOT/'catalog.json').read_text())
picks = ['crown', 'jouster-right', 'castle', 'raven', 'shield-wall', 'scroll', 'dice', 'trebuchet', 'knight', 'archer', 'treasure-chest', 'potion']
icons = ''.join(f'<div class="i">{(ROOT/f"icons/{style}/{name}.svg").read_text()}</div>'
                for k, name in enumerate(picks) for style in [('heraldic', 'outline')[k % 2]])
logo = (ROOT/'assets/brand/lannita-logo.svg').as_uri()
html = f'''<html><body style="margin:0;width:1200px;height:630px;background:#141416;color:#ede7da;font-family:'Segoe UI',system-ui,sans-serif;display:flex;flex-direction:column;justify-content:center;padding:0 90px;box-sizing:border-box">
<img src="{logo}" style="width:300px">
<h1 style="font-size:64px;line-height:1.05;letter-spacing:-.045em;margin:34px 0 18px;font-weight:650">Pequeños símbolos.<br>Grandes historias.</h1>
<p style="color:#aaa497;font-size:24px;margin:0 0 40px">{len(catalog)} iconos SVG gratuitos para foros de rol medieval y fantasía</p>
<div style="display:flex;gap:26px;color:#b48a3c">{icons}</div>
<style>.i svg{{width:60px;height:60px}}</style></body></html>'''
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={'width': 1200, 'height': 630})
    tmp = ROOT/'.og-preview.html'
    tmp.write_text(html)
    page.goto(tmp.as_uri())
    tmp.unlink()
    page.wait_for_timeout(200)
    page.screenshot(path=str(ROOT/'assets/brand/og-image.png'))
    browser.close()
print('Generated assets/brand/og-image.png')
