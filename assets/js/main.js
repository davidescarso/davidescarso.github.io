const i18n = {
  en: {
    nav_home: "Home",
    nav_research: "Research",
    nav_blog: "Notes",
    nav_about: "About",
    nav_contact: "Contact",
    hero_title: "Davide Scarso",
    hero_sub: "Teacher and researcher in the humanities. Focused on cultural history, texts, and ideas.",
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
    hero_sub: "Professor e pesquisador em Humanidades. Foco em história cultural, textos e ideias.",
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
    hero_sub: "Docente e ricercatore nelle scienze umane. Storia culturale, testi e idee.",
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
  const images = [];
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
