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
         'family=Commissioner:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500'
         '&family=Literata:opsz,wght@7..72,500;7..72,600&display=swap">')

CSS = r"""
/* Layout: one reading column; hero = name + building energy-class scale (G→A) as the motif of the work */
:root{
  --paper:#f3f6f5; --surface:#ffffff; --ink:#14262b; --ink-2:#4b5f63; --rule:#d5dfdd;
  --accent:#1d6b66; --accent-soft:#e1efed;
  --c-a:#2f7d4f; --c-b:#5c9a45; --c-c:#9bb540; --c-d:#d2b23a; --c-e:#d48a34; --c-f:#c8642f; --c-g:#b2412e;
  --f-display:"Literata", Georgia, "Times New Roman", serif;
  --f-body:"Commissioner", "Segoe UI", system-ui, sans-serif;
  --f-mono:"IBM Plex Mono", ui-monospace, "Cascadia Mono", Consolas, monospace;
}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){
  --paper:#0f1a1c; --surface:#152427; --ink:#e4ecea; --ink-2:#a3b5b3; --rule:#2a3c3f;
  --accent:#6cc0b8; --accent-soft:#1b3433;
  --c-a:#4fa36f; --c-b:#79b15f; --c-c:#a9c25a; --c-d:#d9bd57; --c-e:#d99a53; --c-f:#d27a4c; --c-g:#c75e4a;
  color-scheme:dark}}
:root[data-theme="dark"]{
  --paper:#0f1a1c; --surface:#152427; --ink:#e4ecea; --ink-2:#a3b5b3; --rule:#2a3c3f;
  --accent:#6cc0b8; --accent-soft:#1b3433;
  --c-a:#4fa36f; --c-b:#79b15f; --c-c:#a9c25a; --c-d:#d9bd57; --c-e:#d99a53; --c-f:#d27a4c; --c-g:#c75e4a;
  color-scheme:dark}
*{box-sizing:border-box}
body{background:var(--paper);color:var(--ink);font-family:var(--f-body);font-size:17px;line-height:1.6;
  padding-left:max(16px, env(safe-area-inset-left, 0px));padding-right:max(16px, env(safe-area-inset-right, 0px))}
a{color:var(--accent);text-underline-offset:3px}
a:focus-visible,button:focus-visible{outline:2px solid var(--accent);outline-offset:3px;border-radius:2px}
.wrap{max-width:1040px;margin:0 auto}
.top{display:flex;justify-content:space-between;align-items:center;gap:16px;padding-block:20px;border-bottom:1px solid var(--rule);flex-wrap:wrap}
.brand{font-family:var(--f-display);font-weight:600;font-size:18px;color:var(--ink);text-decoration:none}
.nav{display:flex;gap:20px;flex-wrap:wrap;font-size:15px}
.nav a{color:var(--ink-2);text-decoration:none}
.nav a:hover{color:var(--accent)}
.nav .lang{font-family:var(--f-mono);font-size:13px;border:1px solid var(--rule);padding:2px 8px;border-radius:4px;color:var(--ink)}
.hero{display:grid;grid-template-columns:minmax(0,1.35fr) minmax(0,1fr);gap:56px;align-items:center;padding-block:64px 56px}
.eyebrow{font-family:var(--f-mono);font-size:12.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--accent);margin:0 0 18px}
h1{font-family:var(--f-display);font-weight:600;font-size:clamp(40px,6vw,64px);line-height:1.05;letter-spacing:-.01em;margin:0 0 20px;text-wrap:balance}
.lead{font-size:20px;line-height:1.5;max-width:34em;margin:0 0 20px}
.meta{color:var(--ink-2);font-size:15px;margin:0 0 28px}
.cta{display:flex;gap:12px;flex-wrap:wrap}
.btn{display:inline-block;padding:11px 18px;border-radius:6px;font-weight:500;font-size:15px;text-decoration:none;border:1px solid var(--accent)}
.btn.primary{background:var(--accent);color:var(--paper)}
.btn.ghost{color:var(--accent)}
.scale{background:var(--surface);border:1px solid var(--rule);border-radius:10px;padding:22px 22px 18px}
.scale-title{font-family:var(--f-mono);font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--ink-2);margin:0 0 14px}
.bars{display:grid;gap:6px}
.bar{display:flex;align-items:center;height:26px;color:#fff;font-family:var(--f-mono);font-weight:500;font-size:13px;padding-left:10px;
  clip-path:polygon(0 0,calc(100% - 13px) 0,100% 50%,calc(100% - 13px) 100%,0 100%)}
.bar span{color:#fff}
.scale-note{font-size:13.5px;color:var(--ink-2);margin:14px 0 0;line-height:1.45}
section{padding-block:56px;border-top:1px solid var(--rule)}
h2{font-family:var(--f-display);font-weight:600;font-size:clamp(26px,3.4vw,34px);line-height:1.15;margin:0 0 10px;text-wrap:balance}
.sub{color:var(--ink-2);margin:0 0 32px;max-width:40em}
.services{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px}
.svc{background:var(--surface);border:1px solid var(--rule);border-radius:10px;padding:24px;display:flex;flex-direction:column;gap:12px}
.who{font-family:var(--f-mono);font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--accent);margin:0}
.svc h3{font-family:var(--f-display);font-weight:600;font-size:21px;line-height:1.25;margin:0}
.svc p{margin:0;font-size:15.5px}
.proof{margin-top:auto;padding-top:12px;border-top:1px dashed var(--rule);font-size:14px;color:var(--ink-2)}
.path{list-style:none;counter-reset:step;margin:0;padding:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:0}
.path li{counter-increment:step;position:relative;padding:44px 20px 0 0;border-top:3px solid var(--accent)}
.path li::before{content:counter(step);position:absolute;top:-17px;left:0;width:32px;height:32px;border-radius:50%;background:var(--accent);color:var(--paper);font-family:var(--f-mono);font-size:14px;display:flex;align-items:center;justify-content:center}
.path h3{font-family:var(--f-display);font-weight:600;font-size:19px;line-height:1.25;margin:0 0 6px}
.path p{margin:0;font-size:15px;color:var(--ink-2)}
.figures{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:20px;margin:0;padding:0;list-style:none}
.figures li{border-left:3px solid var(--accent);padding-left:16px}
.num{font-family:var(--f-display);font-weight:600;font-size:40px;line-height:1.1;font-variant-numeric:tabular-nums;display:block}
.figures .lbl{font-size:14.5px;color:var(--ink-2)}
.src{font-size:13px;color:var(--ink-2);margin:20px 0 0}
.tl{display:grid;gap:0;margin:0;padding:0;list-style:none}
.tl li{display:grid;grid-template-columns:150px minmax(0,1fr);gap:24px;padding-block:20px;border-bottom:1px solid var(--rule)}
.tl li:first-child{padding-top:0}
.yr{font-family:var(--f-mono);font-size:14px;color:var(--ink-2);font-variant-numeric:tabular-nums;padding-top:3px}
.tl h3{font-size:18px;font-weight:600;margin:0 0 2px}
.org{color:var(--ink-2);font-size:15px;margin:0 0 8px}
.tl p.d{margin:0;font-size:15.5px;max-width:44em}
.edu{margin-top:28px;display:grid;grid-template-columns:150px minmax(0,1fr);gap:8px 24px;font-size:15.5px}
.edu dt{font-family:var(--f-mono);font-size:14px;color:var(--ink-2)}
.edu dd{margin:0}
.pubs{list-style:none;margin:0;padding:0;display:grid;gap:18px}
.pubs li{max-width:46em}
.pubs .y{font-family:var(--f-mono);font-size:13px;color:var(--ink-2);display:block}
.contact{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px}
.ct{background:var(--surface);border:1px solid var(--rule);border-radius:10px;padding:20px;display:flex;flex-direction:column;gap:6px;min-width:0}
.ct .k{font-family:var(--f-mono);font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--ink-2)}
.ct .v{font-size:16px;font-weight:500;word-break:break-word;user-select:all}
.copy{align-self:flex-start;margin-top:6px;font:inherit;font-size:13px;background:none;border:1px solid var(--rule);color:var(--ink);border-radius:4px;padding:3px 10px;cursor:pointer}
.copy:hover{border-color:var(--accent);color:var(--accent)}
footer{border-top:1px solid var(--rule);padding-block:28px 40px;font-size:14px;color:var(--ink-2);display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap}
.trust{display:flex;flex-wrap:wrap;gap:10px 28px;align-items:center;padding-block:22px;border-top:1px solid var(--rule);margin:0}
.trust .tt{font-family:var(--f-mono);font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--ink-2);width:100%}
.trust .tn{font-weight:600;font-size:15.5px;color:var(--ink)}
.prep{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px}
.prep .card{border-top:3px solid var(--accent);padding-top:14px}
.prep h3{font-family:var(--f-display);font-weight:600;font-size:19px;margin:0 0 10px}
.prep ul{margin:0;padding-left:18px;display:grid;gap:6px;font-size:15px}
.req{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);gap:28px;margin-bottom:32px}
.form{background:var(--surface);border:1px solid var(--rule);border-radius:10px;padding:24px;display:grid;gap:16px}
.form fieldset{border:0;margin:0;padding:0;display:grid;gap:8px}
.form legend,.form label.l{font-size:14px;font-weight:600;margin-bottom:4px;padding:0}
.chips{display:flex;flex-wrap:wrap;gap:8px}
.chips label{display:inline-flex;align-items:center;gap:6px;border:1px solid var(--rule);border-radius:999px;padding:6px 12px;font-size:14px;cursor:pointer;background:var(--paper)}
.chips input{accent-color:var(--accent)}
.chips label:has(input:checked){border-color:var(--accent);background:var(--accent-soft)}
.row2{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:14px}
.form input[type=text],.form textarea{width:100%;font:inherit;font-size:15px;color:var(--ink);background:var(--paper);border:1px solid var(--rule);border-radius:6px;padding:9px 11px}
.form input[type=text]:focus,.form textarea:focus{outline:2px solid var(--accent);outline-offset:1px;border-color:var(--accent)}
.form textarea{min-height:92px;resize:vertical}
.form .err{color:var(--c-g);font-size:14px;margin:0}
.req:has(.out[hidden]){grid-template-columns:minmax(0,720px)}
.out{align-self:start;border:1px dashed var(--accent);border-radius:10px;padding:20px;background:var(--accent-soft);display:flex;flex-direction:column;gap:10px;min-width:0}
.out h3{margin:0;font-size:16px}
.out pre{margin:0;white-space:pre-wrap;word-break:break-word;font-family:var(--f-body);font-size:15px;line-height:1.55}
.out .hint{color:var(--ink-2);font-size:14px;margin:0}
@media (max-width:860px){
  .prep,.req,.row2{grid-template-columns:minmax(0,1fr)}
  .hero{grid-template-columns:minmax(0,1fr);gap:36px;padding-block:44px 40px}
  .services,.contact{grid-template-columns:minmax(0,1fr)}
  .figures,.path{grid-template-columns:repeat(2,minmax(0,1fr))}
  .path{row-gap:36px}
}
@media (max-width:520px){
  body{font-size:16px}
  .tl li,.edu{grid-template-columns:minmax(0,1fr);gap:4px}
  .path{grid-template-columns:minmax(0,1fr)}
  .nav{gap:14px}
  .lead{font-size:18px}
}
@media (prefers-reduced-motion:no-preference){
  .bar{transition:filter .2s}
  .bar:hover{filter:brightness(1.08)}
}
"""

SCALE_WIDTHS = [("A", 38, "--c-a"), ("B", 48, "--c-b"), ("C", 58, "--c-c"), ("D", 68, "--c-d"),
                ("E", 78, "--c-e"), ("F", 88, "--c-f"), ("G", 98, "--c-g")]

T = {
 "ua": {
  "lang": "uk", "file": "index.html", "other": "en.html", "other_label": "EN",
  "title": "Дмитро Паламарчук",
  "description": "Дмитро Паламарчук — консультант з енергоефективності: муніципальні енергетичні плани для громад, консультації ОСББ щодо програм Фонду енергоефективності, підтримка енергетичних спільнот. Черкаси.",
  "nav": [("#how", "Як працюю"), ("#services", "Послуги"), ("#experience", "Досвід"), ("#publications", "Публікації"), ("#contact", "Контакти")],
  "eyebrow": "Енергоефективність · Енергетичне планування громад · Енергетичні спільноти",
  "name": "Дмитро Паламарчук",
  "lead": "Енергоефективність будинку, громади чи енергетичної спільноти — від першого питання до реалізованого проєкту. Одна людина, яка веде вас усім шляхом.",
  "path_title": "Як я працюю",
  "path_sub": "З чим би ви не прийшли, шлях однаковий. Ви маєте одного співрозмовника, а інженерів, юристів і фінансистів, з якими я працюю роками, я залучаю сам, коли це потрібно.",
  "path": [("Розбираємося з питанням", "Що є зараз, що турбує, які дані вже зібрано і яких бракує."), ("Рахуємо", "Базова лінія, варіанти заходів, вартість, економія й окупність."), ("Знаходимо фінансування", "Програми Фонду енергоефективності, донорські гранти, кредити, бюджет громади."), ("Доводимо до результату", "Загальні збори, заявки, підрядники, верифікація, звіти.")],
  "meta": "Черкаси · кандидат економічних наук · член правління ГО «Е-ТЕАМ»",
  "cta1": "Зв’язатися", "cta2": "Профіль ORCID",
  "scale_title": "Клас енергоефективності будівлі",
  "scale_note": "Шкала з енергетичного сертифіката будівлі. Перевести будинок чи громаду ближче до класу A — це й є робота, описана нижче.",
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
     "Консультації ініціативним групам і громадам: вибір моделі спільноти, правові рамки, бізнес-модель і джерела фінансування.",
     "Національний координатор європейського проєкту LIFE-ECOss — центр підтримки енергетичних спільнот у Луцьку."),
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
    ("2023", "Енергоефективність у житловому секторі України", "Стратегії глобальної конкурентоспроможності: соціально-економічний вимір. Матеріали X Міжнародної науково-практичної конференції, ЧДТУ", "https://bit.ly/3OaJAVb"),
    ("2022", "Дослідження чинників, що впливають на рішення співвласників щодо модернізації багатоквартирних будинків", "Матеріали IX Міжнародної науково-практичної конференції, ЧДТУ", "https://er.chdtu.edu.ua/handle/ChSTU/4287"),
  ],
  "trust_title": "Програми й організації, з якими працюю",
  "trust": ["IFC (Група Світового банку)", "GIZ", "UNIDO", "Програма ЄС LIFE", "Фонд енергоефективності", "ГО «Е-ТЕАМ»"],
  "prep_title": "Підготуйтеся до першої розмови",
  "prep_sub": "Перша консультація коротша і корисніша, коли під рукою є ці дані. Не все обов’язково: принесіть те, що є.",
  "prep": [("ОСББ", ["Рахунки або дані про споживання тепла за 2–3 останні опалювальні сезони", "Технічний паспорт будинку: рік, поверховість, площа, кількість квартир", "Протоколи зборів щодо модернізації, якщо вже були", "Енергетичний сертифікат або енергоаудит, якщо є", "Фото фасаду, підвалу і теплового пункту"]),
           ("Громада", ["Дані про споживання енергії бюджетними будівлями за 3 роки", "Чинні програми енергоефективності, SECAP чи МЕП, якщо є", "Контакт відповідальної особи: енергоменеджер, відділ ЖКГ чи економіки", "Перелік проєктів, які громада вже розглядає"]),
           ("Ініціативна група", ["Склад групи і хто має намір стати учасником", "Можливий об’єкт: дах, ділянка, котельня", "Орієнтовне річне споживання електроенергії чи тепла учасниками", "Позиція органу місцевого самоврядування"])],
  "form_title": "Опишіть ваше питання",
  "form_sub": "Заповніть кілька полів — сторінка складе звернення. Скопіюйте його і надішліть на пошту або в месенджер за номером нижче.",
  "f_role": "Хто звертається", "roles": ["ОСББ або управитель", "Громада (ОМС)", "Ініціативна група / енергоспільнота", "Інше"],
  "f_need": "Що потрібно", "needs": ["Консультація", "Участь у загальних зборах ОСББ", "Огляд будинку і розрахунок", "Муніципальний енергетичний план", "Запуск енергетичної спільноти"],
  "f_place": "Населений пункт", "f_name": "Ваше ім’я", "f_contact": "Телефон або email", "f_msg": "Коротко про питання",
  "f_btn": "Скласти звернення", "f_err": "Вкажіть ім’я і контакт, щоб я міг відповісти.",
  "f_out_title": "Ваше звернення — скопіюйте і надішліть",
  "f_hdr": "Звернення з сайту", "f_lab": ["Хто", "Населений пункт", "Що потрібно", "Питання", "Контакт"],
  "c_title": "Контакти",
  "c_sub": "Пишіть щодо МЕП для вашої громади, консультації для ОСББ чи енергетичної спільноти.",
  "contacts": [("Email", "dmytropalamarchuk@gmail.com", True), ("Телефон", "+380 97 889 13 85", True), ("ORCID", "0000-0002-6023-9780", False)],
  "copy": "Копіювати", "copied": "Скопійовано",
  "footer_l": "© 2026 Дмитро Паламарчук",
  "footer_r": "Організація: ГО «Е-ТЕАМ»",
  "jobTitle": "Експерт з енергоефективності та муніципального енергетичного планування",
 },
 "en": {
  "lang": "en", "file": "en.html", "other": "index.html", "other_label": "UA",
  "title": "Dmytro Palamarchuk",
  "description": "Dmytro Palamarchuk — energy efficiency consultant in Ukraine: municipal energy plans for communities, advisory to homeowner associations on Energy Efficiency Fund programmes, support for energy communities.",
  "nav": [("#how", "How I work"), ("#services", "Services"), ("#experience", "Experience"), ("#publications", "Publications"), ("#contact", "Contact")],
  "eyebrow": "Energy efficiency · Municipal energy planning · Energy communities",
  "name": "Dmytro Palamarchuk",
  "lead": "Energy efficiency for a building, a municipality or an energy community, from the first question to a delivered project. One person who takes you through the whole way.",
  "path_title": "How I work",
  "path_sub": "Whatever you come with, the path is the same. You deal with one person; I bring in the engineers, lawyers and finance specialists I have worked with for years when the task needs them.",
  "path": [("Understand the question", "What exists today, what the problem is, which data are available and which are missing."), ("Run the numbers", "Baseline, options, costs, savings and payback."), ("Find the financing", "Energy Efficiency Fund programmes, donor grants, loans, municipal budgets."), ("Deliver the result", "General meetings, applications, contractors, verification, reporting.")],
  "meta": "Cherkasy, Ukraine · PhD in Economics · Board member, NGO E-TEAM",
  "cta1": "Get in touch", "cta2": "ORCID profile",
  "scale_title": "Building energy performance class",
  "scale_note": "The scale from a building energy certificate. Moving a building, or a whole community, closer to class A is the work described below.",
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
     "Advice to initiative groups and municipalities on the community model, legal framework, business model and financing.",
     "National coordinator of the EU LIFE project LIFE-ECOss, which sets up an energy community One-Stop-Shop in Lutsk."),
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
    ("2023", "Energy efficiency in Ukraine’s housing sector", "Strategies of Global Competitiveness: Socio-Economic Dimensions, X International Conference, ChSTU (in Ukrainian)", "https://bit.ly/3OaJAVb"),
    ("2022", "Factors influencing homeowners’ decisions on the modernisation of multi-apartment buildings", "IX International Scientific and Practical Conference, ChSTU (in Ukrainian)", "https://er.chdtu.edu.ua/handle/ChSTU/4287"),
  ],
  "trust_title": "Programmes and organisations I work with",
  "trust": ["IFC (World Bank Group)", "GIZ", "UNIDO", "EU LIFE Programme", "Energy Efficiency Fund of Ukraine", "NGO E-TEAM"],
  "prep_title": "Prepare for the first conversation",
  "prep_sub": "A first consultation is shorter and more useful when you have this information at hand. Bring what you have.",
  "prep": [("Homeowner association", ["Heat bills or consumption data for the last 2–3 heating seasons", "Building passport: year, storeys, floor area, number of flats", "Minutes of meetings on renovation, if any", "Energy certificate or energy audit, if available", "Photos of the facade, basement and heating substation"]),
           ("Municipality", ["Energy consumption of public buildings for 3 years", "Current energy efficiency programmes, SECAP or energy plan, if any", "Contact of the responsible person: energy manager, housing or economic department", "List of projects the municipality is already considering"]),
           ("Community group", ["Members of the group and who intends to join", "Possible site: roof, land plot, boiler house", "Approximate annual electricity or heat use of members", "Position of the local authority"])],
  "form_title": "Describe your question",
  "form_sub": "Fill in a few fields and the page will compose a message. Copy it and send it by email or messenger to the contacts below.",
  "f_role": "Who you are", "roles": ["Homeowner association or manager", "Municipality", "Community group / energy community", "Other"],
  "f_need": "What you need", "needs": ["Consultation", "Attendance at an HOA general meeting", "Building inspection and calculation", "Municipal energy plan", "Setting up an energy community"],
  "f_place": "Town or village", "f_name": "Your name", "f_contact": "Phone or email", "f_msg": "Your question in brief",
  "f_btn": "Compose message", "f_err": "Please enter your name and a contact so I can reply.",
  "f_out_title": "Your message — copy and send it",
  "f_hdr": "Request from the website", "f_lab": ["Who", "Location", "Needs", "Question", "Contact"],
  "c_title": "Contact",
  "c_sub": "Write about an energy plan for your municipality, HOA advisory or an energy community.",
  "contacts": [("Email", "dmytropalamarchuk@gmail.com", True), ("Phone", "+380 97 889 13 85", True), ("ORCID", "0000-0002-6023-9780", False)],
  "copy": "Copy", "copied": "Copied",
  "footer_l": "© 2026 Dmytro Palamarchuk",
  "footer_r": "Organisation: NGO E-TEAM",
  "jobTitle": "Energy efficiency and municipal energy planning expert",
 },
}

ORCID = "https://orcid.org/0000-0002-6023-9780"
BASE = "https://dmytropalamarchuk-svg.github.io/"
FAVICON = "data:image/svg+xml," + "%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 32 32%27%3E%3Crect width=%2732%27 height=%2732%27 rx=%276%27 fill=%27%231d6b66%27/%3E%3Cpath d=%27M7 10h11l3 3-3 3H7z%27 fill=%27%23fff%27/%3E%3Cpath d=%27M7 18h16l3 3-3 3H7z%27 fill=%27%23b6e0d9%27/%3E%3C/svg%3E"


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;"))


def page(t, skeleton):
    nav = "".join(f'<a href="{h}">{esc(l)}</a>' for h, l in t["nav"])
    nav += f'<a class="lang" href="{t["other"]}" hreflang="{"en" if t["lang"]=="uk" else "uk"}">{t["other_label"]}</a>'
    bars = "".join(f'<div class="bar" style="width:{w}%;background:var({c})"><span>{k}</span></div>' for k, w, c in SCALE_WIDTHS)
    svcs = "".join(
        f'<article class="svc"><p class="who">{esc(a)}</p><h3>{esc(h)}</h3><p>{esc(p)}</p><p class="proof">{esc(pr)}</p></article>'
        for a, h, p, pr in t["services"])
    path = "".join(f'<li><h3>{esc(a)}</h3><p>{esc(b)}</p></li>' for a, b in t["path"])
    trust = f'<div class="trust"><span class="tt">{esc(t["trust_title"])}</span>' + "".join(f'<span class="tn">{esc(x)}</span>' for x in t["trust"]) + '</div>'
    prep = "".join(f'<div class="card"><h3>{esc(h)}</h3><ul>' + "".join(f'<li>{esc(i)}</li>' for i in items) + '</ul></div>' for h, items in t["prep"])
    roles = "".join(f'<label><input type="radio" name="role" value="{esc(r)}" id="role-{k}"{" checked" if k==0 else ""}> {esc(r)}</label>' for k, r in enumerate(t["roles"]))
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
<div class="out" id="f-out" hidden><h3>{esc(t['f_out_title'])}</h3><pre class="v" id="f-text"></pre><button class="copy" type="button" id="copy-msg">{t['copy']}</button><p class="hint">{esc(t['contacts'][0][1])} · {esc(t['contacts'][1][1])}</p></div>
</div>"""
    figs = "".join(f'<li><span class="num">{esc(n)}</span><span class="lbl">{esc(l)}</span></li>' for n, l in t["figures"])
    tl = ""
    for yr, role, org, url, d in t["timeline"]:
        o = f'<a href="{url}" rel="noopener">{esc(org)}</a>' if url else esc(org)
        tl += f'<li><div class="yr">{esc(yr)}</div><div><h3>{esc(role)}</h3><p class="org">{o}</p><p class="d">{esc(d)}</p></div></li>'
    edu = "".join(f'<dt>{y}</dt><dd>{esc(x)}</dd>' for y, x in t["edu"])
    pubs = "".join(f'<li><span class="y">{y}</span><a href="{u}" rel="noopener">{esc(ti)}</a><br><span class="org">{esc(v)}</span></li>' for y, ti, v, u in t["pubs"])
    cts = ""
    for i, (k, v, cp) in enumerate(t["contacts"]):
        btn = f'<button class="copy" type="button" id="copy-{i}" data-v="{esc(v)}">{t["copy"]}</button>' if cp else f'<a href="{ORCID}" rel="noopener">orcid.org</a>'
        cts += f'<div class="ct"><span class="k">{k}</span><span class="v">{esc(v)}</span>{btn}</div>'
    ld = {"@context": "https://schema.org", "@type": "Person", "name": t["name"],
          "alternateName": ["Дмитро Паламарчук", "Dmytro Palamarchuk", "Паламарчук Дмитро Миколайович"],
          "jobTitle": t["jobTitle"], "address": {"@type": "PostalAddress", "addressLocality": "Cherkasy", "addressCountry": "UA"},
          "worksFor": {"@type": "Organization", "name": "NGO E-TEAM", "url": "https://www.eteamngo.org/"},
          "alumniOf": [{"@type": "CollegeOrUniversity", "name": "Taras Shevchenko National University of Kyiv"},
                       {"@type": "CollegeOrUniversity", "name": "Cherkasy State Technological University"}],
          "knowsAbout": ["Energy efficiency", "Municipal energy planning", "Energy communities", "Homeowner associations", "EU energy policy"],
          "sameAs": [ORCID]}
    head = (f'<title>{esc(t["title"])}</title>'
            f'<meta name="claude:viewport-fit-sides" content="cover">'
            f'<meta name="description" content="{esc(t["description"])}">'
            f'<link rel="canonical" href="{BASE}{"" if t["file"]=="index.html" else t["file"]}">'
            f'<link rel="alternate" hreflang="uk" href="{BASE}"><link rel="alternate" hreflang="en" href="{BASE}en.html"><link rel="alternate" hreflang="x-default" href="{BASE}">'
            f'<meta property="og:type" content="profile"><meta property="og:title" content="{esc(t["title"])}"><meta property="og:description" content="{esc(t["description"])}"><meta property="og:url" content="{BASE}{"" if t["file"]=="index.html" else t["file"]}">'
            f'<link rel="icon" href="{FAVICON}">'
            f'{FONTS}<style>{CSS}</style>'
            f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>')
    body = f"""
<div class="wrap">
<header class="top"><a class="brand" href="{t['file']}">{esc(t['name'])}</a><nav class="nav" aria-label="Main">{nav}</nav></header>
<main>
<div class="hero">
  <div>
    <p class="eyebrow">{esc(t['eyebrow'])}</p>
    <h1>{esc(t['name'])}</h1>
    <p class="lead">{esc(t['lead'])}</p>
    <p class="meta">{esc(t['meta'])}</p>
    <div class="cta"><a class="btn primary" href="#contact">{esc(t['cta1'])}</a><a class="btn ghost" href="{ORCID}" rel="noopener">{esc(t['cta2'])}</a></div>
  </div>
  <figure class="scale" aria-label="{esc(t['scale_title'])}" style="margin:0">
    <p class="scale-title">{esc(t['scale_title'])}</p>
    <div class="bars">{bars}</div>
    <figcaption class="scale-note">{esc(t['scale_note'])}</figcaption>
  </figure>
</div>
<section id="how"><h2>{esc(t['path_title'])}</h2><p class="sub">{esc(t['path_sub'])}</p><ol class="path">{path}</ol></section>
<section id="services"><h2>{esc(t['s_title'])}</h2><p class="sub">{esc(t['s_sub'])}</p><div class="services">{svcs}</div></section>
{trust}
<section id="figures" aria-label="{esc(t['f_title'])}"><h2>{esc(t['f_title'])}</h2><ul class="figures" style="margin-top:28px">{figs}</ul><p class="src">{esc(t['f_src'])}</p></section>
<section id="prepare"><h2>{esc(t['prep_title'])}</h2><p class="sub">{esc(t['prep_sub'])}</p><div class="prep">{prep}</div></section>
<section id="experience"><h2>{esc(t['e_title'])}</h2><ul class="tl" style="margin-top:28px">{tl}</ul><dl class="edu">{edu}</dl></section>
<section id="publications"><h2>{esc(t['p_title'])}</h2><ul class="pubs" style="margin-top:28px">{pubs}</ul></section>
<section id="contact"><h2>{esc(t['c_title'])}</h2><p class="sub">{esc(t['c_sub'])}</p><h3 style="font-family:var(--f-display);font-size:21px;margin:0 0 6px">{esc(t['form_title'])}</h3><p class="sub" style="margin-bottom:20px">{esc(t['form_sub'])}</p>{form}<div class="contact">{cts}</div></section>
</main>
<footer><span>{esc(t['footer_l'])}</span><a href="https://www.eteamngo.org/" rel="noopener">{esc(t['footer_r'])}</a></footer>
</div>
<script>
var lab={json.dumps(t['f_lab'], ensure_ascii=False)}, hdr={json.dumps(t['f_hdr'], ensure_ascii=False)};
document.getElementById('reqform').addEventListener('submit',function(e){{e.preventDefault();
  var g=function(id){{return document.getElementById(id).value.trim();}};
  var name=g('f-name'), contact=g('f-contact'), err=document.getElementById('f-err');
  if(!name||!contact){{err.hidden=false;return;}} err.hidden=true;
  var role=(document.querySelector('input[name=role]:checked')||{{}}).value||'';
  var needs=[].slice.call(document.querySelectorAll('input[name=need]:checked')).map(function(x){{return x.value;}}).join(', ');
  var lines=[hdr, lab[0]+': '+role];
  if(g('f-place')) lines.push(lab[1]+': '+g('f-place'));
  if(needs) lines.push(lab[2]+': '+needs);
  if(g('f-msg')) lines.push(lab[3]+': '+g('f-msg'));
  lines.push(lab[4]+': '+name+', '+contact);
  document.getElementById('f-text').textContent=lines.join('\\n');
  var o=document.getElementById('f-out'); o.hidden=false; o.scrollIntoView({{behavior:'smooth',block:'nearest'}});
}});
document.getElementById('copy-msg').setAttribute('data-v','');
document.getElementById('copy-msg').addEventListener('click',function(){{this.setAttribute('data-v',document.getElementById('f-text').textContent);}},true);
document.querySelectorAll('.copy').forEach(function(b){{b.addEventListener('click',function(){{
  var v=b.getAttribute('data-v');
  var done=function(){{b.textContent='{t['copied']}';setTimeout(function(){{b.textContent='{t['copy']}';}},1600);}};
  try{{navigator.clipboard.writeText(v).then(done,function(){{sel(b);}});}}catch(e){{sel(b);}}
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
    open(os.path.join(HERE, "dist", "index.html"), "w").write(page(T["ua"], True))
    open(os.path.join(HERE, "dist", "en.html"), "w").write(page(T["en"], True))
    open(os.path.join(HERE, "dist", "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}sitemap.xml\n")
    open(os.path.join(HERE, "dist", "sitemap.xml"), "w").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f'<url><loc>{BASE}</loc><lastmod>2026-10-19</lastmod></url>\n<url><loc>{BASE}en.html</loc><lastmod>2026-10-19</lastmod></url>\n</urlset>\n')
    open(os.path.join(HERE, "dist", ".nojekyll"), "w").write("")
    print("ok")
