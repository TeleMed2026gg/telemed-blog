#!/usr/bin/env python3
"""Generador estático del blog de Telemed.

Uso:
  python build.py              -> construye dist/ solo con artículos de content/ con status: published (producción)
  python build.py --preview    -> construye preview/ incluyendo content/ y drafts/ (para revisar en local)
"""
import datetime as dt
import html
import json
import math
import re
import shutil
import sys
from pathlib import Path

import markdown
import yaml

ROOT = Path(__file__).parent
CFG = json.loads((ROOT / "config.json").read_text(encoding="utf-8"))
PREVIEW = "--preview" in sys.argv
OUT = ROOT / ("preview" if PREVIEW else "dist")
SITE = CFG["site_url"].rstrip("/")
BASE = CFG["base_path"].rstrip("/")

UI = {
    "en": {"read": "min read", "by": "By", "faq": "Frequently asked questions",
           "related": "Keep reading", "other_lang": "Artículos en español", "other_lang_url": f"{BASE}/es/",
           "cta_title": "See what a nearshore team would cost your practice",
           "cta_text": "Book a free 30-minute consultation. We'll scope your revenue-cycle and front-office workflows and show you the numbers — no commitment required.",
           "cta_btn": "Book a Free Consultation →", "services": "Services", "security": "Security", "blog": "Blog",
           "draft": "DRAFT — not published", "updated": "Updated", "about_author": "About the author",
           "tagline": "HEALTHCARE BPO · RCM", "nav_cta": "Book Free Consultation",
           "hero": "Practical guides for running a leaner, better-paid practice", "all": "All", "soon": "Coming soon.",
           "footer": "Nearshore healthcare BPO & RCM for US medical practices — back-office revenue cycle and bilingual front office. Contracts under US law via our Florida LLC. Not telehealth."},
    "es": {"read": "min de lectura", "by": "Por", "faq": "Preguntas frecuentes",
           "related": "Sigue leyendo", "other_lang": "Articles in English", "other_lang_url": f"{BASE}/",
           "cta_title": "Hablemos de su operación",
           "cta_text": "Agende una conversación de 30 minutos con nuestro equipo. Revisamos sus procesos y le mostramos los números, sin compromiso.",
           "cta_btn": "Contáctenos →", "services": "Servicios", "security": "Nosotros", "blog": "Blog",
           "draft": "BORRADOR — no publicado", "updated": "Actualizado", "about_author": "Sobre el autor",
           "tagline": "BPO · SALUD · CX", "nav_cta": "Contáctenos",
           "hero": "Guías prácticas para operaciones de salud más eficientes", "all": "Todos", "soon": "Próximamente.",
           "footer": "BPO nearshore con más de 20 años de experiencia en salud, servicio al cliente y experiencia del paciente. Medellín, Colombia."},
}
MONTHS_ES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
MONTHS_EN = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n(.*)$", re.S)


def esc(s):
    return html.escape(str(s or ""), quote=True)


def fmt_date(d, lang):
    if lang == "es":
        return f"{d.day} de {MONTHS_ES[d.month - 1]} de {d.year}"
    return f"{MONTHS_EN[d.month - 1]} {d.day}, {d.year}"


def to_date(v):
    return dt.date.fromisoformat(v) if isinstance(v, str) else v


def load_posts():
    posts = []
    dirs = [ROOT / "content"] + ([ROOT / "drafts"] if PREVIEW else [])
    for base in dirs:
        if not base.exists():
            continue
        for f in sorted(base.rglob("*.md")):
            m = FM_RE.match(f.read_text(encoding="utf-8").replace("\r\n", "\n"))
            if not m:
                print(f"[omitido] {f.relative_to(ROOT)}: sin front matter")
                continue
            meta = yaml.safe_load(m.group(1)) or {}
            status = meta.get("status", "draft")
            if not PREVIEW and status != "published":
                continue
            missing = [k for k in ("title", "description", "slug", "lang", "date") if not meta.get(k)]
            if missing:
                print(f"[omitido] {f.relative_to(ROOT)}: faltan campos {missing}")
                continue
            meta["date"] = to_date(meta["date"])
            if meta.get("updated"):
                meta["updated"] = to_date(meta["updated"])
            body = m.group(2)
            meta["html"] = markdown.Markdown(extensions=["tables", "toc", "sane_lists", "attr_list"]).convert(body)
            meta["words"] = len(re.findall(r"\w+", body))
            meta["minutes"] = max(1, math.ceil(meta["words"] / 230))
            meta["draft"] = status != "published"
            lang = meta["lang"]
            meta["path"] = f"{BASE}/{meta['slug']}/" if lang == "en" else f"{BASE}/es/{meta['slug']}/"
            meta["url"] = SITE + meta["path"]
            meta["source"] = f.relative_to(ROOT).as_posix()
            posts.append(meta)
    seen = {}
    for p in posts:
        key = (p["lang"], p["slug"])
        if key in seen:
            sys.exit(f"ERROR: slug duplicado {key}: {seen[key]} y {p['source']}")
        seen[key] = p["source"]
    posts.sort(key=lambda p: p["date"], reverse=True)
    return posts


def head(title, desc, url, lang, og_type="website", extra=""):
    robots = '<meta name="robots" content="noindex">' if PREVIEW else '<meta name="robots" content="index, follow, max-image-preview:large">'
    return f"""<!DOCTYPE html>
<html lang="{'en-US' if lang == 'en' else 'es-CO'}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{esc(url)}">
{robots}
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{esc(url)}">
<meta property="og:image" content="{esc(CFG['og_image'])}">
<meta property="og:site_name" content="Telemed">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;600;700;800&family=DM+Sans:ital,wght@0,400;0,500;0,700;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{BASE}/assets/blog.css?v=1">
<link rel="icon" href="https://telemed.com.co/us/img/LogoTelemed1.png" type="image/png">
<link rel="alternate" type="application/rss+xml" title="Telemed Blog" href="{SITE}{BASE}/feed.xml">
{extra}
</head>
<body>
"""


def nav(lang):
    t = UI[lang]
    home = "https://telemed.com.co/us/" if lang == "en" else "https://telemed.com.co/"
    blog_home = f"{BASE}/" if lang == "en" else f"{BASE}/es/"
    sec = "https://telemed.com.co/us/#security" if lang == "en" else "https://telemed.com.co/nosotros"
    return f"""<nav class="bnav">
  <a class="bnav-brand" href="{home}"><img src="{CFG['logo']}" alt="Telemed" width="56" height="56"><span>{t['tagline']}</span></a>
  <ul class="bnav-links">
    <li><a href="{CFG['services_url'][lang]}">{t['services']}</a></li>
    <li><a href="{sec}">{t['security']}</a></li>
    <li><a href="{blog_home}" class="active">{t['blog']}</a></li>
    <li><a href="{t['other_lang_url']}" class="bnav-lang">{'ES' if lang == 'en' else 'EN'}</a></li>
    <li><a href="{CFG['cta_url'][lang]}" class="btn">{t['nav_cta']}</a></li>
  </ul>
</nav>
"""


def cta(lang):
    t = UI[lang]
    return f"""<section class="cta-band">
  <div class="wrap">
    <h2>{t['cta_title']}</h2>
    <p>{t['cta_text']}</p>
    <a class="btn btn-light" href="{CFG['cta_url'][lang]}">{t['cta_btn']}</a>
  </div>
</section>
"""


def footer(lang):
    t = UI[lang]
    if lang == "en":
        links = ('<a href="https://telemed.com.co/us/">Home</a><a href="https://telemed.com.co/us/about-us.html">About Us</a>'
                 '<a href="https://telemed.com.co/us/careers.html">Careers</a><a href="https://telemed.com.co/us/policies/en/privacy-policy.html">Privacy Policy</a>'
                 '<a href="https://telemed.com.co/us/policies/en/security.html">Security</a>')
        contact = '<a href="tel:+17864678922">+1 (786) 467-8922</a><a href="mailto:sales@telemed.com.co">sales@telemed.com.co</a>'
    else:
        links = ('<a href="https://telemed.com.co/">Inicio</a><a href="https://telemed.com.co/nosotros">Nosotros</a>'
                 '<a href="https://telemed.com.co/trabaja-con-nosotros/">Trabaja con nosotros</a>'
                 '<a href="https://telemed.com.co/us/policies/es/politica-de-privacidad.html">Política de privacidad</a>')
        contact = ""
    return f"""<footer class="bfoot">
  <div class="wrap bfoot-grid">
    <div><img src="https://telemed.com.co/wp-content/uploads/2025/09/Telemed-logo.png" alt="Telemed" height="40"><p>{t['footer']}</p><div class="bfoot-contact">{contact}</div></div>
    <div class="bfoot-links">{links}<a href="https://www.linkedin.com/company/telemed-bpo">LinkedIn</a></div>
  </div>
  <div class="wrap bfoot-bottom">© {dt.date.today().year} Telemed BPO. Medellín, Colombia.</div>
</footer>
</body>
</html>
"""


def card(p):
    t = UI[p["lang"]]
    badge = f'<span class="draft-pill">{t["draft"]}</span>' if p["draft"] else ""
    return f"""<article class="card" data-cat="{esc(p.get('category', ''))}">
  <a href="{p['path']}">
    {badge}<span class="cat">{esc(p.get('category', ''))}</span>
    <h3>{esc(p['title'])}</h3>
    <p>{esc(p['description'])}</p>
    <span class="meta">{fmt_date(p['date'], p['lang'])} · {p['minutes']} {t['read']}</span>
  </a>
</article>"""


def jsonld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + "</script>"


def render_post(p, posts):
    lang = p["lang"]
    t = UI[lang]
    a = CFG["authors"].get(p.get("author", "rod"), CFG["authors"]["rod"])
    blog_home = f"{BASE}/" if lang == "en" else f"{BASE}/es/"
    extra = []
    tr = p.get("translation")
    if tr:
        other = next((x for x in posts if x["slug"] == tr and x["lang"] != lang), None)
        if other:
            extra.append(f'<link rel="alternate" hreflang="{lang}" href="{p["url"]}">')
            extra.append(f'<link rel="alternate" hreflang="{other["lang"]}" href="{other["url"]}">')
    extra.append(jsonld({
        "@context": "https://schema.org", "@type": "BlogPosting",
        "headline": p["title"], "description": p["description"], "inLanguage": lang,
        "datePublished": p["date"].isoformat(), "dateModified": (p.get("updated") or p["date"]).isoformat(),
        "mainEntityOfPage": p["url"], "image": CFG["og_image"],
        "author": {"@type": "Person", "name": a["name"], "jobTitle": a["role"][lang], "url": a.get("linkedin")},
        "publisher": {"@type": "Organization", "name": "Telemed", "logo": {"@type": "ImageObject", "url": CFG["logo"]}},
        "keywords": p.get("keyword", ""), "wordCount": p["words"]}))
    extra.append(jsonld({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Telemed", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Blog", "item": SITE + blog_home},
        {"@type": "ListItem", "position": 3, "name": p["title"], "item": p["url"]}]}))
    faq_html = ""
    if p.get("faq"):
        extra.append(jsonld({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q["q"], "acceptedAnswer": {"@type": "Answer", "text": q["a"]}} for q in p["faq"]]}))
        items = "".join(f"<details><summary>{esc(q['q'])}</summary><p>{esc(q['a'])}</p></details>" for q in p["faq"])
        faq_html = f'<section class="faq"><h2>{t["faq"]}</h2>{items}</section>'
    related = [x for x in posts if x["lang"] == lang and x["slug"] != p["slug"]]
    same = [x for x in related if x.get("category") == p.get("category")]
    rel = (same + [x for x in related if x not in same])[:3]
    rel_html = f'<section class="related wrap"><h2>{t["related"]}</h2><div class="grid">{"".join(card(x) for x in rel)}</div></section>' if rel else ""
    banner = f'<div class="draft-banner">{t["draft"]} · {esc(p["source"])}</div>' if p["draft"] else ""
    upd = f' · {t["updated"]} {fmt_date(p["updated"], lang)}' if p.get("updated") else ""
    return (head(f"{p['title']} | Telemed", p["description"], p["url"], lang, "article", "\n".join(extra)) + banner + nav(lang) + f"""
<main class="post">
  <header class="post-head wrap-narrow">
    <nav class="crumbs"><a href="{blog_home}">Blog</a> / <span>{esc(p.get('category', ''))}</span></nav>
    <h1>{esc(p['title'])}</h1>
    <p class="lede">{esc(p['description'])}</p>
    <div class="byline">{t['by']} <strong>{esc(a['name'])}</strong>, {esc(a['role'][lang])} · {fmt_date(p['date'], lang)}{upd} · {p['minutes']} {t['read']}</div>
  </header>
  <div class="prose wrap-narrow">
    {p['html']}
    {faq_html}
    <aside class="author-box"><h3>{t['about_author']}</h3><p><strong>{esc(a['name'])}</strong> — {esc(a['bio'][lang])}</p></aside>
  </div>
</main>
{rel_html}
""" + cta(lang) + footer(lang))


def render_index(posts, lang):
    t = UI[lang]
    lp = [p for p in posts if p["lang"] == lang]
    path = f"{BASE}/" if lang == "en" else f"{BASE}/es/"
    cats = sorted({p.get("category", "") for p in lp if p.get("category")})
    chips = "".join(f'<button class="chip" data-cat="{esc(c)}">{esc(c)}</button>' for c in cats)
    cards = "\n".join(card(p) for p in lp)
    empty = "" if lp else f"<p class='empty'>{t['soon']}</p>"
    ld = jsonld({"@context": "https://schema.org", "@type": "Blog", "name": CFG["blog_title"][lang], "url": SITE + path,
                 "publisher": {"@type": "Organization", "name": "Telemed"}})
    script = """<script>
document.querySelectorAll('.chip').forEach(function(b){b.addEventListener('click',function(){
 document.querySelectorAll('.chip').forEach(function(x){x.classList.remove('on')});b.classList.add('on');
 var c=b.getAttribute('data-cat');document.querySelectorAll('.list .card').forEach(function(k){k.style.display=(!c||k.getAttribute('data-cat')===c)?'':'none'});});});
</script>"""
    return (head(CFG["blog_title"][lang], CFG["blog_description"][lang], SITE + path, lang, extra=ld) + nav(lang) + f"""
<header class="hero-blog">
  <div class="wrap">
    <span class="eyebrow">Telemed {t['blog']}</span>
    <h1>{t['hero']}</h1>
    <p>{esc(CFG['blog_description'][lang])}</p>
    <a class="other-lang" href="{t['other_lang_url']}">{t['other_lang']} →</a>
  </div>
</header>
<main class="wrap list">
  <div class="chips"><button class="chip on" data-cat="">{t['all']}</button>{chips}</div>
  <div class="grid">{cards}</div>{empty}
</main>
""" + cta(lang) + script + footer(lang))


def sitemap(posts):
    urls = [(SITE + BASE + "/", None), (SITE + BASE + "/es/", None)]
    urls += [(p["url"], (p.get("updated") or p["date"]).isoformat()) for p in posts]
    body = "".join(f"<url><loc>{esc(u)}</loc>{f'<lastmod>{d}</lastmod>' if d else ''}</url>" for u, d in urls)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{body}</urlset>\n'


def feed(posts):
    items = ""
    for p in posts[:30]:
        pub = dt.datetime.combine(p["date"], dt.time(12)).strftime("%a, %d %b %Y %H:%M:%S +0000")
        items += f"<item><title>{esc(p['title'])}</title><link>{p['url']}</link><guid>{p['url']}</guid><pubDate>{pub}</pubDate><description>{esc(p['description'])}</description></item>"
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0"><channel><title>Telemed Blog</title><link>{SITE}{BASE}/</link><description>{esc(CFG["blog_description"]["en"])}</description>{items}</channel></rss>\n'


def write(rel, text):
    f = OUT / rel
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(text, encoding="utf-8")


def main():
    if OUT.exists():
        try:
            shutil.rmtree(OUT)
        except OSError:
            pass  # sin permiso para borrar (carpeta local): se sobrescriben los archivos
    posts = load_posts()
    for p in posts:
        write((p["slug"] if p["lang"] == "en" else f"es/{p['slug']}") + "/index.html", render_post(p, posts))
    write("index.html", render_index(posts, "en"))
    write("es/index.html", render_index(posts, "es"))
    live = [p for p in posts if not p["draft"]]
    write("sitemap.xml", sitemap(live))
    write("feed.xml", feed(live))
    (OUT / "assets").mkdir(parents=True, exist_ok=True)
    shutil.copy(ROOT / "assets" / "blog.css", OUT / "assets" / "blog.css")
    write(".htaccess", "Options -Indexes\nDirectoryIndex index.html\n")
    print(f"OK: {len(posts)} artículos -> {OUT.name}/  ({sum(1 for p in posts if p['draft'])} borradores)")
    for p in posts:
        print(f"  [{'draft' if p['draft'] else 'live '}] {p['lang']} {p['path']}  ({p['words']} palabras)")


if __name__ == "__main__":
    main()
