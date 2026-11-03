"""Salva as figuras estáticas da Q1 em figuras/ (precisa do playwright e do
Chromium: pip install playwright; python -m playwright install chromium).

Uso, a partir da raiz do repositório: python scripts/capturas_q1.py .
"""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

raiz = Path(sys.argv[1]).resolve()
url = (raiz / "vis" / "q1.html").as_uri()
saida = raiz / "figuras"

CAPTURAS = [
    ("Bach. Ciências de Computação", "SCC0202", "q1_bcc_aed1.png"),
    ("Engenharia de Computação", "SEL0637", "q1_ecomp_sel0637.png"),
]

with sync_playwright() as p:
    nav = p.chromium.launch()
    pag = nav.new_page(viewport={"width": 1300, "height": 900}, device_scale_factor=2)
    erros = []
    pag.on("requestfailed", lambda r: erros.append(r.url))
    pag.goto(url, wait_until="networkidle")
    if not pag.evaluate("typeof Plotly !== 'undefined'"):
        print("ERRO: plotly.js não carregou do CDN", erros)
        sys.exit(2)
    opcoes = pag.eval_on_selector_all("select.curso option", "os => os.map(o => [o.value, o.textContent])")
    print("cursos:", opcoes)
    for nome, sigla, arquivo in CAPTURAS:
        valor = next((v for v, t in opcoes if t.strip() == nome), None) \
            or next(v for v, t in opcoes if nome.lower() in t.lower())
        if pag.input_value("select.curso") != valor:
            pag.select_option("select.curso", valor)
        pag.wait_for_function(
            "s => document.querySelector('.t2').textContent.includes('Reprovar em ' + s)", arg=sigla)
        # espera os dois gráficos terem conteúdo e a renderização assentar
        pag.wait_for_function("document.querySelectorAll('.v1 .main-svg, .v2 .main-svg').length >= 2")
        pag.wait_for_timeout(800)
        topo = pag.evaluate("document.querySelector('.v1 .ytick b')?.textContent || ''")
        print(arquivo, "| título:", pag.text_content(".t2"), "| barra marcada:", topo)
        # recorta só o painel (o div que contém os controles e os gráficos)
        pag.locator("div:has(> .ctl)").first.screenshot(path=str(saida / arquivo))
    nav.close()
