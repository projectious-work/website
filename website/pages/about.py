"""About page — company, principal, and approach."""

import reflex as rx

from ..components import page_layout, section, cta_button
from ..styles.theme import LIGHT_GRAY


def company() -> rx.Component:
    return section(
        rx.text(
            "projectious.work is an IT consulting company specialising in "
            "Agentic AI, Agile transformation, and Cloud strategy. Founded in "
            "2026, we operate with a distinctive model: a senior principal "
            "consultant supported by a team of AI agents that handle project "
            "management, marketing, coaching, and development tasks.",
            size="4",
            color_scheme="gray",
            max_width="720px",
        ),
        rx.text(
            "This isn't a gimmick — it's a proof of concept. The same "
            "AI-augmented workflows we use internally are what we bring "
            "to our clients. We understand agent architectures because we "
            "live inside one every day.",
            size="4",
            color_scheme="gray",
            max_width="720px",
        ),
        title="The Company",
        subtitle="AI-augmented consulting, built from the ground up.",
        padding_y="5em",
    )


def principal() -> rx.Component:
    return section(
        rx.text(
            "Bernhard Gerlach brings over 15 years of experience spanning "
            "engineering leadership, people management, analytics, and "
            "strategic consulting. His career includes leading cross-functional "
            "teams, driving Agile adoption across organisations, and "
            "architecting cloud-native platforms at scale.",
            size="4",
            color_scheme="gray",
            max_width="720px",
        ),
        rx.flex(
            rx.badge("People Management", variant="surface", size="3"),
            rx.badge("Strategic Thinking", variant="surface", size="3"),
            rx.badge("Analytics & Data", variant="surface", size="3"),
            rx.badge("Stage Speaking", variant="surface", size="3"),
            rx.badge("Agile Coaching", variant="surface", size="3"),
            rx.badge("Cloud Architecture", variant="surface", size="3"),
            flex_wrap="wrap",
            spacing="2",
        ),
        rx.link(
            rx.button(
                rx.icon("linkedin", size=16),
                "Connect on LinkedIn",
                variant="outline",
                size="3",
            ),
            href="https://www.linkedin.com/in/bege/",
            is_external=True,
            underline="none",
        ),
        title="The Principal",
        subtitle="Bernhard Gerlach — Founder & Principal Consultant",
        bg=LIGHT_GRAY,
    )


def approach() -> rx.Component:
    return section(
        rx.flex(
            _approach_card(
                "cpu",
                "AI-Augmented Delivery",
                "Every engagement leverages AI tools — from research and "
                "analysis to code generation and documentation. You get "
                "senior-level thinking at startup speed.",
            ),
            _approach_card(
                "clipboard-list",
                "Structured Methodology",
                "Clear backlogs, defined acceptance criteria, regular standups, "
                "and transparent progress tracking. No black boxes, no surprises.",
            ),
            _approach_card(
                "zap",
                "Rapid Iteration",
                "Short feedback loops, working deliverables from week one, "
                "and continuous refinement. We ship early and adjust based on "
                "real results.",
            ),
            flex_wrap="wrap",
            spacing="5",
            width="100%",
        ),
        title="The Approach",
        subtitle="How we work with clients.",
    )


def _approach_card(icon: str, title: str, description: str) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.icon(icon, size=28, color=rx.color("accent", 9)),
            rx.heading(title, size="4", weight="bold"),
            rx.text(description, size="3", color_scheme="gray"),
            spacing="3",
        ),
        flex="1",
        min_width="280px",
    )


def speaking() -> rx.Component:
    return section(
        rx.text(
            "Bernhard Gerlach is an experienced speaker and writer on topics spanning "
            "AI adoption, Agile leadership, and cloud strategy. Conference "
            "talks and LinkedIn articles are in the works — watch this space.",
            size="4",
            color_scheme="gray",
            max_width="720px",
        ),
        rx.hstack(
            rx.link(
                rx.button(
                    rx.icon("linkedin", size=16),
                    "Follow on LinkedIn",
                    variant="outline",
                    size="3",
                ),
                href="https://www.linkedin.com/in/bege/",
                is_external=True,
                underline="none",
            ),
            spacing="3",
        ),
        title="Speaking & Writing",
        bg=LIGHT_GRAY,
    )


def about_page() -> rx.Component:
    return page_layout(
        company(),
        principal(),
        approach(),
        speaking(),
    )
