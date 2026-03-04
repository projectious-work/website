"""Page layout wrapper — navbar + content + footer."""

import reflex as rx

from .navbar import navbar
from .footer import footer


def page_layout(*children) -> rx.Component:
    """Wrap page content with navbar and footer."""
    return rx.box(
        navbar(),
        rx.box(
            *children,
            flex="1",
            width="100%",
        ),
        footer(),
        display="flex",
        flex_direction="column",
        min_height="100vh",
        width="100%",
    )
