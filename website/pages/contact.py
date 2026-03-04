"""Contact page — email, LinkedIn, GitHub."""

import reflex as rx

from ..components import page_layout, section
from ..styles.theme import LIGHT_GRAY


def _contact_card(icon: str, label: str, value: str, href: str) -> rx.Component:
    return rx.link(
        rx.card(
            rx.hstack(
                rx.icon(icon, size=28, color=rx.color("accent", 9)),
                rx.vstack(
                    rx.text(label, size="2", weight="bold", color_scheme="gray"),
                    rx.text(value, size="3", weight="medium"),
                    spacing="1",
                ),
                spacing="4",
                align="center",
            ),
            width="100%",
            _hover={"box_shadow": "0 4px 20px rgba(0,0,0,0.06)"},
        ),
        href=href,
        is_external=True if href.startswith("http") else False,
        underline="none",
        width="100%",
        max_width="480px",
    )


def contact_page() -> rx.Component:
    return page_layout(
        section(
            rx.text(
                "We'd love to hear about your project. Reach out directly — "
                "no forms, no gatekeepers.",
                size="4",
                color_scheme="gray",
                max_width="640px",
            ),
            title="Get in Touch",
            subtitle="Let's start a conversation.",
            padding_y="5em",
        ),
        section(
            rx.vstack(
                _contact_card(
                    "mail",
                    "Email",
                    "info@projectious.work",
                    "mailto:info@projectious.work",
                ),
                _contact_card(
                    "linkedin",
                    "LinkedIn",
                    "linkedin.com/in/bege",
                    "https://www.linkedin.com/in/bege/",
                ),
                _contact_card(
                    "github",
                    "GitHub",
                    "github.com/projectious-work",
                    "https://github.com/projectious-work",
                ),
                spacing="4",
                width="100%",
                align_items="start",
            ),
            padding_y="2em",
        ),
        section(
            rx.callout(
                "Based in Germany, serving clients globally. "
                "Available for remote engagements and on-site consulting "
                "in the DACH region.",
                icon="globe",
                size="3",
            ),
            padding_y="2em",
        ),
    )
