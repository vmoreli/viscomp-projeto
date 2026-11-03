# Grade do ICMC como rede

Projeto da disciplina SCC0252 (Visualização Computacional, ICMC-USP, 2026/2). Ele trata a grade curricular dos cursos do ICMC como uma rede de pré-requisitos, com dados do JúpiterWeb coletados em 31/10/2026.

**Autores:** Letícia Raddatz Jönck, Rodrigo Li e Victor Moreli dos Santos
**Professor:** Jean R. Ponciano

## Links

- Visualização interativa (Q1): https://vmoreli.github.io/viscomp-projeto/
- Notebook da Q1 no nbviewer: https://nbviewer.org/github/vmoreli/viscomp-projeto/blob/main/notebooks/02_q1_atraso_reprovacao.ipynb
- Notebook da Q1 no Colab: https://colab.research.google.com/github/vmoreli/viscomp-projeto/blob/main/notebooks/02_q1_atraso_reprovacao.ipynb

## Como rodar localmente

```bash
pip install -r requirements.txt
jupyter notebook notebooks/
```

O `02_q1_atraso_reprovacao.ipynb` lê os CSVs de `dados/processado` e grava `q1_interativo.html` na pasta `notebooks/`. A cópia publicada no GitHub Pages é o `index.html` da raiz.

## Pastas

| Pasta | Conteúdo |
|---|---|
| `index.html` | Visualização interativa da Q1 (GitHub Pages) |
| `notebooks/01_criacao_dataset.ipynb` | Coleta no JúpiterWeb, limpeza e geração das tabelas |
| `notebooks/02_q1_atraso_reprovacao.ipynb` | Q1: quanto uma reprovação em obrigatória atrasa o curso |
| `dados/bruto/` | `disciplinas_brutas.json`: dados de cada disciplina como vieram do scraper |
| `dados/processado/` | As 11 tabelas finais em CSV (descritas abaixo) |
| `figuras/` | Figuras estáticas para o relatório |

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
