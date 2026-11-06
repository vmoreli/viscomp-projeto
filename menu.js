// Lista das visualizações do projeto. Para adicionar uma nova, inclua um item aqui
// e gere a página com scripts/publicar_vis.py. A barra de navegação de todas as
// páginas e os cartões do index.html são montados a partir desta lista.
const VISUALIZACOES = [
  {
    id: "q1",
    arquivo: "vis/q1.html",
    rotulo: "Q1 · Atraso por reprovação",
    titulo: "Se eu reprovar em uma obrigatória, quanto isso me atrasa?",
    descricao: "Para cada curso, quantas disciplinas são adiadas e quanto a formatura " +
      "atrasa quando o aluno reprova em cada obrigatória, e por onde a cascata de " +
      "pré-requisitos se propaga.",
    figura: "figuras/q1_bcc_aed1.png",
  },
  {
    id: "q2",
    arquivo: "vis/q2.html",
    rotulo: "Q2 · Horários da semana",
    titulo: "Quando há aula, e a grade de cada semestre cabe na semana?",
    descricao: "Mapa de calor dia × hora das turmas de 2026/2, filtrável por curso, " +
      "semestre ideal e tipo de disciplina, com simulação de reprovação para ver " +
      "se refazer uma obrigatória choca com o semestre seguinte.",
    figura: "figuras/q2_visao_geral.png",
  },
  {
    id: "q3",
    arquivo: "vis/q3.html",
    rotulo: "Q3 · Optativas disponíveis",
    titulo: "A partir de que semestre eu consigo cursar cada optativa?",
    descricao: "Para cada curso e semestre, quantas e quais optativas o aluno já pode " +
      "cursar, com a sequência mínima de disciplinas até cada uma.",
    figura: "figuras/q3_bcc_scc0270.png",
  },
];

(function () {
  const script = document.currentScript;
  const base = new URL(".", script.src);          // raiz do site, onde está o menu.js
  const atual = script.dataset.atual || "inicio";  // id da página atual
  const url = (caminho) => new URL(caminho, base).href;

  const css = `
    .menu-vis { position: sticky; top: 0; z-index: 10; display: flex; flex-wrap: wrap;
      align-items: center; gap: 6px 20px; padding: 10px 16px; background: #fcfcfb;
      border-bottom: 1px solid #e1e0d9; font: 14px Inter, Arial, sans-serif; }
    .menu-vis a { color: #52514e; text-decoration: none; }
    .menu-vis .marca { font-weight: 600; color: #0b0b0b; }
    .menu-vis nav { display: flex; flex-wrap: wrap; gap: 4px; }
    .menu-vis nav a { padding: 4px 10px; border-radius: 4px; }
    .menu-vis nav a:hover { background: #efeee8; color: #0b0b0b; }
    .menu-vis nav a[aria-current="page"] { background: #2a78d6; color: white; }`;

  function barra() {
    const estilo = document.createElement("style");
    estilo.textContent = css;
    document.head.appendChild(estilo);

    const topo = document.createElement("header");
    topo.className = "menu-vis";
    const marca = document.createElement("a");
    marca.className = "marca";
    marca.href = url("index.html");
    marca.textContent = "Grade do ICMC como rede";
    const nav = document.createElement("nav");
    nav.setAttribute("aria-label", "Visualizações");
    [{id: "inicio", arquivo: "index.html", rotulo: "Início"}, ...VISUALIZACOES].forEach((v) => {
      const a = document.createElement("a");
      a.href = url(v.arquivo);
      a.textContent = v.rotulo;
      if (v.id === atual) a.setAttribute("aria-current", "page");
      nav.appendChild(a);
    });
    topo.append(marca, nav);
    document.body.prepend(topo);
  }

  // cartões do index.html (só se a página tiver o contêiner #lista-vis)
  function cartoes() {
    const lista = document.getElementById("lista-vis");
    if (!lista) return;
    VISUALIZACOES.forEach((v) => {
      const a = document.createElement("a");
      a.className = "cartao";
      a.href = url(v.arquivo);
      if (v.figura) {
        const img = document.createElement("img");
        img.src = url(v.figura);
        img.alt = "";
        img.loading = "lazy";
        a.appendChild(img);
      }
      const corpo = document.createElement("div");
      const r = document.createElement("span");
      r.className = "rotulo";
      r.textContent = v.rotulo;
      const h = document.createElement("h2");
      h.textContent = v.titulo;
      const p = document.createElement("p");
      p.textContent = v.descricao;
      corpo.append(r, h, p);
      a.appendChild(corpo);
      lista.appendChild(a);
    });
  }

  document.addEventListener("DOMContentLoaded", () => { barra(); cartoes(); });
})();
