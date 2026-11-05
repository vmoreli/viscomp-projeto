"""Salva as figuras estáticas da Q2 em figuras/ (precisa do playwright e do
Chromium: pip install playwright; python -m playwright install chromium).

Uso, a partir da raiz do repositório: python scripts/capturas_q2.py .
Sem internet, aponte PLOTLY_JS para uma cópia local do plotly.min.js 2.35.2.
"""
import os
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

raiz = Path(sys.argv[1]).resolve()
url = (raiz / "vis" / "q2.html").as_uri()
saida = raiz / "figuras"

# (arquivo, curso no menu, semestre, medida, disciplina refeita)
CAPTURAS = [
    ("q2_visao_geral.png", "geral", "todos", "alunos", ""),
    ("q2_bsi_refazer_scc0502.png", "Bach. Sistemas de Informação", "4", "disc", "SCC0502"),
]

with sync_playwright() as p:
    nav = p.chromium.launch()
    pag = nav.new_page(viewport={"width": 1300, "height": 900}, device_scale_factor=2)
    if os.environ.get("PLOTLY_JS"):
        pag.route("**/plotly.min.js", lambda r: r.fulfill(path=os.environ["PLOTLY_JS"],
                                                          content_type="application/javascript"))
    pag.goto(url, wait_until="networkidle")
    if not pag.evaluate("typeof Plotly !== 'undefined'"):
        print("ERRO: plotly.js não carregou do CDN")
        sys.exit(2)
    # a barra do menu é fixa no topo e cobriria o recorte
    pag.add_style_tag(content=".menu-vis { display: none !important; }")
    opcoes = pag.eval_on_selector_all("select.curso option", "os => os.map(o => [o.value, o.textContent])")
    for arquivo, curso, nivel, medida, refazer in CAPTURAS:
        valor = curso if curso == "geral" else next(v for v, t in opcoes if t.strip() == curso)
        pag.select_option("select.curso", valor)
        if curso != "geral":
            pag.select_option("select.nivel", nivel)
        pag.click(f".grp[data-k=medida] button[data-v={medida}]")
        if refazer:
            pag.select_option("select.refazer", refazer)
        pag.wait_for_timeout(800)
        print(arquivo, "|", pag.text_content(".resumo"))
        pag.locator("div:has(> .ctl)").first.screenshot(path=str(saida / arquivo))
    nav.close()
