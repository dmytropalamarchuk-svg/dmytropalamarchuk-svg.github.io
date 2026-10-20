"""Personal site of Dmytro Palamarchuk (UA + EN) — trust-first design (DESIGN.md, 20.10.2026).

Outputs:
  preview/index.html  - UA page without document skeleton (Artifact preview)
  preview/en.html     - EN page with full skeleton
  dist/               - index.html, en.html, og.png, robots.txt, sitemap.xml, .nojekyll (GitHub Pages)
Texts: positioning and copy from «Особистий сайт — позиціонування і тексти 20.10.2026»,
figures from «Особистий сайт — реєстр фактів 20.10.2026» (IFC report EEFP_Report_#2-22_Cherkasy-2025_06).
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = "https://dmytropalamarchuk-svg.github.io/"
ORCID = "https://orcid.org/0000-0002-6023-9780"
SCHOLAR = "https://scholar.google.com/citations?user=g-yRUywAAAAJ"
ETEAM = "https://www.eteamngo.org/"
TEL, TEL_H = "tel:+380978891385", "+380 97 889 13 85"
MAIL, MAIL_W = "dmytropalamarchuk@gmail.com", "dmytro.palamarchuk@eteamngo.org"

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
         'family=Source+Serif+4:opsz,wght@8..60,600&family=Commissioner:wght@400;600&display=swap">')
FAVICON = ("data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 32 32%27%3E"
           "%3Crect width=%2732%27 height=%2732%27 rx=%274%27 fill=%27%2314202e%27/%3E"
           "%3Ctext x=%2716%27 y=%2722%27 font-family=%27Georgia,serif%27 font-size=%2716%27 font-weight=%27700%27 "
           "fill=%27%23ffffff%27 text-anchor=%27middle%27%3E%D0%94%D0%9F%3C/text%3E%3C/svg%3E")

CSS = r"""
/* Trust-first: light, text-led, serif headings + Commissioner body, one teal action colour, ruled rows. */
:root{
  --page:#ffffff; --band:#f2f4f6; --surface:#ffffff;
  --ink:#14202e; --ink-2:#4a5866; --ink-3:#5f6b77;
  --rule:#d5dbe1; --field:#6b7885;
  --primary:#0d5f59; --primary-hover:#094a45; --on-primary:#ffffff;
  --btn:#0d5f59; --btn-hover:#094a45; --tint:#e6f0ef;
  --focus:#0d5f59; --error:#b42318;
  --footer:#14202e; --on-footer:#e8edf2; --on-footer-2:#aab6c2;
  --serif:"Source Serif 4",Georgia,"Times New Roman",serif;
  --sans:"Commissioner","Segoe UI",system-ui,sans-serif;
  --fs-fig:56px; --fs-h1:44px; --fs-h2:34px; --fs-h3:21px; --fs-lead:20px; --fs-body:17px; --fs-small:15px;
  --s-1:4px; --s-2:8px; --s-3:12px; --s-4:16px; --s-5:24px; --s-6:32px; --s-7:48px; --s-8:64px; --s-9:88px;
  --r-1:4px; --r-2:6px; --wrap:1120px; --measure:68ch;
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --page:#0f151c; --band:#1a2430; --surface:#212c39;
  --ink:#e8edf2; --ink-2:#b0bcc8; --ink-3:#919daa;
  --rule:#2c3846; --field:#7d8a97;
  --primary:#6cc6bb; --primary-hover:#8fd6cc; --on-primary:#ffffff;
  --btn:#1f7a72; --btn-hover:#1a6f68; --tint:#16302e;
  --focus:#8fd6cc; --error:#f2857a; --footer:#0a0f14; color-scheme:dark}}
:root[data-theme="dark"]{
  --page:#0f151c; --band:#1a2430; --surface:#212c39;
  --ink:#e8edf2; --ink-2:#b0bcc8; --ink-3:#919daa;
  --rule:#2c3846; --field:#7d8a97;
  --primary:#6cc6bb; --primary-hover:#8fd6cc; --on-primary:#ffffff;
  --btn:#1f7a72; --btn-hover:#1a6f68; --tint:#16302e;
  --focus:#8fd6cc; --error:#f2857a; --footer:#0a0f14; color-scheme:dark}
@media (max-width:560px){:root{--fs-fig:44px; --fs-h1:34px; --fs-h2:28px; --fs-h3:20px; --fs-lead:18px; --fs-body:16px; --s-9:56px}}

*{box-sizing:border-box}
[hidden]{display:none !important}
.nw{white-space:nowrap}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
body{margin:0;background:var(--page);color:var(--ink);font-family:var(--sans);font-size:var(--fs-body);line-height:1.6}
a{color:var(--primary);text-underline-offset:3px}
a:hover{color:var(--primary-hover)}
:focus-visible{outline:3px solid var(--focus);outline-offset:2px}
.wrap{max-width:var(--wrap);margin:0 auto;padding-inline:24px}
.skip{position:absolute;left:-999px}.skip:focus{left:16px;top:8px;background:var(--page);padding:8px 12px;z-index:5}
h1,h2,.fig-n{font-family:var(--serif);font-weight:600;font-optical-sizing:auto}
h1{font-size:var(--fs-h1);line-height:1.1;letter-spacing:-.01em;margin:0 0 var(--s-4)}
h2{font-size:var(--fs-h2);line-height:1.15;margin:0 0 var(--s-4);max-width:22em;text-wrap:balance}
h3{font-size:var(--fs-h3);line-height:1.3;font-weight:600;margin:0 0 var(--s-2)}
p{margin:0}
.small{font-size:var(--fs-small);line-height:1.5}

/* header */
.hdr{border-bottom:1px solid var(--rule)}
.hdr .wrap{display:flex;align-items:center;justify-content:space-between;gap:var(--s-5);padding-block:var(--s-4)}
.brand{text-decoration:none;color:var(--ink);display:flex;flex-direction:column;line-height:1.3}
.brand b{font-weight:600;font-size:17px}
.brand span{font-size:var(--fs-small);color:var(--ink-2)}
.nav{display:flex;align-items:center;gap:var(--s-5);font-size:16px}
.nav a{color:var(--ink);text-decoration:none}
.nav a:hover{color:var(--primary);text-decoration:underline}
.nav .tel{font-weight:600;white-space:nowrap;font-variant-numeric:tabular-nums}
.nav .lang{border:1px solid var(--field);border-radius:var(--r-1);padding:2px 9px;font-weight:600;font-size:var(--fs-small)}
.links{display:flex;gap:var(--s-5)}
.tools{display:flex;align-items:center;gap:var(--s-5)}

/* hero */
.hero{display:grid;grid-template-columns:minmax(0,6fr) minmax(0,5fr);gap:var(--s-8);align-items:start;padding-block:72px var(--s-9)}
.kicker{color:var(--ink-3);font-size:var(--fs-small);margin:0 0 var(--s-3)}
.role{font-size:24px;line-height:1.35;font-weight:600;margin:0 0 var(--s-4);max-width:26em;text-wrap:balance}
.lead{font-size:var(--fs-lead);line-height:1.5;color:var(--ink-2);margin:0 0 var(--s-6);max-width:32em}
.acts{display:flex;flex-wrap:wrap;gap:var(--s-3)}
.routes{margin-top:var(--s-5);font-size:var(--fs-small);color:var(--ink-2);display:flex;flex-wrap:wrap;gap:var(--s-2) var(--s-4)}
.routes a{font-weight:600}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:var(--s-2);min-height:48px;padding:12px 20px;border-radius:var(--r-1);font:600 16px/1.2 var(--sans);text-decoration:none;border:1.5px solid var(--primary);cursor:pointer}
.btn-p{background:var(--btn);border-color:var(--btn);color:var(--on-primary)}
.btn-p:hover{background:var(--btn-hover);border-color:var(--btn-hover);color:var(--on-primary)}
.btn-s{background:transparent;color:var(--primary)}
.btn-s:hover{background:var(--band);color:var(--primary-hover)}
.btn-s span{font-variant-numeric:tabular-nums}
.facts{background:var(--surface);border:1px solid var(--rule);border-top:3px solid var(--ink);border-radius:var(--r-2);padding:var(--s-5) var(--s-5) var(--s-4)}
.facts h2{font-family:var(--sans);font-size:var(--fs-small);font-weight:600;color:var(--ink-2);margin:0 0 var(--s-2);line-height:1.4}
.facts dl{margin:0}
.facts .r{display:grid;gap:2px;padding-block:var(--s-3);border-bottom:1px solid var(--rule)}
.facts dt{font-weight:600;font-size:16px;line-height:1.4}
.facts dd{margin:0;color:var(--ink-2);font-size:var(--fs-small);line-height:1.45}
.facts .more{display:inline-block;margin-top:var(--s-3);font-weight:600;font-size:var(--fs-small);text-decoration:none}
.facts .more:hover{text-decoration:underline}

/* sections */
section{padding-block:var(--s-9);border-top:1px solid var(--rule)}
.band{background:var(--band)}
.sh{margin-bottom:var(--s-7)}
.sh::before{content:"";display:block;width:32px;height:3px;background:var(--primary);margin-bottom:var(--s-4)}
.sh p{font-size:var(--fs-lead);line-height:1.5;color:var(--ink-2);max-width:38em}

/* figures */
.figs{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:var(--s-6)}
.figs li{border-top:1px solid var(--ink);padding-top:var(--s-4);display:flex;flex-direction:column;gap:var(--s-2)}
.fig-n{font-size:var(--fs-fig);line-height:1;font-variant-numeric:tabular-nums lining-nums;letter-spacing:-.01em}
.figs .def{font-size:16px;line-height:1.45}
.note{margin-top:var(--s-6);color:var(--ink-2);font-size:var(--fs-small);max-width:var(--measure)}

/* how I work */
.steps{list-style:none;margin:0;padding:0;border-top:2px solid var(--ink)}
.steps li{display:grid;grid-template-columns:64px minmax(0,1fr);gap:var(--s-5);padding-block:var(--s-5);border-bottom:1px solid var(--rule)}
.steps .n{font-family:var(--serif);font-weight:600;font-size:28px;line-height:1;color:var(--primary);font-variant-numeric:lining-nums}
.steps p{color:var(--ink-2);max-width:var(--measure)}
.who{margin-top:var(--s-6);border-left:3px solid var(--primary);background:var(--band);padding:var(--s-4) var(--s-5);max-width:820px}
.who h3{font-size:17px;margin-bottom:var(--s-1)}
.who p{color:var(--ink-2)}

/* services as rows */
.svc{list-style:none;margin:0;padding:0;border-top:2px solid var(--ink)}
.svc>li{display:grid;grid-template-columns:200px minmax(0,1fr) minmax(0,.8fr);gap:var(--s-6);padding-block:var(--s-6);border-bottom:1px solid var(--rule);scroll-margin-top:16px}
.aud{display:flex;flex-direction:column;gap:var(--s-3);color:var(--primary);font-weight:600;font-size:var(--fs-small)}
.aud svg{width:28px;height:28px;color:var(--ink-2)}
.svc p.d{max-width:var(--measure)}
.svc p.c{margin-top:var(--s-3);color:var(--ink-2);font-size:var(--fs-small)}
.free{display:inline-block;margin-top:var(--s-3);background:var(--tint);color:var(--ink);font-weight:600;font-size:var(--fs-small);padding:4px 10px;border-radius:var(--r-1)}
.proof{display:flex;flex-direction:column;gap:var(--s-3)}
.proof p{font-size:var(--fs-small);color:var(--ink-2)}
.proof b{display:block;color:var(--ink-3);font-weight:600;margin-bottom:2px}
.go{font-weight:600;font-size:16px;text-decoration:none}
.go:hover{text-decoration:underline}

/* thermal explainer */
.explain{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,440px);gap:var(--s-7);align-items:start;margin-top:var(--s-7)}
.explain p{color:var(--ink-2);max-width:34em}
.explain h3{margin-bottom:var(--s-3)}
.scheme{margin:0;border:1px solid var(--rule);border-radius:var(--r-2);padding:var(--s-4);background:var(--surface)}
.scheme .cap{color:var(--ink-2);margin:0 0 var(--s-3)}
.scheme svg{display:block;width:100%;height:auto;border-radius:var(--r-1)}
.scale{display:flex;align-items:center;gap:var(--s-2);margin-top:var(--s-3);color:var(--ink-3)}
.scale i{display:inline-block;width:22px;height:10px}

/* partners */
.split{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:var(--s-8);align-items:start}
.plist{margin:0;padding-left:20px;display:grid;gap:var(--s-2);max-width:var(--measure)}

/* prepare */
.prep{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:var(--s-6)}
.prep ul{margin:0;padding:0;list-style:none;display:grid;gap:var(--s-2);font-size:16px}
.prep li{position:relative;padding-left:28px}
.prep li::before{content:"";position:absolute;left:0;top:5px;width:15px;height:15px;border:1.5px solid var(--field);border-radius:3px}

/* experience */
.tl{list-style:none;margin:0;padding:0;border-top:2px solid var(--ink)}
.tl li{display:grid;grid-template-columns:170px minmax(0,1fr);gap:var(--s-6);padding-block:var(--s-5);border-bottom:1px solid var(--rule)}
.yr{font-weight:600;color:var(--ink-2);font-variant-numeric:tabular-nums;font-size:var(--fs-small);padding-top:3px}
.tl h3{font-size:19px;margin-bottom:2px}
.org{color:var(--ink-2);font-size:var(--fs-small);margin:0 0 var(--s-2)}
.tl p.d{max-width:var(--measure)}
.subh{font-family:var(--sans);font-size:19px;margin:var(--s-7) 0 var(--s-4)}
.rows{margin:0;padding:0;list-style:none;display:grid;gap:var(--s-3)}
.rows li{display:grid;grid-template-columns:170px minmax(0,1fr);gap:var(--s-6)}
.rows .y{font-weight:600;color:var(--ink-2);font-size:var(--fs-small);padding-top:2px}
.rows .org{display:block;margin:2px 0 0}

/* contact */
.req{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);gap:var(--s-6);margin-bottom:var(--s-7)}
.req:has(.out[hidden]){grid-template-columns:minmax(0,760px)}
.form{background:var(--surface);border:1px solid var(--rule);border-radius:var(--r-2);padding:var(--s-5);display:grid;gap:var(--s-5)}
.form h3{margin:0}
.form .hint{color:var(--ink-2);font-size:var(--fs-small);margin-top:calc(-1 * var(--s-3))}
.form fieldset{border:0;margin:0;padding:0;display:grid;gap:var(--s-2)}
.form legend,.form label.l{font-size:var(--fs-small);font-weight:600;margin-bottom:var(--s-2);padding:0;display:block}
.opts{display:flex;flex-wrap:wrap;gap:var(--s-2)}
.opts label{display:inline-flex;align-items:center;gap:var(--s-2);border:1px solid var(--field);border-radius:var(--r-1);padding:8px 12px;font-size:var(--fs-small);cursor:pointer;background:var(--page);min-height:40px}
.opts input{accent-color:var(--primary);margin:0;width:16px;height:16px}
.opts label:has(input:checked){border-color:var(--primary);background:var(--tint)}
.row2{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:var(--s-4)}
.form input[type=text],.form textarea{width:100%;font:inherit;font-size:16px;color:var(--ink);background:var(--page);border:1.5px solid var(--field);border-radius:var(--r-1);padding:10px 12px;min-height:46px}
.form input::placeholder,.form textarea::placeholder{color:var(--ink-3)}
.form textarea{min-height:110px;resize:vertical}
.form .err{color:var(--error);font-size:var(--fs-small);font-weight:600}
.out{align-self:start;border:1.5px solid var(--primary);border-radius:var(--r-2);padding:var(--s-5);background:var(--tint);display:flex;flex-direction:column;gap:var(--s-3);min-width:0}
.out h3{margin:0;font-size:18px}
.out pre{margin:0;white-space:pre-wrap;word-break:break-word;font-family:var(--sans);font-size:15px;line-height:1.55}
.out .acts{gap:var(--s-2)}
.copy{font:inherit;font-size:14px;background:var(--page);border:1px solid var(--field);color:var(--ink);border-radius:var(--r-1);padding:5px 12px;cursor:pointer;align-self:flex-start;margin-top:var(--s-2)}
.copy:hover{border-color:var(--primary);color:var(--primary)}
.contact{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));border-top:2px solid var(--ink)}
.ct{border-bottom:1px solid var(--rule);padding:var(--s-5) var(--s-4) var(--s-4) 0;display:flex;flex-direction:column;gap:var(--s-1);min-width:0}
.ct:not(:nth-child(3n+1)){padding-left:var(--s-5);border-left:1px solid var(--rule)}
.ct .k{font-size:var(--fs-small);color:var(--ink-2)}
.ct .v{font-size:16.5px;font-weight:600;overflow-wrap:anywhere;color:var(--ink);text-decoration:none}
.ct a.v:hover{color:var(--primary);text-decoration:underline}

/* footer */
footer{background:var(--footer);color:var(--on-footer-2);font-size:var(--fs-small)}
footer .wrap{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:var(--s-6);padding-block:var(--s-7) var(--s-6)}
footer b{color:var(--on-footer);font-weight:600;display:block;font-size:16px}
footer a{color:var(--on-footer)}
footer :focus-visible{outline-color:var(--on-footer)}
footer .base{grid-column:1/-1;border-top:1px solid #2c3846;padding-top:var(--s-4)}

@media (max-width:900px){
  .hero{grid-template-columns:minmax(0,1fr);gap:var(--s-7);padding-block:var(--s-7) var(--s-9)}
  .svc>li{grid-template-columns:minmax(0,1fr);gap:var(--s-4)}
  .aud{flex-direction:row;align-items:center}
  .explain,.split,.req,.row2{grid-template-columns:minmax(0,1fr)}
  .split{gap:var(--s-6)}
  .prep{grid-template-columns:minmax(0,1fr);gap:var(--s-5)}
  .figs{grid-template-columns:repeat(2,minmax(0,1fr));row-gap:var(--s-6)}
  .contact{grid-template-columns:minmax(0,1fr) minmax(0,1fr)}
  .ct:not(:nth-child(3n+1)){padding-left:0;border-left:0}
  .ct:nth-child(2n){padding-left:var(--s-5);border-left:1px solid var(--rule)}
  footer .wrap{grid-template-columns:minmax(0,1fr)}
}
@media (max-width:560px){
  .wrap{padding-inline:16px}
  .hdr .wrap{flex-wrap:wrap;row-gap:var(--s-3)}
  .nav{display:contents}
  .links{order:2;width:100%;justify-content:space-between;border-top:1px solid var(--rule);padding-top:var(--s-3);font-size:15.5px;gap:var(--s-3)}
  .tools{gap:var(--s-4)}
  .hero{padding-top:var(--s-6)}
  .role{font-size:21px}
  .acts .btn{width:100%}
  .figs{gap:var(--s-5) var(--s-4)}
  .steps li{grid-template-columns:44px minmax(0,1fr);gap:var(--s-3)}
  .tl li,.rows li{grid-template-columns:minmax(0,1fr);gap:var(--s-1)}
  .contact{grid-template-columns:minmax(0,1fr)}
  .ct:nth-child(n){padding:var(--s-4) 0;border-left:0}
  .form{padding:var(--s-4)}
}
@media print{.hdr .links,.tools .lang,.explain,.req,footer .base{display:none}section{padding-block:24px}}
"""

ICONS = [
    '<svg viewBox="0 0 28 28" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M4 24h20M6 21h16M7 12v9M11.5 12v9M16.5 12v9M21 12v9M5 11l9-5 9 5z"/></svg>',
    '<svg viewBox="0 0 28 28" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M7 25V4h14v21M4 25h20M11 8h1M16 8h1M11 12h1M16 12h1M11 16h1M16 16h1M12.5 25v-4h3v4"/></svg>',
    '<svg viewBox="0 0 28 28" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M3 25V15l6-5 6 5v10M13 25V15l6-5 6 5v10M2 25h24M10 8l2-5h8l-2 5z"/></svg>',
]
PHONE_ICON = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M5 3h4l2 5-2.5 1.5a11 11 0 0 0 6 6L16 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 5a2 2 0 0 1 2-2"/></svg>'

# (role index, need index) preselected in the form by each service row and the partners button
SVC_PICK = [(1, 3), (0, 0), (2, 4)]

PUBS_URLS = ["http://dspace.wunu.edu.ua/handle/316497/50505",
             "https://dntb.gov.ua/wp-content/uploads/2023/05/X-%D0%BC%D1%96%D0%B6%D0%BD%D0%B0%D1%80%D0%BE%D0%B4%D0%BD%D0%B0-%D0%BA%D0%BE%D0%BD%D1%84_%D0%A1%D1%82%D1%80%D0%B0%D1%82%D0%B5%D0%B3%D1%96%D1%97-%D0%B3%D0%BB%D0%BE%D0%B1%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D1%97-%D0%BA%D0%BE%D0%BD%D0%BA%D1%83%D1%80%D0%B5%D0%BD%D1%82%D0%BE%D1%81%D0%BF%D1%80%D0%BE%D0%BC%D0%BE%D0%B6%D0%BD%D0%BE%D1%81%D1%82%D1%96_%D1%81%D0%BE%D1%86%D1%96%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE-%D0%B5%D0%BA%D0%BE%D0%BD%D0%BE%D0%BC%D1%96%D1%87%D0%BD%D1%96-%D0%B2%D0%B8%D0%BC%D1%96%D1%80%D0%B8-3.pdf",
             "https://er.chdtu.edu.ua/handle/ChSTU/4287"]

T = {
 "ua": {
  "lang": "uk", "file": "index.html", "other": "en.html", "other_lang": "en", "other_label": "EN",
  "title": "Дмитро Паламарчук",
  "seo_title": "Дмитро Паламарчук — енергоефективність, МЕП, консультації ОСББ",
  "description": "Дмитро Паламарчук — консультант з енергоефективності: муніципальні енергетичні плани для громад, безкоштовні консультації ОСББ щодо програм Фонду енергоефективності, енергетичні спільноти. Черкаси.",
  "skip": "Перейти до змісту",
  "brand_sub": "Енергоефективність · МЕП · ОСББ",
  "nav": [("#services", "Послуги"), ("#figures", "Цифри"), ("#experience", "Досвід"), ("#contact", "Контакти")],
  "nav_label": "Основна навігація",
  "kicker": "Черкаси · працюю з громадами різних областей",
  "name": "Дмитро Паламарчук",
  "role": "Допомагаю ОСББ і громадам ухвалити рішення про енергомодернізацію — і дійти до фінансування",
  "lead": "Рахую, чи вигідна модернізація, готую рішення для загальних зборів ОСББ і матеріали для робочої групи громади, підбираю джерела фінансування й супроводжую заявку до Фонду енергоефективності.",
  "cta1": "Описати своє питання", "call": "Зателефонувати",
  "routes_lbl": "Я звертаюся як:",
  "routes": [("#svc-1", "ОСББ"), ("#svc-0", "громада"), ("#svc-2", "ініціативна група"), ("#partners", "міжнародна програма")],
  "facts_h": "Програми, у яких працюю, і моя роль",
  "facts": [("IFC (Група Світового банку)", "Регіональний радник з енергоефективності, проєкт «Ukraine EE Fund», 2019–2025"),
            ("GIZ", "Регіональний радник у мережі ГО «Е-ТЕАМ», з 2026"),
            ("UNIDO", "МЕП Сміли, 2026 — у команді ГО «Е-ТЕАМ»"),
            ("Програма ЄС LIFE", "Координатор проєкту LIFE-ECOss від ГО «Е-ТЕАМ», з 2026"),
            ("Фонд енергоефективності", "Консультую ОСББ — учасників програм «Енергодім» і «ВідновиДІМ»")],
  "facts_more": "Повний досвід",
  "fig_h": "Робота з ОСББ у цифрах",
  "fig_sub": "Регіональний радник з енергоефективності в Черкаській області, проєкт IFC «Ukraine EE Fund», 2019–2025.",
  "figs": [("380+", "ОСББ Черкащини отримали мої консультації"),
           ("41", "ОСББ, яких я консультував, уклали грантові договори з Фондом енергоефективності («Енергодім»)"),
           ("4 200+", "квартир у будинках цих 41 ОСББ"),
           ("70+", "навчальних заходів для ОСББ і громад: семінари, вебінари, форуми, 2019–2024")],
  "fig_note": "Джерело: звіти регіонального радника IFC по Черкаській області (станом на червень 2025) і архів навчальних заходів. Рішення ухвалювали співвласники, роботи виконували ОСББ та їхні підрядники; моя роль — консультування на етапах рішення, розрахунків і заявки.",
  "how_h": "Як я працюю",
  "how_sub": "З якою б темою ви не прийшли — будинок, громада чи енергоспільнота, — порядок роботи той самий, і співрозмовник у вас один. Коли потрібен інженер, юрист чи проєктант, підключаю колег із команди ГО «Е-ТЕАМ» або фахівців, з якими працював на проєктах ОСББ.",
  "steps": [("Розбираємося з питанням", "Що є зараз, що турбує, які дані вже зібрано і яких бракує. Після першої розмови ви знатимете, чи варто йти далі."),
            ("Рахуємо", "Варіанти заходів, орієнтовна вартість, економія й окупність. Для ОСББ рахую ще й фінансовий результат для квартири, а не лише для будинку в цілому."),
            ("Підбираємо фінансування", "Програми Фонду енергоефективності, донорські гранти, кредити, місцеві програми співфінансування, бюджет громади."),
            ("Супроводжую процедури", "Готуємо рішення загальних зборів або сесії, заявки та звіти. До верифікації консультую голову ОСББ, проєктного менеджера й підрядника.")],
  "who_h": "Хто що робить",
  "who_p": "Рішення ухвалюють співвласники або депутати. Проєкт готує проєктант, роботи виконує підрядник, якість контролює технагляд. Я консультую на кожному етапі й стежу, щоб документи відповідали вимогам програми.",
  "s_h": "З чим до мене звертаються",
  "s_sub": "Громади, ОСББ та ініціативні групи. Для кожної — свій інструмент і робота, яку можна перевірити.",
  "proof_lbl": "Підтвердження",
  "services": [
    ("Громадам", "Муніципальний енергетичний план",
     "МЕП за Методикою, затвердженою наказом № 1163 від 21.12.2023: збір і перевірка даних, енергетичний баланс і базова лінія, цілі до 2030 року, каталог проєктів і план фінансування. За потреби команда навчає працівників громади, щоб план можна було оновлювати самостійно.",
     None, "МЕП Смілянської громади (проєкт UNIDO, 2026) передано на публічне обговорення. МЕП Сарненської громади — у роботі. Обидва плани — у команді ГО «Е-ТЕАМ».",
     "Обговорити МЕП для громади"),
    ("ОСББ", "Консультації з енергомодернізації будинку",
     "Огляд будинку й розрахунок: що модернізувати, скільки це коштуватиме, якою буде частка кожної квартири і яку економію можна очікувати. Підготовка загальних зборів, заявки до програм «Енергодім» і «ВідновиДІМ» Фонду енергоефективності, консультації до верифікації.",
     "Для ОСББ консультації безкоштовні — у межах проєкту GIZ",
     "Регіональний радник: 2019–2025 — у програмі IFC (Черкаська область, з 2024 — також Сумська), з 2026 — у мережі радників ГО «Е-ТЕАМ» (проєкт GIZ). Понад 380 ОСББ Черкащини отримали мої консультації; 41 з них уклали грантові договори з Фондом.",
     "Записатися на консультацію для ОСББ"),
    ("Енергетичним спільнотам", "Енергетична спільнота: з чого почати",
     "Для ініціативної групи, ОСББ чи громади. Оцінюємо, чи є підстави для спільноти, яка правова форма підходить, на якій бізнес-моделі вона триматиметься і звідки взяти гроші. Результат — план підготовки, з яким можна йти до учасників і партнерів.",
     None, "Координую участь ГО «Е-ТЕАМ» у проєкті ЄС LIFE-ECOss (2026–2029): у Луцьку створюємо центр підтримки енергетичних спільнот.",
     "Обговорити енергоспільноту")],
  "svc_cond": [None, None, "Правила для енергоспільнот в Україні лише формуються, тому починаємо з оцінки, а не з купівлі обладнання."],
  "th_kicker": "Для ОСББ", "th_h": "Що показує тепловізор",
  "th_p": "Тепловізор забарвлює теплі ділянки фасаду в жовтий і помаранчевий. Так видно, де будинок втрачає тепло: шви між панелями, вікна, балкони. Після утеплення фасад на знімку «холоднішає», бо тепло лишається всередині. З цього зазвичай починається розмова про те, які заходи має сенс фінансувати.",
  "th_cap": "Схема, не знімок конкретного будинку", "th_before": "До утеплення", "th_after": "Після",
  "th_aria": "Схема: панельний будинок до утеплення з теплими швами і вікнами, та після утеплення з холодним рівномірним фасадом",
  "th_cold": "холодніше", "th_warm": "тепліше",
  "p_h": "Для міжнародних програм і партнерів",
  "p_sub": "Працюю як незалежний експерт (ФОП) або в складі команди ГО «Е-ТЕАМ», залежно від вимог програми.",
  "p_list": ["Муніципальне енергетичне планування за Методикою № 1163 і аналіз енергетичних даних громад",
             "Регіональне консультування ОСББ у програмах Фонду енергоефективності: IFC (2019–2025), GIZ (з 2026)",
             "Навчання для ОСББ і посадовців громад: понад 70 заходів у 2019–2024 роках",
             "Робота в консорціумах ЄС: координую участь ГО «Е-ТЕАМ» у LIFE-ECOss, представляю організацію як LEAR на порталі Funding & Tenders",
             "Адаптація європейських практик підтримки енергоспільнот до українських умов"],
  "p_cta": "Запросити до проєкту",
  "prep_h": "Що підготувати до першої розмови",
  "prep_sub": "З цими даними перша консультація буде коротшою і кориснішою. Не все обов’язково — принесіть те, що є.",
  "prep": [("ОСББ", ["Рахунки або дані про споживання тепла за 2–3 останні опалювальні сезони",
                     "Технічний паспорт будинку: рік побудови, поверховість, площа, кількість квартир",
                     "Протоколи зборів щодо модернізації, якщо вже були",
                     "Енергетичний сертифікат або енергоаудит, якщо є",
                     "Фото фасаду, підвалу і теплового пункту"]),
           ("Громада", ["Дані про споживання енергії бюджетними будівлями за останні 3 роки",
                        "Чинні програми енергоефективності, SECAP або МЕП, якщо є",
                        "Контакт відповідальної особи: енергоменеджер, відділ ЖКГ чи економіки",
                        "Перелік проєктів, які громада вже розглядає"]),
           ("Ініціативна група", ["Склад групи і хто має намір стати учасником",
                                  "Можливий об’єкт: дах, ділянка, котельня",
                                  "Орієнтовне річне споживання електроенергії чи тепла учасниками",
                                  "Позиція органу місцевого самоврядування"])],
  "e_h": "Досвід",
  "timeline": [
    ("2025 — дотепер", "Член правління, координатор проєктів міжнародної співпраці", "ГО «Е-ТЕАМ»", ETEAM,
     "Керую розробкою муніципальних енергетичних планів у команді ГО: МЕП Сарненської громади (у роботі), МЕП Смілянської громади (проєкт UNIDO, передано на публічне обговорення у 2026 році). Координатор проєкту ЄС LIFE-ECOss від ГО «Е-ТЕАМ». Уповноважений представник (LEAR) організації на порталі Funding & Tenders Європейської Комісії."),
    ("2026 — дотепер", "Регіональний радник з енергоефективності, Черкаська область", "Мережа регіональних радників ГО «Е-ТЕАМ», проєкт GIZ", None,
     "Консультую ОСББ щодо програм «Енергодім» і «ВідновиДІМ». Організовую навчальні заходи: у липні 2026 — семінар для ОСББ і посадовців Черкас та навчальний візит для посадовців громад області."),
    ("2019 — 2025", "Регіональний радник з енергоефективності, Черкаська область (з 2024 — також Сумська)", "Проєкт IFC «Ukraine EE Fund», Група Світового банку", None,
     "Консультував ОСББ, їхніх проєктних менеджерів і підрядників, рахував фінансовий результат модернізації для будинків, проводив навчання для ОСББ і органів місцевого самоврядування. Понад 380 ОСББ Черкащини отримали консультації; 41 з них уклали грантові договори з Фондом енергоефективності. Консультував громади щодо місцевих програм підтримки ОСББ."),
    ("2012 — 2026", "Викладач, з 2017 — доцент", "Черкаський державний технологічний університет", None,
     "Курси «Міжнародна економіка», «Європейська інтеграція», «Економіка сталого розвитку»; дослідження адаптації енергетичної політики ЄС до українських умов.")],
  "edu_h": "Освіта",
  "edu": [("2014", "Кандидат економічних наук — Київський національний університет імені Тараса Шевченка"),
          ("2010", "Магістр економіки та підприємництва (з відзнакою) — Черкаський державний технологічний університет")],
  "pubs_h": "Наукові публікації",
  "pubs": [("2024", "Інформаційні кампанії як інструмент зміни поведінки споживачів щодо використання енергії: досвід ЄС", "Матеріали III Міжнародної науково-практичної конференції, Тернопіль, ЗУНУ"),
           ("2023", "Енергоефективність у житловому секторі України", "Стратегії глобальної конкурентоспроможності: соціально-економічний вимір. Матеріали X Міжнародної науково-практичної конференції, ЧДТУ"),
           ("2022", "Дослідження чинників, що впливають на рішення співвласників щодо модернізації багатоквартирних будинків", "Матеріали IX Міжнародної науково-практичної конференції, ЧДТУ")],
  "pub_more": "Повний перелік:",
  "c_h": "Напишіть, з чим звертаєтеся",
  "c_sub": "МЕП для громади, консультація для ОСББ, енергоспільнота чи участь у міжнародному проєкті — опишіть питання в кількох словах, і я відповім.",
  "form_h": "Опишіть ваше питання",
  "form_hint": "Форма складе текст листа. Ви надішлете його поштою або скопіюєте в месенджер — дані нікуди не передаються автоматично і не зберігаються.",
  "f_role": "Хто звертається", "roles": ["ОСББ або управитель", "Громада (ОМС)", "Ініціативна група / енергоспільнота", "Міжнародна організація / донор", "Інше"],
  "f_need": "Що потрібно", "needs": ["Консультація", "Участь у загальних зборах ОСББ", "Огляд будинку і розрахунок", "Муніципальний енергетичний план", "Енергетична спільнота: з чого почати", "Експертна участь у проєкті"],
  "f_place": "Населений пункт", "f_place_ph": "напр., Сміла", "f_name": "Ваше ім’я", "f_contact": "Телефон або email",
  "f_msg": "Коротко про питання", "f_msg_ph": "що є зараз і що хочете змінити",
  "f_err": "Оберіть, хто звертається, і вкажіть ім’я та контакт, щоб я міг відповісти.",
  "f_btn": "Скласти лист", "f_out_h": "Лист готовий. Перевірте текст і надішліть.",
  "f_send": "Надіслати поштою", "copy": "Копіювати текст", "copied": "Скопійовано", "copy_short": "Копіювати",
  "f_hdr": "Звернення з сайту", "f_lab": ["Хто", "Населений пункт", "Що потрібно", "Питання", "Контакт"],
  "contacts": [("Email", MAIL, "mailto:" + MAIL, True), ("Корпоративна пошта, ГО «Е-ТЕАМ»", MAIL_W, "mailto:" + MAIL_W, True),
               ("Телефон", TEL_H, TEL, True), ("Сайт ГО «Е-ТЕАМ»", "eteamngo.org", ETEAM, False),
               ("Google Scholar", "Профіль і цитування", SCHOLAR, False), ("ORCID", "0000-0002-6023-9780", ORCID, False)],
  "ft_role": "Незалежний експерт (ФОП) · Черкаси", "ft_board": "Член правління ГО «Е-ТЕАМ»",
  "ft_base": "© 2026 Дмитро Паламарчук · Оновлено: жовтень 2026",
  "jobTitle": "Консультант з енергоефективності та муніципального енергетичного планування",
 },
 "en": {
  "lang": "en", "file": "en.html", "other": "index.html", "other_lang": "uk", "other_label": "UA",
  "title": "Dmytro Palamarchuk",
  "seo_title": "Dmytro Palamarchuk — energy efficiency, municipal energy planning, HOA advisory (Ukraine)",
  "description": "Dmytro Palamarchuk — energy efficiency consultant in Ukraine: municipal energy plans, free advisory for homeowner associations on Energy Efficiency Fund programmes, energy communities. Cherkasy.",
  "skip": "Skip to content",
  "brand_sub": "Energy efficiency · Energy plans · HOAs",
  "nav": [("#services", "Services"), ("#figures", "Figures"), ("#experience", "Experience"), ("#contact", "Contact")],
  "nav_label": "Main navigation",
  "kicker": "Cherkasy, Ukraine · working with municipalities across regions",
  "name": "Dmytro Palamarchuk",
  "role": "I help homeowner associations and municipalities decide on energy renovation — and get it financed",
  "lead": "I calculate whether renovation pays off, prepare decisions for HOA general meetings and materials for municipal working groups, identify funding sources and guide applications to Ukraine’s Energy Efficiency Fund.",
  "cta1": "Describe your question", "call": "Call",
  "routes_lbl": "I am contacting you as:",
  "routes": [("#svc-1", "an HOA"), ("#svc-0", "a municipality"), ("#svc-2", "a community group"), ("#partners", "an international programme")],
  "facts_h": "Programmes I work in, and my role",
  "facts": [("IFC (World Bank Group)", "Regional energy efficiency advisor, “Ukraine EE Fund” project, 2019–2025"),
            ("GIZ", "Regional advisor in the NGO E-TEAM network, since 2026"),
            ("UNIDO", "Municipal energy plan for Smila, 2026 — in the NGO E-TEAM team"),
            ("EU LIFE Programme", "Project coordinator of LIFE-ECOss for NGO E-TEAM, since 2026"),
            ("Energy Efficiency Fund", "Advising HOAs in the “Energodim” and “VidnovyDIM” programmes")],
  "facts_more": "Full experience",
  "fig_h": "HOA advisory in figures",
  "fig_sub": "Regional energy efficiency advisor in Cherkasy oblast, IFC “Ukraine EE Fund” project, 2019–2025.",
  "figs": [("380+", "homeowner associations in Cherkasy oblast received my advice"),
           ("41", "HOAs I advised signed grant agreements with the Energy Efficiency Fund (“Energodim”)"),
           ("4,200+", "flats in the buildings of these 41 HOAs"),
           ("70+", "training events for HOAs and municipalities: seminars, webinars, forums, 2019–2024")],
  "fig_note": "Source: IFC regional advisor reports for Cherkasy oblast (as of June 2025) and the training-event archive. Decisions were taken by the co-owners; works were carried out by the HOAs and their contractors. My role was advice at the decision, calculation and application stages.",
  "how_h": "How I work",
  "how_sub": "Whatever you come with — a building, a municipality or an energy community — the sequence is the same, and you have one counterpart. When an engineer, lawyer or designer is needed, I bring in colleagues from the NGO E-TEAM team or specialists I have worked with on HOA projects.",
  "steps": [("Understanding the question", "What exists now, what the concern is, which data are available and which are missing. After the first conversation you will know whether it is worth going further."),
            ("Calculating", "Options, indicative cost, savings and payback. For HOAs I also calculate the financial result per flat, not just for the building."),
            ("Finding funding", "Energy Efficiency Fund programmes, donor grants, loans, local co-financing programmes, the municipal budget."),
            ("Guiding the procedures", "We prepare general meeting or council decisions, applications and reports. Up to verification I advise the HOA head, the project manager and the contractor.")],
  "who_h": "Who does what",
  "who_p": "Decisions are taken by co-owners or councillors. The design is prepared by a designer, works are done by a contractor, quality is checked by technical supervision. I advise at every stage and make sure documents meet the programme requirements.",
  "s_h": "What people come to me with",
  "s_sub": "Municipalities, homeowner associations and community groups. Each has its own tool and work that can be checked.",
  "proof_lbl": "Track record",
  "services": [
    ("Municipalities", "Municipal energy plan",
     "Energy plans under the national methodology (Order No. 1163 of 21.12.2023): data collection and validation, energy balance and baseline, targets to 2030, project catalogue and financing plan. If needed, the team trains municipal staff so the plan can be updated in-house.",
     None, "The Smila energy plan (UNIDO project, 2026) has been released for public consultation. The Sarny plan is in progress. Both with the NGO E-TEAM team.",
     "Discuss an energy plan"),
    ("Homeowner associations", "Building energy renovation advice",
     "Building walk-through and calculation: what to renovate, what it will cost, each flat’s share and the expected savings. Preparing the general meeting and applications to the Energy Efficiency Fund’s “Energodim” and “VidnovyDIM” programmes, advice up to verification.",
     "Advice for HOAs is free of charge under the GIZ project",
     "Regional advisor: 2019–2025 in the IFC programme (Cherkasy oblast, from 2024 also Sumy), since 2026 in the NGO E-TEAM advisor network (GIZ project). 380+ HOAs in Cherkasy oblast received my advice; 41 of them signed grant agreements with the Fund.",
     "Book an HOA consultation"),
    ("Energy communities", "Energy community: where to start",
     "For a community group, an HOA or a municipality. We assess whether there is a case for a community, which legal form fits, which business model will carry it and where the money can come from. The result is a preparation plan to take to members and partners.",
     None, "I coordinate NGO E-TEAM’s participation in the EU LIFE-ECOss project (2026–2029): we are setting up an energy community support centre in Lutsk.",
     "Discuss an energy community")],
  "svc_cond": [None, None, "Rules for energy communities in Ukraine are still being formed, so we start with an assessment, not with buying equipment."],
  "th_kicker": "For HOAs", "th_h": "What a thermal camera shows",
  "th_p": "A thermal camera colours warm parts of a facade yellow and orange. It shows where a building loses heat: panel joints, windows, balconies. After insulation the facade looks “colder” on the image because the heat stays inside. That is usually where the conversation about which measures are worth financing begins.",
  "th_cap": "Diagram, not an image of a specific building", "th_before": "Before insulation", "th_after": "After",
  "th_aria": "Diagram: a panel apartment block before insulation with warm joints and windows, and after insulation with an evenly cold facade",
  "th_cold": "colder", "th_warm": "warmer",
  "p_h": "For international programmes and partners",
  "p_sub": "I work as an independent expert (registered sole proprietor) or as part of the NGO E-TEAM team, depending on programme requirements.",
  "p_list": ["Municipal energy planning under the national methodology and analysis of municipal energy data",
             "Regional advice to homeowner associations in Energy Efficiency Fund programmes: IFC (2019–2025), GIZ (since 2026)",
             "Training for HOAs and municipal officials: 70+ events in 2019–2024",
             "EU consortia: I coordinate NGO E-TEAM’s participation in LIFE-ECOss and act as the organisation’s LEAR on the Funding & Tenders portal",
             "Adapting European energy-community support practice to Ukrainian conditions"],
  "p_cta": "Invite to a project",
  "prep_h": "What to prepare for the first conversation",
  "prep_sub": "With this information the first consultation is shorter and more useful. Not everything is required — bring what you have.",
  "prep": [("Homeowner association", ["Heat bills or consumption data for the last 2–3 heating seasons",
                                      "Building passport: year built, storeys, floor area, number of flats",
                                      "Minutes of meetings on renovation, if any",
                                      "Energy certificate or energy audit, if available",
                                      "Photos of the facade, basement and heating substation"]),
           ("Municipality", ["Energy consumption of public buildings for the last 3 years",
                             "Current energy efficiency programmes, SECAP or energy plan, if any",
                             "Contact of the responsible person: energy manager, housing or economic department",
                             "List of projects the municipality is already considering"]),
           ("Community group", ["Members of the group and who intends to join",
                                "Possible site: roof, land plot, boiler house",
                                "Approximate annual electricity or heat use of members",
                                "Position of the local authority"])],
  "e_h": "Experience",
  "timeline": [
    ("2025 — present", "Board member, international cooperation projects coordinator", "NGO E-TEAM", ETEAM,
     "Lead the development of municipal energy plans in the NGO team: Sarny (in progress), Smila (UNIDO project, released for public consultation in 2026). Project coordinator of the EU LIFE-ECOss project for NGO E-TEAM. Legal Entity Appointed Representative (LEAR) of the organisation on the European Commission’s Funding & Tenders portal."),
    ("2026 — present", "Regional energy efficiency advisor, Cherkasy oblast", "NGO E-TEAM regional advisor network, GIZ project", None,
     "Advising HOAs on the “Energodim” and “VidnovyDIM” programmes. Organising training: in July 2026 a seminar for HOAs and Cherkasy city officials and a study visit for officials of oblast municipalities."),
    ("2019 — 2025", "Regional energy efficiency advisor, Cherkasy oblast (from 2024 also Sumy)", "IFC “Ukraine EE Fund” project, World Bank Group", None,
     "Advised HOAs, their project managers and contractors, calculated the financial result of building renovation, trained HOAs and local authorities. 380+ HOAs in Cherkasy oblast received advice; 41 of them signed grant agreements with the Energy Efficiency Fund. Advised municipalities on local HOA support programmes."),
    ("2012 — 2026", "Lecturer, Associate Professor from 2017", "Cherkasy State Technological University", None,
     "Courses in International Economics, European Integration and Economics of Sustainable Development; research on adapting EU energy policy to Ukraine.")],
  "edu_h": "Education",
  "edu": [("2014", "PhD in Economics — Taras Shevchenko National University of Kyiv"),
          ("2010", "Master’s in Economics and Entrepreneurship (Honours) — Cherkasy State Technological University")],
  "pubs_h": "Research publications",
  "pubs": [("2024", "Information campaigns as a tool for changing consumer energy behaviour: EU experience", "Proceedings of the III International Scientific and Practical Conference, Ternopil, WUNU (in Ukrainian)"),
           ("2023", "Energy efficiency in Ukraine’s housing sector", "Strategies of Global Competitiveness: Socio-Economic Dimensions, X International Conference, ChSTU (in Ukrainian)"),
           ("2022", "Factors influencing homeowners’ decisions on the modernisation of multi-apartment buildings", "IX International Scientific and Practical Conference, ChSTU (in Ukrainian)")],
  "pub_more": "Full list:",
  "c_h": "Tell me what you need",
  "c_sub": "An energy plan for a municipality, HOA advice, an energy community or expert input to an international project — describe the question in a few words and I will reply.",
  "form_h": "Describe your question",
  "form_hint": "The form composes an email. You send it from your mail app or copy it into a messenger — nothing is transmitted automatically or stored.",
  "f_role": "Who you are", "roles": ["Homeowner association or manager", "Municipality", "Community group / energy community", "International organisation / donor", "Other"],
  "f_need": "What you need", "needs": ["Consultation", "Attendance at an HOA general meeting", "Building walk-through and calculation", "Municipal energy plan", "Energy community: where to start", "Expert input to a project"],
  "f_place": "Town or village", "f_place_ph": "e.g. Smila", "f_name": "Your name", "f_contact": "Phone or email",
  "f_msg": "Your question in brief", "f_msg_ph": "what exists now and what you want to change",
  "f_err": "Please choose who you are and enter your name and a contact so I can reply.",
  "f_btn": "Compose email", "f_out_h": "Your message is ready. Check the text and send it.",
  "f_send": "Send by email", "copy": "Copy text", "copied": "Copied", "copy_short": "Copy",
  "f_hdr": "Request from the website", "f_lab": ["Who", "Location", "Needs", "Question", "Contact"],
  "contacts": [("Email", MAIL, "mailto:" + MAIL, True), ("Work email, NGO E-TEAM", MAIL_W, "mailto:" + MAIL_W, True),
               ("Phone", TEL_H, TEL, True), ("NGO E-TEAM website", "eteamngo.org", ETEAM, False),
               ("Google Scholar", "Profile and citations", SCHOLAR, False), ("ORCID", "0000-0002-6023-9780", ORCID, False)],
  "ft_role": "Independent expert · Cherkasy, Ukraine", "ft_board": "Board member, NGO E-TEAM",
  "ft_base": "© 2026 Dmytro Palamarchuk · Updated: October 2026",
  "jobTitle": "Energy efficiency and municipal energy planning consultant",
 },
}

JS = r"""
var lab=__LAB__, hdr=__HDR__, COPY=__COPY__, COPIED=__COPIED__;
document.getElementById('reqform').addEventListener('submit',function(e){e.preventDefault();
  var g=function(id){return document.getElementById(id).value.trim();};
  var name=g('f-name'), contact=g('f-contact'), err=document.getElementById('f-err');
  var role=(document.querySelector('input[name=role]:checked')||{}).value||'';
  if(!name||!contact||!role){err.hidden=false;err.focus();return;} err.hidden=true;
  var needs=[].slice.call(document.querySelectorAll('input[name=need]:checked')).map(function(x){return x.value;}).join(', ');
  var lines=[hdr, lab[0]+': '+role];
  if(g('f-place')) lines.push(lab[1]+': '+g('f-place'));
  if(needs) lines.push(lab[2]+': '+needs);
  if(g('f-msg')) lines.push(lab[3]+': '+g('f-msg'));
  lines.push(lab[4]+': '+name+', '+contact);
  var txt=lines.join('\n');
  document.getElementById('f-text').textContent=txt;
  document.getElementById('copy-msg').setAttribute('data-v',txt);
  var m=document.getElementById('f-mail'); m.href=m.href.split('?')[0]+'?subject='+encodeURIComponent(hdr)+'&body='+encodeURIComponent(txt);
  var o=document.getElementById('f-out'); o.hidden=false; o.scrollIntoView({behavior:'smooth',block:'nearest'});
});
var NEED_MAP=[[0,1,2],[0,3],[0,4],[0,5],[0,1,2,3,4,5]];
document.querySelectorAll('input[name=role]').forEach(function(r,ri){r.addEventListener('change',function(){
  var ok=NEED_MAP[ri]||NEED_MAP[4];
  document.querySelectorAll('input[name=need]').forEach(function(c,ci){var show=ok.indexOf(ci)>-1;c.parentNode.hidden=!show;if(!show)c.checked=false;});
});});
document.querySelectorAll('.pick').forEach(function(a){a.addEventListener('click',function(){
  var r=document.getElementById('role-'+a.getAttribute('data-role')); if(r){r.checked=true;r.dispatchEvent(new Event('change'));}
  var n=document.getElementById('need-'+a.getAttribute('data-need')); if(n) n.checked=true;
});});
function sel(b){var s=b.parentNode.querySelector('.v');if(!s)return;var r=document.createRange();r.selectNodeContents(s);var w=window.getSelection();w.removeAllRanges();w.addRange(r);}
document.querySelectorAll('.copy').forEach(function(b){b.addEventListener('click',function(){
  var v=b.getAttribute('data-v'), label=b.textContent;
  var done=function(){b.textContent=COPIED;setTimeout(function(){b.textContent=label;},1600);};
  try{navigator.clipboard.writeText(v).then(done,function(){sel(b);});}catch(e){sel(b);}
});});
"""


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def scheme(t):
    return f"""<figure class="scheme">
<figcaption class="cap small">{esc(t['th_cap'])}</figcaption>
<svg viewBox="0 0 400 230" role="img" aria-label="{esc(t['th_aria'])}">
<defs><pattern id="wb" width="38" height="26" patternUnits="userSpaceOnUse" x="42" y="34"><rect width="38" height="26" fill="#b8336a"/><rect y="23" width="38" height="3" fill="#e0702a"/><rect x="10" y="6" width="18" height="12" fill="#f5c24a"/></pattern>
<pattern id="wa" width="38" height="26" patternUnits="userSpaceOnUse" x="42" y="34"><rect width="38" height="26" fill="#3b2f86"/><rect x="10" y="6" width="18" height="12" fill="#8e2d78"/></pattern></defs>
<rect width="400" height="230" fill="#17163a"/><rect x="42" y="34" width="152" height="182" fill="url(#wb)"/><rect x="206" y="34" width="152" height="182" fill="url(#wa)"/>
<rect x="0" y="216" width="400" height="14" fill="#221f52"/><rect x="196" y="20" width="8" height="200" fill="#17163a"/>
<g font-family="Commissioner, sans-serif" font-size="13" font-weight="600" fill="#ffffff"><text x="42" y="22">{esc(t['th_before'])}</text><text x="358" y="22" text-anchor="end">{esc(t['th_after'])}</text></g>
</svg>
<div class="scale small" aria-hidden="true">{esc(t['th_cold'])} <i style="background:#3b2f86"></i><i style="background:#8e2d78"></i><i style="background:#b8336a"></i><i style="background:#e0702a"></i><i style="background:#f5c24a"></i> {esc(t['th_warm'])}</div>
</figure>"""


def page(t, skeleton, seo=False):
    links = "".join(f'<a href="{h}">{esc(l)}</a>' for h, l in t["nav"])
    routes = " ".join(f'<a href="{h}">{esc(l)}</a>' for h, l in t["routes"])
    facts = "".join(f'<div class="r"><dt>{esc(a)}</dt><dd>{esc(b)}</dd></div>' for a, b in t["facts"])
    figs = "".join(f'<li><span class="fig-n">{esc(n)}</span><p class="def">{esc(d)}</p></li>' for n, d in t["figs"])
    steps = "".join(f'<li><span class="n">{i+1}</span><div><h3>{esc(a)}</h3><p>{esc(b)}</p></div></li>' for i, (a, b) in enumerate(t["steps"]))
    svcs = ""
    for i, (aud, h, d, free, proof, cta) in enumerate(t["services"]):
        cond = t["svc_cond"][i]
        svcs += (f'<li id="svc-{i}"><div class="aud">{ICONS[i]}{esc(aud)}</div>'
                 f'<div><h3>{esc(h)}</h3><p class="d">{esc(d)}</p>'
                 + (f'<p class="c">{esc(cond)}</p>' if cond else '')
                 + (f'<span class="free">{esc(free)}</span>' if free else '') +
                 f'</div><div class="proof"><p><b>{esc(t["proof_lbl"])}</b>{esc(proof)}</p>'
                 f'<a class="go pick" href="#contact" data-role="{SVC_PICK[i][0]}" data-need="{SVC_PICK[i][1]}">{esc(cta)} →</a></div></li>')
    plist = "".join(f'<li>{esc(x)}</li>' for x in t["p_list"])
    prep = "".join(f'<div><h3>{esc(h)}</h3><ul>' + "".join(f'<li>{esc(x)}</li>' for x in items) + '</ul></div>' for h, items in t["prep"])
    tl = ""
    for yr, role, org, url, d in t["timeline"]:
        o = f'<a href="{url}" rel="noopener">{esc(org)}</a>' if url else esc(org)
        tl += f'<li><div class="yr">{esc(yr)}</div><div><h3>{esc(role)}</h3><p class="org">{o}</p><p class="d">{esc(d)}</p></div></li>'
    edu = "".join(f'<li><span class="y">{y}</span><span>{esc(x)}</span></li>' for y, x in t["edu"])
    pubs = "".join(f'<li><span class="y">{y}</span><div><a href="{u}" rel="noopener">{esc(ti)}</a><span class="org">{esc(v)}</span></div></li>'
                   for (y, ti, v), u in zip(t["pubs"], PUBS_URLS))
    roles = "".join(f'<label><input type="radio" name="role" value="{esc(r)}" id="role-{k}"> {esc(r)}</label>' for k, r in enumerate(t["roles"]))
    needs = "".join(f'<label><input type="checkbox" name="need" value="{esc(r)}" id="need-{k}"> {esc(r)}</label>' for k, r in enumerate(t["needs"]))
    cts = ""
    for i, (k, v, href, cp) in enumerate(t["contacts"]):
        ext = ' rel="noopener"' if href.startswith("http") else ''
        btn = f'<button class="copy" type="button" data-v="{esc(v)}">{esc(t["copy_short"])}</button>' if cp else ''
        cts += f'<div class="ct"><span class="k">{esc(k)}</span><a class="v" href="{esc(href)}"{ext}>{esc(v)}</a>{btn}</div>'
    form = f"""<div class="req"><form class="form" id="reqform" novalidate>
<h3>{esc(t['form_h'])}</h3><p class="hint">{esc(t['form_hint'])}</p>
<fieldset><legend>{esc(t['f_role'])}</legend><div class="opts">{roles}</div></fieldset>
<fieldset><legend>{esc(t['f_need'])}</legend><div class="opts">{needs}</div></fieldset>
<div class="row2"><div><label class="l" for="f-place">{esc(t['f_place'])}</label><input type="text" id="f-place" autocomplete="address-level2" placeholder="{esc(t['f_place_ph'])}"></div>
<div><label class="l" for="f-name">{esc(t['f_name'])}</label><input type="text" id="f-name" autocomplete="name"></div></div>
<div><label class="l" for="f-contact">{esc(t['f_contact'])}</label><input type="text" id="f-contact" autocomplete="email"></div>
<div><label class="l" for="f-msg">{esc(t['f_msg'])}</label><textarea id="f-msg" placeholder="{esc(t['f_msg_ph'])}"></textarea></div>
<p class="err" id="f-err" tabindex="-1" hidden>{esc(t['f_err'])}</p>
<div><button class="btn btn-p" type="submit">{esc(t['f_btn'])}</button></div>
</form>
<div class="out" id="f-out" hidden aria-live="polite"><h3>{esc(t['f_out_h'])}</h3><pre id="f-text"></pre>
<div class="acts"><a class="btn btn-p" id="f-mail" href="mailto:{MAIL}">{esc(t['f_send'])}</a><a class="btn btn-s" href="{TEL}">{esc(t['call'])}</a></div>
<button class="copy" type="button" id="copy-msg" data-v="">{esc(t['copy'])}</button></div>
</div>"""
    ld = {"@context": "https://schema.org", "@type": "Person", "name": t["name"],
          "alternateName": ["Дмитро Паламарчук", "Dmytro Palamarchuk", "Паламарчук Дмитро Миколайович"],
          "jobTitle": t["jobTitle"], "email": "mailto:" + MAIL, "telephone": TEL_H,
          "address": {"@type": "PostalAddress", "addressLocality": "Cherkasy", "addressCountry": "UA"},
          "worksFor": {"@type": "Organization", "name": "NGO E-TEAM", "url": ETEAM},
          "alumniOf": [{"@type": "CollegeOrUniversity", "name": "Taras Shevchenko National University of Kyiv"},
                       {"@type": "CollegeOrUniversity", "name": "Cherkasy State Technological University"}],
          "knowsAbout": ["Energy efficiency", "Municipal energy planning", "Energy communities", "Homeowner associations", "EU energy policy"],
          "sameAs": [ORCID, SCHOLAR]}
    ttl = t["seo_title"] if seo else t["title"]
    url = BASE + ("" if t["file"] == "index.html" else t["file"])
    head = (f'<title>{esc(ttl)}</title>' + ('' if seo else '<meta name="claude:viewport-fit-sides" content="cover">') +
            f'<meta name="description" content="{esc(t["description"])}"><link rel="canonical" href="{url}">'
            f'<link rel="alternate" hreflang="uk" href="{BASE}"><link rel="alternate" hreflang="en" href="{BASE}en.html"><link rel="alternate" hreflang="x-default" href="{BASE}">'
            f'<meta property="og:type" content="profile"><meta property="og:title" content="{esc(ttl)}"><meta property="og:description" content="{esc(t["description"])}"><meta property="og:url" content="{url}">'
            f'<meta property="og:image" content="{BASE}og.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image">'
            f'<link rel="icon" href="{FAVICON}">{FONTS}<style>{CSS}</style>'
            f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>')
    js = (JS.replace("__LAB__", json.dumps(t["f_lab"], ensure_ascii=False)).replace("__HDR__", json.dumps(t["f_hdr"], ensure_ascii=False))
            .replace("__COPY__", json.dumps(t["copy"], ensure_ascii=False)).replace("__COPIED__", json.dumps(t["copied"], ensure_ascii=False)))
    p0, p1 = SVC_PICK[0]
    body = f"""
<a class="skip" href="#main">{esc(t['skip'])}</a>
<header class="hdr"><div class="wrap">
  <a class="brand" href="{t['file']}"><b>{esc(t['name'])}</b><span>{esc(t['brand_sub'])}</span></a>
  <nav class="nav" aria-label="{esc(t['nav_label'])}">
    <div class="links">{links}</div>
    <div class="tools"><a class="tel" href="{TEL}">{TEL_H}</a><a class="lang" href="{t['other']}" hreflang="{t['other_lang']}" lang="{t['other_lang']}">{t['other_label']}</a></div>
  </nav>
</div></header>
<main id="main">
<div class="wrap hero">
  <div>
    <p class="kicker">{esc(t['kicker'])}</p>
    <h1>{esc(t['name'])}</h1>
    <p class="role">{esc(t['role'])}</p>
    <p class="lead">{esc(t['lead'])}</p>
    <div class="acts"><a class="btn btn-p" href="#contact">{esc(t['cta1'])}</a><a class="btn btn-s" href="{TEL}" aria-label="{esc(t['call'])}: {TEL_H}">{PHONE_ICON}<span>{TEL_H}</span></a></div>
    <p class="routes"><span>{esc(t['routes_lbl'])}</span> {routes}</p>
  </div>
  <aside class="facts" aria-labelledby="facts-h"><h2 id="facts-h">{esc(t['facts_h'])}</h2><dl>{facts}</dl><a class="more" href="#experience">{esc(t['facts_more'])} →</a></aside>
</div>
<section id="figures" class="band" aria-labelledby="fig-h"><div class="wrap">
  <div class="sh"><h2 id="fig-h">{esc(t['fig_h'])}</h2><p>{esc(t['fig_sub'])}</p></div>
  <ul class="figs">{figs}</ul><p class="note">{esc(t['fig_note'])}</p>
</div></section>
<section id="how" aria-labelledby="how-h"><div class="wrap">
  <div class="sh"><h2 id="how-h">{esc(t['how_h'])}</h2><p>{esc(t['how_sub'])}</p></div>
  <ol class="steps">{steps}</ol>
  <div class="who"><h3>{esc(t['who_h'])}</h3><p>{esc(t['who_p'])}</p></div>
</div></section>
<section id="services" class="band" aria-labelledby="svc-h"><div class="wrap">
  <div class="sh"><h2 id="svc-h">{esc(t['s_h'])}</h2><p>{esc(t['s_sub'])}</p></div>
  <ul class="svc">{svcs}</ul>
  <div class="explain"><div><p class="kicker">{esc(t['th_kicker'])}</p><h3>{esc(t['th_h'])}</h3><p>{esc(t['th_p'])}</p></div>{scheme(t)}</div>
</div></section>
<section id="partners" aria-labelledby="p-h"><div class="wrap split">
  <div class="sh" style="margin:0"><h2 id="p-h">{esc(t['p_h'])}</h2><p>{esc(t['p_sub'])}</p><p style="margin-top:var(--s-5)"><a class="btn btn-s pick" href="#contact" data-role="3" data-need="5">{esc(t['p_cta'])}</a></p></div>
  <ul class="plist">{plist}</ul>
</div></section>
<section id="prepare" class="band" aria-labelledby="prep-h"><div class="wrap">
  <div class="sh"><h2 id="prep-h">{esc(t['prep_h'])}</h2><p>{esc(t['prep_sub'])}</p></div>
  <div class="prep">{prep}</div>
</div></section>
<section id="experience" aria-labelledby="e-h"><div class="wrap">
  <div class="sh"><h2 id="e-h">{esc(t['e_h'])}</h2></div>
  <ul class="tl">{tl}</ul>
  <h3 class="subh">{esc(t['edu_h'])}</h3><ul class="rows">{edu}</ul>
  <h3 class="subh" id="publications">{esc(t['pubs_h'])}</h3><ul class="rows">{pubs}</ul>
  <p class="note">{esc(t['pub_more'])} <a href="{SCHOLAR}" rel="noopener">Google Scholar</a>, <a href="{ORCID}" rel="noopener">ORCID</a></p>
</div></section>
<section id="contact" class="band" aria-labelledby="c-h"><div class="wrap">
  <div class="sh"><h2 id="c-h">{esc(t['c_h'])}</h2><p>{esc(t['c_sub'])}</p></div>
  {form}
  <div class="contact">{cts}</div>
</div></section>
</main>
<footer><div class="wrap">
  <div><b>{esc(t['name'])}</b>{esc(t['ft_role'])}<br>{esc(t['ft_board'])}</div>
  <div><b><a href="{TEL}">{TEL_H}</a></b><a href="mailto:{MAIL}">{MAIL}</a><br><a href="mailto:{MAIL_W}">{MAIL_W}</a></div>
  <div><a href="{ORCID}" rel="noopener">ORCID</a> · <a href="{SCHOLAR}" rel="noopener">Google Scholar</a> · <a href="{ETEAM}" rel="noopener">{'ГО «Е-ТЕАМ»' if t['lang']=='uk' else 'NGO E-TEAM'}</a></div>
  <p class="base">{esc(t['ft_base'])}</p>
</div></footer>
<script>{js}</script>"""
    main_html, script = body.split("<script>", 1)
    for w in ("«Е-ТЕАМ»", "E-TEAM"):
        main_html = main_html.replace(w, f'<span class="nw">{w}</span>')
    body = main_html + "<script>" + script
    if skeleton:
        return (f'<!doctype html><html lang="{t["lang"]}"><head><meta charset="utf-8">'
                f'<meta name="viewport" content="width=device-width, initial-scale=1">{head}</head><body>{body}</body></html>')
    return head + body


def make_og(path):
    from PIL import Image, ImageDraw, ImageFont
    W, H = 1200, 630
    im = Image.new("RGB", (W, H), (255, 255, 255)); d = ImageDraw.Draw(im)
    fs = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"; fr = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    fb = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    d.rectangle([0, 0, W, 14], fill=(20, 32, 46))
    d.rectangle([80, 120, 128, 126], fill=(13, 95, 89))
    d.text((80, 150), "Дмитро Паламарчук", font=ImageFont.truetype(fs, 70), fill=(20, 32, 46))
    d.text((80, 250), "Консультант з енергоефективності", font=ImageFont.truetype(fb, 36), fill=(20, 32, 46))
    for i, line in enumerate(["Муніципальні енергетичні плани · консультації ОСББ", "щодо програм Фонду енергоефективності · енергоспільноти"]):
        d.text((80, 320 + i * 46), line, font=ImageFont.truetype(fr, 30), fill=(74, 88, 102))
    d.line([80, 470, 1120, 470], fill=(213, 219, 225), width=2)
    d.text((80, 500), "IFC 2019–2025 · GIZ · UNIDO · EU LIFE", font=ImageFont.truetype(fr, 28), fill=(13, 95, 89))
    d.text((80, 545), "Черкаси · +380 97 889 13 85", font=ImageFont.truetype(fr, 28), fill=(74, 88, 102))
    im.save(path)


if __name__ == "__main__":
    for d in ("preview", "dist"):
        os.makedirs(os.path.join(HERE, d), exist_ok=True)
    open(os.path.join(HERE, "preview", "index.html"), "w").write(page(T["ua"], False))
    open(os.path.join(HERE, "preview", "en.html"), "w").write(page(T["en"], True))
    open(os.path.join(HERE, "dist", "index.html"), "w").write(page(T["ua"], True, seo=True))
    open(os.path.join(HERE, "dist", "en.html"), "w").write(page(T["en"], True, seo=True))
    make_og(os.path.join(HERE, "dist", "og.png"))
    open(os.path.join(HERE, "dist", "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}sitemap.xml\n")
    open(os.path.join(HERE, "dist", "sitemap.xml"), "w").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f'<url><loc>{BASE}</loc><lastmod>2026-10-20</lastmod></url>\n<url><loc>{BASE}en.html</loc><lastmod>2026-10-20</lastmod></url>\n</urlset>\n')
    open(os.path.join(HERE, "dist", ".nojekyll"), "w").write("")
    print("ok")
