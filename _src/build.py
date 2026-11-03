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

FONTS = ('<link rel="preload" href="fonts/commissioner-cyrillic-400-normal.woff2" as="font" type="font/woff2" crossorigin>')
# fonts/: WOFF2 from npm @fontsource/commissioner@5 (400, 600) and @fontsource/source-serif-4@5 (600), cyrillic + latin subsets
FONT_FACES = r"""
@font-face{font-family:"Commissioner";font-style:normal;font-weight:400;font-display:swap;src:url(fonts/commissioner-cyrillic-400-normal.woff2) format("woff2");unicode-range:U+0301,U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116}
@font-face{font-family:"Commissioner";font-style:normal;font-weight:400;font-display:swap;src:url(fonts/commissioner-latin-400-normal.woff2) format("woff2");unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}
@font-face{font-family:"Commissioner";font-style:normal;font-weight:600;font-display:swap;src:url(fonts/commissioner-cyrillic-600-normal.woff2) format("woff2");unicode-range:U+0301,U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116}
@font-face{font-family:"Commissioner";font-style:normal;font-weight:600;font-display:swap;src:url(fonts/commissioner-latin-600-normal.woff2) format("woff2");unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}
@font-face{font-family:"Source Serif 4";font-style:normal;font-weight:600;font-display:swap;src:url(fonts/source-serif-4-cyrillic-600-normal.woff2) format("woff2");unicode-range:U+0301,U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116}
@font-face{font-family:"Source Serif 4";font-style:normal;font-weight:600;font-display:swap;src:url(fonts/source-serif-4-latin-600-normal.woff2) format("woff2");unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}
"""
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
  --fs-fig:56px; --fs-h1:44px; --fs-h2:30px; --fs-h3:21px; --fs-lead:20px; --fs-body:17px; --fs-small:15px;
  --s-1:4px; --s-2:8px; --s-3:12px; --s-4:16px; --s-5:24px; --s-6:32px; --s-7:48px; --s-8:64px; --s-9:64px;
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
@media (max-width:560px){:root{--fs-fig:44px; --fs-h1:34px; --fs-h2:24px; --fs-h3:19px; --fs-lead:18px; --fs-body:16px; --s-9:40px}}

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
.nav .links a,.nav .tools a{white-space:nowrap}
.nav{display:flex;align-items:center;gap:var(--s-5);font-size:16px}
.nav a{color:var(--ink);text-decoration:none}
.nav a:hover{color:var(--primary);text-decoration:underline}
.nav .tel{font-weight:600;white-space:nowrap;font-variant-numeric:tabular-nums}
.nav .lang{font-weight:600;font-size:var(--fs-small);color:var(--primary);text-decoration:underline}
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

/* hero entries (decision 38) */
.gates{border-top:2px solid var(--ink);margin-top:6px}
.gates .lbl{font-size:var(--fs-small);font-weight:600;color:var(--ink-2);margin:var(--s-3) 0 var(--s-1)}
.gates ul{list-style:none;margin:0;padding:0}
.gates li{border-bottom:1px solid var(--rule)}
.gates a{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:var(--s-2) var(--s-4);align-items:start;padding:var(--s-4) 0;text-decoration:none;color:var(--ink)}
.gates b{display:block;font-size:19px;font-weight:600;line-height:1.3}
.gates span.r{display:block;margin-top:3px;color:var(--ink-2);font-size:var(--fs-small);line-height:1.45}
.gates .arr{color:var(--primary);font-weight:600;font-size:20px;line-height:1.2}
.gates a:hover b{color:var(--primary);text-decoration:underline;text-underline-offset:4px}
/* call-to-action strip instead of the form on each page */
.cta-s .wrap{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:var(--s-5) var(--s-7);align-items:center}
.cta-s h2{margin:0 0 var(--s-2)}
.cta-s p{color:var(--ink-2);max-width:40em}
.cta-s .acts{justify-content:flex-end}
.cta-s .mail{display:block;margin-top:var(--s-3);font-size:var(--fs-small)}
@media (max-width:900px){.cta-s .wrap{grid-template-columns:minmax(0,1fr)}.cta-s .acts{justify-content:flex-start}}
.back{color:var(--ink-3)}
.back a{font-weight:600}

.sub2{color:var(--ink-2);margin:0 0 var(--s-4);max-width:34em}
#self h2{margin-bottom:var(--s-3)}

.vh{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
#contact.plain{border-top:0;padding-top:0}

@media (max-width:360px){.phero h1{font-size:28px}}

.form .hint:first-child{margin-top:0}

/* sections */
section{padding-block:var(--s-9);border-top:1px solid var(--rule)}
.band{background:var(--band)}
.sh{margin-bottom:var(--s-6)}
.sh h2{margin-bottom:var(--s-4)}
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
  .brand span{display:none}
  .tools .tel{display:none}
  .hdr .wrap{flex-wrap:wrap}
  .hdr .wrap{padding-block:var(--s-3)}
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
    d.text((80, 250), "Експерт з енергоефективності", font=ImageFont.truetype(fb, 36), fill=(20, 32, 46))
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
@media (max-width:480px){.links .home{display:none}.links{flex-wrap:wrap;row-gap:var(--s-1)}}
@media (max-width:400px){.links{font-size:14.5px !important;gap:var(--s-2) !important}}
.phero .kicker{margin-bottom:var(--s-3)}
.phero h1{hyphens:auto;overflow-wrap:break-word;font-size:clamp(32px,4vw,40px);max-width:20em;text-wrap:balance}
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
.check li,.prep li{position:relative;padding-left:22px}
.check li::before,.prep li::before{content:"";position:absolute;left:2px;top:.68em;width:7px;height:7px;border-radius:50%;background:var(--ink-2)}
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
(function(){var q=new URLSearchParams(location.search).get('role'); var dr=(q!==null&&/^[0-4]$/.test(q))?q:document.body.getAttribute('data-role'); if(dr===null||dr==='') return;
  var r=document.getElementById('role-'+dr); if(r){r.checked=true;r.dispatchEvent(new Event('change'));}})();
"""

ROLES_UA = ["ОСББ або управитель", "Громада (ОМС)", "Ініціативна група / енергоспільнота", "Міжнародна організація / донор", "Інше"]
NEEDS_UA = ["Консультація", "Участь у загальних зборах ОСББ", "Огляд будинку і розрахунок", "Муніципальний енергетичний план", "Енергетична спільнота: з чого почати", "Експертна участь у проєкті"]
ROLES_EN = ["Homeowner association or manager", "Municipality", "Community group / energy community", "International organisation / donor", "Other"]
NEEDS_EN = ["Consultation", "Attendance at an HOA general meeting", "Building walk-through and calculation", "Municipal energy plan", "Energy community: where to start", "Expert input to a project"]

COMMON = {
 "ua": dict(lang="uk", skip="Перейти до змісту", nav_label="Основна навігація", call="Зателефонувати",
            brand_sub="Енергоефективність · енергетичне планування · енергоспільноти",
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
            name="Дмитро Паламарчук", ft_role="Експерт з енергоефективності та енергетичного планування · Черкаси", ft_board="Член правління ГО «Е-ТЕАМ» на громадських засадах", ft_org="ГО «Е-ТЕАМ»",
            ft_base="© 2026 Дмитро Паламарчук · Оновлено: листопад 2026",
            lg_k="Фізична особа — підприємець", lg_n="Паламарчук Дмитро Миколайович", lg_aria="Юридична особа, що надає послуги",
            cta_btn="Описати питання", back="← Головна",
            c_h="Напишіть, з чим звертаєтеся", c_sub="Опишіть питання в кількох словах — я відповім. Або просто зателефонуйте.",
            th_cap="Схема, не знімок конкретного будинку", th_before="До утеплення", th_after="Після",
            th_aria="Схема: панельний будинок до утеплення з теплими швами і вікнами, та після утеплення з холодним рівномірним фасадом",
            th_cold="холодніше", th_warm="тепліше",
            jobTitle="Експерт з енергоефективності та енергетичного планування"),
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
            ft_base="© 2026 Dmytro Palamarchuk · Updated: November 2026",
            lg_k="Sole proprietor (Ukrainian FOP)", lg_n="Dmytro Mykolaiovych Palamarchuk", lg_aria="Legal entity providing the services",
            cta_btn="Describe your question", back="← Home",
            c_h="Get in touch", c_sub="Describe your question in a few words and I will reply — or simply call.",
            jobTitle="Energy efficiency and municipal energy planning consultant"),
}

NAV_UA = [("index.html", "Головна"), ("osbb.html", "ОСББ"), ("energospilnoty.html", "Енергоспільноти"), ("mep.html", "МЕП громадам"), ("pro-mene.html", "Про мене")]

MENTIONS_UA = [
    ("2026", "«Золотоноша.City»: «Як зробити свій будинок сучасним і комфортним: навчання для голів золотоніських об’єднань» — семінар для голів ОСББ",
     "https://zoloto.city/articles/475163/yak-zrobiti-svij-budinok-suchasnim-i-komfortnim-navchannya-dlya-goliv-zolotoniskih-obyednan"),
    ("2026", "Маньківська селищна громада: інформаційна довідка щодо державних програм для багатоквартирних будинків — регіональний радник з енергоефективності в Черкаській області",
     "https://mankivska-gromada.gov.ua/news/1783503317/"),
    ("2026", "Кам'янська міська громада: «ОСББ можуть отримати грантову підтримку на енергомодернізацію та відновлення будинків» — регіональний радник з енергоефективності",
     "https://kammiskrada.gov.ua/news/1782826532/"),
    ("2020", "Черкаська РДА: «Про Фонд енергоефективності» — регіональний консультант у Черкаській області Програми IFC з підтримки Фонду",
     "https://cherkassyrda.gov.ua/galuzevi-novyny/energoefektyvnist/2020/03/02/pro-fond-energoefektyvnosti/"),
    ("2020", "Канівська міська рада: «Про Фонд енергоефективності» — регіональний консультант у Черкаській області Програми IFC з підтримки Фонду",
     "https://kaniv-rada.pp.ua/pages.php-1147.html"),
    ("2019", "«Дзвін»: семінар для співвласників у Черкасах — регіональний консультант IFC з енергоефективності в житловому секторі",
     "https://dzvin.media/news/trend-na-energooshhadnist-cherkashhan-navchaly-zaluchaty-koshty-na-vtilennya-enregoefektyvnyh-zahodiv/"),
    ("2019", "«ПРОЧЕРК»: «Черкащан навчали залучати кошти на втілення енергоефективних заходів» — регіональний консультант IFC з питань енергоефективності в житловому секторі",
     "https://procherk.info/news/7-cherkassy/72608-cherkaschan-navchali-zaluchati-koshti-na-vtilennja-enregoefektivnih-zahodiv"),
]
PUB_JOURNAL = ("2021", "Регіональний вимір енергоефективності та енергетичної безпеки України",
               "Бізнесінформ, 2021, № 7, с. 127–134. DOI 10.32983/2222-4459-2021-7-127-134",
               "https://doi.org/10.32983/2222-4459-2021-7-127-134")
PUB_JOURNAL_EN = ("2021", "Regional dimension of energy efficiency and energy security of Ukraine",
                  "Business Inform, 2021, No. 7, pp. 127–134 (in Ukrainian). DOI 10.32983/2222-4459-2021-7-127-134",
                  "https://doi.org/10.32983/2222-4459-2021-7-127-134")

LIFE_DB = "https://webgate.ec.europa.eu/life/publicWebsite/project/LIFE25-CET-ECOss-101294756/energy-community-one-stop-shops-facilitation-hub"
FEE = "ДУ «Фонд енергоефективності»"

HOME_UA = dict(
  file="index.html", role_default="",
  title="Дмитро Паламарчук", seo_title="Дмитро Паламарчук — енергоефективність житла та енергетичне планування",
  description="Дмитро Паламарчук — експерт з енергоефективності та енергетичного планування: консультації ОСББ щодо енергомодернізації будинків, муніципальні енергетичні плани для громад, енергетичні спільноти. Черкаси.",
  role="Експерт з енергоефективності та енергетичного планування",
  lead="Консультую ОСББ щодо енергомодернізації будинків, розробляю муніципальні енергетичні плани для громад і допомагаю ініціативним групам підготуватися до створення енергетичних спільнот.",
  big=[("osbb.html", "Енергомодернізація та резервне живлення багатоквартирних будинків",
        f"Оглядаю будинок, пояснюю умови програм {FEE} і допомагаю правлінню підготуватися до кожного кроку.",
        "Регіональний радник з енергоефективності мережі ГО «Е-ТЕАМ» у проєкті «Зелена відбудова України разом із Фондом енергоефективності». Для ОСББ консультації безкоштовні.",
        "Детальніше про роботу з ОСББ"),
       ("energospilnoty.html", "Енергетичні спільноти",
        "Консультую ініціативні групи, які думають про енергетичну спільноту, і передаю їхні запити до хабу LIFE-ECOss у Луцьку.",
        "Національний координатор проєкту ЄС LIFE-ECOss від ГО «Е-ТЕАМ».",
        "Детальніше про енергетичні спільноти"),
       ("mep.html", "Муніципальне енергетичне планування",
        "Розробляю муніципальні енергетичні плани за Методикою, затвердженою наказом № 1163. План затверджує рада громади.",
        "Робота за договором з громадою.",
        "Детальніше про МЕП")],
  about="Про мене: досвід, програми, публікації",
  ask="Описати своє питання",
  media="Для медіа: коментую енергомодернізацію житла, енергетичні спільноти й муніципальне енергетичне планування",
)

CONSENT = ("Надсилаючи форму, ви даєте згоду на обробку і зберігання ваших персональних даних (ім'я, телефон або email, текст звернення) "
           "для відповіді на ваше звернення відповідно до Закону України «Про захист персональних даних». ")
CONSENT_EC = ("Надсилаючи форму, ви даєте згоду на обробку і зберігання ваших персональних даних (ім'я, телефон або email, текст звернення) "
              "для відповіді на ваше звернення і на передачу ваших контактів до хабу LIFE-ECOss у Луцьку (ГО «Е-ТЕАМ»), щоб з вами зв'язалися, "
              "щойно він почне роботу, — відповідно до Закону України «Про захист персональних даних». ")

OSBB_UA = dict(
  file="osbb.html", role_default="0",
  title="Енергомодернізація багатоквартирних будинків — Дмитро Паламарчук",
  seo_title="Енергомодернізація та резервне живлення багатоквартирних будинків — консультації для ОСББ, Черкаська область",
  description="Безкоштовні консультації для ОСББ Черкаської області щодо програм ДУ «Фонд енергоефективності» «Енергодім», «ВідновиДІМ» і «ГрінДІМ»: огляд будинку, розрахунок, загальні збори, заявка, супровід до верифікації.",
  kicker="Для ОСББ · Черкаська область",
  h1="Енергомодернізація та резервне живлення багатоквартирних будинків",
  lead=f"Консультую ОСББ як регіональний радник з енергоефективності мережі ГО «Е-ТЕАМ» у проєкті «Зелена відбудова України разом із Фондом енергоефективності» — від першої розмови до завершення проєкту за програмами {FEE} («Енергодім», «ВідновиДІМ», «ГрінДІМ»).",
  free="Для ОСББ консультації безкоштовні — їх оплачує проєкт", btn="Описати своє питання",
  fund="Проєкт «Зелена відбудова України разом із Фондом енергоефективності» фінансується Федеральним міністерством навколишнього середовища, захисту клімату, охорони природи та ядерної безпеки Німеччини (BMUKN) у рамках Міжнародної кліматичної ініціативи (IKI), співфінансується Європейським Союзом та підтримується Deutsche Gesellschaft für Internationale Zusammenarbeit (GIZ) GmbH.",
  plan_h="Як проходить робота",
  plan_sub="Шлях однаковий для більшості будинків. На кожному кроці рішення за правлінням і співвласниками; я пояснюю, рахую і допомагаю з документами.",
  you_lbl="Ваша частина",
  plan=[("Знайомство", True, f"Проводжу семінар для ОСББ або зустрічаюся з головою й активом — телефоном чи на місці. Пояснюю програми {FEE} і допомагаю правлінню вирішити, чи рухатися далі.", "Розповісти про будинок і про те, що турбує мешканців."),
        ("Огляд будинку", False, "Приїжджаю й оглядаю будинок разом із головою правління: фасад, дах, підвал, тепловий пункт, вікна й двері в під'їздах.", "Забезпечити доступ до технічних приміщень, підготувати рахунки за тепло і технічний паспорт."),
        ("Індикативний розрахунок вартості реалізації проєкту", False, "Рахую варіанти заходів, їхню вартість, грант, кредит, зміну внесків і очікувану економію — до підсумку для квартири. Пояснюю умови програм і різницю між пакетами заходів.", "Обговорити варіанти на правлінні."),
        ("Загальні збори", False, "Допомагаю підготувати збори: питання до порядку денного, робота з ініціативною групою. За потреби беру участь у зборах і пояснюю розрахунок співвласникам.", "Провести збори й ухвалити рішення відповідно до закону."),
        (f"Заявка до {FEE} і фінансування", False, f"Консультую щодо пакета документів, перевіряю його перед поданням, допомагаю врахувати зауваження {FEE}. Консультую щодо кредиту в банку, якщо він потрібен.", "Зібрати документи, укласти договори з енергоаудитором, проєктантом, банком (за потреби)."),
        ("Проєктування і роботи", False, f"Пояснюю, як організувати роботи, що контролювати і де найчастіше трапляються помилки. Консультую голову ОСББ, менеджера проєкту і підрядника щодо вимог {FEE}.", "Керувати проєктом, контролювати підрядника й ухвалювати рішення."),
        ("Супровід до фінішу", False, f"Поки тривають роботи, тримаю зв'язок із правлінням і менеджером проєкту: звіряємо графік, щоб вчасно помітити відхилення. Якщо треба щось скоригувати (обсяг робіт, кошторис чи строки), пояснюю, як це зробити за правилами {FEE}, і допомагаю з документами. Такі коригування — звична частина багатьох проєктів.", "Тримати мене в курсі ходу робіт і одразу казати про відхилення від плану."),
        ("Верифікація і завершення", False, f"Допомагаю підготуватися до перевірки {FEE} й опрацювати зауваження.", "Усунути недоліки разом із підрядником.")],
  plan_note="Не кожен будинок доходить до проєкту — і це нормально. Після огляду й розрахунку стає видно, чи готові співвласники до модернізації зараз.",
  self_h="Перш ніж почати — кілька запитань до себе",
  self_sub="Від відповідей на них залежить, чи дійде будинок до проєкту.",
  selfcheck=["Чи є в правлінні людина, готова вести проєкт?",
             "Як співвласники ставляться до внесків на модернізацію будинку?",
             "Чи зможете зібрати загальні збори з потрібною кількістю голосів?"],
  prep_h="Що підготувати до першої розмови",
  prep=["Рахунки або дані про споживання тепла за 2–3 останні опалювальні сезони",
        "Технічна документація будинку: рік побудови, поверховість, площа, кількість квартир",
        "Звіт з енергоаудиту, якщо є"],
  progs_h="Умови програм — у першоджерелі",
  progs_sub=f"Умови програм змінюються, тому посилаюся на сайт {FEE}, а на консультації пояснюю, що вони означають для вашого будинку.",
  progs=[(f"{FEE} — офіційний сайт", "https://eefund.org.ua/")],
  also_h="Кого ще консультую",
  also=[("Громади.", f"Працівників виконавчих органів і депутатів — щодо місцевих програм підтримки ОСББ і співфінансування разом із програмами {FEE}. Допомагаю організувати навчання для голів ОСББ і працівників громади."),
        ("Підрядників і менеджерів проєктів ОСББ.", "Пояснюю вимоги програм до підрядника, авансу, матеріалів і документації, щоб роботи відповідали вимогам програм."),
        ("Медіа.", "Пояснюю журналістам, як працюють програми енергомодернізації будинків і як їх виконують у регіоні.")],
  q_h="Обговорімо можливості для вашого будинку",
  q_sub="Опишіть будинок у кількох словах — я відповім телефоном або листом.",
  consent=CONSENT, gmail=False,
)

EC_UA = dict(
  file="energospilnoty.html", role_default="2",
  title="Енергетичні спільноти — Дмитро Паламарчук",
  seo_title="Енергетичні спільноти: з чого почати — проєкт ЄС LIFE-ECOss, хаб у Луцьку",
  description="Енергетична спільнота: з чого почати ініціативній групі, ОСББ чи громаді. Проєкт ЄС LIFE-ECOss: хаб підтримки енергоспільнот у Луцьку. Збираю контакти зацікавлених груп.",
  kicker="Для ініціативних груп, ОСББ і громад",
  h1="Енергетичні спільноти: почати з оцінки, а не з купівлі обладнання",
  lead="Простими словами, енергетична спільнота — це об'єднання людей, ОСББ, бізнесу чи громади, які разом виробляють, зберігають або купують енергію для власних потреб. Закон уже передбачає енергетичні спільноти, але для старту потрібні підзаконні акти уряду. Тому перший крок — чесна оцінка, чи є для спільноти підстави.",
  project=("Проєкт ЄС LIFE-ECOss (2026–2029).", "У проєкті створюють три центри підтримки енергетичних спільнот — у Луцьку, Софії та Будапешті — за досвідом муніципальних офісів Іспанії: у Хетафе, Віладекансі та регіоні Наварра. Я — національний координатор проєкту від ГО «Е-ТЕАМ». Консультую ініціативні групи на старті й допомагаю підготуватися до звернення в хаб LIFE-ECOss у Луцьку."),
  now_h="Що зараз",
  now=[("Зараз —", "попередні консультації і збір контактів. Поки що збираю контакти груп, які розглядають створення спільноти. Щойно правила ухвалять, зв'яжуся з вами, і почнемо роботу."),
       ("Весна 2027 —", "очікувані підзаконні акти уряду щодо енергетичних спільнот."),
       ("З вересня 2027 —", "запланований початок супроводу на місці від хабу LIFE-ECOss у Луцьку.")],
  plan_h="З чого почати", plan_sub="Ці питання розбираємо разом на першій консультації.", you_lbl="Що підготувати",
  plan=[("Хто учасники", True, "Хто має намір увійти до спільноти і з якою метою: економія, надійність, власна генерація.", "Склад групи і контакти."),
        ("Об'єкт і споживання", False, "Де може бути генерація чи накопичення — дах, ділянка, котельня — і скільки енергії споживають учасники.", "Адреса об'єкта, орієнтовне річне споживання."),
        ("Правова форма", False, "Яка організаційно-правова форма підходить і чи може нею стати, наприклад, ваше ОСББ.", "Документи наявної організації, якщо є."),
        ("Бізнес-модель і фінансування", False, "На чому спільнота триматиметься економічно і з яких джерел фінансувати старт.", "Очікування учасників щодо внесків."),
        ("Передача до хабу", False, "Коли хаб LIFE-ECOss у Луцьку почне роботу, за вашою згодою передам туди ваш запит і те, що ми вже з'ясували, — щоб там не починали з нуля.", "Згода на передачу ваших контактів до хабу.")],
  links_lbl="Офіційні канали проєкту:",
  links=[("Сайт проєкту", "https://www.climatealliance.org/projects/life-ecoss/"), ("LinkedIn", "https://www.linkedin.com/showcase/life-ecoss/"),
         ("Facebook", "https://www.facebook.com/profile.php?id=61595728792719"), ("Instagram", "https://www.instagram.com/lifeecoss.eu/"),
         ("Bluesky", "https://bsky.app/profile/lifeecoss.bsky.social"), ("картка проєкту в базі LIFE Європейської Комісії", LIFE_DB)],
  q_h="Обговорімо ідею вашої спільноти",
  q_sub="Опишіть, хто ви і що хочете зробити. Я відповім і зв'яжуся з вами, щойно уряд ухвалить правила для спільнот.",
  consent=CONSENT_EC, gmail=False,
)

MEP_UA = dict(
  file="mep.html", role_default="1",
  title="Муніципальне енергетичне планування — Дмитро Паламарчук",
  seo_title="Муніципальний енергетичний план (МЕП) для громади — розробка за Методикою № 1163",
  description="Розробка муніципального енергетичного плану (МЕП) за Методикою, затвердженою наказом № 1163 від 21.12.2023: етапи роботи, що потрібно від громади, що підготувати до першої розмови.",
  kicker="Для громад",
  h1="Муніципальне енергетичне планування",
  lead="Розробка МЕП за Методикою, затвердженою наказом № 1163 від 21.12.2023.",
  btn="Описати своє питання",
  plan_h="Етапи роботи", plan_sub="Порядок і обсяг кожного етапу уточнюємо з громадою на старті.", you_lbl="Що потрібно від громади",
  plan=[("Старт і робоча група", True, "Узгоджуємо межі плану, строки й відповідальних; громада визначає робочу групу.", "Рішення про розробку, відповідальна особа, контакти структурних підрозділів."),
        ("Збір і перевірка даних", False, "Збираю й перевіряю дані про споживання енергії бюджетними будівлями, житлом, теплопостачанням, вуличним освітленням, транспортом — на повноту й узгодженість.", "Дані від підрозділів і комунальних підприємств."),
        ("Енергетичний баланс і базова лінія", False, "Будую енергетичний баланс громади і базову лінію, з якою порівнюватимуть результати плану.", "Погодити, як заповнювати прогалини в даних."),
        ("Цілі й заходи", False, "Пропоную цілі й формую каталог заходів і проєктів з оцінкою вартості та ефекту.", "Пріоритети громади, перелік проєктів, які вже розглядаються."),
        ("План фінансування і реалізації", False, "Пов'язую заходи з джерелами фінансування й строками.", "Звірити план з бюджетними можливостями громади."),
        ("Обговорення й затвердження", False, "Доопрацьовую план за результатами громадського обговорення, а також за рекомендаціями й зауваженнями обласної військової адміністрації (ОВА).", "Провести громадське обговорення, подати план на розгляд ОВА і затвердити його рішенням ради.")],
  prep_h="Що підготувати до першої розмови",
  prep=["Наявні плани й програми (за наявності): SECAP, генеральний план, стратегія розвитку, програми підвищення енергоефективності та енергетичної стійкості",
        "Коротка довідка про громаду: промисловість, сільське господарство, житловий сектор, транспорт",
        "Контактна особа для збору даних: енергоменеджер або призначений працівник"],
  q_h="Обговорімо план для вашої громади",
  q_sub="Опишіть, на якому етапі громада і які документи вже є. Відповім і запропоную порядок роботи.",
  consent=CONSENT, gmail=True,
)

ABOUT_UA = dict(
  file="pro-mene.html", role_default="",
  title="Про мене — Дмитро Паламарчук",
  seo_title="Дмитро Паламарчук — досвід, міжнародні програми, публікації",
  description="Дмитро Паламарчук: регіональний радник з енергоефективності (IFC 2019–2025, проєкт GIZ з 2026), національний координатор LIFE-ECOss, МЕП Сміли (UNIDO). Досвід, публікації, згадки.",
  kicker="Про мене", h1="Дмитро Паламарчук",
  lead="Експерт з енергоефективності та енергетичного планування, Черкаси. З 2019 року консультую ОСББ і громади. Кандидат економічних наук.",
  cards_h="Досвід у міжнародних програмах і проєктах",
  cards=[("з 2026", "«Зелена відбудова України разом із Фондом енергоефективності»", "BMUKN (IKI), ЄС, GIZ", "Регіональний радник з енергоефективності, мережа ГО «Е-ТЕАМ»"),
         ("з 2026", "LIFE-ECOss «Хаб сприяння центрам єдиного вікна для енергетичних спільнот»", "Програма ЄС LIFE", "Національний координатор від ГО «Е-ТЕАМ»"),
         ("2026", "«Розбудова спроможності, енергетичне оцінювання та попереднє техніко-економічне обґрунтування для Муніципального енергетичного плану Сміли»", "UNIDO", "Керівник проєкту від ГО «Е-ТЕАМ»"),
         ("2019–2025", "«Фонд енергоефективності та програма реагування на кризу для України»", "IFC (Група Світового банку)", "Регіональний радник з енергоефективності, Черкаська область (з 2024 — також Сумська)")],
  e_h="Професійний досвід",
  timeline=[
    ("2026 — дотепер", "Регіональний радник з енергоефективності, Черкаська область",
     "проєкт «Зелена відбудова України разом із Фондом енергоефективності» (BMUKN, IKI; співфінансування ЄС; за підтримки GIZ), мережа регіональних радників ГО «Е-ТЕАМ»", None,
     f"Консультую ОСББ і обстежую житлові будинки; готую звіти передпроєктного обстеження й енергетичні паспорти з розрахунком заходів пакетів А і Б. Допомагаю ОСББ опрацьовувати зауваження {FEE} до верифікації та налагоджувати взаємодію з підрядниками й управителями. Проводжу просвітницькі заходи з енергомодернізації багатоквартирних будинків; консультую ОСББ і органи місцевого самоврядування щодо умов програм {FEE}."),
    ("2025 — дотепер", "Експерт з енергоефективності та муніципального енергетичного планування", "", None,
     "Національний координатор від ГО «Е-ТЕАМ» у проєкті ЄС LIFE-ECOss. У проєкті UNIDO «Розбудова спроможності, енергетичне оцінювання та попереднє техніко-економічне обґрунтування для Муніципального енергетичного плану Сміли» — координатор і співвиконавець. Координую підготовку муніципального енергетичного плану Сарненської МТГ."),
    ("2019 — червень 2025", "Регіональний радник з енергоефективності, Черкаська область (з 2024 — також Сумська)",
     "проєкт IFC «Фонд енергоефективності та програма реагування на кризу для України», Група Світового банку", None,
     f"Розробляв і проводив навчання для ОСББ і органів місцевого самоврядування з енергоефективності та участі в програмах підтримки. Допоміг підготувати 41 успішну заявку на грантову підтримку {FEE}. Консультував органи місцевого самоврядування щодо розроблення місцевих програм підтримки енергомодернізації. Розробляв фінансові моделі та аналіз витрат і вигод проєктів енергомодернізації ОСББ."),
    ("2017 — серпень 2026", "Доцент (за сумісництвом)", "Черкаський державний технологічний університет", None,
     "Розробив і впровадив курс «Економіка сталого розвитку»: циркулярна економіка, Європейський зелений курс, інструменти зеленого фінансування. Лекції та дослідження з міжнародної економіки, європейської інтеграції та політики енергоефективності; прикладні дослідження адаптації енергетичного законодавства ЄС до українських умов.")],
  civic_h="Громадська діяльність",
  civic=[("2025 — дотепер", "Член правління, координатор проєктів міжнародної співпраці", "ГО «Е-ТЕАМ», на громадських засадах", ETEAM,
          "Уповноважений представник організації (LEAR) на порталі Funding & Tenders Європейської Комісії. Комунікую з громадами й міжнародними партнерами у проєктах зеленого переходу.")],
  practice_h="Робота в цифрах, 2019–2026",
  practice="1 200+ консультацій для ОСББ · участь у 50+ загальних зборах співвласників ОСББ · спікер на понад 80 семінарах, вебінарах чи форумах.",
  edu_h="Науковий ступінь",
  edu=[("2014", "Кандидат економічних наук — Київський національний університет імені Тараса Шевченка")],
  pubs_h="Публікації",
  pubs=[("2024", "Інформаційні кампанії як інструмент зміни поведінки споживачів щодо використання енергії: досвід ЄС", "Матеріали III Міжнародної науково-практичної конференції, Тернопіль, ЗУНУ", PUBS_URLS[0]),
        ("2022", "Дослідження чинників, що впливають на рішення співвласників щодо модернізації багатоквартирних будинків", "Матеріали IX Міжнародної науково-практичної конференції, ЧДТУ", PUBS_URLS[2]),
        ("2021", "Механізм формування економічної політики у сфері енергоефективності", "Вісник соціально-економічних досліджень (ОНЕУ), 2021, № 2 (77), с. 25–40. DOI 10.33987/vsed.2(77).2021.25-40", "http://vsed.oneu.edu.ua/collections/2021/77/pdf/25-40.pdf"),
        PUB_JOURNAL],
  pub_more="Повний перелік:",
  mentions_h="Згадки в інших джерелах",
  mentions=MENTIONS_UA,
  q_h="Опишіть своє питання", q_sub="Я відповім телефоном або листом. Якщо зручніше поговорити, зателефонуйте.",
  consent=CONSENT, gmail=False, roles=True,
)

ZV_UA = dict(
  file="zvernennia.html", role_default="",
  title="Звернення — Дмитро Паламарчук",
  seo_title="Звернення — Дмитро Паламарчук: ОСББ, МЕП, енергоспільноти",
  description="Опишіть питання щодо енергомодернізації ОСББ, муніципального енергетичного плану чи енергетичної спільноти — Дмитро Паламарчук відповість.",
  kicker="Звернення", h1="Опишіть своє питання",
  lead="Коротко опишіть ситуацію — я відповім телефоном або листом. Якщо зручніше поговорити, зателефонуйте.",
  consent="Натискаючи «Надіслати повідомлення», ви даєте згоду Дмитру Паламарчуку на обробку і зберігання ваших персональних даних для відповіді на ваше звернення, а якщо ви обрали «Ініціативна група / енергоспільнота», — і на передачу ваших контактів до хабу LIFE-ECOss у Луцьку (ГО «Е-ТЕАМ») відповідно до Закону України «Про захист персональних даних».",
  data_h="Як обробляються дані",
  data=[("Що надсилається:", "ім'я, телефон або email, хто звертається і текст питання."),
        ("Навіщо:", "лише для відповіді на ваше звернення. Розсилок не буде."),
        ("Хто отримує:", f"лист надходить мені особисто: звернення громад щодо муніципальних енергетичних планів — на {MAIL}, усі інші — на {MAIL_W}."),
        ("Передача до хабу LIFE-ECOss:", "якщо ви звертаєтесь щодо енергоспільноти, ваші контакти передаються хабу у Луцьку (ГО «Е-ТЕАМ»). Іншим третім особам дані не передаються."),
        ("Ваші права:", "ви можете дізнатися, які дані про вас зберігаються, виправити чи видалити їх або відкликати згоду — напишіть на ту саму адресу."),
        ("", "Сайт не використовує cookie та аналітику.")],
  contacts=[("Зв'язок", [("Email, ГО «Е-ТЕАМ» — ОСББ, енергоспільноти", MAIL_W, "mailto:" + MAIL_W, True), ("Email — МЕП для громад", MAIL, "mailto:" + MAIL, True), ("Телефон", TEL_H, TEL, True)]),
            ("Профілі", [("Сайт ГО «Е-ТЕАМ»", "eteamngo.org", ETEAM, False), ("Google Scholar", "Профіль і цитування", SCHOLAR, False),
                         ("ORCID", "0000-0002-6023-9780", ORCID, False)])],
  consent_q=CONSENT, roles=True,
)

HOME_EN = dict(
  file="en.html", other="index.html", other_label="UA", other_lang="uk", role_default="",
  title="Dmytro Palamarchuk", seo_title="Dmytro Palamarchuk — energy efficiency, municipal energy planning, energy communities (Ukraine)",
  description="Dmytro Palamarchuk — energy efficiency expert in Ukraine: regional advisor to homeowner associations (GIZ project), municipal energy plans, National Coordinator of the EU LIFE-ECOss project. Cherkasy.",
  kicker="Cherkasy, Ukraine · working with municipalities across regions",
  role="Residential energy efficiency and municipal energy planning in Ukraine",
  lead="Regional energy efficiency advisor to homeowner associations (IFC 2019–2025, GIZ project since 2026), municipal energy plans, National Coordinator of the EU LIFE-ECOss energy community project.",
  cta1="Get in touch",
  facts_h="Programmes I have worked and work in",
  facts=[("“ReBuildGreen Ukraine with the Energy Efficiency Fund” — BMUKN (IKI), EU, GIZ", "Regional energy efficiency advisor, NGO E-TEAM network, since 2026"),
         ("LIFE-ECOss “Energy Community One-Stop-Shops Facilitation Hub” — EU LIFE", "National Coordinator for NGO E-TEAM, since 2026"),
         ("Municipal Energy Plan of Smila — UNIDO", "Project lead for NGO E-TEAM, 2026"),
         ("IFC Energy Efficiency Fund and Crisis Response Program for Ukraine — World Bank Group", "Regional energy efficiency advisor, Cherkasy oblast (from 2024 also Sumy), 2019–2025")],
  facts_more="Experience",
  formats_h="How I work with programmes and partners",
  formats="As an independent expert (registered sole proprietor) under contracts, including in NGO E-TEAM projects. Pages for Ukrainian homeowner associations and municipalities are in Ukrainian.",
  e_h="Experience",
  timeline=[
    ("2026 — present", "Regional energy efficiency advisor, Cherkasy oblast", "“ReBuildGreen Ukraine with the Energy Efficiency Fund” (BMUKN, IKI; co-financed by the EU; supported by GIZ), NGO E-TEAM regional advisor network", None,
     "Consultations and inspections of residential buildings; pre-project inspection reports and energy passports with Package A / Package B measures. Helping HOAs address the Energy Efficiency Fund’s verification comments and work with contractors and property managers; outreach events; advice to HOAs and local authorities on the Fund’s programmes."),
    ("2025 — present", "Energy efficiency and municipal energy planning expert", "", None,
     "National Coordinator in the EU LIFE-ECOss project; coordinator and co-implementer of the UNIDO project “Capacity building, energy assessment and pre-feasibility study for the Municipal Energy Plan of Smila”; coordinator of the Municipal Energy Plan for Sarny."),
    ("2019 — June 2025", "Regional energy efficiency adviser, Cherkasy oblast (from 2024 also Sumy)", "IFC Energy Efficiency Fund and Crisis Response Program for Ukraine, World Bank Group", None,
     "Designed and delivered training for HOAs and local authorities; helped prepare 41 successful grant applications to the Energy Efficiency Fund; advised municipalities on local support programmes for energy modernisation; financial models and cost-benefit analyses for HOA projects."),
    ("2017 — August 2026", "Associate Professor (part-time)", "Cherkasy State Technological University", None,
     "Developed and introduced the course “Economics of Sustainable Development”; lectures and research on international economics, European integration and energy efficiency policy."),
    ("2025 — present", "Board member, international cooperation projects coordinator (voluntary)", "NGO E-TEAM", ETEAM,
     "LEAR of the organisation on the European Commission’s Funding & Tenders portal; cooperation with international partners in green transition projects.")],
  practice_h="Practice in figures, 2019–2026",
  practice="1,200+ consultations for homeowner associations · 50+ co-owners’ general meetings attended · speaker at 80+ seminars, webinars and forums.",
  edu_h="Academic degree",
  edu=[("2014", "PhD in Economics — Taras Shevchenko National University of Kyiv")],
  pubs_h="Publications",
  pubs=[("2024", "Information campaigns as a tool for changing consumer energy behaviour: EU experience", "III International Scientific and Practical Conference, Ternopil, WUNU (in Ukrainian)", PUBS_URLS[0]),
        ("2022", "Factors influencing homeowners’ decisions on the modernisation of multi-apartment buildings", "IX International Scientific and Practical Conference, ChSTU (in Ukrainian)", PUBS_URLS[2]),
        ("2021", "Economic policy formation mechanism for energy efficiency area", "Socio-Economic Research Bulletin (ONEU), 2021, No. 2 (77), pp. 25–40. DOI 10.33987/vsed.2(77).2021.25-40", "http://vsed.oneu.edu.ua/collections/2021/77/pdf/25-40.pdf"),
        PUB_JOURNAL_EN],
  pub_more="Full list:",
  mentions_h="Mentioned in",
  mentions=[("2026", "Zolotonosha.City: seminar for heads of homeowner associations (in Ukrainian)", MENTIONS_UA[0][2]),
            ("2019", "Dzvin media: seminar for co-owners in Cherkasy — IFC regional energy efficiency consultant (in Ukrainian)",
             "https://dzvin.media/news/trend-na-energooshhadnist-cherkashhan-navchaly-zaluchaty-koshty-na-vtilennya-enregoefektyvnyh-zahodiv/")],
)


# ----------------------------------------------------------------- components

def c_header(c, cur, nav, other=None):
    links = "".join(f'<a href="{h}"{" class=\"home\"" if i == 0 and len(nav) > 3 else ""}{" aria-current=\"page\"" if h == cur else ""}>{esc(l)}</a>' for i, (h, l) in enumerate(nav))
    lang = f'<a class="lang" href="{other[0]}" hreflang="{other[2]}" lang="{other[2]}">{other[1]}</a>' if other else ''
    return f"""<a class="skip" href="#main">{esc(c['skip'])}</a>
<header class="hdr"><div class="wrap">
  <a class="brand" href="{nav[0][0]}"><b>{esc(c['name'])}</b><span>{esc(c['brand_sub']).replace(' · ', '&nbsp;· ').replace('енергетичне планування', 'енергетичне&nbsp;планування')}</span></a>
  <nav class="nav" aria-label="{esc(c['nav_label'])}">
    <div class="links">{links}</div>
    <div class="tools"><a class="tel" href="{TEL}">{TEL_H}</a>{lang}</div>
  </nav>
</div></header>"""


def c_footer(c):
    return f"""<footer><div class="wrap">
  <div><b>{esc(c['name'])}</b>{esc(c['ft_role'])}<br>{esc(c['ft_board'])}</div>
  <div><b><a href="{TEL}">{TEL_H}</a></b><a href="mailto:{MAIL_W}">{MAIL_W}</a></div>
  <div><a href="{ORCID}" rel="noopener">ORCID</a> · <a href="{SCHOLAR}" rel="noopener">Google Scholar</a> · <a href="{ETEAM}" rel="noopener">{esc(c['ft_org'])}</a>{' · <a href="pro-mene.html">Про мене</a>' if c['lang']=='uk' else ''}</div>
  <div class="base"><p class="legal" aria-label="{esc(c['lg_aria'])}"><span class="lg-k">{esc(c['lg_k'])}</span><span class="lg-n">{esc(c['lg_n'])}</span></p><p class="cr">{esc(c['ft_base'])}</p></div>
</div></footer>"""


def c_contact(c, band=True, head=True):
    roles = "".join(f'<label><input type="radio" name="role" value="{esc(r)}" id="role-{k}"> {esc(r)}</label>' for k, r in enumerate(c["roles"]))
    needs = "".join(f'<label><input type="checkbox" name="need" value="{esc(r)}" id="need-{k}"> {esc(r)}</label>' for k, r in enumerate(c["needs"]))
    cts = ""
    for k, v, href, cp in c["contacts"]:
        ext = ' rel="noopener"' if href.startswith("http") else ''
        btn = f'<button class="copy" type="button" data-v="{esc(v)}">{esc(c["copy_short"])}</button>' if cp else ''
        cts += f'<div class="ct"><span class="k">{esc(k)}</span><a class="v" href="{esc(href)}"{ext}>{esc(v)}</a>{btn}</div>'
    return f"""<section id="contact" class="{'band' if band else ('' if head else 'plain')}" aria-labelledby="c-h"><div class="wrap">
  {f'<div class="sh"><h2 id="c-h">{esc(c["c_h"])}</h2><p>{esc(c["c_sub"])}</p></div>' if head else f'<h2 id="c-h" class="vh">{esc(c["form_h"])}</h2>'}
  <div class="req"><form class="form" id="reqform" novalidate>
{f'<h3>{esc(c["form_h"])}</h3>' if head else ''}<p class="hint">{esc(c['form_hint'])}</p>
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


def c_gates(p):
    rows = "".join(f'<li><a href="{h}"><span><b>{esc(t)}</b><span class="r">{esc(r)}</span></span><span class="arr" aria-hidden="true">→</span></a></li>'
                   for h, t, r in p["gates"])
    return f'<nav class="gates" aria-labelledby="gates-l"><p class="lbl" id="gates-l">{esc(p["gates_h"])}</p><ul>{rows}</ul></nav>'


def c_cta(c, h, sub, role):
    return f"""<section id="contact" class="band cta-s" aria-labelledby="cta-h"><div class="wrap">
  <div><h2 id="cta-h">{esc(h)}</h2><p>{esc(sub)}</p><a class="mail" href="mailto:{MAIL}">{MAIL}</a></div>
  <div class="acts"><a class="btn btn-p" href="zvernennia.html?role={role}">{esc(c['cta_btn'])}</a><a class="btn btn-s" href="{TEL}" aria-label="{esc(c['call'])}: {TEL_H}">{PHONE_ICON}<span>{TEL_H}</span></a></div>
</div></section>"""


def c_plan(p, sid="plan"):
    items = ""
    for i, (h, first, d, you) in enumerate(p["plan"]):
        fl = f'<span class="first">{"почніть із цього"}</span>' if first else ''
        items += (f'<li><span class="n">{i+1:02d}</span><div><h3>{esc(h)}{fl}</h3><p>{esc(d)}</p></div>'
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
        tl += f'<li><div class="yr">{esc(yr)}</div><div><h3>{esc(role)}</h3>{f"<p class=org>{o}</p>" if org else ""}<p class="d">{esc(d)}</p></div></li>'
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
          "jobTitle": c["jobTitle"], "email": "mailto:" + MAIL_W, "telephone": TEL_H, "url": BASE,
          "address": {"@type": "PostalAddress", "addressLocality": "Cherkasy", "addressCountry": "UA"},
          "memberOf": {"@type": "Organization", "name": "NGO E-TEAM", "url": ETEAM},
          "knowsAbout": ["Energy efficiency", "Municipal energy planning", "Energy communities", "Homeowner associations"],
          "sameAs": [ORCID, SCHOLAR]}
    alts = (f'<link rel="alternate" hreflang="uk" href="{BASE}"><link rel="alternate" hreflang="en" href="{BASE}en.html"><link rel="alternate" hreflang="x-default" href="{BASE}">' if alt else '')
    head = (f'<title>{esc(ttl)}</title>' + ('' if seo else '<meta name="claude:viewport-fit-sides" content="cover">') +
            f'<meta name="description" content="{esc(p["description"])}"><link rel="canonical" href="{url}">{alts}'
            f'<meta property="og:type" content="website"><meta property="og:title" content="{esc(ttl)}"><meta property="og:description" content="{esc(p["description"])}"><meta property="og:url" content="{url}">'
            f'<meta property="og:image" content="{BASE}og.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image">'
            f'<link rel="icon" href="{FAVICON}">{FONTS}<style>{FONT_FACES}{CSS}{CSS_PAGES}{CSS_NEW}</style>'
            f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>')
    js = (JS.replace("__LAB__", json.dumps(c["f_lab"], ensure_ascii=False)).replace("__HDR__", json.dumps(c["f_hdr"], ensure_ascii=False))
            .replace("__COPY__", json.dumps(c["copy"], ensure_ascii=False)).replace("__COPIED__", json.dumps(c["copied"], ensure_ascii=False))) + JS_PAGES
    def _nw(m):
        t = m.group(1)
        for w in ("«Е-ТЕАМ»", "E-TEAM"):
            t = t.replace(w, f'<span class="nw">{w}</span>')
        return '>' + t + '<'
    body = re.sub(r'>([^<]+)<', _nw, body)  # text nodes only, never attributes
    if 'id="reqform"' in body:
        full_body = f'{body}<script>{js}</script>'
    elif 'id="qform"' in body:
        jq = JS_Q.replace("__T__", json.dumps(Q_UA, ensure_ascii=False)).replace("__KEY__", json.dumps(WEB3_KEY)).replace("__TO__", json.dumps(MAIL_W))
        full_body = f'{body}<script>{jq}{JS_PAGES}</script>'
    else:
        full_body = body
    return (f'<!doctype html><html lang="{c["lang"]}"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width, initial-scale=1">{head}</head>'
            f'<body data-role="{p.get("role_default", "")}">{full_body}</body></html>')


# ----------------------------------------------------------------- pages

def home_en(c, p, nav, other, lang_ua=False):
    if lang_ua:
        mid = ""
    elif False:
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
    <div class="acts"><a class="btn btn-p" href="{'zvernennia.html' if lang_ua else '#contact'}">{esc(p['cta1'])}</a><a class="btn btn-s" href="{TEL}" aria-label="{esc(c['call'])}: {TEL_H}">{PHONE_ICON}<span>{TEL_H}</span></a></div>
  </div>
  {c_gates(p) if lang_ua else c_facts(p)}
</div>
{mid}
{c_experience(p)}
{c_cta(c, p['cta_h'], p['cta_sub'], '') if lang_ua else c_contact(c)}
</main>
{c_footer(c)}"""
    return body


WEB3_KEY = ""  # ключ доступу Web3Forms; поки порожній — лист складається в поштовій програмі відвідувача

Q_UA = dict(name="Ваше ім’я", contact="Телефон або email", msg="Ваше питання", msg_ph="кілька слів про ситуацію",
            role="Хто звертається", btn="Надіслати повідомлення",
            err="Вкажіть ім’я та телефон або email, щоб я міг відповісти.", err_role="Оберіть, хто звертається.",
            ok="Дякую, звернення надіслано.",
            mail="Відкрилася ваша поштова програма з готовим листом — залишилося натиснути «Надіслати» в ній. Якщо вона не відкрилася, скопіюйте текст і надішліть його на {to} або зателефонуйте.",
            fail="Не вдалося надіслати. Скопіюйте текст і надішліть його на {to} або зателефонуйте.",
            copy="Копіювати текст", copied="Скопійовано", hdr="Звернення з сайту",
            more="Як обробляються дані — на сторінці «Звернення».")

JS_Q = r"""
(function(){var f=document.getElementById('qform'); if(!f) return; var T=__T__, KEY=__KEY__, TO=__TO__;
var out=document.getElementById('q-out'), msg=document.getElementById('q-msgout'), pre=document.getElementById('q-text'), cp=document.getElementById('q-copy');
f.addEventListener('submit',function(e){e.preventDefault();
  var g=function(id){var x=document.getElementById(id);return x?x.value.trim():'';};
  var err=document.getElementById('q-err'), rr=f.querySelector('input[name=role]:checked');
  var role=f.querySelector('input[name=role]')?(rr?rr.value:''):f.getAttribute('data-role');
  var name=g('q-name'), contact=g('q-contact'); var to=f.getAttribute('data-to')||TO; if(f.getAttribute('data-to-gov')&&role===f.getAttribute('data-gov-role')) to=f.getAttribute('data-to-gov');
  if(!name||!contact||!role){err.textContent=!role?T.err_role:T.err;err.hidden=false;err.focus();return;} err.hidden=true;
  var txt=[T.hdr+' ('+location.pathname.split('/').pop()+')', T.role+': '+role, T.name+': '+name, T.contact+': '+contact].concat(g('q-msg')?[T.msg+': '+g('q-msg')]:[]).join('\n');
  pre.textContent=txt; cp.setAttribute('data-v',txt);
  var show=function(m,ok){msg.textContent=m.replace('{to}',to); out.hidden=false; pre.hidden=ok; cp.hidden=ok; out.scrollIntoView({behavior:'smooth',block:'nearest'});};
  if(KEY){
    fetch('https://api.web3forms.com/submit',{method:'POST',headers:{'Content-Type':'application/json','Accept':'application/json'},
      body:JSON.stringify({access_key:KEY,subject:T.hdr+': '+role,from_name:name,contact:contact,role:role,message:g('q-msg'),botcheck:''})})
    .then(function(r){return r.json();}).then(function(j){if(j&&j.success){show(T.ok,true);f.reset();}else show(T.fail,false);})
    .catch(function(){show(T.fail,false);});
  } else {
    location.href='mailto:'+to+'?subject='+encodeURIComponent(T.hdr+': '+role)+'&body='+encodeURIComponent(txt);
    show(T.mail,false);
  }
});
cp.addEventListener('click',function(){var v=cp.getAttribute('data-v'),l=cp.textContent;try{navigator.clipboard.writeText(v).then(function(){cp.textContent=T.copied;setTimeout(function(){cp.textContent=l;},1600);});}catch(e){}});
document.querySelectorAll('.ct .copy').forEach(function(b){b.addEventListener('click',function(){var v=b.getAttribute('data-v'),l=b.textContent;try{navigator.clipboard.writeText(v).then(function(){b.textContent=T.copied;setTimeout(function(){b.textContent=l;},1600);});}catch(e){}});});
})();
"""

CSS_NEW = r"""
.card-home{padding-block:64px var(--s-8)}
.card-home h1{font-size:clamp(36px,5vw,48px)}
.card-home .lead{max-width:40em;margin-bottom:var(--s-6)}
.bigbtns{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:var(--s-4)}
.bigbtns a{display:flex;flex-direction:column;gap:var(--s-3);height:100%;box-sizing:border-box;padding:var(--s-5);border:1.5px solid var(--rule);border-top:3px solid var(--primary);border-radius:var(--r-2);background:var(--surface);color:var(--ink);text-decoration:none}
.bigbtns a:hover{border-color:var(--primary)}
.bigbtns a:hover b{color:var(--primary)}
.bigbtns b{font-family:var(--serif);font-weight:600;font-size:22px;line-height:1.25}
.bigbtns .txt{font-size:var(--fs-small);line-height:1.5}
.bigbtns .cap{font-size:13.5px;line-height:1.5;color:var(--ink-2)}
.fundnote{max-width:var(--measure);font-size:13.5px;line-height:1.5;color:var(--ink-2);margin:var(--s-5) 0 0}
.when{list-style:none;margin:0 0 var(--s-4);padding:0;display:grid;gap:var(--s-2);max-width:var(--measure)}
.when b{color:var(--primary)}
.ctg{margin:0 0 var(--s-2);font-size:var(--fs-small);color:var(--ink-2);font-weight:600}
.ctg+.contact{margin-bottom:var(--s-6)}
.bigbtns .go{margin-top:auto;padding-top:var(--s-2);font-weight:600;color:var(--primary)}
.homelinks{list-style:none;margin:var(--s-6) 0 0;padding:0;border-top:1px solid var(--rule)}
.homelinks li{border-bottom:1px solid var(--rule);padding-block:var(--s-3)}
.homelinks a.go2{font-weight:600;text-decoration:none}
.homelinks a.go2:hover{text-decoration:underline}
.homelinks .ctl{display:flex;flex-wrap:wrap;gap:var(--s-2) var(--s-5)}
.homelinks .media{color:var(--ink-2);font-size:var(--fs-small)}
.mailline{margin:var(--s-3) 0 0;font-size:var(--fs-small)}
.prose{max-width:var(--measure);margin:0 0 var(--s-4)}
.chlinks{max-width:var(--measure);font-size:var(--fs-small);color:var(--ink-2);margin-top:var(--s-6)}
.also{list-style:none;margin:0;padding:0;display:grid;gap:var(--s-4);max-width:860px}
.also li{position:relative;padding-left:22px}
.also li::before{content:"";position:absolute;left:2px;top:.68em;width:7px;height:7px;border-radius:50%;background:var(--ink-2)}
.qwrap{display:grid;grid-template-columns:minmax(0,5fr) minmax(0,7fr);gap:var(--s-7);align-items:start}
.qintro h2{margin-bottom:var(--s-3)}
.qintro p{color:var(--ink-2)}
.qct{margin-top:var(--s-4);display:grid;gap:var(--s-1);font-size:var(--fs-small)}
.qct a{font-weight:600}
.qct .tel{font-size:18px}
.consent{color:var(--ink-2);margin:calc(-1 * var(--s-2)) 0 0}
.qout{grid-column:2;border:1.5px solid var(--primary);border-radius:var(--r-2);padding:var(--s-5);background:var(--tint);display:flex;flex-direction:column;gap:var(--s-3);min-width:0}
.qout p{margin:0;font-weight:600}
.qout pre{margin:0;white-space:pre-wrap;word-break:break-word;font-family:var(--sans);font-size:15px;line-height:1.55}
.pcards{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:var(--s-4)}
.pcards li{border:1px solid var(--rule);border-radius:var(--r-2);padding:var(--s-5);display:flex;flex-direction:column;gap:var(--s-2);background:var(--surface)}
.pcards .yrs{align-self:flex-start;font-size:13px;font-weight:600;color:var(--primary);border:1px solid var(--primary);border-radius:var(--r-1);padding:1px 8px}
.pcards h3{font-size:18px;line-height:1.35;margin:var(--s-1) 0 0}
.pcards .fund{font-size:13.5px;color:var(--ink-2);margin:0}
.pcards .prole{margin:auto 0 0;padding-top:var(--s-3);border-top:1px solid var(--rule);font-size:var(--fs-small)}
.datal{list-style:none;margin:0;padding:0;display:grid;gap:var(--s-2);max-width:var(--measure);font-size:var(--fs-small)}
@media (max-width:900px){.bigbtns,.qwrap,.pcards{grid-template-columns:minmax(0,1fr)}.qwrap{gap:var(--s-5)}.qout{grid-column:1}}
@media (max-width:560px){.card-home{padding-block:var(--s-6) var(--s-7)}}
"""


def c_qform(c, p, role_idx=None, with_roles=False, sid="contact", band=True):
    q = Q_UA
    roles = ""
    if with_roles:
        roles = ('<fieldset><legend>' + esc(q["role"]) + '</legend><div class="opts">' +
                 "".join(f'<label><input type="radio" name="role" value="{esc(r)}" id="role-{k}"> {esc(r)}</label>' for k, r in enumerate(c["roles"])) +
                 '</div></fieldset>')
    drole = esc(c["roles"][int(role_idx)]) if role_idx not in (None, "") else ""
    mails = (f'<a href="mailto:{MAIL}">{MAIL}</a><a href="mailto:{MAIL_W}">{MAIL_W}</a>' if p.get("gmail") else f'<a href="mailto:{MAIL_W}">{MAIL_W}</a>')
    to = MAIL if p.get("gmail") else MAIL_W
    route = f' data-to-gov="{MAIL}" data-gov-role="{esc(c["roles"][1])}"' if with_roles else ''
    consent = p.get("consent_q", p.get("consent", ""))
    more = "" if p["file"] == "zvernennia.html" else f' <a href="zvernennia.html#data">{esc(q["more"])}</a>'
    if p["file"] == "zvernennia.html":
        consent = p["consent"]
    head = (f'<div class="qintro"><h2 id="q-h">{esc(p["q_h"])}</h2><p>{esc(p["q_sub"])}</p>'
            f'<p class="qct"><a class="tel" href="{TEL}">{TEL_H}</a>{mails}</p></div>') if p.get("q_h") else '<h2 id="q-h" class="vh">' + esc(p["h1"]) + '</h2><div></div>'
    return f"""<section id="{sid}" class="{'band' if band else 'plain'}" aria-labelledby="q-h"><div class="wrap qwrap">
  {head}
  <form class="form qf" id="qform" novalidate data-role="{drole}" data-to="{to}"{route}>
    {roles}
    <div class="row2"><div><label class="l" for="q-name">{esc(q['name'])}</label><input type="text" id="q-name" autocomplete="name"></div>
    <div><label class="l" for="q-contact">{esc(q['contact'])}</label><input type="text" id="q-contact" autocomplete="email"></div></div>
    <div><label class="l" for="q-msg">{esc(q['msg'])}</label><textarea id="q-msg" placeholder="{esc(q['msg_ph'])}"></textarea></div>
    <p class="err" id="q-err" tabindex="-1" hidden></p>
    <div><button class="btn btn-p" type="submit">{esc(q['btn'])}</button></div>
    <p class="consent small">{esc(consent)}{more}</p>
  </form>
  <div class="qout" id="q-out" hidden aria-live="polite"><p id="q-msgout"></p><pre id="q-text"></pre><button class="copy" type="button" id="q-copy" data-v="">{esc(q['copy'])}</button></div>
</div></section>"""


def c_hero(c, p, btns=True):
    acts = ""
    if btns:
        acts = (f'<div class="acts"><a class="btn btn-p" href="#contact">{esc(p["btn"])}</a>'
                f'<a class="btn btn-s" href="{TEL}" aria-label="{esc(c["call"])}: {TEL_H}">{PHONE_ICON}<span>{TEL_H}</span></a></div>'
                f'<p class="mailline"><a href="mailto:{MAIL if p.get("gmail") else MAIL_W}">{MAIL if p.get("gmail") else MAIL_W}</a></p>')
    free = f'<p class="tag-free">{esc(p["free"])}</p>' if p.get("free") else ''
    fund = f'<p class="fundnote">{esc(p["fund"])}</p>' if p.get("fund") else ''
    return f"""<div class="wrap phero">
  <p class="kicker back"><a href="index.html">{esc(c['back'])}</a> · {esc(p['kicker'])}</p>
  <h1>{esc(p['h1'])}</h1>
  <p class="lead">{esc(p['lead'])}</p>
  {free}{acts}{fund}
</div>"""


def home(c, p, nav, other):
    big = "".join(f'<li><a href="{h}"><b>{esc(t)}</b><span class="txt">{esc(txt)}</span><span class="cap">{esc(cap)}</span><span class="go">{esc(go)} →</span></a></li>'
                  for h, t, txt, cap, go in p["big"])
    return f"""{c_header(c, p['file'], nav, other)}
<main id="main">
<div class="wrap card-home">
  <h1>{esc(c['name'])}</h1>
  <p class="role">{esc(p['role'])}</p>
  <p class="lead">{esc(p['lead'])}</p>
  <ul class="bigbtns">{big}</ul>
  <ul class="homelinks">
    <li><a class="go2" href="pro-mene.html">{esc(p['about'])} →</a></li>
    <li><a class="go2" href="zvernennia.html">{esc(p['ask'])} →</a></li>
    <li><span class="ctl"><a href="{TEL}"><b>{TEL_H}</b></a><a href="mailto:{MAIL_W}">{MAIL_W}</a></span></li>
    <li class="media">{esc(p['media'])} — <a href="{TEL}">{TEL_H}</a> · <a href="mailto:{MAIL_W}">{MAIL_W}</a></li>
  </ul>
</div>
</main>
{c_footer(c)}"""


def c_list(items):
    return "".join(f'<li>{esc(x)}</li>' for x in items)


def osbb(c, p, nav):
    progs = "".join(f'<li><a href="{u}" rel="noopener">{esc(t)}</a></li>' for t, u in p["progs"])
    also = "".join(f'<li><b>{esc(a)}</b> {esc(b)}</li>' for a, b in p["also"])
    return f"""{c_header(c, p['file'], nav, ('en.html', 'EN', 'en'))}
<main id="main">
{c_hero(c, p)}
{c_plan(p)}
<section id="self" class="band" aria-labelledby="self-h"><div class="wrap split">
  <div><h2 id="self-h">{esc(p['self_h'])}</h2><p class="sub2">{esc(p['self_sub'])}</p><ul class="check">{c_list(p['selfcheck'])}</ul></div>
  <div id="prepare"><h2 id="prep-h">{esc(p['prep_h'])}</h2><div class="prep" style="display:block"><ul>{c_list(p['prep'])}</ul></div></div>
</div></section>
<section id="programs" aria-labelledby="pr-h"><div class="wrap">
  <div class="sh"><h2 id="pr-h">{esc(p['progs_h'])}</h2><p>{esc(p['progs_sub'])}</p></div>
  <ul class="links-out">{progs}</ul>
</div></section>
<section id="also" aria-labelledby="al-h"><div class="wrap">
  <div class="sh"><h2 id="al-h">{esc(p['also_h'])}</h2></div>
  <ul class="also">{also}</ul>
</div></section>
{c_qform(c, p, p['role_default'])}
</main>
{c_footer(c)}"""


def ec_page(c, p, nav):
    links = " · ".join(f'<a href="{u}" rel="noopener">{esc(t)}</a>' for t, u in p["links"])
    return f"""{c_header(c, p['file'], nav, ('en.html', 'EN', 'en'))}
<main id="main">
<div class="wrap phero">
  <p class="kicker back"><a href="index.html">{esc(c['back'])}</a> · {esc(p['kicker'])}</p>
  <h1>{esc(p['h1'])}</h1>
  <p class="lead">{esc(p['lead'])}</p>
  <p class="prose"><b>{esc(p['project'][0])}</b> {esc(p['project'][1])}</p>
  <p class="prose"><b>{esc(p['now_h'])}</b></p>
  <ul class="when">{"".join(f'<li><b>{esc(a)}</b> {esc(b)}</li>' for a, b in p['now'])}</ul>
</div>
{c_plan(p).replace('</ol>', '</ol><p class="chlinks">' + esc(p['links_lbl']) + ' ' + links + '</p>', 1)}
{c_qform(c, p, p['role_default'])}
</main>
{c_footer(c)}"""


def mep_page(c, p, nav):
    return f"""{c_header(c, p['file'], nav, ('en.html', 'EN', 'en'))}
<main id="main">
{c_hero(c, p)}
{c_plan(p)}
<section id="prepare" class="band" aria-labelledby="prep-h"><div class="wrap split">
  <div class="sh" style="margin:0"><h2 id="prep-h">{esc(p['prep_h'])}</h2></div>
  <div class="prep" style="display:block"><ul>{c_list(p['prep'])}</ul></div>
</div></section>
{c_qform(c, p, p['role_default'], band=False)}
</main>
{c_footer(c)}"""


def about_page(c, p, nav):
    cards = "".join(f'<li><span class="yrs">{esc(y)}</span><h3>{esc(t)}</h3><p class="fund">{esc(f)}</p><p class="prole">{esc(r)}</p></li>'
                    for y, t, f, r in p["cards"])
    def tl(items):
        out = ""
        for yr, role, org, url, d in items:
            o = (f'<a href="{url}" rel="noopener">{esc(org)}</a>' if url else esc(org)) if org else ''
            out += f'<li><div class="yr">{esc(yr)}</div><div><h3>{esc(role)}</h3>{f"<p class=org>{o}</p>" if o else ""}<p class="d">{esc(d)}</p></div></li>'
        return out
    edu = "".join(f'<li><span class="y">{y}</span><span>{esc(x)}</span></li>' for y, x in p["edu"])
    ment = "".join(f'<li><span class="y">{y}</span><a href="{u}" rel="noopener">{esc(t)}</a></li>' for y, t, u in p["mentions"])
    return f"""{c_header(c, p['file'], nav, ('en.html', 'EN', 'en'))}
<main id="main">
<div class="wrap phero">
  <p class="kicker back"><a href="index.html">{esc(c['back'])}</a> · {esc(p['kicker'])}</p>
  <h1>{esc(p['h1'])}</h1>
  <p class="lead">{esc(p['lead'])}</p>
</div>
<section id="programs" class="band" aria-labelledby="pc-h"><div class="wrap">
  <div class="sh"><h2 id="pc-h">{esc(p['cards_h'])}</h2></div>
  <ul class="pcards">{cards}</ul>
</div></section>
<section id="experience" aria-labelledby="e-h"><div class="wrap">
  <div class="sh"><h2 id="e-h">{esc(p['e_h'])}</h2></div>
  <ul class="tl">{tl(p['timeline'])}</ul>
  <h2 class="subh" id="civic-h" style="font-size:var(--fs-h2)">{esc(p['civic_h'])}</h2>
  <ul class="tl">{tl(p['civic'])}</ul>
  <div class="practice"><h3>{esc(p['practice_h'])}</h3><p>{esc(p['practice'])}</p></div>
  <h3 class="subh">{esc(p['edu_h'])}</h3><ul class="rows">{edu}</ul>
  <h3 class="subh" id="publications">{esc(p['pubs_h'])}</h3><ul class="rows">{c_rows(p['pubs'])}</ul>
  <p class="note">{esc(p['pub_more'])} <a href="{SCHOLAR}" rel="noopener">Google Scholar</a>, <a href="{ORCID}" rel="noopener">ORCID</a></p>
  <h3 class="subh">{esc(p['mentions_h'])}</h3><ul class="mentions">{ment}</ul>
</div></section>
{c_qform(c, p, None, with_roles=True)}
</main>
{c_footer(c)}"""


def contact_page(c, p, nav):
    cts = ""
    for g, items in p["contacts"]:
        cts += f'<h3 class="ctg">{esc(g)}</h3><div class="contact">'
        for k, v, href, cp in items:
            ext = ' rel="noopener"' if href.startswith("http") else ''
            btn = f'<button class="copy" type="button" data-v="{esc(v)}">{esc(c["copy_short"])}</button>' if cp else ''
            cts += f'<div class="ct"><span class="k">{esc(k)}</span><a class="v" href="{esc(href)}"{ext}>{esc(v)}</a>{btn}</div>'
        cts += '</div>'
    data = "".join(f'<li>{f"<b>{esc(a)}</b> " if a else ""}{esc(b)}</li>' for a, b in p["data"])
    return f"""{c_header(c, p['file'], nav, ('en.html', 'EN', 'en'))}
<main id="main">
<div class="wrap phero">
  <p class="kicker back"><a href="index.html">{esc(c['back'])}</a> · {esc(p['kicker'])}</p>
  <h1>{esc(p['h1'])}</h1>
  <p class="lead">{esc(p['lead'])}</p>
</div>
{c_qform(c, p, None, with_roles=True, band=False)}
<section id="data" class="band" aria-labelledby="d-h"><div class="wrap">
  <div class="sh"><h2 id="d-h">{esc(p['data_h'])}</h2></div>
  <ul class="datal">{data}</ul>
</div></section>
<section id="contacts" aria-label="Контакти"><div class="wrap">{cts}</div></section>
</main>
{c_footer(c)}"""


def build_all():
    cu, ce = COMMON["ua"], COMMON["en"]
    nav_en = [("en.html", "Home"), ("#experience", "Experience"), ("#contact", "Contact")]
    pages = {
        "index.html": doc(cu, HOME_UA, home(cu, HOME_UA, NAV_UA, ("en.html", "EN", "en")), True),
        "en.html": doc(ce, HOME_EN, home_en(ce, HOME_EN, nav_en, ("index.html", "UA", "uk")), True),
        "osbb.html": doc(cu, OSBB_UA, osbb(cu, OSBB_UA, NAV_UA), True, alt=False),
        "energospilnoty.html": doc(cu, EC_UA, ec_page(cu, EC_UA, NAV_UA), True, alt=False),
        "mep.html": doc(cu, MEP_UA, mep_page(cu, MEP_UA, NAV_UA), True, alt=False),
        "pro-mene.html": doc(cu, ABOUT_UA, about_page(cu, ABOUT_UA, NAV_UA), True, alt=False),
        "zvernennia.html": doc(cu, ZV_UA, contact_page(cu, ZV_UA, NAV_UA), True, alt=False),
    }
    return pages


if __name__ == "__main__":
    for d in ("preview", "dist"):
        os.makedirs(os.path.join(HERE, d), exist_ok=True)
    pages = build_all()
    for fn, html in pages.items():
        open(os.path.join(HERE, "dist", fn), "w").write(html)
        open(os.path.join(HERE, "preview", fn), "w").write(html)
    import shutil
    for d in ("preview", "dist"):
        shutil.copytree(os.path.join(HERE, "fonts"), os.path.join(HERE, d, "fonts"), dirs_exist_ok=True)
    make_og(os.path.join(HERE, "dist", "og.png"))
    open(os.path.join(HERE, "dist", "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}sitemap.xml\n")
    urls = ["", "osbb.html", "energospilnoty.html", "mep.html", "pro-mene.html", "zvernennia.html", "en.html"]
    open(os.path.join(HERE, "dist", "sitemap.xml"), "w").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "".join(f'<url><loc>{BASE}{u}</loc><lastmod>2026-11-03</lastmod></url>\n' for u in urls) + '</urlset>\n')
    open(os.path.join(HERE, "dist", ".nojekyll"), "w").write("")
    print("ok", list(pages))
