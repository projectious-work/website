# projectious.work

Company website for [projectious.work](https://projectious.work) — IT consulting for the AI era, specialising in Agentic AI, Agile transformation, and Cloud strategy.

Built with [Reflex](https://reflex.dev), a Python full-stack web framework.

## Pages

| Route | Description |
|---|---|
| `/` | Landing page — hero, service pillars, credibility, CTA |
| `/services` | Three consulting pillars with deliverables |
| `/about` | Company, principal profile, approach, speaking |
| `/contact` | Email, LinkedIn, GitHub — direct contact |

## Getting Started

### Prerequisites

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) (Python package manager)
- Node.js 20+ (Reflex compiles to Next.js)
- `unzip` (required by bun, which Reflex uses internally)

### Setup

```bash
git clone https://github.com/projectious-work/website.git
cd website
uv sync
```

### Development

```bash
uv run reflex run
```

Opens at [http://localhost:3000](http://localhost:3000). The dev server hot-reloads on file changes.

### Production Export

```bash
uv run reflex export
```

Produces a static build in the `.web` directory.

## Project Structure

```
website/
  rxconfig.py              # Reflex app configuration
  assets/                  # Static files (favicon, robots.txt, sitemap.xml)
  website/
    website.py             # App entry point, page routes, SEO meta tags
    pages/                 # Page modules (index, services, about, contact)
    components/            # Shared UI (navbar, footer, layout, section, cta_button)
    styles/                # Theme configuration (colours, fonts, spacing)
```

## Contributing

This is the website for a small consulting company, so contributions are primarily internal. That said, if you spot a bug or have a suggestion:

1. Fork the repo
2. Create a feature branch (`git checkout -b fix/description`)
3. Make your changes and verify with `uv run reflex run`
4. Commit with a descriptive message referencing the change
5. Open a pull request

## License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.
