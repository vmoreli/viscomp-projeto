"""Salva as figuras estáticas da Q3 em figuras/ (precisa do playwright e do
Chromium: pip install playwright; python -m playwright install chromium).

Uso, a partir da raiz do repositório: python scripts/capturas_q3.py .
"""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

raiz = Path(sys.argv[1]).resolve()
url = (raiz / "vis" / "q3.html").as_uri()
saida = raiz / "figuras"

# (arquivo, curso no menu, semestre, aba da lista, optativa selecionada)
CAPTURAS = [
    ("q3_bcc_scc0270.png", "Bach. Ciências de Computação", 3, "nao", "SCC0270"),
    ("q3_bcd_optativas.png", "Bach. Ciência de Dados", 5, "sim", None),
]

with sync_playwright() as p:
    nav = p.chromium.launch()
    pag = nav.new_page(viewport={"width": 1300, "height": 1000}, device_scale_factor=2)
    pag.goto(url, wait_until="networkidle")
    if not pag.evaluate("typeof Plotly !== 'undefined'"):
        print("ERRO: plotly.js não carregou do CDN")
        sys.exit(2)
    pag.add_style_tag(content=".menu-vis { position: static !important; }")
    for arquivo, curso, semestre, aba, optativa in CAPTURAS:
        pag.select_option("select.curso", label=curso)
        pag.locator("input.sem").evaluate(
            "(el, v) => { el.value = v; el.dispatchEvent(new Event('input')); }", semestre)
        pag.click(f".abas button[data-v={aba}]")
        if optativa:
            pag.click(f"button.op[data-s={optativa}]")
        pag.mouse.move(0, 0)
        pag.wait_for_timeout(500)
        print(arquivo, "|", pag.text_content(".resumo"))
        pag.locator("div:has(> .ctl)").first.screenshot(path=str(saida / arquivo))
    nav.close()
