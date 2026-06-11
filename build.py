#!/usr/bin/env python3
"""
Static site generator for Shannon Craver's portfolio.

Authoring lives here as plain data; running this emits dependency-free static
HTML (index.html + projects/*.html). No build tooling is needed to *serve* the
result — just open index.html or host the folder anywhere.

    python3 build.py
"""
import html, os, pathlib

ROOT = pathlib.Path(__file__).parent

# --------------------------------------------------------------------------- #
#  CONTENT
# --------------------------------------------------------------------------- #
SITE = {
    "name":    "Shannon Craver",
    "role":    "Freelance UX / UI Design & Direction",
    "tagline": "Crafting extraordinary brands & experiences from the ground up.",
    "email":   "shannon@studiocontrary.com",
    "pdf":     "assets/files/ShannonCraver_Portfolio_2023.pdf",
    "socials": [
        {"label": "LinkedIn", "url": "https://uk.linkedin.com/in/shannoncraver"},
    ],
}

ABOUT = {
    "intro": "Hey, I’m Shannon — a freelance designer specialising in crafting "
             "extraordinary brands &amp; experiences <em>from the ground up.</em>",
    "bio": [
        "With over 10 years of experience across branding, digital products and "
        "experiential design — in leading agencies and as a freelance designer in "
        "the UK, USA and Canada — I’ve built a wide range of skills across many "
        "disciplines and industries.",
        "I’m a generalist in the best sense of the word: able to assess and deploy "
        "exactly what’s needed, design-wise, for the startups, businesses and "
        "agencies I work with — to create work that truly moves the needle.",
    ],
    "with": [
        "Enthusiastic, positive and sociable; calm under pressure",
        "Versatile, and quick to fit into teams and hit the ground running",
        "Comfortable across the whole project — strategy, research, design, "
        "prototyping, testing and implementation",
        "Confident with stakeholder and user-facing presentations and workshops",
        "Experienced managing, motivating and building design teams",
        "Set up for remote work from my home studio",
    ],
    "clients": [
        "American Cancer Society", "Aritzia", "Barclay’s", "BBC", "British Airways",
        "Compare the Market", "Holland &amp; Barrett", "Lululemon", "Marks &amp; Spencer",
        "McDonald’s", "Nintendo", "PizzaExpress", "Streetbees", "Tesco",
        "Tourism Canada", "UK Ministry of Justice",
    ],
    "capabilities": [
        "Interface design (UI)", "Experience design (UX)", "Product design",
        "Web design", "Prototyping", "Design systems", "Design sprints",
        "User research", "Visual design", "Brand design &amp; strategy",
        "Building design teams",
    ],
    "experience": [
        ("Freelance", "Design &amp; creative direction", "Jan 2020 – Present"),
        ("Whippet", "Design Director", "Jan 2019 – Jan 2020"),
        ("Whippet", "Senior Designer", "Jun 2015 – Dec 2018"),
        ("Freelance", "Brand &amp; digital", "Jul 2014 – Jun 2015"),
        ("Free Agency Creative", "Designer", "Jan – Jul 2014"),
        ("DDB", "Junior Designer", "Jan 2012 – Dec 2013"),
        ("Western Front Arts", "Design Intern", "Jan – Apr 2011"),
        ("Fluevog", "Designer", "Aug 2010 – Feb 2011"),
    ],
    "education": [
        ("Emily Carr University of Art and Design", "Bachelor of Design"),
        ("Maryland Institute College of Art", "International Exchange"),
    ],
}

TESTIMONIALS = [
    ("Shannon is one of those rare talents that has a combination of exceptional "
     "design skills alongside a great ‘can do’ attitude. From large scale branding "
     "projects to smaller day to day tasks she’s got the goods to deliver whatever "
     "is required.", "Sean Dwyer", "Creative Director, Whippet"),
    ("Shannon is a superstar designer!",
     "Sharry Cramond", "Marketing Director, M&amp;S Food, Hospitality &amp; Loyalty"),
    ("Our new brand brings a vibrancy to the impact space whilst being respectful "
     "of the tough work and challenges we face in delivering healthcare in "
     "low-income countries. Many people now comment on our rebrand and the "
     "reception has been fantastic.", "Edward Booty", "Founder &amp; CEO, reach52"),
    ("Strategically focused, she was also able to develop concepts in a smart and "
     "collaborative way. She was as technically adept in digital design as she was "
     "in print, and also positive, enthusiastic and focused on problem solving.",
     "Chris Taylor", "Business Transformation Comms Director, News UK"),
    ("Shannon really did go above and beyond, bringing professionalism, excitement "
     "and energy to our projects. She really gets the essence of who we are and "
     "what we’re trying to achieve.", "Joe Norman", "Head of Sales &amp; Retail Marketing, Freesat"),
    ("Shannon’s strength is in her understanding of creative process and the "
     "elements required for high-level design. Her kind and pleasant demeanour "
     "made tight deadlines and situations manageable.",
     "Tak Yukawa", "Founder &amp; Creative Director, Free Agency Creative"),
]

PROJECTS = [
    {
        "slug": "streetbees", "title": "Streetbees", "hero": 7,
        "card": "assets/cards/streetbees.jpg",
        "eyebrow": "Product design · Design system",
        "tagline": "Bringing cohesion, personality &amp; user delight to a consumer survey app.",
        "context": "Sole designer · B2B product, iOS &amp; Android",
        "tags": ["Product design", "Feature ideation", "Wireframing", "Prototyping",
                 "UX research &amp; testing", "UI &amp; visual refresh", "Design system"],
        "brief": "Streetbees is a mobile app where people complete surveys about their "
                 "everyday life, and get paid to do it. I worked freelance as the sole "
                 "designer on their B2B product, responsible for the iOS and Android apps. "
                 "That meant creating and maintaining a refreshed design system, and "
                 "interviewing users to find the key moments in the journey causing churn. "
                 "From there I prioritised — with the wider company — which features fit "
                 "the roadmap and budget while delivering the biggest results, carrying each "
                 "from idea, to wireframe, to tested prototype, to live feature.",
        "spreads": [(5, "Brand &amp; onboarding"),
                    (6, "UI design refresh — before &amp; after"),
                    (7, "Refreshed app interface")],
    },
    {
        "slug": "greek-national-lottery", "title": "Greek National Lottery", "hero": 12,
        "eyebrow": "Product strategy · UX/UI",
        "tagline": "Bringing the experience of a Greek high-street institution online.",
        "context": "Freelance Design Lead at Else London · Client: OPAP",
        "tags": ["Strategy &amp; concepts", "UX workshops", "Journey mapping",
                 "Wireframing", "Prototyping", "Design system"],
        "brief": "I joined Else London as a freelance Design Lead to shape a new digital "
                 "strategy for the Greek National Lottery (OPAP) — a much-loved institution "
                 "with shops in every neighbourhood. With lockdowns in full swing, we created "
                 "a bold new direction for OPAP’s online presence, building a brand-new, "
                 "expandable design system in Figma alongside the UX and UI for their new "
                 "lottery app.",
        "spreads": [(9, "Strategy &amp; identity"),
                    (10, "User research &amp; journey"),
                    (11, "Visual concept board"),
                    (12, "Lottery app — UI concepts")],
    },
    {
        "slug": "sevva", "title": "Sevva", "hero": 16,
        "eyebrow": "Brand &amp; product · Research",
        "tagline": "A strong brand to launch a digital publication &amp; app focused on sustainability.",
        "context": "Brand strategy, then product prototype, for a sustainability startup",
        "tags": ["Brand strategy &amp; design", "User research &amp; testing",
                 "Wireframing", "Prototyping", "Component library"],
        "brief": "Sevva is a startup building a lightweight, customisable community and "
                 "content-sharing platform focused on sustainability. The client first hired "
                 "me to develop a strategy for the brand and product — including user "
                 "interviews, generative research and competitor analysis — then rehired me "
                 "to design a testable prototype of the platform itself.",
        "spreads": [(15, "Brand &amp; product concepts"),
                    (16, "UI concepts"),
                    (17, "Wireframes"),
                    (18, "UX research outcomes"),
                    (19, "Design prototype")],
    },
    {
        "slug": "unifi", "title": "UniFi", "hero": 22,
        "eyebrow": "Fintech · Design sprint",
        "tagline": "Helping an early-stage fintech startup find their voice &amp; designing their first MVP.",
        "context": "Brand &amp; product strategy via a remote Google Design Sprint",
        "tags": ["Brand strategy &amp; design", "Design sprint facilitation",
                 "User research &amp; testing", "Prototyping"],
        "brief": "UniFi is an early-stage startup helping expats manage finances spread "
                 "across multiple countries by connecting them to a single account, with "
                 "expert advice on investing and tax on a subscription basis. I worked with "
                 "the founders on brand and product strategy, developing an MVP through a "
                 "one-week Google Design Sprint that I facilitated remotely.",
        "spreads": [(21, "Strategy &amp; design sprint"),
                    (22, "UI concepts"),
                    (23, "Design sprint prototype")],
    },
    {
        "slug": "ms-energy", "title": "M&amp;S Energy", "hero": 27,
        "eyebrow": "Brand · Web design",
        "tagline": "Creating a brand &amp; website for a new sustainable energy offering from M&amp;S.",
        "context": "Rebrand &amp; website for a digital-first energy brand",
        "tags": ["Brand identity", "Brand guidelines", "Website design"],
        "brief": "A new, digital-first energy offering from a well-known high-street brand "
                 "needed a complete rebrand to stand a chance against the new energy "
                 "start-ups. I created a friendly, contemporary yet trustworthy digital-first "
                 "brand, plus a fresh new website — including a quiz-like marketing funnel "
                 "built to drive sign-ups.",
        "spreads": [(25, "Brand &amp; design system"),
                    (26, "Website design"),
                    (27, "App onboarding design"),
                    (28, "Icon design")],
    },
    {
        "slug": "just-access", "title": "Just: Access", "hero": 34,
        "eyebrow": "Research · Product · Web",
        "tagline": "Refining the product &amp; brand of a machine-learning legal transcription service.",
        "context": "UX, brand &amp; web for a legal-tech social enterprise",
        "tags": ["User research", "Wireframing", "Prototyping", "Website design",
                 "Illustration", "App design"],
        "brief": "Just: Access is a legal-tech social enterprise providing affordable access "
                 "to legal transcription through a mix of machine learning and expert human "
                 "transcribers. They had a basic, functional MVP and wanted to improve the "
                 "overall experience, market themselves better and raise funds. I led user "
                 "research, wireframes, prototypes, illustration and the design of their app "
                 "and website.",
        "spreads": [(31, "Experience map"),
                    (32, "Paper prototypes"),
                    (33, "User research outputs"),
                    (34, "Website design")],
    },
    {
        "slug": "immediate-media", "title": "Immediate Media", "hero": 30,
        "card": "assets/cards/immediate-media.jpg",
        "eyebrow": "Brand · Web design",
        "tagline": "A brand refresh &amp; new corporate website for the UK’s biggest special-interest media company.",
        "context": "Embedded freelance designer — branding, guidelines &amp; site",
        "tags": ["Content strategy", "UX research", "Stakeholder workshops",
                 "Wireframes &amp; prototypes", "Website design"],
        "brief": "The UK’s biggest consumer media company needed a brand refresh, along with a "
                 "new corporate website. I worked as an embedded freelance designer to create "
                 "the branding and guidelines, and then a new site — including its structure "
                 "and content strategy.",
        "spreads": [(30, "Brand &amp; corporate website")],
    },
    {
        "slug": "freesat", "title": "Freesat", "hero": 29,
        "card": "assets/cards/freesat.jpg",
        "eyebrow": "Brand · Ecommerce",
        "tagline": "Launching a free-satellite-TV brand into direct-to-consumer retail.",
        "context": "Ecommerce, packaging &amp; campaign for a BBC / ITV venture",
        "tags": ["Ecommerce design", "Campaign strategy &amp; design",
                 "Packaging design", "Photoshoot art direction"],
        "brief": "Freesat is a free satellite-TV service and joint venture between the BBC and "
                 "ITV. To launch their first digital TV product — entirely created and "
                 "manufactured by them — they wanted an updated, forward-looking brand "
                 "strategy: tone of voice and visuals, plus product packaging built to succeed "
                 "on the high street and in a new direct-to-consumer online store.",
        "spreads": [(29, "Ecommerce, packaging &amp; campaign")],
    },
    {
        "slug": "framework", "title": "Framework", "hero": 36,
        "eyebrow": "Brand · Web design",
        "tagline": "A brand &amp; digital experience for a downtown residential development aimed at first-time buyers.",
        "context": "Brand strategy, art direction &amp; website",
        "tags": ["Brand strategy &amp; design", "Photoshoot art direction", "Website design"],
        "brief": "A centrally located residential development aimed at young, first-time "
                 "buyers. The client wanted a brand and digital experience that stood out from "
                 "competitors and appealed to first-time buyers, while highlighting the best of "
                 "what the downtown area had to offer in terms of lifestyle.",
        "spreads": [(35, "Brand &amp; wireframes"),
                    (36, "Website design"),
                    (37, "Icon system")],
    },
]

# --------------------------------------------------------------------------- #
#  HELPERS
# --------------------------------------------------------------------------- #
ARROW = ('<svg class="arrow" width="15" height="15" viewBox="0 0 24 24" fill="none" '
         'stroke="currentColor" stroke-width="1.7" stroke-linecap="round" '
         'stroke-linejoin="round"><path d="M7 17L17 7M9 7h8v8"/></svg>')

def thumb(p, root):  return f"{root}assets/spreads/thumb/p{p:02d}.jpg"
def full(p, root):   return f"{root}assets/spreads/full/p{p:02d}.jpg"
def card_img(proj, root):
    return f"{root}{proj['card']}" if proj.get("card") else thumb(proj["hero"], root)
def role_list(tags): return "".join(f"<li>{t}</li>" for t in tags)
def tag_line(tags):  return " &middot; ".join(tags)

def head(title, desc, root, og_image):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{og_image}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{root}assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{root}assets/css/style.css">
</head>"""

def header(home):
    """home = '' on index, '../index.html' on project pages."""
    base = home if home else ""
    brand_href = (home or "#top")
    return f"""<header class="site-header" id="top">
  <div class="wrap">
    <a class="brand" href="{brand_href}">Shannon Craver</a>
    <nav class="nav" aria-label="Primary">
      <a href="{base}#work">Work</a>
      <a href="{base}#about">About</a>
      <a href="{base}#testimonials">Testimonials</a>
      <a href="{base}#contact">Contact</a>
    </nav>
    <button class="menu-toggle" aria-label="Menu" aria-expanded="false">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>"""

def contact_and_footer(root):
    socials = "".join(
        f'<a href="{s["url"]}" target="_blank" rel="noopener">{s["label"]} {ARROW}</a>'
        for s in SITE["socials"])
    return f"""<section class="contact section" id="contact">
  <div class="wrap">
    <p class="eyebrow reveal" style="color:var(--muted-2)">Available for freelance &amp; contract work</p>
    <h2 class="big reveal d1">Let’s build<br>something<br><a href="mailto:{SITE['email']}">that moves<br>the needle.</a></h2>
    <p class="sub reveal d1">Have a project in mind, or just want to say hello? I’d love to hear from you.</p>
    <div class="cta-row reveal d2">
      <a class="link-arrow" href="mailto:{SITE['email']}">{SITE['email']} {ARROW}</a>
    </div>
    <div class="socials reveal d3">{socials}</div>
  </div>
</section>
<footer class="site-footer">
  <div class="wrap">
    <span>© <span data-year>2023</span> Shannon Craver — {SITE['role']}</span>
    <a class="to-top" href="#top">Back to top
      <svg class="arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19V5M5 12l7-7 7 7"/></svg>
    </a>
  </div>
</footer>
<script src="{root}assets/js/main.js"></script>
</body>
</html>"""

# --------------------------------------------------------------------------- #
#  INDEX PAGE
# --------------------------------------------------------------------------- #
def build_index():
    root = ""
    og = "assets/spreads/full/p22.jpg"
    parts = [head(f"{SITE['name']} — UX / UI Designer &amp; Director",
                  "Freelance UX/UI designer and creative director. 10+ years crafting "
                  "brands, digital products and experiences for startups, businesses and "
                  "agencies across the UK, USA and Canada.", root, og)]
    parts.append("<body>")
    parts.append(header(""))

    # hero
    parts.append(f"""<main>
<section class="hero" data-hero>
  <div class="wrap">
    <p class="eyebrow on-dark">{SITE['role']}</p>
    <h1>Shannon<br>Craver</h1>
    <p class="lede">{SITE['tagline']}</p>
    <div class="cta-row">
      <a class="link-arrow" href="#work">Selected work {ARROW}</a>
      <a class="link-arrow" href="#contact">Get in touch {ARROW}</a>
    </div>
  </div>
  <div class="scroll-cue"><span class="bar"></span> Scroll</div>
</section>""")

    # work grid
    cards = []
    for i, p in enumerate(PROJECTS, 1):
        cards.append(f"""<a class="card reveal" href="projects/{p['slug']}.html" aria-label="{p['title'].replace('&amp;','&')} case study">
    <div class="card-img">
      <img src="{card_img(p, root)}" alt="{p['title']} — preview" width="800" height="500" loading="lazy">
    </div>
    <div class="card-body">
      <div class="card-title"><h3>{p['title']}</h3>{ARROW}</div>
      <p class="card-desc">{p['tagline']}</p>
      <p class="card-tags">{tag_line(p['tags'][:5])}</p>
    </div>
  </a>""")
    parts.append(f"""<section class="section" id="work">
  <div class="wrap">
    <div class="sec-head reveal">
      <p class="eyebrow">Work</p>
      <h2>Selected work.</h2>
    </div>
    <div class="work-grid">
      {''.join(cards)}
    </div>
  </div>
</section>""")

    # about
    clients = "".join(f"<li>{c}</li>" for c in ABOUT["clients"])
    caps = "".join(f"<li>{c}</li>" for c in ABOUT["capabilities"])
    withs = "".join(f"<li>{w}</li>" for w in ABOUT["with"])
    bio = "".join(f"<p>{b}</p>" for b in ABOUT["bio"])
    exp = "".join(
        f'<div class="cv-row"><span class="role"><b>{c}</b> {r}</span><span class="when">{w}</span></div>'
        for c, r, w in ABOUT["experience"])
    edu = "".join(
        f'<div class="cv-row"><span class="role"><b>{s}</b> {d}</span></div>'
        for s, d in ABOUT["education"])
    parts.append(f"""<section class="about section" id="about">
  <div class="wrap">
    <p class="eyebrow dash reveal">About</p>
    <p class="intro reveal d1">{ABOUT['intro']}</p>
    <div class="about-grid">
      <div class="about-bio reveal">
        {bio}
        <ul class="with">{withs}</ul>
      </div>
      <div class="facts">
        <div class="fact reveal d1">
          <h4>Selected clients</h4>
          <ul>{clients}</ul>
        </div>
        <div class="fact single reveal d2">
          <h4>Capabilities</h4>
          <ul>{caps}</ul>
        </div>
      </div>
    </div>
    <div class="about-grid">
      <div class="fact single reveal">
        <h4>Experience</h4>
        {exp}
      </div>
      <div class="fact single reveal d1">
        <h4>Education</h4>
        {edu}
      </div>
    </div>
  </div>
</section>""")

    # testimonials
    qs = []
    for quote, name, title in TESTIMONIALS:
        qs.append(f"""<figure class="quote reveal">
      <div class="mark" aria-hidden="true">“</div>
      <blockquote>{quote}</blockquote>
      <figcaption class="who"><b>{name}</b><span>{title}</span></figcaption>
    </figure>""")
    parts.append(f"""<section class="quotes section" id="testimonials">
  <div class="wrap">
    <div class="sec-head reveal">
      <p class="eyebrow">Testimonials</p>
      <h2>Kind words from people I’ve worked with.</h2>
    </div>
    <div class="quote-grid">{''.join(qs)}</div>
  </div>
</section>""")

    parts.append("</main>")
    parts.append(contact_and_footer(root))
    (ROOT / "index.html").write_text("\n".join(parts), encoding="utf-8")

# --------------------------------------------------------------------------- #
#  PROJECT PAGES
# --------------------------------------------------------------------------- #
def build_project(i, p):
    root = "../"
    home = "../index.html"
    nxt = PROJECTS[(i + 1) % len(PROJECTS)]
    plain_title = p["title"].replace("&amp;", "&")

    spreads = []
    for n, (pg, cap) in enumerate(p["spreads"], 1):
        spreads.append(f"""<figure class="spread reveal">
      <button class="frame" data-full="{full(pg, root)}" data-cap="{cap}" aria-label="Enlarge: {cap}">
        <img src="{full(pg, root)}" alt="{plain_title} — {cap}" width="2560" height="1600" loading="lazy">
      </button>
      <figcaption><span class="n">{n:02d}</span> {cap} <span class="zoom">Click to enlarge</span></figcaption>
    </figure>""")

    parts = [head(f"{plain_title} — Shannon Craver",
                  p["tagline"].replace("&amp;", "&").replace("<em>", "").replace("</em>", ""),
                  root, full(p["hero"], root))]
    parts.append("<body>")
    parts.append(header(home))
    parts.append(f"""<main>
<section class="proj-hero">
  <div class="wrap">
    <p class="eyebrow"><a href="{home}#work">Work</a> &nbsp;/&nbsp; {p['eyebrow']}</p>
    <h1>{p['title']}</h1>
    <p class="tagline">{p['tagline']}</p>
  </div>
</section>
<section class="wrap">
  <div class="proj-meta">
    <p class="brief reveal">{p['brief']}</p>
    <div class="side reveal d1">
      <div><h4>Role</h4><ul class="role-list">{role_list(p['tags'])}</ul></div>
      <div><h4>Context</h4><p class="ctx">{p['context']}</p></div>
    </div>
  </div>
</section>
<section class="spreads section">
  <div class="wrap">
    {''.join(spreads)}
  </div>
</section>
</main>
<a class="next-proj" href="{nxt['slug']}.html">
  <div class="wrap">
    <span class="label">Next project</span>
    <div class="row">
      <h3>{nxt['title']} {ARROW}</h3>
      <div class="np-thumb"><img src="{card_img(nxt, root)}" alt="{nxt['title']}" width="800" height="500" loading="lazy"></div>
    </div>
  </div>
</a>""")
    parts.append(contact_and_footer(root))
    out = ROOT / "projects" / f"{p['slug']}.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text("\n".join(parts), encoding="utf-8")

# --------------------------------------------------------------------------- #
def main():
    build_index()
    for i, p in enumerate(PROJECTS):
        build_project(i, p)
    print(f"Built index.html + {len(PROJECTS)} project pages.")

if __name__ == "__main__":
    main()
