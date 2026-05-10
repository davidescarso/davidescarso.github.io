const i18n = {
  en: {
    nav_notas: "notes",
    nav_cronicas: "chronicles",
    nav_research: "research",
    nav_about: "about",
    nav_contact: "contact",
    page_title_home: "davide scarso",
    page_title_arquivo: "davide scarso – archive",
    page_title_notas: "davide scarso – notes",
    page_title_cronicas: "davide scarso – chronicles",
    page_title_research: "davide scarso – research",
    page_title_about: "davide scarso – about",
    page_title_contact: "davide scarso – contact",
    meta_desc_home: "Chronicles and notes.",
    meta_desc_arquivo: "Full archive.",
    meta_desc_notas: "Short notes.",
    meta_desc_cronicas: "Long-form writing.",
    meta_desc_research: "Peer-reviewed papers, preprints, and working drafts.",
    meta_desc_about: "Short bio and academic profile.",
    meta_desc_contact: "Email and institutional affiliation.",
    archive_link: "full archive →",
    back_archive: "← archive",
    footer_quote: "They used to be on Facebook. A month locked out, with no explanation, made me move house.",
    lang_label: "Language"
  },
  pt: {
    nav_notas: "notas",
    nav_cronicas: "crónicas",
    nav_research: "pesquisa",
    nav_about: "sobre",
    nav_contact: "contato",
    page_title_home: "davide scarso",
    page_title_arquivo: "davide scarso – arquivo",
    page_title_notas: "davide scarso – notas",
    page_title_cronicas: "davide scarso – crónicas",
    page_title_research: "davide scarso – pesquisa",
    page_title_about: "davide scarso – sobre",
    page_title_contact: "davide scarso – contato",
    meta_desc_home: "Crónicas e notas.",
    meta_desc_arquivo: "Arquivo completo.",
    meta_desc_notas: "Notas curtas.",
    meta_desc_cronicas: "Textos longos.",
    meta_desc_research: "Artigos revisados por pares, preprints e textos em andamento.",
    meta_desc_about: "Breve biografia e perfil académico.",
    meta_desc_contact: "Email e afiliação institucional.",
    archive_link: "arquivo completo →",
    back_archive: "← arquivo",
    footer_quote: "Antes estavam no Facebook. Um mês de bloqueio sem explicação fez-me mudar de casa.",
    lang_label: "Idioma"
  },
  it: {
    nav_notas: "note",
    nav_cronicas: "cronache",
    nav_research: "ricerca",
    nav_about: "chi sono",
    nav_contact: "contatti",
    page_title_home: "davide scarso",
    page_title_arquivo: "davide scarso – archivio",
    page_title_notas: "davide scarso – note",
    page_title_cronicas: "davide scarso – cronache",
    page_title_research: "davide scarso – ricerca",
    page_title_about: "davide scarso – chi sono",
    page_title_contact: "davide scarso – contatti",
    meta_desc_home: "Cronache e note.",
    meta_desc_arquivo: "Archivio completo.",
    meta_desc_notas: "Note brevi.",
    meta_desc_cronicas: "Testi lunghi.",
    meta_desc_research: "Articoli peer-reviewed, preprint e testi in lavorazione.",
    meta_desc_about: "Breve bio e profilo accademico.",
    meta_desc_contact: "Email e affiliazione istituzionale.",
    archive_link: "archivio completo →",
    back_archive: "← archivio",
    footer_quote: "Prima erano su Facebook. Un mese di blocco senza spiegazioni mi ha fatto traslocare.",
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
  updateLangSwitcher(lang);

  // .lang-block (about page): mostra apenas o bloco da língua activa
  document.querySelectorAll(".lang-block").forEach((block) => {
    block.classList.toggle("show", block.dataset.lang === lang);
  });

  document.body.classList.remove("lang-pending");
}

function initLang() {
  const lang = getPreferredLang();
  setLang(lang);
  updateLangSwitcher(lang);
  document.querySelectorAll(".lang-toggle button, .home-lang button").forEach((btn) => {
    btn.addEventListener("click", () => setLang(btn.dataset.lang));
  });
  document.querySelectorAll(".lang-switcher .lang-opt").forEach((opt) => {
    opt.addEventListener("click", (e) => {
      const target = opt.dataset.lang;
      if (!target || !i18n[target]) return;
      e.preventDefault();
      setLang(target);
    });
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

function updateLangSwitcher(lang) {
  document.querySelectorAll(".lang-switcher .lang-opt").forEach((opt) => {
    const target = opt.dataset.lang;
    opt.classList.toggle("active", target === lang);
    if (target) {
      opt.href = `${window.location.pathname}?lang=${target}`;
    }
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
    if (!link.dataset.emailKeepLabel) {
      link.textContent = address;
    }
    link.setAttribute("href", `mailto:${address}`);
  });
}

window.addEventListener("DOMContentLoaded", () => {
  document.body.classList.add("lang-pending");
  initLang();
  initEmailObfuscation();
});
