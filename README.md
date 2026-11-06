# Grade do ICMC como rede

Projeto da disciplina SCC0252 (Visualização Computacional, ICMC-USP, 2026/2). Ele trata a grade curricular dos cursos do ICMC como uma rede de pré-requisitos, com dados do JúpiterWeb coletados em 31/10/2026.

**Autores:** Letícia Raddatz Jönck, Rodrigo Li e Victor Moreli dos Santos
**Professor:** Jean R. Ponciano

## Links

- [Site com as visualizações](https://vmoreli.github.io/viscomp-projeto/) (menu com todas)
- [Q1: atraso por reprovação](https://vmoreli.github.io/viscomp-projeto/vis/q1.html)
- [Notebook da Q1 no nbviewer](https://nbviewer.org/github/vmoreli/viscomp-projeto/blob/main/notebooks/02_q1_atraso_reprovacao.ipynb)
- [Notebook da Q1 no Colab](https://colab.research.google.com/github/vmoreli/viscomp-projeto/blob/main/notebooks/02_q1_atraso_reprovacao.ipynb)
- [Q2: horários da semana](https://vmoreli.github.io/viscomp-projeto/vis/q2.html)
- [Notebook da Q2 no nbviewer](https://nbviewer.org/github/vmoreli/viscomp-projeto/blob/main/notebooks/03_q2_horarios.ipynb)
- [Notebook da Q2 no Colab](https://colab.research.google.com/github/vmoreli/viscomp-projeto/blob/main/notebooks/03_q2_horarios.ipynb)
- [Q3: optativas disponíveis](https://vmoreli.github.io/viscomp-projeto/vis/q3.html)
- [Notebook da Q3 no nbviewer](https://nbviewer.org/github/vmoreli/viscomp-projeto/blob/main/notebooks/04_q3_optativas.ipynb)
- [Notebook da Q3 no Colab](https://colab.research.google.com/github/vmoreli/viscomp-projeto/blob/main/notebooks/04_q3_optativas.ipynb)

## Como rodar localmente

```bash
pip install -r requirements.txt
jupyter notebook notebooks/
```

Os notebooks `02_q1_atraso_reprovacao.ipynb`, `03_q2_horarios.ipynb` e `04_q3_optativas.ipynb` leem os CSVs de `dados/processado` e gravam `q1_interativo.html`, `q2_interativo.html` e `q3_interativo.html` na pasta `notebooks/`.

## Como publicar uma visualização no site

O site tem uma página inicial (`index.html`) e uma página por visualização em `vis/`. O menu do topo e os cartões da página inicial vêm da lista `VISUALIZACOES` em `menu.js`.

1. Rode o notebook que gera o HTML da visualização (ex.: `notebooks/q1_interativo.html`).
2. Na raiz do repositório, gere a página:
   `python scripts/publicar_vis.py notebooks/q1_interativo.html q1 "Grade do ICMC como rede: Q1"`
3. Se a visualização for nova, adicione um item em `VISUALIZACOES` no `menu.js` (id, arquivo, rótulo, título, descrição e, se houver, uma figura).
4. Faça commit e push; o GitHub Pages atualiza sozinho.

## Pastas

| Pasta | Conteúdo |
|---|---|
| `index.html` | Página inicial do site (GitHub Pages), com o menu das visualizações |
| `menu.js` | Lista das visualizações; monta o menu do topo e os cartões da página inicial |
| `vis/` | Uma página por visualização (`q1.html`, `q2.html`, `q3.html`, …) |
| `scripts/` | `publicar_vis.py` (gera as páginas de `vis/`) e `capturas_q1.py`, `capturas_q2.py` e `capturas_q3.py` (geram as figuras com Playwright) |
| `notebooks/01_criacao_dataset.ipynb` | Coleta no JúpiterWeb, limpeza e geração das tabelas |
| `notebooks/02_q1_atraso_reprovacao.ipynb` | Q1: quanto uma reprovação em obrigatória atrasa o curso |
| `notebooks/03_q2_horarios.ipynb` | Q2: quando há aula, por curso e semestre ideal, e se refazer uma reprovada choca |
| `notebooks/04_q3_optativas.ipynb` | Q3: a partir de que semestre o aluno consegue cursar cada optativa |
| `dados/bruto/` | `disciplinas_brutas.json`: dados de cada disciplina como vieram do scraper |
| `dados/processado/` | As 11 tabelas finais em CSV (descritas abaixo) |
| `figuras/` | Figuras estáticas para o relatório: Q1 (`q1_bcc_aed1.png`, `q1_ecomp_sel0637.png`) , Q2 (`q2_visao_geral.png`, `q2_bsi_refazer_scc0502.png`) e Q3 (`q3_bcc_scc0270.png`, `q3_bcd_optativas.png`) |

## Tabelas de `dados/processado`

| Tabela | Uma linha por… |
|---|---|
| `cursos.csv` | curso/habilitação (código, nome, URL da grade) |
| `grade_curricular.csv` | disciplina na grade de um curso (tipo de vínculo, semestre ideal, créditos) |
| `requisitos.csv` | relação de pré-requisito entre duas disciplinas num curso (com grupos de alternativas) |
| `periodo_ideal.csv` | período ideal de uma disciplina num curso |
| `disciplinas.csv` | disciplina (nome, unidade, departamento, créditos, ementa, programa, avaliação…) |
| `docentes.csv` | docente (nome, nº USP, nº de disciplinas) |
| `disciplina_docente.csv` | vínculo docente–disciplina (responsável ou professor de turma) |
| `oferecimentos.csv` | turma oferecida (datas, tipo, observações) |
| `horarios.csv` | horário de aula de uma turma (dia, início, fim, professor) |
| `vagas.csv` | vagas de uma turma por tipo e curso (vagas, inscritos, pendentes, matriculados) |
| `bibliografia.csv` | referência bibliográfica de uma disciplina |

## Observação sobre o cache

A pasta `dados/cache_html/` (~70 MB de páginas do JúpiterWeb salvas na coleta) não está no repositório. O `01_criacao_dataset.ipynb` a recria ao rodar. Uma coleta nova pode trazer dados diferentes dos publicados aqui, além de uma nova data de coleta.
