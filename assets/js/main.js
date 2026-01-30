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
    meta_desc_home: "Teacher and researcher in the humanities. Based in Lisbon, working on contemporary thought, digital society, and the Anthropocene debate.",
    meta_desc_research: "Peer-reviewed papers, preprints, and working drafts.",
    meta_desc_blog: "Personal comments and other notes.",
    meta_desc_about: "Short bio and academic profile.",
    meta_desc_contact: "Email and institutional affiliation.",
    home_research_more: "See all publications",
    home_notes_more: "See all notes",
    research_title: "Research & Papers",
    research_intro: "Peer-reviewed papers, and not",
    blog_title: "Notes",
    blog_intro: "Personal comments and other notes.",
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
    meta_desc_home: "Professor e investigador em humanidades. Em Lisboa, trabalho sobre pensamento contemporâneo, sociedade digital e o debate do Antropocénico.",
    meta_desc_research: "Artigos revisados por pares, preprints e textos em andamento.",
    meta_desc_blog: "Comentários pessoais e outras anotações.",
    meta_desc_about: "Breve biografia e perfil acadêmico.",
    meta_desc_contact: "Email e afiliação institucional.",
    home_research_more: "Ver todas as publicações",
    home_notes_more: "Ver todas as notas",
    research_title: "Pesquisa e Artigos",
    research_intro: "Artigos revisados por pares, e outros nem tanto",
    blog_title: "Notas",
    blog_intro: "Comentários pessoais e outras anotações.",
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
    hero_sub: "Sono nato a Vicenza e vivo a Lisbona. Ho studiato filosofia e sono professore alla NOVA FCT, dove insegno pensiero contemporaneo, società digitale e sociologia dell'educazione. Mi interessano troppe cose, ma tra queste ci sono l'Antropocene, il negazionismo scientifico e, più in generale, gli intrecci tra scienza, tecnologia e politica.",
    page_title_home: "Davide Scarso – Home",
    page_title_research: "Davide Scarso – Ricerca",
    page_title_blog: "Davide Scarso – Note",
    page_title_about: "Davide Scarso – Chi sono",
    page_title_contact: "Davide Scarso – Contatti",
    meta_desc_home: "Docente e ricercatore in ambito umanistico. A Lisbona, lavoro su pensiero contemporaneo, società digitale e dibattito sull'Antropocene.",
    meta_desc_research: "Articoli peer‑reviewed, preprint e testi in lavorazione.",
    meta_desc_blog: "Commenti personali e altre annotazioni.",
    meta_desc_about: "Breve bio e profilo accademico.",
    meta_desc_contact: "Email e affiliazione istituzionale.",
    home_research_more: "Tutte le pubblicazioni",
    home_notes_more: "Tutte le note",
    research_title: "Ricerca e Articoli",
    research_intro: "Articoli con peer-review, e altri senza",
    blog_title: "Note",
    blog_intro: "Commenti personali e altre annotazioni.",
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
  document.querySelectorAll("[data-i18n-content]").forEach((el) => {
    const key = el.getAttribute("data-i18n-content");
    if (dict[key]) el.setAttribute("content", dict[key]);
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
  updateLangLink(lang);

  // Remove loading class to show content
  document.body.classList.remove("loading");
}

function initLang() {
  const lang = getPreferredLang();
  setLang(lang);
  updateLangLink(lang);
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

function updateLangLink(lang) {
  const alt = lang === "pt" ? "en" : "pt";
  document.querySelectorAll(".lang-link").forEach((link) => {
    link.textContent = alt.toUpperCase();
    link.href = `${window.location.pathname}?lang=${alt}`;
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
  const sourceEl = document.getElementById("imageSource");
  const images = (window.RANDOM_IMAGES || []).map((src) => ({ src }));
  if (!images.length) {
    if (section) section.style.display = "none";
    return;
  }
  const choice = images[Math.floor(Math.random() * images.length)];
  img.src = choice.src;
  img.alt = choice.alt || "";
  const loadSources = () => {
    if (window.IMAGE_SOURCES) {
      return Promise.resolve(window.IMAGE_SOURCES);
    }
    return fetch("assets/image_sources.json").then((res) => res.json());
  };
  if (sourceEl) {
    loadSources()
      .then((sources) => {
        const file = choice.src.split("/").pop();
        const data = sources[file];
        const desc = data && data.description ? String(data.description).trim() : "";
        const src = data && data.source ? String(data.source).trim() : "";
        if (!desc && !src) {
          sourceEl.textContent = "";
          return;
        }
        const parts = [];
        if (desc) parts.push(desc);
        if (src) parts.push(src);
        const text = parts.join(" - ");
        if (data && data.url) {
          sourceEl.innerHTML = `<a href="${data.url}">${text}</a>`;
        } else {
          sourceEl.textContent = text;
        }
      })
      .catch(() => {
        sourceEl.textContent = "";
      });
  }
  if (section) section.style.display = "";
}

function initNotes() {
  const container = document.getElementById("notes");
  if (!container) return;
  if (container.dataset.static === "true") return;
  fetch("notes.json")
    .then((res) => res.json())
    .then((notes) => {
      const langLabels = { pt: "PT", en: "EN", it: "IT" };
      container.innerHTML = "";
      const filtered = notes.filter((note) => note.title !== "[TÍTULO]");
      filtered.forEach((note, idx) => {
        const article = document.createElement("article");
        article.className = "post-item";
        if (note.lang) article.dataset.lang = note.lang;

        const title = document.createElement("h2");
        title.textContent = note.title || "";
        article.appendChild(title);

        const meta = document.createElement("p");
        meta.className = "meta";
        const dateRaw = note.date || "";
        const date = dateRaw.split(" ")[0];
        const langTag = langLabels[note.lang] || (note.lang || "").toUpperCase();
        const parts = [];
        if (date) parts.push(date);
        if (langTag) parts.push(`<span class="lang-tag">${langTag}</span>`);
        if (note.source) parts.push(note.source);
        meta.innerHTML = parts.join(" · ");
        article.appendChild(meta);

        const body = document.createElement("div");
        body.className = "post-body";
        body.innerHTML = note.body_html || "";
        const firstPara = body.firstElementChild;
        if (firstPara && firstPara.tagName === "P" && !firstPara.textContent.trim()) {
          firstPara.remove();
        }
        article.appendChild(body);

        container.appendChild(article);
        if (idx < filtered.length - 1) {
          const hr = document.createElement("hr");
          hr.className = "post-divider";
          container.appendChild(hr);
        }
      });
    })
    .catch(() => {
      container.innerHTML = '<p class="meta">Notes unavailable.</p>';
    });
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

function initHomeNotes() {
  const container = document.getElementById("home-notes");
  if (!container) return;
  fetch("notes.json")
    .then((res) => res.json())
    .then((notes) => {
      const filtered = notes.filter((note) => note.title !== "[TÍTULO]");
      filtered.sort((a, b) => (b.date || "").localeCompare(a.date || ""));
      const items = filtered.slice(0, 5);
      container.innerHTML = "";
      items.forEach((note) => {
        const item = document.createElement("div");
        item.className = "note-item";

        const title = document.createElement("div");
        title.className = "note-title";
        title.textContent = note.title || "";
        item.appendChild(title);

        const meta = document.createElement("div");
        meta.className = "note-meta";
        const date = (note.date || "").split(" ")[0];
        meta.textContent = date;
        item.appendChild(meta);

        const plain = stripHtml(note.body_html || "");
        const excerpt = buildExcerpt(plain, 360, Boolean(note.full_page && note.slug));
        const excerptEl = document.createElement("p");
        excerptEl.className = "note-excerpt";
        excerptEl.textContent = excerpt;
        item.appendChild(excerptEl);
        if (note.full_page && note.slug) {
          const more = document.createElement("a");
          more.className = "note-more";
          more.href = `notes/${note.slug}.html`;
          more.textContent = "[...]";
          excerptEl.appendChild(document.createTextNode(" "));
          excerptEl.appendChild(more);
        }

        container.appendChild(item);
      });
    })
    .catch(() => {
      container.innerHTML = '<p class="meta">Notes unavailable.</p>';
    });
}

function stripHtml(text) {
  return (text || "").replace(/<[^>]+>/g, " ").replace(/\\s+/g, " ").trim();
}

function buildExcerpt(text, limit, withEllipsis) {
  if (text.length <= limit) return text;
  const cut = text.slice(0, limit);
  return `${cut.replace(/\\s+\\S*$/, "")}${withEllipsis ? "" : " [...]"}`;
}

function initMenuToggle() {
  const toggle = document.querySelector(".menu-toggle");
  if (!toggle) return;
  const nav = toggle.closest(".nav");
  if (!nav) return;
  toggle.addEventListener("click", () => {
    const open = nav.classList.toggle("menu-open");
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
  });
  nav.addEventListener("click", (event) => {
    if (event.target && event.target.tagName === "A") {
      nav.classList.remove("menu-open");
      toggle.setAttribute("aria-expanded", "false");
    }
  });
  document.addEventListener("click", (event) => {
    if (!nav.classList.contains("menu-open")) return;
    if (nav.contains(event.target)) return;
    nav.classList.remove("menu-open");
    toggle.setAttribute("aria-expanded", "false");
  });
}

window.addEventListener("DOMContentLoaded", () => {
  initLang();
  initBlogFilter();
  initNotes();
  initHomeNotes();
  initRandomImage();
  initEmailObfuscation();
  initMenuToggle();
});
