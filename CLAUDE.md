# projectious.work Website

Company website built with Reflex (Python full-stack framework).

## Tech Stack

- **Framework:** Reflex 0.8.x (compiles to Next.js)
- **Styling:** Radix Themes via rx.theme(), Tailwind V4 plugin
- **Fonts:** Inter (Google Fonts)
- **Package manager:** uv

## Project Structure

```
website/
  rxconfig.py            # App config
  assets/                # Static files (favicon, robots.txt, sitemap)
  website/
    website.py           # Main app entry, page routes, SEO meta
    pages/               # Page modules (index, services, about, contact)
    components/          # Shared UI (navbar, footer, layout, section, cta_button)
    styles/              # Theme config (colors, fonts, spacing)
```

## Commands

- Dev server: `uv run reflex run`
- Production build: `uv run reflex export`

## Design Tokens

- Primary: navy `#0f172a`, slate `#1e293b`
- Accent: teal `#0d9488`, electric blue `#06b6d4`
- Max width: 1200px
- Radix accent_color: teal, gray_color: slate
