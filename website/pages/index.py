"""Home page — the main landing page."""

import reflex as rx

from ..components import page_layout, section, cta_button
from ..styles.theme import NAVY, LIGHT_GRAY, SLATE, BORDER_RADIUS


def hero() -> rx.Component:
    return section(
        rx.heading(
            "IT Consulting for the AI Era",
            size="9",
            weight="bold",
            trim="both",
        ),
        rx.text(
            "Agentic AI. Agile. Cloud.",
            size="6",
            color_scheme="gray",
        ),
        rx.text(
            "We help organisations adopt AI-augmented workflows, "
            "ship faster with proven Agile practices, and build "
            "resilient cloud infrastructure.",
            size="4",
            color_scheme="gray",
            max_width="640px",
        ),
        rx.hstack(
            cta_button("Get in touch", "/contact"),
            cta_button("Our services", "/services", variant="outline"),
            spacing="4",
        ),
        padding_y="8em",
    )


def _pillar_card(icon: str, title: str, description: str, href: str) -> rx.Component:
    return rx.link(
        rx.card(
            rx.vstack(
                rx.icon(icon, size=32, color=rx.color("accent", 9)),
                rx.heading(title, size="5", weight="bold"),
                rx.text(description, size="3", color_scheme="gray"),
                spacing="3",
            ),
            width="100%",
            _hover={"box_shadow": "0 8px 30px rgba(0,0,0,0.08)"},
        ),
        href=href,
        underline="none",
        flex="1",
        min_width="280px",
    )


def pillars() -> rx.Component:
    return section(
        rx.text(
            "What we do",
            size="2",
            weight="bold",
            color=rx.color("accent", 9),
            text_transform="uppercase",
            letter_spacing="0.1em",
        ),
        rx.flex(
            _pillar_card(
                "bot",
                "Agentic AI Consulting",
                "Design and build multi-agent architectures, "
                "tool integrations, and evaluation frameworks "
                "that deliver measurable business outcomes.",
                "/services#agentic-ai",
            ),
            _pillar_card(
                "iteration-cw",
                "Agile Transformation",
                "Hands-on coaching that moves teams from "
                "ceremony theatre to genuine iterative delivery "
                "with real metrics.",
                "/services#agile",
            ),
            _pillar_card(
                "cloud",
                "Cloud Strategy",
                "Architecture reviews, migration planning, "
                "cost optimisation, and cloud-native patterns "
                "built for scale.",
                "/services#cloud",
            ),
            flex_wrap="wrap",
            spacing="5",
            width="100%",
        ),
        title="Three Pillars, One Mission",
        subtitle="Deep expertise across the technologies that matter most.",
        bg=LIGHT_GRAY,
    )


def credibility() -> rx.Component:
    return section(
        rx.text(
            "We don't just advise — we build. Our own company runs on "
            "AI-augmented workflows: autonomous agents handle project management, "
            "marketing strategy, coaching, and development. The tools we use "
            "are open source.",
            size="4",
            color_scheme="gray",
            max_width="720px",
        ),
        rx.link(
            rx.button(
                rx.icon("github", size=16),
                "View our open-source plugins",
                variant="outline",
                size="3",
            ),
            href="https://github.com/projectious-work/company-plugins",
            is_external=True,
            underline="none",
        ),
        title="Built with the Tools We Teach",
    )


def cta_strip() -> rx.Component:
    return rx.box(
        rx.box(
            rx.hstack(
                rx.vstack(
                    rx.heading("Ready to talk?", size="7", weight="bold", color="white"),
                    rx.text(
                        "Let's discuss how we can accelerate your next initiative.",
                        size="4",
                        color=rx.color("gray", 8),
                    ),
                    spacing="2",
                    flex="1",
                ),
                cta_button("Contact us", "/contact"),
                align="center",
                width="100%",
                flex_wrap="wrap",
                spacing="5",
            ),
            max_width="1200px",
            width="100%",
            margin_x="auto",
            padding_x="2em",
        ),
        width="100%",
        padding_y="5em",
        background=NAVY,
    )


def index_page() -> rx.Component:
    return page_layout(
        hero(),
        pillars(),
        credibility(),
        cta_strip(),
    )
