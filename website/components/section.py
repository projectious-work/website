"""Reusable full-width section component."""

import reflex as rx

from ..styles.theme import MAX_WIDTH, SECTION_PADDING_Y


def section(
    *children,
    title: str = "",
    subtitle: str = "",
    bg: str = "transparent",
    **kwargs,
) -> rx.Component:
    """A full-width section with optional title, subtitle, and content."""
    header_items = []
    if title:
        header_items.append(
            rx.heading(title, size="7", weight="bold", trim="both")
        )
    if subtitle:
        header_items.append(
            rx.text(subtitle, size="4", color_scheme="gray")
        )

    # Allow kwargs to override defaults
    box_props = dict(
        width="100%",
        padding_y=SECTION_PADDING_Y,
        background=bg,
    )
    box_props.update(kwargs)

    return rx.box(
        rx.box(
            rx.vstack(
                *header_items,
                *children,
                spacing="5",
                width="100%",
            ),
            max_width=MAX_WIDTH,
            width="100%",
            margin_x="auto",
            padding_x="2em",
        ),
        **box_props,
    )
