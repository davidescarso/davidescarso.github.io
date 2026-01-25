const i18n = {
  en: {
    nav_home: "Home",
    nav_research: "Research",
    nav_blog: "Notes",
    nav_about: "About",
    nav_contact: "Contact",
    hero_title: "Davide Scarso",
    hero_sub: "I was born in Vicenza, Italy, and live in Lisbon. I studied philosophy and work as a professor at NOVA FCT, where I teach contemporary thought, digital society, and sociology of education. I'm interested in too many things, among them the Anthropocene, science denial, and, more broadly, the entanglements of science, technology, and politics.",
    page_title_home: "Davide Scarso – Home",
    page_title_research: "Davide Scarso – Research",
    page_title_blog: "Davide Scarso – Notes",
    page_title_about: "Davide Scarso – About",
    page_title_contact: "Davide Scarso – Contact",
    research_title: "Research & Papers",
    research_intro: "Peer-reviewed papers, preprints, and working drafts.",
    blog_title: "Notes",
    blog_intro: "Personal comments, short essays, and notes.",
    blog_filter_all: "All",
    blog_filter_label: "Filter by language",
    page_prev: "Previous",
    page_next: "Next",
    about_title: "About",
    about_intro: "Short bio and academic profile.",
    contact_title: "Contact",
    contact_intro: "Email and institutional affiliation.",
    lang_label: "Language"
  },
  pt: {
    nav_home: "Início",
    nav_research: "Pesquisa",
    nav_blog: "Notas",
    nav_about: "Sobre",
    nav_contact: "Contato",
    hero_title: "Davide Scarso",
    hero_sub: "Nasci em Vicenza, na Itália, e vivo em Lisboa. Formei-me me filosofia e trabalho como professor na NOVA FCT, onde dou aulas sobre pensamento contemporâneo, sociedade digital e sociologia da educação. Interessam-me demasiadas coisas, entre elas o Antropocénico, o negacionismo científico e, mais em geral, os cruzamentos entre ciências, tecnologia e política.",
    page_title_home: "Davide Scarso – Início",
    page_title_research: "Davide Scarso – Pesquisa",
    page_title_blog: "Davide Scarso – Notas",
    page_title_about: "Davide Scarso – Sobre",
    page_title_contact: "Davide Scarso – Contato",
    research_title: "Pesquisa e Artigos",
    research_intro: "Artigos revisados por pares, preprints e textos em andamento.",
    blog_title: "Notas",
    blog_intro: "Comentários pessoais, ensaios curtos e notas.",
    blog_filter_all: "Todos",
    blog_filter_label: "Filtrar por idioma",
    page_prev: "Anterior",
    page_next: "Seguinte",
    about_title: "Sobre",
    about_intro: "Breve biografia e perfil acadêmico.",
    contact_title: "Contato",
    contact_intro: "Email e afiliação institucional.",
    lang_label: "Idioma"
  },
  it: {
    nav_home: "Home",
    nav_research: "Ricerca",
    nav_blog: "Note",
    nav_about: "Chi sono",
    nav_contact: "Contatti",
    hero_title: "Davide Scarso",
    hero_sub: "Sono nato a Vicenza e vivo a Lisbona. Ho studiato filosofia e lavoro come professore alla NOVA FCT, dove insegno pensiero contemporaneo, società digitale e sociologia dell'educazione. Mi interessano troppe cose, ma tra queste ci sono l'Antropocene, il negazionismo scientifico e, più in generale, gli intrecci tra scienza, tecnologia e politica.",
    page_title_home: "Davide Scarso – Home",
    page_title_research: "Davide Scarso – Ricerca",
    page_title_blog: "Davide Scarso – Note",
    page_title_about: "Davide Scarso – Chi sono",
    page_title_contact: "Davide Scarso – Contatti",
    research_title: "Ricerca e Articoli",
    research_intro: "Articoli peer-reviewed, preprint e testi in lavorazione.",
    blog_title: "Note",
    blog_intro: "Commenti personali, brevi saggi e appunti.",
    blog_filter_all: "Tutti",
    blog_filter_label: "Filtra per lingua",
    page_prev: "Precedente",
    page_next: "Successivo",
    about_title: "Chi sono",
    about_intro: "Breve bio e profilo accademico.",
    contact_title: "Contatti",
    contact_intro: "Email e affiliazione istituzionale.",
    lang_label: "Lingua"
  }
};

function setLang(lang) {
  const dict = i18n[lang] || i18n.en;
  document.querySelectorAll("[data-i18n]").forEach((el) => {
    const key = el.getAttribute("data-i18n");
    if (dict[key] && el.textContent !== dict[key]) {
      el.textContent = dict[key];
    }
  });
  document.querySelectorAll("[data-i18n-aria]").forEach((el) => {
    const key = el.getAttribute("data-i18n-aria");
    if (dict[key]) el.setAttribute("aria-label", dict[key]);
  });
  const titleEl = document.querySelector("title[data-i18n-title]");
  if (titleEl) {
    const key = titleEl.getAttribute("data-i18n-title");
    if (dict[key]) titleEl.textContent = dict[key];
  }
  document.querySelectorAll("[data-lang].lang-block").forEach((block) => {
    block.style.display = block.dataset.lang === lang ? "" : "none";
  });
  document.querySelectorAll(".lang-toggle button, .home-lang button").forEach((btn) => {
    btn.classList.toggle("active", btn.dataset.lang === lang);
    btn.style.display = btn.dataset.lang === lang ? "none" : "";
  });
  document.documentElement.setAttribute("lang", lang);
  localStorage.setItem("site-lang", lang);
  syncLangLinks(lang);
  updateLangQuery(lang);

  // Remove loading class to show content
  document.body.classList.remove("loading");
}

function initLang() {
  const lang = getPreferredLang();
  setLang(lang);
  document.querySelectorAll(".lang-toggle button, .home-lang button").forEach((btn) => {
    btn.addEventListener("click", () => setLang(btn.dataset.lang));
  });
}

function getPreferredLang() {
  const params = new URLSearchParams(window.location.search);
  const fromQuery = params.get("lang");
  if (fromQuery && i18n[fromQuery]) return fromQuery;
  const saved = localStorage.getItem("site-lang");
  if (saved && i18n[saved]) return saved;
  const browserLang = (navigator.language || "").toLowerCase();
  if (browserLang.startsWith("pt")) return "pt";
  if (browserLang.startsWith("it")) return "it";
  return "en";
}

function updateLangQuery(lang) {
  const url = new URL(window.location.href);
  url.searchParams.set("lang", lang);
  window.history.replaceState({}, "", url.toString());
}

function syncLangLinks(lang) {
  document.querySelectorAll("a[href]").forEach((a) => {
    const href = a.getAttribute("href");
    if (!href) return;
    if (href.startsWith("http") || href.startsWith("mailto:") || href.startsWith("tel:") || href.startsWith("#")) return;

    const hashSplit = href.split("#");
    const base = hashSplit[0];
    const hash = hashSplit[1] ? `#${hashSplit[1]}` : "";
    const qSplit = base.split("?");
    const path = qSplit[0];
    if (!path.endsWith(".html")) return;
    const params = new URLSearchParams(qSplit[1] || "");
    params.set("lang", lang);
    const query = params.toString();
    const next = `${path}?${query}${hash}`;
    a.setAttribute("href", next);
  });
}

function initBlogFilter() {
  const filterButtons = document.querySelectorAll("[data-filter]");
  const posts = document.querySelectorAll(".post-item");
  if (!filterButtons.length || !posts.length) return;

  function applyFilter(lang) {
    filterButtons.forEach((btn) => {
      btn.classList.toggle("active", btn.dataset.filter === lang);
    });
    posts.forEach((post) => {
      const plang = post.dataset.lang;
      post.style.display = (lang === "all" || plang === lang) ? "block" : "none";
    });
  }

  filterButtons.forEach((btn) => {
    btn.addEventListener("click", () => applyFilter(btn.dataset.filter));
  });

  applyFilter("all");
}

function initRandomImage() {
  const img = document.getElementById("randomImage");
  if (!img) return;
  const section = img.closest(".random-image-section");
  const images = [
    { src: "assets/images/random/0dea2668-elon-musk.webp" },
    { src: "assets/images/random/1922791.jpeg" },
    { src: "assets/images/random/440430037_1182898072700370_6561321007850818657_n.jpg" },
    { src: "assets/images/random/449929117_422100794158735_8911510627448816814_n.jpg" },
    { src: "assets/images/random/458650724_809111731431617_4584681770143956972_n.jpg" },
    { src: "assets/images/random/473127227_10236455696642179_7950903120735615375_n.jpg" },
    { src: "assets/images/random/478114996_9189394741149188_4727753969961460943_n.jpg" },
    { src: "assets/images/random/72830959007-afp-2048585802.webp" },
    { src: "assets/images/random/alcantara2.jpeg" },
    { src: "assets/images/random/museulagos.jpg" },
    { src: "assets/images/random/no_hope_by_s_h_ores_d5s6l1y-fullview.jpg" },
    { src: "assets/images/random/photo_2024-05-25_16-03-12.jpg" },
    { src: "assets/images/random/Sem título.jpeg" },
    { src: "assets/images/random/yMB9Rwx.png" }
  ];
  if (!images.length) {
    if (section) section.style.display = "none";
    return;
  }
  const choice = images[Math.floor(Math.random() * images.length)];
  img.src = choice.src;
  img.alt = choice.alt || "";
  if (section) section.style.display = "";
}

function initEmailObfuscation() {
  const links = document.querySelectorAll(".js-email");
  links.forEach((link) => {
    const user = link.dataset.emailUser || "";
    const domain = link.dataset.emailDomain || "";
    const tld = link.dataset.emailTld || "";
    if (!user || !domain || !tld) return;
    const address = `${user}@${domain}.${tld}`;
    link.textContent = address;
    link.setAttribute("href", `mailto:${address}`);
  });
}

window.addEventListener("DOMContentLoaded", () => {
  initLang();
  initBlogFilter();
  initRandomImage();
  initEmailObfuscation();
});
