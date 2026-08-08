# projectious.work Hugo website v1 specification

Status: Proposed  
Target repository: `projectious-work/website`  
Coordinating issues:
[`internal#7`](https://github.com/projectious-work/internal/issues/7) and
[`internal#9`](https://github.com/projectious-work/internal/issues/9)

## 1. Authority and issue evaluation

This specification defines the implementation-ready replacement of the current
Reflex website with the canonical static Projectious site.

`internal#9` governs because it contains the current positioning,
career/commercial optionality, thesis model, deployment requirements, and
complete acceptance criteria. `internal#7` remains a valid earlier request and
contributes concrete migration, content, and taxonomy requirements. This
document resolves both into one target-repository specification.

Authority, from highest to most implementation-specific:

1. Projectious company policy and repository standards.
2. The
   [Positioning Baseline](https://docs.google.com/document/d/1QkRMK-Jo-Krd0zKZCzM2H92s6MC3j-5CqKD-rzwQXSs/edit).
3. The
   [Website Specification](https://docs.google.com/document/d/1SPqb3ChmXVJkzTQoXLTgnzmBY7mCy0yiKMc2ub2iVNM/edit).
4. The founding roadmap as commercial/career context, not as authority for
   unsupported public claims:
   [Gründungsfahrplan](https://docs.google.com/document/d/192x6iXjYZFpK4BgthZK20NJNBMTAQPD5RzFMYCv1v18/edit).
5. Current public repository evidence and the
   [GitHub organisation profile](https://github.com/projectious-work/.github/blob/main/profile/README.md).
6. The first-party theme contract specified by
   [`internal#8`](https://github.com/projectious-work/internal/issues/8).

Conflicts are not silently reconciled in copy. The positioning baseline and
website product specification govern public identity; repository evidence
governs project capability and maturity.

## 2. Product definition

Projectious is an independent initiative led by Bernhard Gerlach. The website
is its durable public home:

- a public workbench;
- an evidence-grounded project portfolio;
- a publication platform for articles and thesis-led pieces;
- a home for longer, versioned papers;
- the canonical narrative referenced from GitHub and professional channels;
- a restrained contact point;
- a foundation that can later expose validated advisory activity without
  redesigning or claiming that it exists today.

Primary thesis:

> Turning emerging technical capabilities into predictable, auditable
> delivery.

Secondary motif:

> Agentic AI. Agile. Cloud.

The motif describes interacting forces. It is not three services. Agentic AI
changes productive units and economics; Agile supplies iterative learning under
uncertainty; Cloud supplies programmable infrastructure; operating models,
governance, and accountability connect them to reliable delivery.

Preferred narrative:

> experience informs the questions; projects test the ideas.

## 3. Audiences and dual-use positioning

### Primary audiences

- future collaborators and potential clients evaluating the initiative's
  thinking and evidence;
- hiring managers evaluating Bernhard's established leadership experience and
  active technical/organisational exploration;
- practitioners reading articles, papers, and project evidence;
- open-source users evaluating a specific repository.

### Required impression

Visitors should understand within two minutes:

1. what Projectious is;
2. who leads it;
3. what is being investigated or built;
4. what evidence exists;
5. which claims and maturity limits apply.

The site must not imitate a multi-person consultancy or an impersonal lab.
Bernhard's Operations, Transformation, and Technical Program experience is
established background. Projectious's AI-oriented tools, experiments, and
theses are newer evidence and must not inherit unearned maturity from that
background.

Do not use “Founder & Principal Consultant” as the default v1 identity.

## 4. Goals

- Replace the current application stack with a simple Hugo static site.
- Make Work, Writing, theses, papers, and Bernhard's role legible.
- Ground every material capability/maturity claim in observable evidence.
- Use the first-party Projectious theme without creating local brand drift.
- Deliver accessible, responsive, fast light/dark experiences.
- Provide local static search and strong discovery metadata.
- Deploy predictably through Cloudflare Pages.
- Allow later commercial content to be activated through content/configuration.

## 5. Non-goals

- A services catalogue or conventional consultancy conversion site.
- A public “Product Studio” identity.
- Testimonials, client logos, case studies, metrics, certifications, or
  security/production claims without evidence and owner approval.
- CRM, marketing automation, accounts, database CMS, application server,
  newsletter system, or dynamic form backend.
- Cloudflare Functions/Workers in v1.
- A Python, Reflex, Next.js, Node, or npm production dependency.
- Filler articles, papers, projects, or theses.
- A website-local design system or copied theme source.

## 6. Technical architecture

```text
Git repository
    ↓
Hugo 0.157.0+ with pinned Projectious brand module
    ↓
static HTML + canonical CSS + minimal vanilla JavaScript + JSON search index
    ↓
Cloudflare Pages
    ↓
projectious.work
```

### Decisions

- Hugo is the only production site generator.
- The standard Hugo binary is sufficient; Extended may be used only if the
  accepted theme contract later requires it.
- The website imports `github.com/projectious-work/brand` as a Hugo module,
  pins an exact release in `go.mod`, and commits `go.sum`.
- Production commits Hugo's `_vendor/` snapshot so Cloudflare builds do not
  depend on live module resolution. Generated vendored files are never edited.
- No npm installation/build occurs.
- JavaScript is limited to the theme's navigation, colour preference, and
  static search enhancements.
- Content and data are Markdown/YAML with page bundles for owned resources.
- No GitHub Actions are added. Validation is local/manual.

## 7. Proposed repository structure

```text
archetypes/
assets/                         # site-specific approved resources only
config/
└── _default/
    ├── hugo.yaml
    ├── languages.yaml
    ├── menus.yaml
    ├── module.yaml
    ├── outputs.yaml
    └── params.yaml
content/
├── _index.md
├── work/
│   ├── _index.md
│   └── <slug>/
│       ├── index.md
│       └── <page resources>
├── writing/
│   ├── _index.md
│   ├── articles/
│   ├── theses/
│   └── papers/
├── about/
│   └── index.md
├── legal/
│   ├── imprint.md
│   └── privacy.md
└── now/                       # optional, omitted unless content is ready
data/
├── maturity.yaml
├── theses.yaml                # index/relationships, not theme logic
└── evidence-sources.yaml
static/
├── _headers
└── _redirects
go.mod
go.sum
_vendor/                       # generated pinned theme snapshot
scripts/
├── build.sh
├── serve.sh
├── check-content.sh
├── check-links.sh
└── verify.sh
spec/
```

There is no public `services/` section in v1. Optional future advisory content
may be prepared only as draft content outside published menus and builds.

## 8. Information architecture and URLs

Top-level navigation:

- `/` — Home
- `/work/` — Work
- `/writing/` — Writing
- `/about/` — About

`/now/` is added only when an owner-reviewed page contains useful current
information and has an explicit maintenance expectation.

Writing URLs:

- `/writing/articles/<slug>/`
- `/writing/theses/<slug>/`
- `/writing/papers/<slug>/`

Legal pages may live below `/legal/` but are linked from the footer. No
separate Contact page is required; About and the footer provide quiet email,
LinkedIn, GitHub, and other approved profile links.

URLs remain stable after publication. Renames add Hugo aliases and Cloudflare
redirects where necessary. Slugs are lowercase, semantic, and date-free unless
date is essential to the content identity.

## 9. Page requirements

### 9.1 Home

Sequence:

1. hero with the primary thesis;
2. concise independent-initiative explanation;
3. 3–4 selected evidence-grounded Work entries;
4. selected theses/current ideas explicitly presented as being tested;
5. latest substantive Writing;
6. concise Bernhard identity block;
7. restrained contact/profile/footer links.

The page contains no generic service cards, “ready to transform” language,
consultation booking, unsupported “we help organisations” claim, or
fabricated social proof.

### 9.2 Work

Work is an evidence portfolio, not a live GitHub directory. Every published
entry answers:

- What problem or question does this work investigate?
- What exists now?
- What does the evidence demonstrate?
- What does it not demonstrate?
- Where can a visitor inspect or reproduce evidence?
- Which writing or theses relate to it?

The initial release contains approximately 4–6 entries with current evidence.
The current organisation hierarchy provides the starting candidates:

| Project | Initial public class | Treatment |
|---|---|---|
| aibox | Usable project — active development | Primary evidence |
| processkit | Usable project — active, pre-1.0 | Primary evidence with version caveat |
| ai-market-research | Applied research — maintained | Research evidence |
| kubeclaw | Working prototype — not production ready | Explicit learning/prototype story |
| ainfra | Experiment or current repository wording | Publish only after evidence review |
| kaits | Experiment or current repository wording | Do not feature prominently without stronger proof |
| brand | Supporting asset — maintained | Supporting infrastructure |

Repository README/release/test evidence at implementation time overrides this
planning table. A repository is not promoted merely because it exists.

### 9.3 Writing

“Writing” is the umbrella. It includes:

- Articles: substantial analysis and essays.
- Theses: explicit propositions under testing/refinement.
- Papers: longer versioned publications.

The index supports curated/latest views and topic filtering without becoming a
tag cloud. Papers infrastructure may ship empty; no filler paper is created.
At least one article ships only when suitable reviewed content exists.

### 9.4 About

The page explains Projectious and Bernhard together:

- Projectious as the initiative and evidence/publication container;
- Bernhard as the person leading it;
- established Operations, Transformation, and Technical Program experience;
- newer AI-assisted delivery, agent-infrastructure, and open-source exploration;
- the evidence-first working method;
- restrained profile/contact links.

It must not claim established consulting scale, a team of autonomous employees,
client engagement history, global service availability, speaking credentials,
or other facts without explicit evidence and owner approval.

### 9.5 Legal/privacy

The implementation supplies an owner-reviewed German imprint and privacy
notice appropriate to the deployed services. Analytics remains disabled by
default. If Cloudflare Web Analytics is enabled, its data handling and privacy
text are reviewed before deployment. No other tracker is included by default.

## 10. Content contracts

### 10.1 Common

```yaml
title: Page title
description: One-sentence factual summary
date: 2026-08-08
lastmod: 2026-08-08
draft: false
topics: [agent-workflows]
image: cover.png
noindex: false
```

Dates are content metadata, not automatically displayed on timeless pages.
Draft and noindex content is excluded from search, feeds where appropriate,
sitemap, and production lists.

### 10.2 Work

```yaml
title: Example project
description: Concise evidence-grounded description
purpose: Question or problem explored
maturity: working-prototype
maturity_label: Working prototype
repository: https://github.com/projectious-work/example
demonstrates:
  - Narrow observable capability
evidence:
  - label: Repository
    url: https://github.com/projectious-work/example
  - label: Release
    url: https://github.com/projectious-work/example/releases/tag/v0.1.0
limitations:
  - Not production ready
related:
  writing: []
  theses: []
featured: false
evidence_reviewed: 2026-08-08
```

Required: purpose, maturity, demonstrates, evidence, limitations, and evidence
review date. Empty limitations require explicit owner review; omission is not
interpreted as “no limitations.”

### 10.3 Articles

```yaml
title: Article title
description: Summary
authors: [Bernhard Gerlach]
date: 2026-08-08
lastmod: 2026-08-08
topics: [governance]
related:
  work: []
  theses: []
```

### 10.4 Theses

```yaml
title: The proposition
description: Careful summary
authors: [Bernhard Gerlach]
status: testing
version: 0.1
date: 2026-08-08
lastmod: 2026-08-08
evidence_for: []
evidence_against: []
related:
  work: []
  writing: []
```

Allowed lifecycle: `proposed`, `testing`, `refined`, `retired`. Theses
are propositions to test, not predictions presented as settled facts.

### 10.5 Papers

```yaml
title: Paper title
subtitle: Optional subtitle
description: Abstract-length summary
authors: [Bernhard Gerlach]
paper:
  status: working-paper
  version: 0.1
  number: PW-001
  abstract: Abstract
  pdf: paper.pdf
date: 2026-08-08
lastmod: 2026-08-08
topics: [operating-models]
related:
  work: []
  theses: []
references: []
```

HTML is canonical. An optional PDF is a matching versioned page resource.
Allowed status values are `working-paper`, `reviewed`, `revised`, and
`retired`.

## 11. Thesis model

The positioning baseline's current eight theses are initial content, not theme
code:

1. the minimum viable enterprise is changing;
2. software-quality economics are changing;
3. the build-versus-buy boundary will move;
4. Software of One;
5. AI adoption is an operating-model problem;
6. governance increasingly moves into the system;
7. organisations become more programmable;
8. AI changes what is economically viable, not only what can be automated.

Each becomes a reviewed thesis page only when it has a careful proposition,
status, version, limitations, and evidence plan. `data/theses.yaml` holds
stable slugs and curated relationship metadata; page content carries the
argument. Work and Writing reference thesis slugs, and validation fails broken
references.

Theses appear under Writing and in curated Home/Work relationships. They do not
require a top-level navigation item.

## 12. Topics and relationships

Use one controlled `topics` taxonomy. Initial candidates:

- `ai-operating-models`
- `governance-accountability`
- `agent-workflows`
- `reproducible-delivery`
- `ai-cloud-infrastructure`
- `organisational-design`
- `transformation-adoption`
- `sourcing`
- `operational-excellence`

The initial set is reduced during content preparation if a topic has no useful
navigation value. Authors do not invent synonyms in front matter. Relationships
among work, articles, theses, and papers use stable slugs and are checked
bidirectionally where the model requires it.

## 13. Evidence and claims policy

Every material public claim belongs to one class:

- source-backed current fact;
- observable repository/release/test evidence;
- clearly attributed professional experience;
- explicitly labelled thesis/hypothesis;
- owner-approved positioning statement.

The implementation maintains `data/evidence-sources.yaml` with source URL,
repository/ref where applicable, review date, and affected content slugs.
Content checks flag stale evidence-review dates according to an owner-defined
review interval but do not automatically alter claims.

Prohibited without evidence and owner approval:

- customer adoption or outcomes;
- production operation or enterprise readiness;
- security assurance or compliance;
- support commitments;
- scale, performance, ROI, delivery-speed, or defect claims;
- client availability, speaking record, team size, or geographic service claims;
- generated testimonials, logos, screenshots, metrics, or case studies.

AI-assisted copy receives the same source and owner-review requirements as
human-written copy.

## 14. Current-site migration inventory

| Current material | Decision | Treatment |
|---|---|---|
| Reflex/Python/Next.js stack | Discard | Replace with Hugo/static output |
| Page routes and component code | Discard | Theme owns layout behavior |
| Navbar/footer interaction ideas | Adapt | Re-express through canonical theme |
| “Agentic AI. Agile. Cloud.” | Adapt | Conceptual motif, not service structure |
| GitHub/open-source evidence idea | Adapt | Use evidence-bearing Work model |
| Bernhard as visible leader | Reuse/adapt | Separate established experience from experiments |
| “IT Consulting for the AI Era” | Discard | Replace with current primary thesis |
| “Three Pillars, One Mission” | Discard | Not the information architecture |
| Service cards and Services page | Discard | No v1 services section |
| “We help organisations…” | Discard | Unsupported established-offer claim |
| Agentic AI/Agile/Cloud deliverable lists | Discard | Unsupported productized services |
| “Founder & Principal Consultant” | Discard | Not default v1 identity |
| “How we work with clients” | Discard | Implies established engagements |
| CTA strips/contact conversion copy | Discard | Use restrained links |
| Email, LinkedIn, GitHub links | Reuse after verification | Place in About/footer |
| Current About intent | Adapt substantially | Initiative + Bernhard + evidence |
| Speaking/writing claims | Replace | Publish only observable writing/evidence |
| NAVY/SLATE/teal/electric/Inter theme | Discard | Noncanonical; consume brand module |
| favicon/logo files | Replace/review | Consume canonical brand assets |
| static robots/sitemap | Discard | Generate/configure through Hugo |

No current copy is migrated without source and positioning review.

## 15. Theme integration boundary

The brand module owns:

- tokens, typography, logo/favicons, CSS, light/dark behavior;
- base/list/single/404 layouts and generic Work/Article/Thesis/Paper layouts;
- header/footer/navigation, search UI/index contract, metadata and feeds;
- generic cards, evidence, limitations, status, related-content, figures,
  tables, code, callouts, and other authoring primitives.

The website owns:

- truthful content and maturity vocabulary;
- navigation/menu configuration and curated selections;
- controlled topics, thesis identities, Work relationships;
- site title/description/base URL/profile links;
- legal/privacy text, Cloudflare configuration, redirects, and deployment;
- rare site-specific layouts justified by a content requirement.

The website does not copy theme templates or token values by default. If an
override is unavoidable, it is documented with upstream rationale and covered
by an upgrade check.

Upgrade procedure:

1. update the exact brand module version;
2. inspect brand/theme release notes;
3. regenerate `go.sum` and `_vendor/`;
4. run full local verification in both modes;
5. inspect visual/content diffs;
6. commit the version and generated snapshot together.

## 16. Search, modes, accessibility, and performance

The theme provides system/light/dark modes and the Hugo-generated JSON search
index. Website configuration enables both.

Search includes Home-relevant ordinary pages, Work, Articles, Theses, and
Papers. It excludes drafts, noindex/legal pages where configured, and private
metadata. Search is keyboard accessible and has a normal `/search/?q=` URL.

Targets:

- WCAG 2.2 AA;
- semantic landmarks and headings;
- skip link, visible focus, keyboard navigation/search/mode control;
- reduced-motion support;
- meaningful alt text and responsive images with dimensions;
- no default third-party requests;
- no blocking third-party scripts;
- theme CSS/JS budgets inherited from the theme specification;
- representative homepage local Lighthouse scores of at least 95 in
  performance, accessibility, best practices, and SEO.

## 17. SEO and discovery

- canonical `baseURL` and per-page canonical URLs;
- sitemap and appropriate RSS/Atom feeds;
- generated robots policy;
- useful titles and descriptions;
- OpenGraph/social metadata with canonical brand assets;
- Article/Person/CreativeWork or other accurate JSON-LD, avoiding Organization
  claims that imply unsupported company scale;
- semantic URLs and aliases/redirects;
- useful branded 404 with search;
- social-preview generation or curated assets with provenance.

Bernhard may be represented as a Person. Projectious may be described as an
independent initiative; structured metadata must not silently upgrade it to an
established consulting organisation.

## 18. Cloudflare Pages deployment

### Production

- Connected repository: `projectious-work/website`.
- Production branch: `main`.
- Build command: `./scripts/build.sh`.
- Output directory: `public`.
- Exact Hugo version: set through the Cloudflare build environment and mirrored
  in repository documentation/config.
- Module source: committed `_vendor/`; production build performs no module
  update.
- Custom domains: `projectious.work` canonical; `www` redirects to the
  canonical host unless owner policy selects the reverse.
- Only nonsecret build configuration is present by default.

Cloudflare preview deployments are allowed for pull-request/branch review but
must be treated as public, use `noindex`, and contain no draft/private content.

### Headers

`static/_headers` defines and verifies at least:

- `X-Content-Type-Options: nosniff`;
- `Referrer-Policy: strict-origin-when-cross-origin`;
- `Permissions-Policy` denying unused capabilities;
- a content security policy derived from actual same-origin assets;
- frame protection through CSP `frame-ancestors`;
- appropriate cache policies for fingerprinted and HTML assets.

The CSP is tested against search, mode switching, previews, and any approved
analytics. It is not weakened for hypothetical future integrations.

### Verification and rollback

After deployment:

- verify canonical and `www` behavior, TLS, headers, robots, sitemap, feeds,
  search, mode switching, 404, and key page links;
- record deployed source commit and theme version;
- retain the last known-good Cloudflare deployment;
- rollback through Cloudflare deployment rollback, then repair `main` through
  the normal reviewed Git process.

Cloudflare Web Analytics is the only preferred optional v1 analytics path. It
requires explicit owner enablement and privacy review.

## 19. Local validation

No GitHub Actions are added. Required commands:

```bash
./scripts/serve.sh
./scripts/build.sh
./scripts/check-content.sh
./scripts/check-links.sh
./scripts/verify.sh
```

`verify.sh` is the canonical aggregate and covers:

- clean production Hugo build with warnings treated as errors;
- exact module/vendor identity and no uncommitted vendor drift;
- no npm, Python, Reflex, or unexpected production dependency;
- internal/external links, redirects, canonical URLs, sitemap, feeds, and 404;
- front-matter schema, controlled topics/statuses, relationships, and slugs;
- evidence-source presence, limitation fields, and review dates;
- prohibited/unsupported claim review patterns as a warning plus human review;
- draft/noindex exclusion from production lists, search, sitemap, and feeds;
- search index schema and representative query fixtures;
- HTML semantics, accessibility, both colour modes, keyboard interactions;
- contrast, responsive layouts, images/alt text, and performance budgets;
- CSP/security headers and absence of unexpected third-party requests;
- legal/privacy pages and required footer links;
- clean deployment build from the committed vendor snapshot.

The implementation PR includes a manual review checklist for Home, Work,
Writing, thesis, paper, About, search, 404, mobile, and both colour modes.

## 20. Migration strategy

1. **Prepare foundation on a topic branch:** Hugo config, pinned brand module,
   vendoring, scripts, empty content structure, Cloudflare files.
2. **Build content model:** schemas/checks, controlled maturity/topics, evidence
   source map, relationships, archetypes.
3. **Author minimum credible content:** Home, About, legal/privacy, 4–6
   reviewed Work entries, Writing structure, reviewed theses, and article only
   if ready.
4. **Validate previews:** accessibility, responsive/mode/search, evidence and
   claim review, links, metadata, and headers.
5. **Cut over:** preserve required URLs with redirects, configure domains,
   deploy, run verification, and retain rollback.
6. **Retire Reflex:** remove Python/Reflex/Next.js code and obsolete assets only
   after the Hugo production deployment is accepted.

Do not run both stacks as independently evolving public sources. The cutover PR
must make the canonical source clear.

## 21. Staged commercial activation

V1 publishes no productized services and makes no established availability
claim. Quiet contact links are sufficient.

Future advisory/assessment/fractional content may be activated only when:

- an owner-approved offering and evidence exist;
- claims, availability, legal, and career-positioning implications are reviewed;
- content is introduced through ordinary pages/configuration;
- navigation and homepage modules are deliberately enabled;
- the change does not relabel historical experiments as client outcomes.

Latent drafts may exist for planning but are excluded from production output,
search, feeds, and preview deployments. “Product Studio” remains a
hypothesis.

## 22. Editorial/channel model

```text
project or experiment
    ↓
observation or thesis
    ↓
professional-channel discussion
    ↓
canonical website article
    ↓
mature concept or versioned paper
```

The website is canonical editorial storage. GitHub is technical evidence.
LinkedIn is professional distribution/discussion. XING is a concise
professional/business adaptation. Social posts link back to canonical content;
they do not become the sole durable copy.

## 23. Implementation phases

1. Static foundation and theme pin.
2. Content contracts, evidence policy, and validation.
3. Home/About/legal and Work portfolio.
4. Writing, theses, papers, relationships, and search.
5. Accessibility, performance, SEO, headers, and deployment rehearsal.
6. Owner content/claim review, production cutover, and Reflex retirement.

Each phase is independently reviewable and keeps production claims fail-closed.

## 24. Acceptance criteria

- [ ] Projectious is consistently an independent initiative led by Bernhard.
- [ ] Current positioning and website source documents are represented without
      unsupported expansion.
- [ ] Reflex/Python/Next.js and noncanonical theme values are retired.
- [ ] Hugo builds static output with no npm production step.
- [ ] The exact Projectious brand/theme release is pinned and vendored.
- [ ] Home, Work, Writing/Articles/Theses/Papers, About, legal, search, and 404
      meet their content contracts.
- [ ] Approximately 4–6 Work entries have current evidence and limitations.
- [ ] Current theses are represented as propositions under test, not facts.
- [ ] No services catalogue, fabricated content, or unsupported maturity/client
      claim is published.
- [ ] Bernhard's established experience and Projectious experiments are clearly
      distinguished.
- [ ] Theme/site ownership boundaries and upgrade procedure are enforced.
- [ ] Light/dark/system, keyboard, responsive, WCAG AA, performance, and search
      requirements have local evidence.
- [ ] Cloudflare Pages production, previews, headers, verification, and rollback
      are documented and rehearsed.
- [ ] Legal/privacy and optional analytics have owner review.
- [ ] No GitHub Actions are added.
- [ ] Future commercial content can be activated without redesign but remains
      unpublished until separately approved.

## 25. Owner-review gates before implementation completion

The following require explicit owner review and cannot be inferred:

- final public biography and career/commercial wording;
- every initial Work description, maturity, evidence, and limitation;
- which theses are sufficiently formed to publish;
- initial article readiness;
- legal/imprint/privacy text;
- whether Cloudflare Web Analytics is enabled;
- production domain/canonical-host choice and cutover timing;
- any future commercial/advisory visibility.

No unresolved technical architecture prevents implementation. If the brand
theme contract changes before implementation, this specification is updated by
reviewed PR rather than silently diverging.
