"""Build Dmytro Palamarchuk's personal site (UA + EN) from one template.

Outputs:
  preview/index.html  - UA page without document skeleton (for Artifact preview)
  preview/en.html     - EN page with full skeleton
  dist/index.html, dist/en.html - both with full skeleton (for GitHub Pages)
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
         'family=Commissioner:wght@400;500;600;700;800&display=swap">')

CSS = r"""
/* Concept: a thermal camera pointed at a Ukrainian panel block. Night bands carry the thermal image and the figures;
   light bands carry reading. One typeface (Commissioner, Ukrainian design) in a tight weight scale. */
:root{
  --paper:#f1f4f6; --surface:#ffffff; --ink:#122130; --ink-2:#4a5a68; --rule:#d6dee5;
  --accent:#0e6a64; --accent-ink:#ffffff; --accent-soft:#e0eeec;
  --night:#101b28; --night-2:#172536; --on-night:#edf1f5; --on-night-2:#a8b6c5; --night-rule:#2a3a4d;
  --heat:#e8642c; --c-g:#c0412c; --c-c:#8fae3a;
  --f:"Commissioner","Segoe UI",system-ui,sans-serif;
}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){
  --paper:#0e1620; --surface:#15202c; --ink:#e6ecf1; --ink-2:#a3b1bf; --rule:#26354a;
  --accent:#5cc2b8; --accent-ink:#0a1918; --accent-soft:#14302f;
  --night:#09111a; --night-2:#111c28; --night-rule:#223246; color-scheme:dark}}
:root[data-theme="dark"]{
  --paper:#0e1620; --surface:#15202c; --ink:#e6ecf1; --ink-2:#a3b1bf; --rule:#26354a;
  --accent:#5cc2b8; --accent-ink:#0a1918; --accent-soft:#14302f;
  --night:#09111a; --night-2:#111c28; --night-rule:#223246; color-scheme:dark}
*{box-sizing:border-box}
[hidden]{display:none !important}
html{scroll-behavior:smooth}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--f);font-size:17px;line-height:1.6;font-weight:400}
a{color:var(--accent);text-underline-offset:3px}
a:focus-visible,button:focus-visible,input:focus-visible,textarea:focus-visible{outline:2px solid var(--accent);outline-offset:3px}
.wrap{max-width:1120px;margin:0 auto;padding-left:max(20px,env(safe-area-inset-left,0px));padding-right:max(20px,env(safe-area-inset-right,0px))}
.night{background:var(--night);color:var(--on-night)}
.night a:focus-visible,.night button:focus-visible{outline-color:var(--on-night)}

/* header */
.top{display:flex;justify-content:space-between;align-items:center;gap:20px;padding-block:22px;border-bottom:1px solid var(--night-rule)}
.brand{font-weight:700;font-size:17px;letter-spacing:-.01em;color:var(--on-night);text-decoration:none}
.nav{display:flex;gap:26px;font-size:15px}
.nav a{color:var(--on-night-2);text-decoration:none}
.nav a:hover{color:var(--on-night)}
.nav .lang{color:var(--on-night);border:1px solid var(--night-rule);padding:1px 9px;border-radius:6px;font-weight:600;font-size:13.5px}

/* hero */
.hero{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.02fr);gap:64px;align-items:center;padding-block:76px 92px}
h1{font-weight:800;font-size:clamp(46px,6.6vw,84px);line-height:.98;letter-spacing:-.035em;margin:0 0 28px}
h1 span{display:block}
.lead{font-size:21px;line-height:1.45;max-width:30em;margin:0 0 14px;color:var(--on-night)}
.lead2{font-size:16.5px;line-height:1.55;color:var(--on-night-2);max-width:34em;margin:0 0 26px}
.quick{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 30px}
.quick a{font-size:14.5px;text-decoration:none;color:var(--on-night);border:1px solid var(--night-rule);border-radius:999px;padding:6px 14px;background:var(--night-2)}
.quick a:hover{border-color:var(--on-night-2)}
.cta{display:flex;gap:12px;flex-wrap:wrap;margin:0 0 26px}
.btn{display:inline-block;padding:12px 20px;border-radius:8px;font-weight:600;font-size:15.5px;text-decoration:none;border:1.5px solid var(--accent);font-family:inherit;cursor:pointer}
.btn.primary{background:var(--accent);color:var(--accent-ink)}
.btn.ghost{color:var(--accent);background:transparent}
.night .btn.primary{background:var(--on-night);border-color:var(--on-night);color:var(--night)}
.night .btn.ghost{color:var(--on-night);border-color:var(--night-rule)}
.night .btn.ghost:hover{border-color:var(--on-night-2)}
.meta{color:var(--on-night-2);font-size:14.5px;margin:0;max-width:36em}

/* thermal figure */
.thermo-fig{margin:0}
.thermo{position:relative;aspect-ratio:600/540;border-radius:16px;overflow:hidden;background:#0b1520;--pos:50%;user-select:none;touch-action:pan-y}
.thermo svg{position:absolute;inset:0;width:100%;height:100%;display:block}
.thermo .before{clip-path:inset(0 calc(100% - var(--pos)) 0 0)}
.thermo .handle{position:absolute;top:0;bottom:0;left:var(--pos);width:2px;margin-left:-1px;background:#fff;pointer-events:none}
.thermo .knob{position:absolute;top:50%;left:50%;width:44px;height:44px;margin:-22px 0 0 -22px;border-radius:50%;background:#fff;display:flex;align-items:center;justify-content:center;box-shadow:0 2px 10px rgba(0,0,0,.35)}
.thermo input{position:absolute;inset:0;width:100%;height:100%;margin:0;opacity:0;cursor:ew-resize}
.thermo:has(input:focus-visible){outline:2px solid #fff;outline-offset:4px}
.tag{position:absolute;top:14px;display:flex;align-items:center;gap:8px;font-size:13.5px;font-weight:600;color:#fff;background:rgba(9,17,26,.72);padding:5px 10px 5px 5px;border-radius:8px;pointer-events:none}
.tag.l{left:14px}.tag.r{right:14px}
.tag b{display:inline-flex;align-items:center;justify-content:center;width:24px;height:24px;border-radius:5px;font-size:14px;color:#fff}
.legend{display:flex;align-items:center;gap:12px;margin-top:14px;font-size:13.5px;color:var(--on-night-2);line-height:1.45}
.legend i{flex:0 0 96px;height:8px;border-radius:4px;background:linear-gradient(90deg,#211c5e,#5b2a8a,#b8336a,#f07a2a,#ffe066)}

/* light sections */
section{padding-block:96px}
section + section{border-top:1px solid var(--rule)}
.band{background:var(--surface)}
h2{font-weight:700;font-size:clamp(30px,3.9vw,46px);line-height:1.06;letter-spacing:-.025em;margin:0 0 16px;max-width:18em;text-wrap:balance}
.sub{color:var(--ink-2);font-size:18px;line-height:1.55;margin:0 0 48px;max-width:36em}
h3{font-weight:700;letter-spacing:-.01em}

/* path */
.path{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:28px;position:relative}
.path::before{content:"";position:absolute;left:0;right:0;top:19px;height:3px;border-radius:2px;background:linear-gradient(90deg,var(--heat),var(--accent))}
.path li{position:relative;padding-top:62px}
.path .n{position:absolute;top:0;left:0;width:41px;height:41px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:16px;color:#fff;border:3px solid var(--paper)}
.path h3{font-size:20px;line-height:1.25;margin:0 0 8px}
.path p{margin:0;font-size:15.5px;color:var(--ink-2)}

/* services */
.services{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px}
.svc{background:var(--paper);border-radius:16px;padding:30px 28px 26px;display:flex;flex-direction:column;gap:12px;scroll-margin-top:24px}
.svc svg{width:52px;height:52px;color:var(--accent);margin-bottom:6px}
.who{font-size:14.5px;font-weight:600;color:var(--accent);margin:0}
.svc h3{font-size:23px;line-height:1.2;margin:0}
.svc p{margin:0;font-size:15.5px}
.proof{margin-top:auto !important;padding-top:16px;border-top:1px solid var(--rule);font-size:14px !important;color:var(--ink-2)}

/* partners + trust */
.split{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.15fr);gap:64px;align-items:start}
.split .sub{margin-bottom:24px}
.plist{margin:0;padding-left:20px;display:grid;gap:10px;font-size:16px}
.trust{margin:0;padding:0;list-style:none;display:grid;gap:0;border-top:1px solid var(--rule)}
.trust li{display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);gap:20px;padding-block:16px;border-bottom:1px solid var(--rule)}
.trust .tn{font-weight:600}
.trust .tr{color:var(--ink-2);font-size:15px}
.trust-h{font-size:15px;font-weight:600;color:var(--ink-2);margin:0 0 14px}

/* figures */
.figs{padding-block:88px}
.figs h2{color:var(--on-night)}
.figures{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:32px;margin:48px 0 0;padding:0;list-style:none}
.figures li{display:flex;flex-direction:column;gap:10px;padding-top:18px;border-top:3px solid var(--heat)}
.figures li:nth-child(2){border-color:#c9663f}.figures li:nth-child(3){border-color:#6f8a63}.figures li:nth-child(4){border-color:#3f9a90}
.num{font-weight:800;font-size:clamp(48px,5.6vw,68px);line-height:1;letter-spacing:-.03em;font-variant-numeric:tabular-nums}
.figures .lbl{font-size:15px;color:var(--on-night-2);line-height:1.45}
.src{font-size:13.5px;color:var(--ink-2);margin:32px 0 0}
.figs .src{color:var(--on-night-2)}

/* prepare */
.prep{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:40px}
.prep h3{font-size:20px;margin:0 0 16px}
.prep ul{margin:0;padding:0;list-style:none;display:grid;gap:10px;font-size:15.5px}
.prep li{position:relative;padding-left:30px}
.prep li::before{content:"";position:absolute;left:0;top:4px;width:16px;height:16px;border:1.5px solid var(--accent);border-radius:4px}

/* experience */
.tl{display:grid;margin:0;padding:0;list-style:none;border-top:1px solid var(--rule)}
.tl li{display:grid;grid-template-columns:170px minmax(0,1fr);gap:32px;padding-block:24px;border-bottom:1px solid var(--rule)}
.yr{font-size:15px;font-weight:600;color:var(--ink-2);font-variant-numeric:tabular-nums;padding-top:2px}
.tl h3{font-size:19px;margin:0 0 2px}
.org{color:var(--ink-2);font-size:15px;margin:0 0 8px}
.tl p.d{margin:0;font-size:15.5px;max-width:46em}
.sub-h{font-size:21px;margin:56px 0 18px}
.edu{display:grid;grid-template-columns:170px minmax(0,1fr);gap:10px 32px;font-size:15.5px;margin:0}
.edu dt{font-weight:600;color:var(--ink-2);font-size:15px}
.edu dd{margin:0}
.pubs{list-style:none;margin:0;padding:0;display:grid;gap:14px;font-size:15.5px}
.pubs li{display:grid;grid-template-columns:170px minmax(0,1fr);gap:32px}
.pubs .y{font-weight:600;color:var(--ink-2);font-size:15px}
.pubs .org{display:block;margin:2px 0 0;font-size:14px}

/* contact */
.req{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);gap:28px;margin-bottom:40px}
.req:has(.out[hidden]){grid-template-columns:minmax(0,760px)}
.form-h{font-size:22px;margin:0 0 6px}
.form{background:var(--paper);border-radius:16px;padding:28px;display:grid;gap:18px}
.form fieldset{border:0;margin:0;padding:0;display:grid;gap:8px}
.form legend,.form label.l{font-size:14.5px;font-weight:600;margin-bottom:6px;padding:0;display:block}
.chips{display:flex;flex-wrap:wrap;gap:8px}
.chips label{display:inline-flex;align-items:center;gap:7px;border:1px solid var(--rule);border-radius:999px;padding:7px 13px;font-size:14.5px;cursor:pointer;background:var(--surface)}
.chips input{accent-color:var(--accent);margin:0}
.chips label:has(input:checked){border-color:var(--accent);background:var(--accent-soft)}
.row2{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:16px}
.form input[type=text],.form textarea{width:100%;font:inherit;font-size:15.5px;color:var(--ink);background:var(--surface);border:1px solid var(--rule);border-radius:8px;padding:10px 12px}
.form textarea{min-height:96px;resize:vertical}
.form .err{color:var(--c-g);font-size:14.5px;margin:0}
.out{align-self:start;border:1.5px dashed var(--accent);border-radius:16px;padding:22px;background:var(--accent-soft);display:flex;flex-direction:column;gap:12px;min-width:0}
.out h3{margin:0;font-size:17px}
.out pre{margin:0;white-space:pre-wrap;word-break:break-word;font-family:var(--f);font-size:15px;line-height:1.55}
.acts{display:flex;flex-wrap:wrap;gap:10px}
.pick{font-weight:600;font-size:15px;text-decoration:none}
.svc .pick{margin-top:6px}
.svc .pick::after{content:"";display:inline-block;width:7px;height:7px;border-right:2px solid currentColor;border-top:2px solid currentColor;transform:rotate(45deg);margin-left:8px;vertical-align:2px}
.out .hint{color:var(--ink-2);font-size:14.5px;margin:0}
.contact{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:0;border-top:1px solid var(--rule)}
.ct{border-bottom:1px solid var(--rule);padding:22px 16px 18px 0;display:flex;flex-direction:column;gap:4px;min-width:0}
.ct:not(:nth-child(3n+1)){padding-left:24px;border-left:1px solid var(--rule)}
.ct .k{font-size:14px;font-weight:600;color:var(--ink-2)}
.ct .v{font-size:16.5px;font-weight:600;overflow-wrap:anywhere;color:var(--ink);text-decoration:none}
.ct a.v:hover{color:var(--accent)}
.copy{align-self:flex-start;margin-top:8px;font:inherit;font-size:13.5px;background:none;border:1px solid var(--rule);color:var(--ink);border-radius:6px;padding:4px 11px;cursor:pointer}
.copy:hover{border-color:var(--accent);color:var(--accent)}

footer.night .wrap{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;padding-block:30px 40px;font-size:14.5px;color:var(--on-night-2)}
footer.night a{color:var(--on-night)}

@media (max-width:900px){
  .hero{grid-template-columns:minmax(0,1fr);gap:44px;padding-block:52px 64px}
  .split,.req,.row2{grid-template-columns:minmax(0,1fr)}
  .split{gap:40px}
  .services,.prep{grid-template-columns:minmax(0,1fr)}
  .prep{gap:32px}
  .figures,.path{grid-template-columns:repeat(2,minmax(0,1fr))}
  .path{row-gap:40px}
  .path::before{display:none}
  section{padding-block:72px}
}
@media (max-width:560px){
  body{font-size:16px}
  .top{flex-wrap:wrap;padding-block:16px;gap:10px}
  .nav{gap:18px;flex-wrap:nowrap;overflow-x:auto;width:100%;padding-bottom:4px;-webkit-overflow-scrolling:touch}
  .nav a{white-space:nowrap}
  .top{position:relative}
  .nav .lang{position:absolute;top:14px;right:0}
  .lead{font-size:19px}
  .tl li,.edu,.pubs li{grid-template-columns:minmax(0,1fr);gap:4px}
  .path{grid-template-columns:minmax(0,1fr);row-gap:30px}
  .path li{padding:0 0 0 60px;min-height:41px}
  .figures{grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:28px 20px}
  .contact{grid-template-columns:minmax(0,1fr)}
  .contact .ct{padding:18px 0 14px;border-left:0}
  .trust li{grid-template-columns:minmax(0,1fr);gap:2px}
  .form{padding:20px}
  section{padding-block:60px}
  .tag{font-size:12.5px}
}
"""

SCALE_WIDTHS = [("A", 38, "--c-a"), ("B", 48, "--c-b"), ("C", 58, "--c-c"), ("D", 68, "--c-d"),
                ("E", 78, "--c-e"), ("F", 88, "--c-f"), ("G", 98, "--c-g")]

T = {
 "ua": {
  "lang": "uk", "file": "index.html", "other": "en.html", "other_label": "EN",
  "title": "Дмитро Паламарчук",
  "seo_title": "Дмитро Паламарчук — енергоефективність, МЕП, енергоспільноти",
  "lead2": "Громадам — муніципальні енергетичні плани, ОСББ — підготовка до енергомодернізації, ініціативним групам — моделі енергетичних спільнот.",
  "quick": [("#svc-0", "Громаді"), ("#svc-1", "ОСББ"), ("#svc-2", "Енергоспільноті"), ("#partners", "Міжнародним програмам")],
  "pub_more": "Повний перелік публікацій:",
  "description": "Дмитро Паламарчук — консультант з енергоефективності: муніципальні енергетичні плани для громад, консультації ОСББ щодо програм Фонду енергоефективності, підтримка енергетичних спільнот. Черкаси.",
  "nav": [("#how", "Як працюю"), ("#services", "Послуги"), ("#experience", "Досвід"), ("#contact", "Контакти")],
  "eyebrow": "Енергоефективність · Енергетичне планування громад · Енергетичні спільноти",
  "name": "Дмитро Паламарчук",
  "lead": "Енергоефективність будинку, громади чи енергетичної спільноти — від першого питання до реалізованого проєкту. Одна людина, яка веде вас усім шляхом.",
  "path_title": "Як я працюю",
  "path_sub": "З чим би ви не прийшли, шлях однаковий. Ви маєте одного співрозмовника, а інженерів, юристів і фінансистів, з якими я працюю роками, я залучаю сам, коли це потрібно.",
  "path": [("Розбираємося з питанням", "Що є зараз, що турбує, які дані вже зібрано і яких бракує."), ("Рахуємо", "Базова лінія, варіанти заходів, вартість, економія й окупність."), ("Знаходимо фінансування", "Програми Фонду енергоефективності, донорські гранти, кредити, бюджет громади."), ("Доводимо до результату", "Загальні збори, заявки, підрядники, верифікація, звіти.")],
  "meta": "Базуюся в Черкасах, працюю з громадами різних областей · кандидат економічних наук · член правління ГО «Е-ТЕАМ»",
  "cta1": "Зв’язатися", "cta2": "З чим звертаються",
  "th_label": "Тепловізійний знімок фасаду до і після енергомодернізації. Повзунок порівнює два стани.",
  "th_before": "До утеплення", "th_after": "Після модернізації",
  "th_caption": "Умовна ілюстрація: так тепловізор бачить панельний будинок до і після енергомодернізації. Потягніть повзунок.",
  "pubs_h": "Наукові публікації", "edu_h": "Освіта",
  "scale_title": "Клас енергоефективності будівлі",
  "scale_note": "Умовна ілюстрація за шкалою енергетичного сертифіката будівлі. Мета роботи — наблизити будинок чи громаду до класу A.",
  "s_title": "З чим до мене звертаються",
  "s_sub": "Звертаються три групи клієнтів. Для кожної — свій інструмент, підтверджений реальними проєктами.",
  "services": [
    ("Громадам", "Муніципальний енергетичний план",
     "МЕП за Методикою, затвердженою наказом Мінвідновлення № 1163: збір і перевірка даних, базова лінія енергоспоживання, цілі, каталог проєктів, навчання команди громади.",
     "МЕП Сміли (на замовлення UNIDO, 2026) і МЕП Сарненської громади (у роботі) — у складі команди ГО «Е-ТЕАМ»."),
    ("ОСББ", "Консультації з енергомодернізації",
     "Огляд будинку, розрахунок фінансового результату, підготовка загальних зборів і заявки до програм «Енергодім» та «ВідновиДІМ» Фонду енергоефективності, супровід до верифікації.",
     "Регіональний радник у Черкаській області: 2019–2025 — у програмі IFC, з 2026 — у мережі радників ГО «Е-ТЕАМ» (проєкт GIZ)."),
    ("Енергетичним спільнотам", "Запуск енергетичної спільноти",
     "Що можна замовити зараз: консультацію для ініціативної групи чи громади, попередню оцінку моделі спільноти, план запуску з правовими рамками, бізнес-моделлю і джерелами фінансування.",
     "Національний координатор проєкту ЄС LIFE-ECOss (старт — вересень 2026): створюємо центр підтримки енергетичних спільнот у Луцьку."),
  ],
  "f_title": "Цифри з роботи з ОСББ",
  "figures": [("41", "успішна заявка ОСББ до Фонду енергоефективності"),
              ("70+", "навчальних заходів для ОСББ і громад"),
              ("400+", "ОСББ, охоплених консультаціями"),
              ("6,5", "року в програмі IFC (Група Світового банку)")],
  "f_src": "Регіональний радник з енергоефективності в Черкаській області, 2019–2025.",
  "e_title": "Досвід",
  "timeline": [
    ("2025 — дотепер", "Член правління, координатор проєктів міжнародної співпраці", "ГО «Е-ТЕАМ»", "https://www.eteamngo.org/",
     "Керую розробкою муніципальних енергетичних планів. Національний координатор проєкту LIFE-ECOss. Уповноважений представник (LEAR) організації на порталі Funding & Tenders Європейської Комісії."),
    ("2026 — дотепер", "Регіональний радник з енергоефективності, Черкаська область", "Мережа регіональних радників ГО «Е-ТЕАМ», проєкт GIZ", None,
     "Консультую ОСББ щодо програм Фонду енергоефективності, проводжу семінари й навчальні візити для голів ОСББ і громад."),
    ("2019 — 2025", "Регіональний радник з енергоефективності, Черкаська область", "Проєкт IFC «Ukraine EE Fund», Група Світового банку", "https://disclosures.ifc.org/project-detail/AS/602817/ukraine-ee-fund",
     "Навчання для ОСББ і органів місцевого самоврядування, 41 успішна заявка ОСББ на гранти Фонду енергоефективності, фінансові моделі енергомодернізації будинків, консультації громадам щодо місцевих програм підтримки."),
    ("2012 — 2026", "Викладач, з 2017 — доцент", "Черкаський державний технологічний університет", None,
     "Курси «Міжнародна економіка», «Європейська інтеграція», «Економіка сталого розвитку»; дослідження адаптації енергетичної політики ЄС до українських умов."),
  ],
  "edu": [("2014", "Кандидат економічних наук — Київський національний університет імені Тараса Шевченка"),
          ("2010", "Магістр економіки та підприємництва (з відзнакою) — Черкаський державний технологічний університет")],
  "p_title": "Публікації",
  "pubs": [
    ("2024", "Інформаційні кампанії як інструмент зміни поведінки споживачів щодо використання енергії: досвід ЄС", "Матеріали III Міжнародної науково-практичної конференції, Тернопіль, ЗУНУ", "http://dspace.wunu.edu.ua/handle/316497/50505"),
    ("2023", "Енергоефективність у житловому секторі України", "Стратегії глобальної конкурентоспроможності: соціально-економічний вимір. Матеріали X Міжнародної науково-практичної конференції, ЧДТУ", "https://dntb.gov.ua/wp-content/uploads/2023/05/X-%D0%BC%D1%96%D0%B6%D0%BD%D0%B0%D1%80%D0%BE%D0%B4%D0%BD%D0%B0-%D0%BA%D0%BE%D0%BD%D1%84_%D0%A1%D1%82%D1%80%D0%B0%D1%82%D0%B5%D0%B3%D1%96%D1%97-%D0%B3%D0%BB%D0%BE%D0%B1%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D1%97-%D0%BA%D0%BE%D0%BD%D0%BA%D1%83%D1%80%D0%B5%D0%BD%D1%82%D0%BE%D1%81%D0%BF%D1%80%D0%BE%D0%BC%D0%BE%D0%B6%D0%BD%D0%BE%D1%81%D1%82%D1%96_%D1%81%D0%BE%D1%86%D1%96%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE-%D0%B5%D0%BA%D0%BE%D0%BD%D0%BE%D0%BC%D1%96%D1%87%D0%BD%D1%96-%D0%B2%D0%B8%D0%BC%D1%96%D1%80%D0%B8-3.pdf"),
    ("2022", "Дослідження чинників, що впливають на рішення співвласників щодо модернізації багатоквартирних будинків", "Матеріали IX Міжнародної науково-практичної конференції, ЧДТУ", "https://er.chdtu.edu.ua/handle/ChSTU/4287"),
  ],
  "trust_title": "Програми й організації, з якими працюю, і моя роль",
  "trust": [("IFC (Група Світового банку)", "регіональний радник, проєкт «Ukraine EE Fund», 2019–2025"),
            ("GIZ", "регіональний радник у мережі ГО «Е-ТЕАМ», з 2026"),
            ("UNIDO", "МЕП Сміли, 2026, у команді ГО «Е-ТЕАМ»"),
            ("Програма ЄС LIFE", "національний координатор LIFE-ECOss, з 2026, від ГО «Е-ТЕАМ»"),
            ("Фонд енергоефективності", "супровід ОСББ у програмах «Енергодім» і «ВідновиДІМ»")],
  "partners_title": "Для міжнародних програм і партнерів",
  "partners_sub": "Працюю як незалежний експерт (ФОП) або в складі команди ГО «Е-ТЕАМ» — залежно від вимог програми.",
  "partners": ["Муніципальне енергетичне планування за Методикою № 1163 і аналіз енергетичних даних громад",
               "Навчання й консультації для ОСББ та органів місцевого самоврядування — понад 70 заходів",
               "Координація українського партнера в консорціумах ЄС: національний координатор LIFE-ECOss, LEAR організації на порталі Funding & Tenders",
               "Адаптація європейських практик енергетичного переходу до українських умов"],
  "prep_title": "Підготуйтеся до першої розмови",
  "prep_sub": "Перша консультація коротша і корисніша, коли під рукою є ці дані. Не все обов’язково: принесіть те, що є.",
  "prep": [("ОСББ", ["Рахунки або дані про споживання тепла за 2–3 останні опалювальні сезони", "Технічний паспорт будинку: рік, поверховість, площа, кількість квартир", "Протоколи зборів щодо модернізації, якщо вже були", "Енергетичний сертифікат або енергоаудит, якщо є", "Фото фасаду, підвалу і теплового пункту"]),
           ("Громада", ["Дані про споживання енергії бюджетними будівлями за 3 роки", "Чинні програми енергоефективності, SECAP чи МЕП, якщо є", "Контакт відповідальної особи: енергоменеджер, відділ ЖКГ чи економіки", "Перелік проєктів, які громада вже розглядає"]),
           ("Ініціативна група", ["Склад групи і хто має намір стати учасником", "Можливий об’єкт: дах, ділянка, котельня", "Орієнтовне річне споживання електроенергії чи тепла учасниками", "Позиція органу місцевого самоврядування"])],
  "form_title": "Опишіть ваше питання",
  "form_sub": "Заповніть кілька полів — сторінка складе текст звернення. Повідомлення не надсилається автоматично: натисніть «Надіслати листом» — відкриється ваша пошта з готовим текстом, — або скопіюйте текст у месенджер. Дані з форми нікуди не передаються і не зберігаються.",
  "f_role": "Хто звертається", "roles": ["ОСББ або управитель", "Громада (ОМС)", "Ініціативна група / енергоспільнота", "Міжнародна організація / донор", "Інше"],
  "f_need": "Що потрібно", "needs": ["Консультація", "Участь у загальних зборах ОСББ", "Огляд будинку і розрахунок", "Муніципальний енергетичний план", "Запуск енергетичної спільноти", "Експертна участь у проєкті"],
  "f_place": "Населений пункт", "f_name": "Ваше ім’я", "f_contact": "Телефон або email", "f_msg": "Коротко про питання",
  "f_btn": "Скласти звернення", "f_err": "Оберіть, хто звертається, і вкажіть ім’я та контакт, щоб я міг відповісти.", "f_send": "Надіслати листом", "f_call": "Зателефонувати",
  "f_out_title": "Звернення готове",
  "f_hdr": "Звернення з сайту", "f_lab": ["Хто", "Населений пункт", "Що потрібно", "Питання", "Контакт"],
  "c_title": "Контакти",
  "c_sub": "Пишіть щодо МЕП для вашої громади, консультації для ОСББ чи енергетичної спільноти.",
  "contacts": [("Email", "dmytropalamarchuk@gmail.com", "mailto:dmytropalamarchuk@gmail.com", True), ("Корпоративна пошта, ГО «Е-ТЕАМ»", "dmytro.palamarchuk@eteamngo.org", "mailto:dmytro.palamarchuk@eteamngo.org", True), ("Телефон", "+380 97 889 13 85", "tel:+380978891385", True), ("Сайт ГО «Е-ТЕАМ»", "eteamngo.org", "https://www.eteamngo.org/", False), ("Google Scholar", "Профіль і цитування", "https://scholar.google.com/citations?user=g-yRUywAAAAJ", False), ("ORCID", "0000-0002-6023-9780", "https://orcid.org/0000-0002-6023-9780", False)],
  "copy": "Копіювати", "copied": "Скопійовано",
  "svc_cta": ["Обговорити МЕП для громади", "Записатися на консультацію ОСББ", "Обговорити енергоспільноту"], "partners_cta": "Запросити до проєкту",
  "footer_l": "© 2026 Дмитро Паламарчук",
  "footer_r": "Організація: ГО «Е-ТЕАМ»",
  "jobTitle": "Експерт з енергоефективності та муніципального енергетичного планування",
 },
 "en": {
  "lang": "en", "file": "en.html", "other": "index.html", "other_label": "UA",
  "title": "Dmytro Palamarchuk",
  "seo_title": "Dmytro Palamarchuk — energy efficiency, municipal energy planning, energy communities",
  "lead2": "Municipal energy plans for municipalities, renovation preparation for homeowner associations, energy community models for community groups.",
  "quick": [("#svc-0", "Municipalities"), ("#svc-1", "Homeowner associations"), ("#svc-2", "Energy communities"), ("#partners", "International programmes")],
  "pub_more": "Full list of publications:",
  "description": "Dmytro Palamarchuk — energy efficiency consultant in Ukraine: municipal energy plans for communities, advisory to homeowner associations on Energy Efficiency Fund programmes, support for energy communities.",
  "nav": [("#how", "How I work"), ("#services", "Services"), ("#experience", "Experience"), ("#contact", "Contact")],
  "eyebrow": "Energy efficiency · Municipal energy planning · Energy communities",
  "name": "Dmytro Palamarchuk",
  "lead": "Energy efficiency for a building, a municipality or an energy community, from the first question to a delivered project. One person who takes you through the whole way.",
  "path_title": "How I work",
  "path_sub": "Whatever you come with, the path is the same. You deal with one person; I bring in the engineers, lawyers and finance specialists I have worked with for years when the task needs them.",
  "path": [("Understand the question", "What exists today, what the problem is, which data are available and which are missing."), ("Run the numbers", "Baseline, options, costs, savings and payback."), ("Find the financing", "Energy Efficiency Fund programmes, donor grants, loans, municipal budgets."), ("Deliver the result", "General meetings, applications, contractors, verification, reporting.")],
  "meta": "Based in Cherkasy, working with municipalities across Ukraine · PhD in Economics · Board member, NGO E-TEAM",
  "cta1": "Get in touch", "cta2": "What I do",
  "th_label": "Thermal image of a facade before and after retrofit. The slider compares the two states.",
  "th_before": "Before insulation", "th_after": "After retrofit",
  "th_caption": "Illustration: how a thermal camera sees a panel apartment block before and after energy retrofit. Drag the slider.",
  "pubs_h": "Research publications", "edu_h": "Education",
  "scale_title": "Building energy performance class",
  "scale_note": "Illustration based on the building energy certificate scale. The aim of the work is to move a building or a community closer to class A.",
  "s_title": "Who comes to me, and with what",
  "s_sub": "Three groups of clients. Each gets its own instrument, backed by delivered projects.",
  "services": [
    ("Municipalities", "Municipal energy plans",
     "Energy plans under Ukraine's official methodology (Ministry for Restoration Order No. 1163): data collection and validation, energy baseline, targets, project catalogue, training for the municipal team.",
     "Smila energy plan (commissioned by UNIDO, 2026) and Sarny community plan (in progress), as part of the NGO E-TEAM team."),
    ("Homeowner associations", "Energy renovation advisory",
     "Building inspection, financial outcome calculation, preparation of general meetings and applications to the Energy Efficiency Fund programmes EnergoDim and VidnovyDIM, support through verification.",
     "Regional adviser in Cherkasy oblast: 2019–2025 under the IFC programme, since 2026 in the NGO E-TEAM adviser network (GIZ project)."),
    ("Energy communities", "Setting up an energy community",
     "Available now: advice for an initiative group or municipality, a preliminary assessment of the community model, a launch plan covering the legal framework, business model and financing.",
     "National coordinator of the EU LIFE project LIFE-ECOss (started September 2026), which is setting up an energy community One-Stop-Shop in Lutsk."),
  ],
  "f_title": "Work with homeowner associations in figures",
  "figures": [("41", "successful HOA applications to the Energy Efficiency Fund"),
              ("70+", "training events for HOAs and municipalities"),
              ("400+", "HOAs reached through advisory work"),
              ("6.5", "years with the IFC programme (World Bank Group)")],
  "f_src": "Regional energy efficiency adviser, Cherkasy oblast, 2019–2025.",
  "e_title": "Experience",
  "timeline": [
    ("2025 — present", "Board member, Coordinator of International Cooperation Projects", "NGO E-TEAM", "https://www.eteamngo.org/",
     "Lead the development of municipal energy plans. National coordinator of LIFE-ECOss. LEAR of the organisation on the European Commission Funding & Tenders Portal."),
    ("2026 — present", "Regional Energy Efficiency Adviser, Cherkasy oblast", "NGO E-TEAM regional adviser network, GIZ project", None,
     "Advise homeowner associations on Energy Efficiency Fund programmes; run seminars and study visits for HOA chairs and municipalities."),
    ("2019 — 2025", "Regional Energy Efficiency Adviser, Cherkasy oblast", "IFC project “Ukraine EE Fund”, World Bank Group", "https://disclosures.ifc.org/project-detail/AS/602817/ukraine-ee-fund",
     "Training for HOAs and local authorities; 41 successful HOA grant applications to the Energy Efficiency Fund; financial models and cost-benefit analysis for building renovation; advice to municipalities on local support programmes."),
    ("2012 — 2026", "Lecturer, Associate Professor from 2017", "Cherkasy State Technological University", None,
     "Courses in International Economics, European Integration and Economics of Sustainable Development; research on adapting EU energy policy to Ukraine."),
  ],
  "edu": [("2014", "PhD in Economics — Taras Shevchenko National University of Kyiv"),
          ("2010", "Master’s in Economics and Entrepreneurship (Honours) — Cherkasy State Technological University")],
  "p_title": "Publications",
  "pubs": [
    ("2024", "Information campaigns as a tool for changing consumer energy behaviour: EU experience", "Proceedings of the III International Scientific and Practical Conference, Ternopil, WUNU (in Ukrainian)", "http://dspace.wunu.edu.ua/handle/316497/50505"),
    ("2023", "Energy efficiency in Ukraine’s housing sector", "Strategies of Global Competitiveness: Socio-Economic Dimensions, X International Conference, ChSTU (in Ukrainian)", "https://dntb.gov.ua/wp-content/uploads/2023/05/X-%D0%BC%D1%96%D0%B6%D0%BD%D0%B0%D1%80%D0%BE%D0%B4%D0%BD%D0%B0-%D0%BA%D0%BE%D0%BD%D1%84_%D0%A1%D1%82%D1%80%D0%B0%D1%82%D0%B5%D0%B3%D1%96%D1%97-%D0%B3%D0%BB%D0%BE%D0%B1%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D1%97-%D0%BA%D0%BE%D0%BD%D0%BA%D1%83%D1%80%D0%B5%D0%BD%D1%82%D0%BE%D1%81%D0%BF%D1%80%D0%BE%D0%BC%D0%BE%D0%B6%D0%BD%D0%BE%D1%81%D1%82%D1%96_%D1%81%D0%BE%D1%86%D1%96%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE-%D0%B5%D0%BA%D0%BE%D0%BD%D0%BE%D0%BC%D1%96%D1%87%D0%BD%D1%96-%D0%B2%D0%B8%D0%BC%D1%96%D1%80%D0%B8-3.pdf"),
    ("2022", "Factors influencing homeowners’ decisions on the modernisation of multi-apartment buildings", "IX International Scientific and Practical Conference, ChSTU (in Ukrainian)", "https://er.chdtu.edu.ua/handle/ChSTU/4287"),
  ],
  "trust_title": "Programmes and organisations I work with, and my role",
  "trust": [("IFC (World Bank Group)", "regional adviser, “Ukraine EE Fund” project, 2019–2025"),
            ("GIZ", "regional adviser in the NGO E-TEAM network, since 2026"),
            ("UNIDO", "Smila municipal energy plan, 2026, with the NGO E-TEAM team"),
            ("EU LIFE Programme", "national coordinator of LIFE-ECOss, since 2026, for NGO E-TEAM"),
            ("Energy Efficiency Fund of Ukraine", "support to HOAs in the EnergoDim and VidnovyDIM programmes")],
  "partners_title": "For international programmes and partners",
  "partners_sub": "I work as an independent expert (registered sole proprietor) or as part of the NGO E-TEAM team, depending on programme requirements.",
  "partners": ["Municipal energy planning under Ukraine's official methodology (Order No. 1163) and analysis of municipal energy data",
               "Training and advisory for homeowner associations and local authorities — more than 70 events",
               "Coordinating the Ukrainian partner in EU consortia: national coordinator of LIFE-ECOss, LEAR on the Funding & Tenders Portal",
               "Adapting European energy transition practice to Ukrainian conditions"],
  "prep_title": "Prepare for the first conversation",
  "prep_sub": "A first consultation is shorter and more useful when you have this information at hand. Bring what you have.",
  "prep": [("Homeowner association", ["Heat bills or consumption data for the last 2–3 heating seasons", "Building passport: year, storeys, floor area, number of flats", "Minutes of meetings on renovation, if any", "Energy certificate or energy audit, if available", "Photos of the facade, basement and heating substation"]),
           ("Municipality", ["Energy consumption of public buildings for 3 years", "Current energy efficiency programmes, SECAP or energy plan, if any", "Contact of the responsible person: energy manager, housing or economic department", "List of projects the municipality is already considering"]),
           ("Community group", ["Members of the group and who intends to join", "Possible site: roof, land plot, boiler house", "Approximate annual electricity or heat use of members", "Position of the local authority"])],
  "form_title": "Describe your question",
  "form_sub": "Fill in a few fields and the page will compose a message. It is not sent automatically: press “Send by email” to open your mail app with the text filled in, or copy it into a messenger. Form data is not transmitted or stored anywhere.",
  "f_role": "Who you are", "roles": ["Homeowner association or manager", "Municipality", "Community group / energy community", "International organisation / donor", "Other"],
  "f_need": "What you need", "needs": ["Consultation", "Attendance at an HOA general meeting", "Building inspection and calculation", "Municipal energy plan", "Setting up an energy community", "Expert input to a project"],
  "f_place": "Town or village", "f_name": "Your name", "f_contact": "Phone or email", "f_msg": "Your question in brief",
  "f_btn": "Compose message", "f_err": "Please choose who you are and enter your name and a contact so I can reply.", "f_send": "Send by email", "f_call": "Call",
  "f_out_title": "Your message is ready",
  "f_hdr": "Request from the website", "f_lab": ["Who", "Location", "Needs", "Question", "Contact"],
  "c_title": "Contact",
  "c_sub": "Write about an energy plan for your municipality, HOA advisory or an energy community.",
  "contacts": [("Email", "dmytropalamarchuk@gmail.com", "mailto:dmytropalamarchuk@gmail.com", True), ("Work email, NGO E-TEAM", "dmytro.palamarchuk@eteamngo.org", "mailto:dmytro.palamarchuk@eteamngo.org", True), ("Phone", "+380 97 889 13 85", "tel:+380978891385", True), ("NGO E-TEAM website", "eteamngo.org", "https://www.eteamngo.org/", False), ("Google Scholar", "Profile and citations", "https://scholar.google.com/citations?user=g-yRUywAAAAJ", False), ("ORCID", "0000-0002-6023-9780", "https://orcid.org/0000-0002-6023-9780", False)],
  "copy": "Copy", "copied": "Copied",
  "svc_cta": ["Discuss a municipal energy plan", "Book an HOA consultation", "Discuss an energy community"], "partners_cta": "Invite to a project",
  "footer_l": "© 2026 Dmytro Palamarchuk",
  "footer_r": "Organisation: NGO E-TEAM",
  "jobTitle": "Energy efficiency and municipal energy planning expert",
 },
}

ORCID = "https://orcid.org/0000-0002-6023-9780"
SCHOLAR = "https://scholar.google.com/citations?user=g-yRUywAAAAJ"
BASE = "https://dmytropalamarchuk-svg.github.io/"
FAVICON = "data:image/svg+xml," + "%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 32 32%27%3E%3Crect width=%2732%27 height=%2732%27 rx=%276%27 fill=%27%231d6b66%27/%3E%3Cpath d=%27M7 10h11l3 3-3 3H7z%27 fill=%27%23fff%27/%3E%3Cpath d=%27M7 18h16l3 3-3 3H7z%27 fill=%27%23b6e0d9%27/%3E%3C/svg%3E"


def make_og(path):
    from PIL import Image, ImageDraw, ImageFont
    W, H = 1200, 630
    im = Image.new("RGB", (W, H), (16, 27, 40)); d = ImageDraw.Draw(im)
    fb = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"; fr = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    d.text((72, 140), "Дмитро", font=ImageFont.truetype(fb, 84), fill=(237, 241, 245))
    d.text((72, 236), "Паламарчук", font=ImageFont.truetype(fb, 84), fill=(237, 241, 245))
    for i, line in enumerate(["Енергоефективність будинків і громад", "МЕП · ОСББ · енергетичні спільноти"]):
        d.text((72, 372 + i * 48), line, font=ImageFont.truetype(fr, 34), fill=(168, 182, 197))
    # thermal facade block on the right
    stops = [(33, 28, 94), (91, 42, 138), (184, 51, 106), (240, 122, 42), (255, 224, 102)]
    bx, by, bw, bh = 820, 110, 300, 420
    d.rectangle([bx, by, bx + bw, by + bh], fill=(124, 42, 121))
    for f in range(9):
        for b in range(6):
            c = stops[2 + (f * 5 + b * 7 + f * b) % 3]
            x = bx + 14 + b * 48; y = by + 12 + f * 45
            d.rectangle([x, y, x + 26, y + 24], fill=c)
    for i, c in enumerate(stops):
        d.rectangle([72 + i * 60, 520, 72 + i * 60 + 56, 530], fill=c)
    im.save(path)


def thermal_svg(kind):
    """Panel block (9 floors x 8 bays) drawn as a thermal image. kind = 'before' | 'after'."""
    X0, BW, NB, Y0, FH, NF = 70, 57.5, 8, 66, 46, 9
    W = BW * NB
    p = kind
    hot = kind == "before"
    if hot:
        wall = ("#c23b67", "#7c2a79"); joint = "#ff9a33"; win = ["#ffe36b", "#ffd04f", "#ffb347", "#fff08a"]
        halo = "#ff8a2a"; balc = "#ff7a2e"; roof = "#ffad42"; base = "#a9306f"
    else:
        wall = ("#3a2f8e", "#231e63"); joint = None; win = ["#b23a7c", "#9e3480", "#c0447a", "#a33882"]
        halo = "#5d2a86"; balc = "#41338e"; roof = "#3f3494"; base = "#2b2370"
    o = [f'<svg class="{kind}" viewBox="0 0 600 540" aria-hidden="true" focusable="false" preserveAspectRatio="xMidYMid slice">',
         f'<defs><linearGradient id="{p}-w" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{wall[0]}"/><stop offset="1" stop-color="{wall[1]}"/></linearGradient>',
         f'<radialGradient id="{p}-sky" cx=".5" cy=".9" r=".9"><stop offset="0" stop-color="#1a1f4a"/><stop offset="1" stop-color="#0b1220"/></radialGradient>',
         f'<filter id="{p}-b" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="7"/></filter>',
         f'<filter id="{p}-s" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="1.6"/></filter></defs>',
         f'<rect width="600" height="540" fill="url(#{p}-sky)"/>',
         f'<rect x="0" y="{Y0+FH*NF}" width="600" height="{540-Y0-FH*NF}" fill="#141d3d"/>',
         f'<rect x="{X0-8}" y="{Y0-12}" width="{W+16}" height="14" fill="{roof}"/>',
         f'<rect x="{X0}" y="{Y0}" width="{W}" height="{FH*NF}" fill="url(#{p}-w)"/>',
         f'<rect x="{X0}" y="{Y0+FH*NF-26}" width="{W}" height="26" fill="{base}"/>']
    halos, wins, balcs = [], [], []
    for f in range(NF):
        y = Y0 + f * FH
        for b in range(NB):
            x = X0 + b * BW
            wx, wy = x + (BW - 26) / 2, y + 10
            if f == NF - 1 and b in (2, 5):  # entrances
                wins.append(f'<rect x="{x+16}" y="{y+8}" width="26" height="30" fill="{win[1]}"/>')
                continue
            k = (f * 7 + b * 3) % 4
            halos.append(f'<rect x="{wx-6}" y="{wy-6}" width="38" height="36" rx="6" fill="{halo}" opacity="{0.9 if hot else 0.7}"/>')
            wins.append(f'<rect x="{wx}" y="{wy}" width="26" height="24" fill="{win[k]}"/>')
            if b in (1, 6) and f < NF - 1:
                balcs.append(f'<rect x="{x+4}" y="{y+34}" width="{BW-8}" height="9" fill="{balc}"/>')
    o.append(f'<g filter="url(#{p}-b)">{"".join(halos)}</g>')
    if joint:
        lines = "".join(f'<line x1="{X0}" y1="{Y0+f*FH}" x2="{X0+W}" y2="{Y0+f*FH}"/>' for f in range(1, NF))
        lines += "".join(f'<line x1="{X0+b*BW*2}" y1="{Y0}" x2="{X0+b*BW*2}" y2="{Y0+FH*NF}"/>' for b in range(1, NB // 2))
        o.append(f'<g stroke="{joint}" stroke-width="5" opacity=".75" filter="url(#{p}-s)">{lines}</g>')
    o.append("".join(balcs) + "".join(wins))
    if not hot:  # insulation layer reads as an even, slightly thicker outline
        o.append(f'<rect x="{X0-3}" y="{Y0-1}" width="{W+6}" height="{FH*NF+1}" fill="none" stroke="#2c2575" stroke-width="6"/>')
    o.append('</svg>')
    return "".join(o)


ICONS = [
    # community: town hall
    '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round" aria-hidden="true"><path d="M6 20 24 8l18 12"/><path d="M10 20v18M18 20v18M30 20v18M38 20v18"/><path d="M5 40h38"/><path d="M24 8V3"/><path d="M24 3h7v4h-7"/></svg>',
    # apartment building
    '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round" aria-hidden="true"><rect x="10" y="5" width="28" height="38"/><path d="M16 12h4M28 12h4M16 19h4M28 19h4M16 26h4M28 26h4"/><path d="M21 43v-8h6v8"/><path d="M5 43h38"/></svg>',
    # energy community: houses + solar + link
    '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round" aria-hidden="true"><path d="M4 30 13 22l9 8v12H4z"/><path d="M26 30l9-8 9 8v12H26z"/><path d="M15 6h18l-3 9H12z"/><path d="M18 6l-2 9M24 6v9M30 6l2 9M13 10.5h21"/><path d="M24 15v7"/><path d="M13 22v-2M35 22v-2M13 20h22"/></svg>',
]


SVC_PICK = [(1, 3), (0, 0), (2, 4)]  # (role index, need index) per service card


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;"))


def page(t, skeleton, seo=False):
    nav = "".join(f'<a href="{h}">{esc(l)}</a>' for h, l in t["nav"])
    nav += f'<a class="lang" href="{t["other"]}" hreflang="{"en" if t["lang"]=="uk" else "uk"}">{t["other_label"]}</a>'
    svcs = "".join(
        f'<article class="svc" id="svc-{i}">{ICONS[i]}<p class="who">{esc(a)}</p><h3>{esc(h)}</h3><p>{esc(p)}</p><p class="proof">{esc(pr)}</p><a class="pick" href="#contact" data-role="{SVC_PICK[i][0]}" data-need="{SVC_PICK[i][1]}">{esc(t['svc_cta'][i])}</a></article>'
        for i, (a, h, p, pr) in enumerate(t["services"]))
    quick = "".join(f'<a href="{h}">{esc(l)}</a>' for h, l in t["quick"])
    partners = "".join(f'<li>{esc(x)}</li>' for x in t["partners"])
    path = "".join(f'<li><span class="n" style="background:{c}">{i+1}</span><h3>{esc(a)}</h3><p>{esc(b)}</p></li>' for i, ((a, b), c) in enumerate(zip(t["path"], ["#e3632d", "#b8694a", "#5a8a6e", "var(--accent)"])))
    trust = f'<p class="trust-h">{esc(t["trust_title"])}</p><ul class="trust">' + "".join(f'<li><span class="tn">{esc(x)}</span><span class="tr">{esc(r)}</span></li>' for x, r in t["trust"]) + '</ul>'
    first, last = t['name'].split(' ', 1)
    prep = "".join(f'<div class="card"><h3>{esc(h)}</h3><ul>' + "".join(f'<li>{esc(i)}</li>' for i in items) + '</ul></div>' for h, items in t["prep"])
    roles = "".join(f'<label><input type="radio" name="role" value="{esc(r)}" id="role-{k}"{" checked" if k==0 else ""}> {esc(r)}</label>' for k, r in enumerate(t["roles"])).replace(" checked", "")
    needs = "".join(f'<label><input type="checkbox" name="need" value="{esc(r)}" id="need-{k}"> {esc(r)}</label>' for k, r in enumerate(t["needs"]))
    form = f"""<div class="req"><form class="form" id="reqform" novalidate>
<fieldset><legend>{esc(t['f_role'])}</legend><div class="chips">{roles}</div></fieldset>
<fieldset><legend>{esc(t['f_need'])}</legend><div class="chips">{needs}</div></fieldset>
<div class="row2"><div><label class="l" for="f-place">{esc(t['f_place'])}</label><input type="text" id="f-place" autocomplete="address-level2"></div>
<div><label class="l" for="f-name">{esc(t['f_name'])}</label><input type="text" id="f-name" autocomplete="name"></div></div>
<div><label class="l" for="f-contact">{esc(t['f_contact'])}</label><input type="text" id="f-contact" autocomplete="email"></div>
<div><label class="l" for="f-msg">{esc(t['f_msg'])}</label><textarea id="f-msg"></textarea></div>
<p class="err" id="f-err" hidden>{esc(t['f_err'])}</p>
<div><button class="btn primary" type="submit" style="cursor:pointer">{esc(t['f_btn'])}</button></div>
</form>
<div class="out" id="f-out" hidden><h3>{esc(t['f_out_title'])}</h3><pre class="v" id="f-text"></pre><button class="copy" type="button" id="copy-msg">{t['copy']}</button><div class="acts"><a class="btn primary" id="f-mail" href="mailto:{t['contacts'][0][1]}">{esc(t['f_send'])}</a><a class="btn ghost" href="{t['contacts'][2][2]}">{esc(t['f_call'])}</a></div><p class="hint">{esc(t['contacts'][0][1])}, {esc(t['contacts'][2][1])}</p></div>
</div>"""
    figs = "".join(f'<li><span class="num">{esc(n)}</span><span class="lbl">{esc(l)}</span></li>' for n, l in t["figures"])
    tl = ""
    for yr, role, org, url, d in t["timeline"]:
        o = f'<a href="{url}" rel="noopener">{esc(org)}</a>' if url else esc(org)
        tl += f'<li><div class="yr">{esc(yr)}</div><div><h3>{esc(role)}</h3><p class="org">{o}</p><p class="d">{esc(d)}</p></div></li>'
    edu = "".join(f'<dt>{y}</dt><dd>{esc(x)}</dd>' for y, x in t["edu"])
    pubs = "".join(f'<li><span class="y">{y}</span><div><a href="{u}" rel="noopener">{esc(ti)}</a><span class="org">{esc(v)}</span></div></li>' for y, ti, v, u in t["pubs"])
    cts = ""
    for i, (k, v, href, cp) in enumerate(t["contacts"]):
        ext = href.startswith("http")
        btn = f'<button class="copy" type="button" id="copy-{i}" data-v="{esc(v)}">{t["copy"]}</button>' if cp else ''
        cts += f'<div class="ct"><span class="k">{esc(k)}</span><a class="v" href="{esc(href)}"{' rel="noopener"' if ext else ''}>{esc(v)}</a>{btn}</div>'
    ld = {"@context": "https://schema.org", "@type": "Person", "name": t["name"],
          "alternateName": ["Дмитро Паламарчук", "Dmytro Palamarchuk", "Паламарчук Дмитро Миколайович"],
          "jobTitle": t["jobTitle"], "address": {"@type": "PostalAddress", "addressLocality": "Cherkasy", "addressCountry": "UA"},
          "worksFor": {"@type": "Organization", "name": "NGO E-TEAM", "url": "https://www.eteamngo.org/"},
          "alumniOf": [{"@type": "CollegeOrUniversity", "name": "Taras Shevchenko National University of Kyiv"},
                       {"@type": "CollegeOrUniversity", "name": "Cherkasy State Technological University"}],
          "knowsAbout": ["Energy efficiency", "Municipal energy planning", "Energy communities", "Homeowner associations", "EU energy policy"],
          "email": "mailto:dmytropalamarchuk@gmail.com", "sameAs": [ORCID, SCHOLAR]}
    ttl = t["seo_title"] if seo else t["title"]
    head = (f'<title>{esc(ttl)}</title>'
            + ('' if seo else '<meta name="claude:viewport-fit-sides" content="cover">') +
            f'<meta property="og:image" content="{BASE}og.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image">'
            f'<meta name="description" content="{esc(t["description"])}">'
            f'<link rel="canonical" href="{BASE}{"" if t["file"]=="index.html" else t["file"]}">'
            f'<link rel="alternate" hreflang="uk" href="{BASE}"><link rel="alternate" hreflang="en" href="{BASE}en.html"><link rel="alternate" hreflang="x-default" href="{BASE}">'
            f'<meta property="og:type" content="profile"><meta property="og:title" content="{esc(ttl)}"><meta property="og:description" content="{esc(t["description"])}"><meta property="og:url" content="{BASE}{"" if t["file"]=="index.html" else t["file"]}">'
            f'<link rel="icon" href="{FAVICON}">'
            f'{FONTS}<style>{CSS}</style>'
            f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>')
    body = f"""
<header class="night"><div class="wrap">
<div class="top"><a class="brand" href="{t['file']}">{esc(t['name'])}</a><nav class="nav" aria-label="Main">{nav}</nav></div>
<div class="hero">
  <div>
    <h1><span>{esc(first)}</span><span>{esc(last)}</span></h1>
    <p class="lead">{esc(t['lead'])}</p>
    <p class="lead2">{esc(t['lead2'])}</p>
    <nav class="quick" aria-label="Quick">{quick}</nav>
    <div class="cta"><a class="btn primary" href="#contact">{esc(t['cta1'])}</a><a class="btn ghost" href="#services">{esc(t['cta2'])}</a></div>
    <p class="meta">{esc(t['meta'])}</p>
  </div>
  <figure class="thermo-fig">
    <div class="thermo" id="thermo">{thermal_svg('after')}{thermal_svg('before')}
      <span class="tag l"><b style="background:var(--c-g)">G</b>{esc(t['th_before'])}</span>
      <span class="tag r"><b style="background:var(--c-c)">C</b>{esc(t['th_after'])}</span>
      <div class="handle"><span class="knob"><svg width="22" height="22" viewBox="0 0 22 22" fill="none" stroke="#101b28" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M8 6 3 11l5 5M14 6l5 5-5 5"/></svg></span></div>
      <input type="range" min="0" max="100" value="50" step="1" id="th-range" aria-label="{esc(t['th_label'])}">
    </div>
    <figcaption class="legend"><i></i><span>{esc(t['th_caption'])}</span></figcaption>
  </figure>
</div>
</div></header>
<main>
<section id="how"><div class="wrap"><h2>{esc(t['path_title'])}</h2><p class="sub">{esc(t['path_sub'])}</p><ol class="path">{path}</ol></div></section>
<section id="services" class="band"><div class="wrap"><h2>{esc(t['s_title'])}</h2><p class="sub">{esc(t['s_sub'])}</p><div class="services">{svcs}</div></div></section>
<section id="partners"><div class="wrap split"><div><h2>{esc(t['partners_title'])}</h2><p class="sub">{esc(t['partners_sub'])}</p><ul class="plist">{partners}</ul><p style="margin:28px 0 0"><a class="btn primary pick" href="#contact" data-role="3" data-need="5">{esc(t['partners_cta'])}</a></p></div><div>{trust}</div></div></section>
<section id="figures" class="night figs"><div class="wrap"><h2>{esc(t['f_title'])}</h2><ul class="figures">{figs}</ul><p class="src">{esc(t['f_src'])}</p></div></section>
<section id="prepare" class="band"><div class="wrap"><h2>{esc(t['prep_title'])}</h2><p class="sub">{esc(t['prep_sub'])}</p><div class="prep">{prep}</div></div></section>
<section id="experience"><div class="wrap"><h2>{esc(t['e_title'])}</h2><ul class="tl" style="margin-top:40px">{tl}</ul>
<h3 class="sub-h">{esc(t['edu_h'])}</h3><dl class="edu">{edu}</dl>
<h3 class="sub-h" id="publications">{esc(t['pubs_h'])}</h3><ul class="pubs">{pubs}</ul><p class="src">{esc(t['pub_more'])} <a href="{esc(SCHOLAR)}" rel="noopener">Google Scholar</a>, <a href="{ORCID}" rel="noopener">ORCID</a></p></div></section>
<section id="contact" class="band"><div class="wrap"><h2>{esc(t['c_title'])}</h2><p class="sub">{esc(t['c_sub'])}</p><h3 class="form-h">{esc(t['form_title'])}</h3><p class="sub" style="margin-bottom:24px;font-size:16px">{esc(t['form_sub'])}</p>{form}<div class="contact">{cts}</div></div></section>
</main>
<footer class="night"><div class="wrap"><span>{esc(t['footer_l'])}</span><a href="https://www.eteamngo.org/" rel="noopener">{esc(t['footer_r'])}</a></div></footer>
<script>
var lab={json.dumps(t['f_lab'], ensure_ascii=False)}, hdr={json.dumps(t['f_hdr'], ensure_ascii=False)};
document.getElementById('reqform').addEventListener('submit',function(e){{e.preventDefault();
  var g=function(id){{return document.getElementById(id).value.trim();}};
  var name=g('f-name'), contact=g('f-contact'), err=document.getElementById('f-err');
  var role=(document.querySelector('input[name=role]:checked')||{{}}).value||'';
  if(!name||!contact||!role){{err.hidden=false;return;}} err.hidden=true;
  var needs=[].slice.call(document.querySelectorAll('input[name=need]:checked')).map(function(x){{return x.value;}}).join(', ');
  var lines=[hdr, lab[0]+': '+role];
  if(g('f-place')) lines.push(lab[1]+': '+g('f-place'));
  if(needs) lines.push(lab[2]+': '+needs);
  if(g('f-msg')) lines.push(lab[3]+': '+g('f-msg'));
  lines.push(lab[4]+': '+name+', '+contact);
  document.getElementById('f-text').textContent=lines.join('\\n');
  var m=document.getElementById('f-mail'); m.href=m.href.split('?')[0]+'?subject='+encodeURIComponent(hdr)+'&body='+encodeURIComponent(lines.join('\\n'));
  var o=document.getElementById('f-out'); o.hidden=false; o.scrollIntoView({{behavior:'smooth',block:'nearest'}});
}});
var NEED_MAP=[[0,1,2],[0,3],[0,4],[0,5],[0,1,2,3,4,5]];
document.querySelectorAll('input[name=role]').forEach(function(r,ri){{r.addEventListener('change',function(){{
  var ok=NEED_MAP[ri]||NEED_MAP[4];
  document.querySelectorAll('input[name=need]').forEach(function(c,ci){{var show=ok.indexOf(ci)>-1;c.parentNode.hidden=!show;if(!show)c.checked=false;}});
}});}});
document.getElementById('copy-msg').setAttribute('data-v','');
document.getElementById('copy-msg').addEventListener('click',function(){{this.setAttribute('data-v',document.getElementById('f-text').textContent);}},true);
document.querySelectorAll('.copy').forEach(function(b){{b.addEventListener('click',function(){{
  var v=b.getAttribute('data-v');
  var done=function(){{b.textContent='{t['copied']}';setTimeout(function(){{b.textContent='{t['copy']}';}},1600);}};
  try{{navigator.clipboard.writeText(v).then(done,function(){{sel(b);}});}}catch(e){{sel(b);}}
}});}});
(function(){{
  var th=document.getElementById('thermo'), rg=document.getElementById('th-range'), touched=false;
  function setp(v){{th.style.setProperty('--pos',v+'%');}}
  rg.addEventListener('input',function(){{touched=true;setp(rg.value);}});
  rg.addEventListener('pointerdown',function(){{touched=true;}});
  if(window.matchMedia && !window.matchMedia('(prefers-reduced-motion: reduce)').matches){{
    setp(90); var t0=null;
    function step(ts){{ if(touched) return; if(!t0) t0=ts; var k=Math.min(1,(ts-t0)/1700), e=1-Math.pow(1-k,3), v=90-40*e; setp(v); rg.value=Math.round(v); if(k<1) requestAnimationFrame(step); }}
    setTimeout(function(){{requestAnimationFrame(step);}},500);
  }}
}})();
document.querySelectorAll('.pick').forEach(function(a){{a.addEventListener('click',function(){{
  var r=document.getElementById('role-'+a.getAttribute('data-role')); if(r){{r.checked=true;r.dispatchEvent(new Event('change'));}}
  var n=document.getElementById('need-'+a.getAttribute('data-need')); if(n) n.checked=true;
}});}});
function sel(b){{var s=b.parentNode.querySelector('.v');var r=document.createRange();r.selectNodeContents(s);var w=window.getSelection();w.removeAllRanges();w.addRange(r);}}
</script>"""
    if skeleton:
        return (f'<!doctype html><html lang="{t["lang"]}"><head><meta charset="utf-8">'
                f'<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">'
                f'{head}</head><body>{body}</body></html>')
    return head + body


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
        f'<url><loc>{BASE}</loc><lastmod>2026-10-19</lastmod></url>\n<url><loc>{BASE}en.html</loc><lastmod>2026-10-19</lastmod></url>\n</urlset>\n')
    open(os.path.join(HERE, "dist", ".nojekyll"), "w").write("")
    print("ok")
