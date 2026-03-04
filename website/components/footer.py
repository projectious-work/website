"""Site footer."""

import reflex as rx

from ..styles.theme import MAX_WIDTH, NAVY


def footer() -> rx.Component:
    return rx.box(
        rx.box(
            rx.vstack(
                rx.hstack(
                    rx.text(
                        "projectious.work",
                        size="3",
                        weight="bold",
                        color="white",
                    ),
                    rx.spacer(),
                    rx.hstack(
                        rx.link(
                            rx.icon("linkedin", size=20, color="white"),
                            href="https://www.linkedin.com/in/bernhardglueck/",
                            is_external=True,
                        ),
                        rx.link(
                            rx.icon("github", size=20, color="white"),
                            href="https://github.com/projectious-work",
                            is_external=True,
                        ),
                        rx.link(
                            rx.icon("mail", size=20, color="white"),
                            href="mailto:hello@projectious.work",
                        ),
                        spacing="4",
                    ),
                    width="100%",
                    align="center",
                ),
                rx.separator(color_scheme="gray", opacity=0.3),
                rx.text(
                    "\u00a9 2026 projectious.work. All rights reserved.",
                    size="2",
                    color=rx.color("gray", 8),
                ),
                spacing="4",
                width="100%",
            ),
            max_width=MAX_WIDTH,
            width="100%",
            margin_x="auto",
            padding_x="2em",
        ),
        width="100%",
        padding_y="3em",
        background=NAVY,
    )
