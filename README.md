# Shannon Craver — Portfolio

A minimal, responsive portfolio site built from `ShannonCraver_Creds_2023.pdf`.
Plain HTML / CSS / vanilla JS — **no build tooling required to run or host it.**

## Preview locally

Any static file server works. For example:

```bash
cd portfolio-website
python3 -m http.server 8000
# open http://localhost:8000
```

(You can also just double-click `index.html`, though a server is recommended so
the lightbox and relative paths behave exactly like production.)

## Structure

```
portfolio-website/
├── index.html              ← home: hero, work grid, about, testimonials, contact
├── projects/               ← one case-study page per project
│   ├── streetbees.html
│   ├── greek-national-lottery.html
│   ├── sevva.html
│   ├── unifi.html
│   ├── ms-energy.html
│   └── just-access.html
├── build.py                ← regenerates all HTML from the content data below
└── assets/
    ├── css/style.css
    ├── js/main.js
    ├── favicon.svg
    ├── files/ShannonCraver_Portfolio_2023.pdf   ← the source PDF (kept for reference)
    ├── cards/               ← clean cropped card-hero images (device-on-colour)
    ├── spreads/full/        ← retina page renders (used in the lightbox)
    ├── spreads/thumb/        ← small renders (cards / grids)
    └── extracted/           ← every embedded image pulled from the PDF + _manifest.json
```

There are **nine** project pages under `projects/`. The spread images have the
old email, phone, and the on-page project titles redacted, and any blank top
margin auto-trimmed (see the render script that produced `assets/spreads/`).

## Editing content

All copy lives as plain data at the top of **`build.py`** (`SITE`, `ABOUT`,
`TESTIMONIALS`, `PROJECTS`). Edit it, then regenerate the static pages:

```bash
python3 build.py
```

- **Add / remove / reorder projects** → edit the `PROJECTS` list.
- **Change which page renders show in a case study** → edit each project's
  `spreads` list (page numbers map to `assets/spreads/full/pNN.jpg`).
- **Card / next-project thumbnail** → each project's `hero` page number, or a
  custom crop via the optional `card` field (e.g. `assets/cards/streetbees.jpg`).

The page spreads are images of your original PDF layouts. To swap in different
imagery, replace the matching files in `assets/spreads/` (or `assets/cards/`).

## Good to know

- **Contact email** — `shannon@studiocontrary.com`. **LinkedIn** —
  `https://uk.linkedin.com/in/shannoncraver`. Phone is intentionally omitted.
- Add more social links in `build.py` → `SITE["socials"]`, then rebuild.

## Deploying

It's a static folder, so anything works — drop it on Netlify / Vercel /
Cloudflare Pages / GitHub Pages, or any web host. No server runtime needed.
Point the host's publish/root directory at `portfolio-website/`.
