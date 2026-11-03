"""Gera a página de uma visualização para o site (GitHub Pages).

Pega o HTML que o notebook grava (ex.: notebooks/q1_interativo.html), coloca-o
numa página completa com o menu de navegação (menu.js) e salva em vis/<id>.html.

Uso, a partir da raiz do repositório:
    python scripts/publicar_vis.py notebooks/q1_interativo.html q1 "Grade do ICMC como rede: Q1"

Depois, se a visualização for nova, adicione um item em VISUALIZACOES no menu.js.
"""
import re
import sys
from pathlib import Path

MODELO = """<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo}</title>
<script src="../menu.js" data-atual="{id}"></script>
<style>body {{ margin: 0; background: #fcfcfb; }} main {{ padding: 8px 8px 24px; }}</style>
</head>
<body>
<main>
{conteudo}
</main>
</body>
</html>
"""


def conteudo_da_pagina(html: str) -> str:
    """Devolve só o conteúdo visível: o miolo do <body> ou o que vem depois do <title>."""
    corpo = re.search(r"<body[^>]*>(.*)</body>", html, flags=re.S | re.I)
    if corpo:
        return corpo.group(1).strip()
    return re.sub(r"^.*?</title>", "", html, count=1, flags=re.S | re.I).strip()


def main() -> None:
    origem, id_vis, titulo = sys.argv[1], sys.argv[2], sys.argv[3]
    html = Path(origem).read_text(encoding="utf-8")
    destino = Path("vis") / f"{id_vis}.html"
    destino.parent.mkdir(exist_ok=True)
    destino.write_text(MODELO.format(titulo=titulo, id=id_vis,
                                     conteudo=conteudo_da_pagina(html)),
                       encoding="utf-8", newline="\n")
    print("gravado:", destino)


if __name__ == "__main__":
    main()
