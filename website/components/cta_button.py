"""Styled call-to-action button."""

import reflex as rx


def cta_button(text: str, href: str, variant: str = "solid") -> rx.Component:
    """A styled CTA button that links to a page."""
    return rx.link(
        rx.button(
            text,
            size="3",
            variant=variant,
            cursor="pointer",
        ),
        href=href,
        underline="none",
    )
