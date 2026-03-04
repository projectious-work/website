"""Sticky top navigation bar."""

import reflex as rx

from ..styles.theme import MAX_WIDTH


NAV_LINKS = [
    ("Services", "/services"),
    ("About", "/about"),
    ("Contact", "/contact"),
]


def nav_link(text: str, href: str) -> rx.Component:
    return rx.link(
        text,
        href=href,
        size="3",
        weight="medium",
        color_scheme="gray",
        underline="none",
        _hover={"color": rx.color("accent", 11)},
    )


def desktop_nav() -> rx.Component:
    return rx.hstack(
        *[nav_link(text, href) for text, href in NAV_LINKS],
        spacing="6",
        display=["none", "none", "flex"],
    )


def mobile_menu() -> rx.Component:
    return rx.box(
        rx.menu.root(
            rx.menu.trigger(
                rx.icon_button(
                    rx.icon("menu"),
                    variant="ghost",
                    size="3",
                    color_scheme="gray",
                ),
            ),
            rx.menu.content(
                *[
                    rx.menu.item(
                        rx.link(text, href=href, underline="none", color_scheme="gray"),
                    )
                    for text, href in NAV_LINKS
                ],
            ),
        ),
        display=["block", "block", "none"],
    )


def navbar() -> rx.Component:
    return rx.box(
        rx.box(
            rx.hstack(
                rx.link(
                    rx.text(
                        "projectious.work",
                        size="4",
                        weight="bold",
                        color_scheme="gray",
                    ),
                    href="/",
                    underline="none",
                ),
                rx.spacer(),
                desktop_nav(),
                mobile_menu(),
                align="center",
                width="100%",
            ),
            max_width=MAX_WIDTH,
            width="100%",
            margin_x="auto",
            padding_x="2em",
        ),
        position="sticky",
        top="0",
        z_index="50",
        width="100%",
        padding_y="1em",
        backdrop_filter="blur(12px)",
        background="rgba(255, 255, 255, 0.85)",
        border_bottom=f"1px solid {rx.color('gray', 4)}",
    )
