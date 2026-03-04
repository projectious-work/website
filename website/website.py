"""projectious.work — company website."""

import reflex as rx

from .styles.theme import get_theme
from .pages.index import index_page
from .pages.services import services_page
from .pages.about import about_page
from .pages.contact import contact_page


app = rx.App(
    theme=get_theme(),
    style={
        "font_family": "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif",
    },
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap",
    ],
)

# Home
app.add_page(
    index_page,
    route="/",
    title="projectious.work — Agentic AI, Agile & Cloud Consulting",
    description="IT consulting for the AI era. We help organisations adopt agentic AI, transform delivery with Agile, and build resilient cloud infrastructure.",
    meta=[
        {"property": "og:title", "content": "projectious.work — Agentic AI, Agile & Cloud Consulting"},
        {"property": "og:description", "content": "IT consulting for the AI era. Agentic AI, Agile transformation, and Cloud strategy."},
        {"property": "og:type", "content": "website"},
        {"property": "og:url", "content": "https://projectious.work"},
        {"property": "og:image", "content": "https://projectious.work/og-image.png"},
    ],
)

# Services
app.add_page(
    services_page,
    route="/services",
    title="Services — projectious.work",
    description="Agentic AI consulting, Agile transformation coaching, and Cloud strategy. Concrete deliverables, measurable outcomes.",
    meta=[
        {"property": "og:title", "content": "Services — projectious.work"},
        {"property": "og:description", "content": "Agentic AI, Agile transformation, and Cloud strategy consulting."},
    ],
)

# About
app.add_page(
    about_page,
    route="/about",
    title="About — projectious.work",
    description="AI-augmented IT consulting founded by Bernhard Gerlach. Senior expertise in Agentic AI, Agile, and Cloud.",
    meta=[
        {"property": "og:title", "content": "About — projectious.work"},
        {"property": "og:description", "content": "Meet the team behind projectious.work — AI-augmented consulting."},
    ],
)

# Contact
app.add_page(
    contact_page,
    route="/contact",
    title="Contact — projectious.work",
    description="Get in touch with projectious.work. Email, LinkedIn, or GitHub — no forms, no gatekeepers.",
    meta=[
        {"property": "og:title", "content": "Contact — projectious.work"},
        {"property": "og:description", "content": "Reach out to discuss your next AI, Agile, or Cloud initiative."},
    ],
)
