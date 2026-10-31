"""Personal site of Dmytro Palamarchuk — multi-page (рішення № 36): index, osbb, mep, energospilnoty (UA) + en (EN home).
Trust-first design (DESIGN.md, 20.10.2026).

Outputs:
  preview/index.html  - UA page without document skeleton (Artifact preview)
  preview/en.html     - EN page with full skeleton
  dist/               - index.html, en.html, og.png, robots.txt, sitemap.xml, .nojekyll (GitHub Pages)
Texts: positioning and copy from «Особистий сайт — позиціонування і тексти 20.10.2026»,
figures from «Особистий сайт — реєстр фактів 20.10.2026» (IFC report EEFP_Report_#2-22_Cherkasy-2025_06).
"""
import json, os, re

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
footer .base{grid-column:1/-1;border-top:1px solid #2c3846;padding-top:var(--s-5);margin-top:var(--s-2);display:flex;justify-content:space-between;align-items:flex-end;gap:var(--s-5);flex-wrap:wrap}
footer .legal{margin:0;display:flex;flex-direction:column;gap:3px;padding-left:var(--s-4);border-left:2px solid #4fb3a8}
footer .lg-k{font-size:13px;line-height:1.3;letter-spacing:.02em;color:var(--on-footer-2)}
footer .lg-n{font-family:var(--serif);font-weight:600;font-size:19px;line-height:1.25;color:var(--on-footer);letter-spacing:-.005em}
footer .cr{margin:0;font-size:13px;color:var(--on-footer-2)}

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
@media print{.hdr .links,.tools .lang,.explain,.req,footer .cr{display:none}section{padding-block:24px}}
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



# ---------------------------------------------------------------------------
# Multi-page structure (рішення № 36): головна + ОСББ (проєкт GIZ) + МЕП + енергоспільноти; EN — лише головна.
# ---------------------------------------------------------------------------

CSS_PAGES = r"""
.nav .links a[aria-current="page"]{color:var(--primary);text-decoration:underline;text-decoration-thickness:2px;text-underline-offset:6px}
.phero{padding-block:64px var(--s-8)}
@media (max-width:400px){.links{font-size:14.5px !important;gap:var(--s-2) !important}}
.phero .kicker{margin-bottom:var(--s-3)}
.phero h1{font-size:clamp(32px,4.4vw,44px);max-width:20em;text-wrap:balance}
.phero .lead{margin-bottom:var(--s-5)}
.tag-free{display:inline-block;background:var(--tint);color:var(--ink);font-weight:600;font-size:var(--fs-small);padding:6px 12px;border-radius:var(--r-1);margin:0 0 var(--s-5)}
.entries{list-style:none;margin:0;padding:0;border-top:2px solid var(--ink)}
.entries li{border-bottom:1px solid var(--rule)}
.entries a{display:grid;grid-template-columns:44px minmax(0,1fr) auto;gap:var(--s-5);align-items:center;padding-block:var(--s-5);text-decoration:none;color:var(--ink)}
.entries a:hover h3{color:var(--primary);text-decoration:underline;text-underline-offset:4px}
.entries svg{width:32px;height:32px;color:var(--ink-2)}
.entries h3{margin:0 0 2px}
.entries p{color:var(--ink-2);font-size:16px;max-width:60ch}
.entries .arr{color:var(--primary);font-weight:600;white-space:nowrap}
.plan{list-style:none;margin:0;padding:0;border-top:2px solid var(--ink)}
.plan>li{display:grid;grid-template-columns:64px minmax(0,1fr) minmax(0,.75fr);gap:var(--s-6);padding-block:var(--s-6);border-bottom:1px solid var(--rule)}
.plan .n{font-family:var(--serif);font-weight:600;font-size:28px;line-height:1;color:var(--primary)}
.plan h3{margin-bottom:var(--s-2)}
.plan .first{display:inline-block;margin-left:var(--s-2);vertical-align:3px;font-family:var(--sans);font-size:13px;font-weight:600;color:var(--primary);border:1px solid var(--primary);border-radius:var(--r-1);padding:1px 7px}
.plan p{max-width:var(--measure)}
.plan .you{font-size:var(--fs-small);color:var(--ink-2);border-left:2px solid var(--rule);padding-left:var(--s-4)}
.plan .you b{display:block;color:var(--ink-3);font-weight:600;margin-bottom:2px}
.plan-note{margin-top:var(--s-5);color:var(--ink-2);max-width:var(--measure)}
.check{list-style:none;margin:0;padding:0;display:grid;gap:var(--s-3);max-width:760px}
.check li{position:relative;padding-left:32px;font-size:17px}
.check li::before{content:"?";position:absolute;left:0;top:1px;width:22px;height:22px;border-radius:50%;border:1.5px solid var(--primary);color:var(--primary);font-weight:600;font-size:13px;display:flex;align-items:center;justify-content:center}
.links-out{margin:var(--s-5) 0 0;padding-left:20px;display:grid;gap:var(--s-2)}
.mentions{list-style:none;margin:0;padding:0;display:grid;gap:var(--s-3)}
.mentions li{display:grid;grid-template-columns:170px minmax(0,1fr);gap:var(--s-6)}
.mentions .y{font-weight:600;color:var(--ink-2);font-size:var(--fs-small);padding-top:2px}
.practice{margin-top:var(--s-6);padding:var(--s-4) var(--s-5);border-left:3px solid var(--primary);background:var(--band);max-width:860px}
.practice p{color:var(--ink-2)}
@media (max-width:900px){
  .plan>li{grid-template-columns:44px minmax(0,1fr);gap:var(--s-3) var(--s-4)}
  .plan .you{grid-column:2}
}
@media (max-width:560px){
  .entries a{grid-template-columns:32px minmax(0,1fr);gap:var(--s-3)}
  .entries .arr{grid-column:2}
  .mentions li{grid-template-columns:minmax(0,1fr);gap:var(--s-1)}
  .phero{padding-block:var(--s-6) var(--s-7)}
}
"""

JS_PAGES = r"""
(function(){var dr=document.body.getAttribute('data-role'); if(dr===null||dr==='') return;
  var r=document.getElementById('role-'+dr); if(r){r.checked=true;r.dispatchEvent(new Event('change'));}})();
"""

ROLES_UA = ["ОСББ або управитель", "Громада (ОМС)", "Ініціативна група / енергоспільнота", "Міжнародна організація / донор", "Інше"]
NEEDS_UA = ["Консультація", "Участь у загальних зборах ОСББ", "Огляд будинку і розрахунок", "Муніципальний енергетичний план", "Енергетична спільнота: з чого почати", "Експертна участь у проєкті"]
ROLES_EN = ["Homeowner association or manager", "Municipality", "Community group / energy community", "International organisation / donor", "Other"]
NEEDS_EN = ["Consultation", "Attendance at an HOA general meeting", "Building walk-through and calculation", "Municipal energy plan", "Energy community: where to start", "Expert input to a project"]

COMMON = {
 "ua": dict(lang="uk", skip="Перейти до змісту", nav_label="Основна навігація", call="Зателефонувати",
            brand_sub="Енергоефективність · МЕП · енергоспільноти",
            f_role="Хто звертається", roles=ROLES_UA, f_need="Що потрібно", needs=NEEDS_UA,
            f_place="Населений пункт", f_place_ph="напр., Сміла", f_name="Ваше ім’я", f_contact="Телефон або email",
            f_msg="Коротко про питання", f_msg_ph="що є зараз і що хочете змінити",
            f_err="Оберіть, хто звертається, і вкажіть ім’я та контакт, щоб я міг відповісти.",
            f_btn="Скласти лист", f_out_h="Лист готовий. Перевірте текст і надішліть.", f_send="Надіслати поштою",
            copy="Копіювати текст", copied="Скопійовано", copy_short="Копіювати",
            f_hdr="Звернення з сайту", f_lab=["Хто", "Населений пункт", "Що потрібно", "Питання", "Контакт"],
            form_h="Опишіть ваше питання",
            form_hint="Форма складе текст листа. Ви надішлете його поштою або скопіюєте в месенджер — дані нікуди не передаються автоматично і не зберігаються.",
            contacts=[("Email", MAIL, "mailto:" + MAIL, True), ("Корпоративна пошта, ГО «Е-ТЕАМ»", MAIL_W, "mailto:" + MAIL_W, True),
                      ("Телефон", TEL_H, TEL, True), ("Сайт ГО «Е-ТЕАМ»", "eteamngo.org", ETEAM, False),
                      ("Google Scholar", "Профіль і цитування", SCHOLAR, False), ("ORCID", "0000-0002-6023-9780", ORCID, False)],
            name="Дмитро Паламарчук", ft_role="Незалежний експерт · Черкаси", ft_board="Член правління ГО «Е-ТЕАМ»", ft_org="ГО «Е-ТЕАМ»",
            ft_base="© 2026 Дмитро Паламарчук · Оновлено: жовтень 2026",
            lg_k="Фізична особа — підприємець", lg_n="Паламарчук Дмитро Миколайович", lg_aria="Юридична особа, що надає послуги",
            c_h="Напишіть, з чим звертаєтеся", c_sub="Опишіть питання в кількох словах — я відповім. Або просто зателефонуйте.",
            th_cap="Схема, не знімок конкретного будинку", th_before="До утеплення", th_after="Після",
            th_aria="Схема: панельний будинок до утеплення з теплими швами і вікнами, та після утеплення з холодним рівномірним фасадом",
            th_cold="холодніше", th_warm="тепліше",
            jobTitle="Консультант з енергоефективності та муніципального енергетичного планування"),
 "en": dict(lang="en", skip="Skip to content", nav_label="Main navigation", call="Call",
            brand_sub="Energy efficiency · Energy plans · Energy communities",
            f_role="Who you are", roles=ROLES_EN, f_need="What you need", needs=NEEDS_EN,
            f_place="Town or village", f_place_ph="e.g. Smila", f_name="Your name", f_contact="Phone or email",
            f_msg="Your question in brief", f_msg_ph="what exists now and what you want to change",
            f_err="Please choose who you are and enter your name and a contact so I can reply.",
            f_btn="Compose email", f_out_h="Your message is ready. Check the text and send it.", f_send="Send by email",
            copy="Copy text", copied="Copied", copy_short="Copy",
            f_hdr="Request from the website", f_lab=["Who", "Location", "Needs", "Question", "Contact"],
            form_h="Describe your question",
            form_hint="The form composes an email. You send it from your mail app or copy it into a messenger — nothing is transmitted automatically or stored.",
            contacts=[("Email", MAIL, "mailto:" + MAIL, True), ("Work email, NGO E-TEAM", MAIL_W, "mailto:" + MAIL_W, True),
                      ("Phone", TEL_H, TEL, True), ("NGO E-TEAM website", "eteamngo.org", ETEAM, False),
                      ("Google Scholar", "Profile and citations", SCHOLAR, False), ("ORCID", "0000-0002-6023-9780", ORCID, False)],
            name="Dmytro Palamarchuk", ft_role="Independent expert · Cherkasy, Ukraine", ft_board="Board member, NGO E-TEAM", ft_org="NGO E-TEAM",
            ft_base="© 2026 Dmytro Palamarchuk · Updated: October 2026",
            lg_k="Sole proprietor (Ukrainian FOP)", lg_n="Dmytro Mykolaiovych Palamarchuk", lg_aria="Legal entity providing the services",
            c_h="Get in touch", c_sub="Describe your question in a few words and I will reply — or simply call.",
            jobTitle="Energy efficiency and municipal energy planning consultant"),
}

NAV_UA = [("index.html", "Головна"), ("osbb.html", "ОСББ"), ("mep.html", "МЕП громадам"), ("energospilnoty.html", "Енергоспільноти")]

MENTIONS_UA = [
    ("2023", "Фонд енергоефективності — брошура з історіями успіху: регіональний радник по Черкаській області",
     "https://eefund.org.ua/wp-content/uploads/2023/12/broshura-istoriyi-uspihu.pdf"),
    ("2019", "«Дзвін»: семінар для співвласників у Черкасах — регіональний консультант IFC з енергоефективності в житловому секторі",
     "https://dzvin.media/news/trend-na-energooshhadnist-cherkashhan-navchaly-zaluchaty-koshty-na-vtilennya-enregoefektyvnyh-zahodiv/"),
]
PUB_JOURNAL = ("2021", "Регіональний вимір енергоефективності та енергетичної безпеки України",
               "Бізнесінформ, 2021, № 7, с. 127–134. DOI 10.32983/2222-4459-2021-7-127-134",
               "https://doi.org/10.32983/2222-4459-2021-7-127-134")
PUB_JOURNAL_EN = ("2021", "Regional dimension of energy efficiency and energy security of Ukraine",
                  "Business Inform, 2021, No. 7, pp. 127–134 (in Ukrainian). DOI 10.32983/2222-4459-2021-7-127-134",
                  "https://doi.org/10.32983/2222-4459-2021-7-127-134")

HOME_UA = dict(
  file="index.html", other="en.html", other_label="EN", other_lang="en", role_default="",
  title="Дмитро Паламарчук", seo_title="Дмитро Паламарчук — енергоефективність, МЕП, енергоспільноти",
  description="Дмитро Паламарчук — консультант з енергоефективності: консультації ОСББ у проєкті GIZ, муніципальні енергетичні плани для громад, енергетичні спільноти. Черкаси.",
  kicker="Черкаси · працюю з громадами різних областей",
  role="Енергоефективність житла й енергетичне планування громад",
  lead="Консультую ОСББ щодо програм Фонду енергоефективності, розробляю муніципальні енергетичні плани в команді ГО «Е-ТЕАМ», допомагаю ініціативним групам зрозуміти, з чого почати енергетичну спільноту.",
  cta1="Описати своє питання",
  facts_h="Програми, у яких працюю, і моя роль",
  facts=[("IFC (Група Світового банку)", "Регіональний радник з енергоефективності, проєкт «Ukraine EE Fund», 2019–2025"),
         ("GIZ", "Регіональний радник з енергоефективності в мережі ГО «Е-ТЕАМ», з 2026"),
         ("UNIDO", "МЕП Сміли, 2026 — у команді ГО «Е-ТЕАМ»"),
         ("Програма ЄС LIFE", "Координатор проєкту LIFE-ECOss від ГО «Е-ТЕАМ», з 2026"),
         ("Фонд енергоефективності", "Консультую ОСББ — учасників програм «Енергодім» і «ВідновиДІМ»")],
  facts_more="Досвід",
  entries_h="З чим звертатися",
  entries=[("osbb.html", 1, "ОСББ: консультації щодо енергомодернізації", "Безкоштовно в межах проєкту GIZ. Як проходить шлях від першої розмови до рішення співвласників і що підготувати."),
           ("mep.html", 0, "Громадам: муніципальний енергетичний план", "МЕП за Методикою (наказ № 1163 від 21.12.2023): етапи, що потрібно від громади, приклади."),
           ("energospilnoty.html", 2, "Ініціативним групам: енергетичні спільноти", "З чого почати і як оцінити, чи є підстави для спільноти, — до купівлі обладнання.")],
  entries_go="Детальніше",
  e_h="Досвід",
  timeline=[
    ("2025 — дотепер", "Член правління, координатор проєктів міжнародної співпраці", "ГО «Е-ТЕАМ»", ETEAM,
     "Керую розробкою муніципальних енергетичних планів у команді ГО: МЕП Сарненської громади (у роботі), МЕП Смілянської громади (проєкт UNIDO, передано на публічне обговорення у 2026 році). Координатор проєкту ЄС LIFE-ECOss від ГО «Е-ТЕАМ». Уповноважений представник (LEAR) організації на порталі Funding & Tenders Європейської Комісії."),
    ("2026 — дотепер", "Регіональний радник з енергоефективності, Черкаська область", "Мережа регіональних радників ГО «Е-ТЕАМ», проєкт GIZ", None,
     "Консультую ОСББ щодо програм «Енергодім» і «ВідновиДІМ», проводжу семінари для ОСББ і посадовців громад."),
    ("2019 — 2025", "Регіональний радник з енергоефективності, Черкаська область (з 2024 — також Сумська)", "Проєкт IFC «Ukraine EE Fund», Група Світового банку", None,
     "Консультував ОСББ, їхніх менеджерів проєктів і підрядників, оглядав будинки й рахував фінансовий результат модернізації, брав участь у загальних зборах співвласників, проводив семінари для ОСББ і органів місцевого самоврядування."),
    ("2012 — 2026", "Викладач, з 2017 — доцент", "Черкаський державний технологічний університет", None,
     "Курси «Міжнародна економіка», «Європейська інтеграція», «Економіка сталого розвитку»; дослідження адаптації енергетичної політики ЄС до українських умов.")],
  practice_h="Практика в цифрах, 2019–2026",
  practice="1 200+ консультацій для ОСББ · 50 загальних зборів співвласників, у яких я брав участь · 81 семінар, вебінар чи форум, на яких я виступав (40 організував). Джерело — щомісячні звіти регіонального радника IFC і GIZ.",
  edu_h="Освіта",
  edu=[("2014", "Кандидат економічних наук — Київський національний університет імені Тараса Шевченка"),
       ("2010", "Магістр економіки та підприємництва (з відзнакою) — Черкаський державний технологічний університет")],
  pubs_h="Публікації",
  pubs=[PUB_JOURNAL,
        ("2024", "Інформаційні кампанії як інструмент зміни поведінки споживачів щодо використання енергії: досвід ЄС", "Матеріали III Міжнародної науково-практичної конференції, Тернопіль, ЗУНУ", PUBS_URLS[0]),
        ("2022", "Дослідження чинників, що впливають на рішення співвласників щодо модернізації багатоквартирних будинків", "Матеріали IX Міжнародної науково-практичної конференції, ЧДТУ", PUBS_URLS[2])],
  pub_more="Повний перелік:",
  mentions_h="Згадки в інших джерелах",
  mentions=MENTIONS_UA,
)

OSBB_UA = dict(
  file="osbb.html", role_default="0",
  title="Консультації для ОСББ — Дмитро Паламарчук",
  seo_title="Консультації для ОСББ щодо енергомодернізації — Черкаська область, проєкт GIZ",
  description="Безкоштовні консультації для ОСББ Черкаської області щодо програм Фонду енергоефективності «Енергодім» і «ВідновиДІМ»: огляд будинку, розрахунок, підготовка рішення співвласників і заявки.",
  kicker="Для ОСББ · Черкаська область",
  h1="Консультації для ОСББ щодо енергомодернізації будинку",
  lead="Консультую ОСББ як регіональний радник з енергоефективності мережі ГО «Е-ТЕАМ» у проєкті GIZ: допомагаю розібратися з програмами Фонду енергоефективності, порахувати, чи має сенс модернізація для вашого будинку, і пройти процедури.",
  free="Для ОСББ консультації безкоштовні",
  plan_h="Як проходить робота",
  plan_sub="Шлях однаковий для більшості будинків. На кожному кроці рішення за правлінням і співвласниками; я пояснюю, рахую і допомагаю з документами.",
  you_lbl="Ваша частина",
  plan=[("Знайомство", True, "Семінар для ОСББ або перша розмова телефоном чи зустріч. Говоримо про будинок, про програми Фонду і про те, чи варто рухатися далі.", "Розповісти про будинок і про те, що турбує мешканців."),
        ("Огляд будинку", False, "Приїжджаю й оглядаю будинок разом із головою правління: фасад, дах, підвал, тепловий пункт, вікна й двері в під'їздах.", "Забезпечити доступ до технічних приміщень, підготувати рахунки за тепло і технічний паспорт."),
        ("Розрахунок і орієнтовні ціни", False, "Рахую варіанти заходів, орієнтовну вартість, внесок кожної квартири і можливу економію; пояснюю умови програм і різницю між пакетами.", "Обговорити варіанти на правлінні."),
        ("Рішення співвласників", False, "Співвласники вирішують, чи йти в програму і з яким набором заходів. За потреби допомагаю підготувати питання до загальних зборів і пояснюю програму мешканцям.", "Провести загальні збори й ухвалити рішення."),
        ("Заявка до Фонду", False, "Консультую щодо пакета документів, перевіряю його перед поданням, пояснюю зауваження Фонду.", "Зібрати документи, укласти договори з енергоаудитором і проєктантом."),
        ("Супровід до завершення", False, "Консультую голову ОСББ, менеджера проєкту і підрядника на етапах проєктування, робіт і верифікації.", "Керувати проєктом і ухвалювати рішення.")],
  plan_note="Не кожен будинок доходить до проєкту — і це нормально. Після огляду й розрахунку стає видно, чи готові співвласники до модернізації зараз.",
  self_h="Перш ніж почати — кілька запитань до себе",
  self_sub="Від відповідей на них залежить, чи дійде будинок до проєкту.",
  selfcheck=["Чи є в правлінні людина, готова вести проєкт кілька місяців?",
             "Як співвласники ставляться до внесків на модернізацію будинку?",
             "Чи немає в ОСББ значних боргів за внесками?",
             "Чи є технічний паспорт будинку і рахунки за тепло за останні сезони?",
             "Чи зможете зібрати загальні збори з потрібною кількістю голосів?"],
  prep_h="Що підготувати до першої розмови",
  prep=["Рахунки або дані про споживання тепла за 2–3 останні опалювальні сезони",
        "Технічний паспорт будинку: рік побудови, поверховість, площа, кількість квартир",
        "Протоколи зборів щодо модернізації, якщо вже були",
        "Енергетичний сертифікат або енергоаудит, якщо є",
        "Фото фасаду, підвалу і теплового пункту"],
  progs_h="Умови програм — у першоджерелі",
  progs_sub="Умови й ліміти програм змінюються, тому посилаюся на сайт Фонду, а на консультації пояснюю, що вони означають для вашого будинку.",
  progs=[("Фонд енергоефективності — офіційний сайт", "https://eefund.org.ua/")],
  th_kicker="Огляд будинку", th_h="Що показує тепловізор",
  th_p="Тепловізор забарвлює теплі ділянки фасаду в жовтий і помаранчевий. Так видно, де будинок втрачає тепло: шви між панелями, вікна, балкони. Після утеплення фасад на знімку «холоднішає», бо тепло лишається всередині.",
)

MEP_UA = dict(
  file="mep.html", role_default="1",
  title="Муніципальний енергетичний план — Дмитро Паламарчук",
  seo_title="Муніципальний енергетичний план (МЕП) для громади — розробка за Методикою № 1163",
  description="Розробка муніципального енергетичного плану (МЕП) для громади за Методикою, затвердженою наказом № 1163 від 21.12.2023: етапи, що потрібно від громади, приклади — Сміла, Сарни.",
  kicker="Для громад",
  h1="Муніципальний енергетичний план, який громада може виконати",
  lead="Розробляю МЕП у команді ГО «Е-ТЕАМ» або як незалежний експерт — залежно від вимог замовника. Мета — план, у якому громада розуміє кожну цифру і може його оновлювати.",
  plan_h="Етапи роботи",
  plan_sub="За Методикою, затвердженою наказом № 1163 від 21.12.2023. Порядок і обсяг кожного етапу уточнюємо з громадою на старті.",
  you_lbl="Що потрібно від громади",
  plan=[("Старт і робоча група", True, "Узгоджуємо межі плану, строки й відповідальних; громада визначає робочу групу.", "Рішення про розробку, відповідальна особа, контакти структурних підрозділів."),
        ("Збір і перевірка даних", False, "Збираємо дані про споживання енергії бюджетними будівлями, житлом, теплопостачанням, освітленням, транспортом; перевіряємо їх на повноту й узгодженість.", "Дані від підрозділів і комунальних підприємств."),
        ("Енергетичний баланс і базова лінія", False, "Будуємо енергетичний баланс громади і базову лінію, з якою порівнюватимуться результати.", "Погодити методичні рішення щодо даних."),
        ("Цілі й заходи", False, "Визначаємо цілі й формуємо каталог заходів і проєктів з оцінкою вартості та ефекту.", "Пріоритети громади, перелік проєктів, які вже розглядаються."),
        ("План фінансування і реалізації", False, "Пов'язуємо заходи з джерелами фінансування й строками.", "Узгодити план з бюджетними можливостями."),
        ("Обговорення й затвердження", False, "Супроводжую доопрацювання плану після обговорення.", "Організувати обговорення і затвердження."),
        ("Моніторинг", False, "Допомагаю налагодити щорічний звіт про виконання плану.", "Щороку збирати дані для звіту.")],
  plan_note="Стратегічна екологічна оцінка і громадські обговорення — окремі роботи; обговорюємо їх окремо.",
  ex_h="Приклади",
  examples=[("МЕП Смілянської громади", "Проєкт UNIDO, 2026, у команді ГО «Е-ТЕАМ». План передано на публічне обговорення."),
            ("МЕП Сарненської громади", "У роботі, у команді ГО «Е-ТЕАМ».")],
  prep_h="Що підготувати до першої розмови",
  prep=["Дані про споживання енергії бюджетними будівлями за останні 3 роки",
        "Чинні програми енергоефективності, SECAP або МЕП, якщо є",
        "Контакт відповідальної особи: енергоменеджер, відділ ЖКГ чи економіки",
        "Перелік проєктів, які громада вже розглядає"],
)

EC_UA = dict(
  file="energospilnoty.html", role_default="2",
  title="Енергетичні спільноти — Дмитро Паламарчук",
  seo_title="Енергетична спільнота: з чого почати — консультації для ініціативних груп і громад",
  description="Енергетичні спільноти: з чого почати ініціативній групі, ОСББ чи громаді — оцінка учасників, об'єкта, споживання, правової форми й фінансування. Проєкт ЄС LIFE-ECOss.",
  kicker="Для ініціативних груп, ОСББ і громад",
  h1="Енергетична спільнота: почати з оцінки, а не з купівлі обладнання",
  lead="Енергетична спільнота — це коли люди, ОСББ, бізнес чи громада разом виробляють, зберігають або купують енергію для себе. Правила для таких спільнот в Україні ще формуються, тому перший крок — чесна оцінка, чи є для неї підстави.",
  plan_h="З чого почати",
  plan_sub="Ці питання ми проходимо на першій консультації.",
  you_lbl="Що підготувати",
  plan=[("Хто учасники", True, "Хто має намір увійти до спільноти і з якою метою: економія, надійність, власна генерація.", "Склад групи і контакти."),
        ("Об'єкт і споживання", False, "Де може бути генерація чи накопичення — дах, ділянка, котельня — і скільки енергії споживають учасники.", "Адреса об'єкта, орієнтовне річне споживання."),
        ("Правова форма", False, "Яка організаційно-правова форма підходить і чи може нею стати, наприклад, ваше ОСББ.", "Документи наявної організації, якщо є."),
        ("Бізнес-модель і фінансування", False, "На чому спільнота триматиметься економічно і звідки взяти гроші на старт.", "Очікування учасників щодо внесків."),
        ("План підготовки", False, "Результат — план, з яким можна йти до учасників, громади й партнерів.", "Позиція органу місцевого самоврядування.")],
  plan_note="Координую участь ГО «Е-ТЕАМ» у проєкті ЄС LIFE-ECOss (2026–2029): у Луцьку створюємо центр підтримки енергетичних спільнот.",
)

HOME_EN = dict(
  file="en.html", other="index.html", other_label="UA", other_lang="uk", role_default="",
  title="Dmytro Palamarchuk", seo_title="Dmytro Palamarchuk — energy efficiency, municipal energy planning, energy communities (Ukraine)",
  description="Dmytro Palamarchuk — energy efficiency consultant in Ukraine: regional advisor to homeowner associations (GIZ project), municipal energy plans, energy communities. Cherkasy.",
  kicker="Cherkasy, Ukraine · working with municipalities across regions",
  role="Residential energy efficiency and municipal energy planning in Ukraine",
  lead="Regional energy efficiency advisor to homeowner associations (IFC 2019–2025, GIZ since 2026), developer of municipal energy plans with NGO E-TEAM, project coordinator of the EU LIFE-ECOss energy community project.",
  cta1="Get in touch",
  facts_h="Programmes I work in, and my role",
  facts=[("IFC (World Bank Group)", "Regional energy efficiency advisor, “Ukraine EE Fund” project, 2019–2025"),
         ("GIZ", "Regional energy efficiency advisor in the NGO E-TEAM network, since 2026"),
         ("UNIDO", "Municipal energy plan for Smila, 2026 — in the NGO E-TEAM team"),
         ("EU LIFE Programme", "Project coordinator of LIFE-ECOss for NGO E-TEAM, since 2026"),
         ("Energy Efficiency Fund of Ukraine", "Advising HOAs in the “Energodim” and “VidnovyDIM” programmes")],
  facts_more="Experience",
  formats_h="How I work with programmes and partners",
  formats="As an independent expert (registered sole proprietor) or as part of the NGO E-TEAM team, depending on programme requirements. Pages for Ukrainian homeowner associations and municipalities are in Ukrainian.",
  e_h="Experience",
  timeline=[
    ("2025 — present", "Board member, international cooperation projects coordinator", "NGO E-TEAM", ETEAM,
     "Lead the development of municipal energy plans in the NGO team: Sarny (in progress), Smila (UNIDO project, released for public consultation in 2026). Project coordinator of the EU LIFE-ECOss project for NGO E-TEAM. LEAR of the organisation on the European Commission’s Funding & Tenders portal."),
    ("2026 — present", "Regional energy efficiency advisor, Cherkasy oblast", "NGO E-TEAM regional advisor network, GIZ project", None,
     "Advising homeowner associations on the “Energodim” and “VidnovyDIM” programmes; seminars for HOAs and municipal officials."),
    ("2019 — 2025", "Regional energy efficiency advisor, Cherkasy oblast (from 2024 also Sumy)", "IFC “Ukraine EE Fund” project, World Bank Group", None,
     "Advised HOAs, their project managers and contractors; building walk-throughs and financial calculations; participation in co-owners’ general meetings; seminars for HOAs and local authorities."),
    ("2012 — 2026", "Lecturer, Associate Professor from 2017", "Cherkasy State Technological University", None,
     "Courses in International Economics, European Integration and Economics of Sustainable Development; research on adapting EU energy policy to Ukraine.")],
  practice_h="Practice in figures, 2019–2026",
  practice="1,200+ consultations for homeowner associations · 50 co-owners’ general meetings attended · 81 seminars, webinars and forums as a speaker (40 organised). Source: monthly regional advisor reports to IFC and GIZ.",
  edu_h="Education",
  edu=[("2014", "PhD in Economics — Taras Shevchenko National University of Kyiv"),
       ("2010", "Master’s in Economics and Entrepreneurship (Honours) — Cherkasy State Technological University")],
  pubs_h="Publications",
  pubs=[PUB_JOURNAL_EN,
        ("2024", "Information campaigns as a tool for changing consumer energy behaviour: EU experience", "III International Scientific and Practical Conference, Ternopil, WUNU (in Ukrainian)", PUBS_URLS[0]),
        ("2022", "Factors influencing homeowners’ decisions on the modernisation of multi-apartment buildings", "IX International Scientific and Practical Conference, ChSTU (in Ukrainian)", PUBS_URLS[2])],
  pub_more="Full list:",
  mentions_h="Mentioned in",
  mentions=[("2023", "Energy Efficiency Fund of Ukraine — success stories brochure: regional advisor for Cherkasy oblast (in Ukrainian)", MENTIONS_UA[0][2]),
            ("2019", "Dzvin media: seminar for co-owners in Cherkasy — IFC regional energy efficiency consultant (in Ukrainian)", MENTIONS_UA[1][2])],
)


# ----------------------------------------------------------------- components

def c_header(c, cur, nav, other=None):
    links = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h == cur else ""}>{esc(l)}</a>' for h, l in nav)
    lang = f'<a class="lang" href="{other[0]}" hreflang="{other[2]}" lang="{other[2]}">{other[1]}</a>' if other else ''
    return f"""<a class="skip" href="#main">{esc(c['skip'])}</a>
<header class="hdr"><div class="wrap">
  <a class="brand" href="{nav[0][0]}"><b>{esc(c['name'])}</b><span>{esc(c['brand_sub'])}</span></a>
  <nav class="nav" aria-label="{esc(c['nav_label'])}">
    <div class="links">{links}</div>
    <div class="tools"><a class="tel" href="{TEL}">{TEL_H}</a>{lang}</div>
  </nav>
</div></header>"""


def c_footer(c):
    return f"""<footer><div class="wrap">
  <div><b>{esc(c['name'])}</b>{esc(c['ft_role'])}<br>{esc(c['ft_board'])}</div>
  <div><b><a href="{TEL}">{TEL_H}</a></b><a href="mailto:{MAIL}">{MAIL}</a><br><a href="mailto:{MAIL_W}">{MAIL_W}</a></div>
  <div><a href="{ORCID}" rel="noopener">ORCID</a> · <a href="{SCHOLAR}" rel="noopener">Google Scholar</a> · <a href="{ETEAM}" rel="noopener">{esc(c['ft_org'])}</a></div>
  <div class="base"><p class="legal" aria-label="{esc(c['lg_aria'])}"><span class="lg-k">{esc(c['lg_k'])}</span><span class="lg-n">{esc(c['lg_n'])}</span></p><p class="cr">{esc(c['ft_base'])}</p></div>
</div></footer>"""


def c_contact(c, band=True):
    roles = "".join(f'<label><input type="radio" name="role" value="{esc(r)}" id="role-{k}"> {esc(r)}</label>' for k, r in enumerate(c["roles"]))
    needs = "".join(f'<label><input type="checkbox" name="need" value="{esc(r)}" id="need-{k}"> {esc(r)}</label>' for k, r in enumerate(c["needs"]))
    cts = ""
    for k, v, href, cp in c["contacts"]:
        ext = ' rel="noopener"' if href.startswith("http") else ''
        btn = f'<button class="copy" type="button" data-v="{esc(v)}">{esc(c["copy_short"])}</button>' if cp else ''
        cts += f'<div class="ct"><span class="k">{esc(k)}</span><a class="v" href="{esc(href)}"{ext}>{esc(v)}</a>{btn}</div>'
    return f"""<section id="contact" class="{'band' if band else ''}" aria-labelledby="c-h"><div class="wrap">
  <div class="sh"><h2 id="c-h">{esc(c['c_h'])}</h2><p>{esc(c['c_sub'])}</p></div>
  <div class="req"><form class="form" id="reqform" novalidate>
<h3>{esc(c['form_h'])}</h3><p class="hint">{esc(c['form_hint'])}</p>
<fieldset><legend>{esc(c['f_role'])}</legend><div class="opts">{roles}</div></fieldset>
<fieldset><legend>{esc(c['f_need'])}</legend><div class="opts">{needs}</div></fieldset>
<div class="row2"><div><label class="l" for="f-place">{esc(c['f_place'])}</label><input type="text" id="f-place" autocomplete="address-level2" placeholder="{esc(c['f_place_ph'])}"></div>
<div><label class="l" for="f-name">{esc(c['f_name'])}</label><input type="text" id="f-name" autocomplete="name"></div></div>
<div><label class="l" for="f-contact">{esc(c['f_contact'])}</label><input type="text" id="f-contact" autocomplete="email"></div>
<div><label class="l" for="f-msg">{esc(c['f_msg'])}</label><textarea id="f-msg" placeholder="{esc(c['f_msg_ph'])}"></textarea></div>
<p class="err" id="f-err" tabindex="-1" hidden>{esc(c['f_err'])}</p>
<div><button class="btn btn-p" type="submit">{esc(c['f_btn'])}</button></div>
</form>
<div class="out" id="f-out" hidden aria-live="polite"><h3>{esc(c['f_out_h'])}</h3><pre id="f-text"></pre>
<div class="acts"><a class="btn btn-p" id="f-mail" href="mailto:{MAIL}">{esc(c['f_send'])}</a><a class="btn btn-s" href="{TEL}">{esc(c['call'])}</a></div>
<button class="copy" type="button" id="copy-msg" data-v="">{esc(c['copy'])}</button></div>
</div>
  <div class="contact">{cts}</div>
</div></section>"""


def c_plan(p, sid="plan"):
    items = ""
    for i, (h, first, d, you) in enumerate(p["plan"]):
        fl = f'<span class="first">{"почніть із цього"}</span>' if first else ''
        items += (f'<li><span class="n">{i+1}</span><div><h3>{esc(h)}{fl}</h3><p>{esc(d)}</p></div>'
                  f'<p class="you"><b>{esc(p["you_lbl"])}</b>{esc(you)}</p></li>')
    note = f'<p class="plan-note">{esc(p["plan_note"])}</p>' if p.get("plan_note") else ''
    return f"""<section id="{sid}" aria-labelledby="{sid}-h"><div class="wrap">
  <div class="sh"><h2 id="{sid}-h">{esc(p['plan_h'])}</h2><p>{esc(p['plan_sub'])}</p></div>
  <ol class="plan">{items}</ol>{note}
</div></section>"""


def c_rows(items, with_link=True):
    out = ""
    for it in items:
        y, ti, v, u = it
        out += f'<li><span class="y">{y}</span><div><a href="{u}" rel="noopener">{esc(ti)}</a><span class="org">{esc(v)}</span></div></li>'
    return out


def c_experience(p):
    tl = ""
    for yr, role, org, url, d in p["timeline"]:
        o = f'<a href="{url}" rel="noopener">{esc(org)}</a>' if url else esc(org)
        tl += f'<li><div class="yr">{esc(yr)}</div><div><h3>{esc(role)}</h3><p class="org">{o}</p><p class="d">{esc(d)}</p></div></li>'
    edu = "".join(f'<li><span class="y">{y}</span><span>{esc(x)}</span></li>' for y, x in p["edu"])
    ment = "".join(f'<li><span class="y">{y}</span><a href="{u}" rel="noopener">{esc(t)}</a></li>' for y, t, u in p["mentions"])
    return f"""<section id="experience" aria-labelledby="e-h"><div class="wrap">
  <div class="sh"><h2 id="e-h">{esc(p['e_h'])}</h2></div>
  <ul class="tl">{tl}</ul>
  <div class="practice"><h3>{esc(p['practice_h'])}</h3><p>{esc(p['practice'])}</p></div>
  <h3 class="subh">{esc(p['edu_h'])}</h3><ul class="rows">{edu}</ul>
  <h3 class="subh" id="publications">{esc(p['pubs_h'])}</h3><ul class="rows">{c_rows(p['pubs'])}</ul>
  <p class="note">{esc(p['pub_more'])} <a href="{SCHOLAR}" rel="noopener">Google Scholar</a>, <a href="{ORCID}" rel="noopener">ORCID</a></p>
  <h3 class="subh">{esc(p['mentions_h'])}</h3><ul class="mentions">{ment}</ul>
</div></section>"""


def c_facts(p):
    facts = "".join(f'<div class="r"><dt>{esc(a)}</dt><dd>{esc(b)}</dd></div>' for a, b in p["facts"])
    return f'<aside class="facts" aria-labelledby="facts-h"><h2 id="facts-h">{esc(p["facts_h"])}</h2><dl>{facts}</dl><a class="more" href="#experience">{esc(p["facts_more"])} →</a></aside>'


def doc(c, p, body, seo, alt=True, extra_ld=None):
    ttl = p["seo_title"] if seo else p["title"]
    url = BASE + ("" if p["file"] == "index.html" else p["file"])
    ld = {"@context": "https://schema.org", "@type": "Person", "name": c["name"],
          "alternateName": ["Дмитро Паламарчук", "Dmytro Palamarchuk", "Паламарчук Дмитро Миколайович"],
          "jobTitle": c["jobTitle"], "email": "mailto:" + MAIL, "telephone": TEL_H, "url": BASE,
          "address": {"@type": "PostalAddress", "addressLocality": "Cherkasy", "addressCountry": "UA"},
          "worksFor": {"@type": "Organization", "name": "NGO E-TEAM", "url": ETEAM},
          "knowsAbout": ["Energy efficiency", "Municipal energy planning", "Energy communities", "Homeowner associations"],
          "sameAs": [ORCID, SCHOLAR]}
    alts = (f'<link rel="alternate" hreflang="uk" href="{BASE}"><link rel="alternate" hreflang="en" href="{BASE}en.html"><link rel="alternate" hreflang="x-default" href="{BASE}">' if alt else '')
    head = (f'<title>{esc(ttl)}</title>' + ('' if seo else '<meta name="claude:viewport-fit-sides" content="cover">') +
            f'<meta name="description" content="{esc(p["description"])}"><link rel="canonical" href="{url}">{alts}'
            f'<meta property="og:type" content="website"><meta property="og:title" content="{esc(ttl)}"><meta property="og:description" content="{esc(p["description"])}"><meta property="og:url" content="{url}">'
            f'<meta property="og:image" content="{BASE}og.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image">'
            f'<link rel="icon" href="{FAVICON}">{FONTS}<style>{CSS}{CSS_PAGES}</style>'
            f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>')
    js = (JS.replace("__LAB__", json.dumps(c["f_lab"], ensure_ascii=False)).replace("__HDR__", json.dumps(c["f_hdr"], ensure_ascii=False))
            .replace("__COPY__", json.dumps(c["copy"], ensure_ascii=False)).replace("__COPIED__", json.dumps(c["copied"], ensure_ascii=False))) + JS_PAGES
    def _nw(m):
        t = m.group(1)
        for w in ("«Е-ТЕАМ»", "E-TEAM"):
            t = t.replace(w, f'<span class="nw">{w}</span>')
        return '>' + t + '<'
    body = re.sub(r'>([^<]+)<', _nw, body)  # text nodes only, never attributes
    full_body = f'{body}<script>{js}</script>'
    return (f'<!doctype html><html lang="{c["lang"]}"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width, initial-scale=1">{head}</head>'
            f'<body data-role="{p.get("role_default", "")}">{full_body}</body></html>')


# ----------------------------------------------------------------- pages

ENTRY_ICONS = {0: ICONS[0], 1: ICONS[1], 2: ICONS[2]}


def home(c, p, nav, other, lang_ua=True):
    if lang_ua:
        entries = "".join(f'<li><a href="{h}">{ENTRY_ICONS[ic]}<div><h3>{esc(t)}</h3><p>{esc(d)}</p></div><span class="arr">{esc(p["entries_go"])} →</span></a></li>'
                          for h, ic, t, d in p["entries"])
        mid = f"""<section id="services" class="band" aria-labelledby="en-h"><div class="wrap">
  <div class="sh"><h2 id="en-h">{esc(p['entries_h'])}</h2></div><ul class="entries">{entries}</ul>
</div></section>"""
    else:
        mid = f"""<section id="services" class="band" aria-labelledby="fm-h"><div class="wrap">
  <div class="sh"><h2 id="fm-h">{esc(p['formats_h'])}</h2><p>{esc(p['formats'])}</p></div>
</div></section>"""
    body = f"""{c_header(c, p['file'], nav, other)}
<main id="main">
<div class="wrap hero">
  <div>
    <p class="kicker">{esc(p['kicker'])}</p>
    <h1>{esc(c['name'])}</h1>
    <p class="role">{esc(p['role'])}</p>
    <p class="lead">{esc(p['lead'])}</p>
    <div class="acts"><a class="btn btn-p" href="#contact">{esc(p['cta1'])}</a><a class="btn btn-s" href="{TEL}" aria-label="{esc(c['call'])}: {TEL_H}">{PHONE_ICON}<span>{TEL_H}</span></a></div>
  </div>
  {c_facts(p)}
</div>
{mid}
{c_experience(p)}
{c_contact(c)}
</main>
{c_footer(c)}"""
    return body


def osbb(c, p, nav):
    selfc = "".join(f'<li>{esc(x)}</li>' for x in p["selfcheck"])
    prep = "".join(f'<li>{esc(x)}</li>' for x in p["prep"])
    progs = "".join(f'<li><a href="{u}" rel="noopener">{esc(t)}</a></li>' for t, u in p["progs"])
    th = dict(c); th.update(th_cap=c["th_cap"])
    body = f"""{c_header(c, p['file'], nav)}
<main id="main">
<div class="wrap phero">
  <p class="kicker">{esc(p['kicker'])}</p>
  <h1>{esc(p['h1'])}</h1>
  <p class="lead">{esc(p['lead'])}</p>
  <p class="tag-free">{esc(p['free'])}</p>
  <div class="acts"><a class="btn btn-p" href="#contact">{esc('Записатися на консультацію')}</a><a class="btn btn-s" href="{TEL}" aria-label="{esc(c['call'])}: {TEL_H}">{PHONE_ICON}<span>{TEL_H}</span></a></div>
</div>
{c_plan(p)}
<section id="self" class="band" aria-labelledby="self-h"><div class="wrap split">
  <div class="sh" style="margin:0"><h2 id="self-h">{esc(p['self_h'])}</h2><p>{esc(p['self_sub'])}</p></div>
  <ul class="check">{selfc}</ul>
</div></section>
<section id="prepare" aria-labelledby="prep-h"><div class="wrap split">
  <div class="sh" style="margin:0"><h2 id="prep-h">{esc(p['prep_h'])}</h2></div>
  <div class="prep" style="display:block"><ul>{prep}</ul></div>
</div></section>
<section id="thermo" class="band" aria-labelledby="th-h"><div class="wrap">
  <div class="explain" style="margin-top:0"><div><p class="kicker">{esc(p['th_kicker'])}</p><h2 id="th-h" style="font-size:var(--fs-h2)">{esc(p['th_h'])}</h2><p>{esc(p['th_p'])}</p></div>{scheme(th)}</div>
</div></section>
<section id="programs" aria-labelledby="pr-h"><div class="wrap">
  <div class="sh"><h2 id="pr-h">{esc(p['progs_h'])}</h2><p>{esc(p['progs_sub'])}</p></div>
  <ul class="links-out">{progs}</ul>
</div></section>
{c_contact(c)}
</main>
{c_footer(c)}"""
    return body


def generic(c, p, nav):
    prep = "".join(f'<li>{esc(x)}</li>' for x in p.get("prep", []))
    ex = ""
    if p.get("examples"):
        ex = f"""<section id="examples" class="band" aria-labelledby="ex-h"><div class="wrap">
  <div class="sh"><h2 id="ex-h">{esc(p['ex_h'])}</h2></div>
  <ul class="rows">{''.join(f'<li><span class="y">{esc(a)}</span><span>{esc(b)}</span></li>' for a, b in p['examples'])}</ul>
</div></section>"""
    prep_s = f"""<section id="prepare" aria-labelledby="prep-h"><div class="wrap split">
  <div class="sh" style="margin:0"><h2 id="prep-h">{esc(p['prep_h'])}</h2></div>
  <div class="prep" style="display:block"><ul>{prep}</ul></div>
</div></section>""" if prep else ''
    body = f"""{c_header(c, p['file'], nav)}
<main id="main">
<div class="wrap phero">
  <p class="kicker">{esc(p['kicker'])}</p>
  <h1>{esc(p['h1'])}</h1>
  <p class="lead">{esc(p['lead'])}</p>
  <div class="acts"><a class="btn btn-p" href="#contact">{esc('Обговорити ваше питання')}</a><a class="btn btn-s" href="{TEL}" aria-label="{esc(c['call'])}: {TEL_H}">{PHONE_ICON}<span>{TEL_H}</span></a></div>
</div>
{c_plan(p)}
{ex}
{prep_s}
{c_contact(c)}
</main>
{c_footer(c)}"""
    return body


def build_all():
    cu, ce = COMMON["ua"], COMMON["en"]
    nav_en = [("en.html", "Home"), ("#experience", "Experience"), ("#contact", "Contact")]
    pages = {
        "index.html": doc(cu, HOME_UA, home(cu, HOME_UA, NAV_UA, ("en.html", "EN", "en")), True),
        "en.html": doc(ce, HOME_EN, home(ce, HOME_EN, nav_en, ("index.html", "UA", "uk"), lang_ua=False), True),
        "osbb.html": doc(cu, OSBB_UA, osbb(cu, OSBB_UA, NAV_UA), True, alt=False),
        "mep.html": doc(cu, MEP_UA, generic(cu, MEP_UA, NAV_UA), True, alt=False),
        "energospilnoty.html": doc(cu, EC_UA, generic(cu, EC_UA, NAV_UA), True, alt=False),
    }
    return pages


if __name__ == "__main__":
    for d in ("preview", "dist"):
        os.makedirs(os.path.join(HERE, d), exist_ok=True)
    pages = build_all()
    for fn, html in pages.items():
        open(os.path.join(HERE, "dist", fn), "w").write(html)
        open(os.path.join(HERE, "preview", fn), "w").write(html)
    make_og(os.path.join(HERE, "dist", "og.png"))
    open(os.path.join(HERE, "dist", "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}sitemap.xml\n")
    urls = ["", "osbb.html", "mep.html", "energospilnoty.html", "en.html"]
    open(os.path.join(HERE, "dist", "sitemap.xml"), "w").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "".join(f'<url><loc>{BASE}{u}</loc><lastmod>2026-10-31</lastmod></url>\n' for u in urls) + '</urlset>\n')
    open(os.path.join(HERE, "dist", ".nojekyll"), "w").write("")
    print("ok", list(pages))
