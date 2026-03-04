"""Services page — three consulting pillars."""

import reflex as rx

from ..components import page_layout, section, cta_button
from ..styles.theme import LIGHT_GRAY


def _deliverable_list(*items: str) -> rx.Component:
    return rx.vstack(
        *[
            rx.hstack(
                rx.icon("check", size=16, color=rx.color("accent", 9)),
                rx.text(item, size="3"),
                spacing="2",
                align="center",
            )
            for item in items
        ],
        spacing="2",
        align_items="start",
    )


def agentic_ai() -> rx.Component:
    return section(
        rx.text(
            "Large language models are powerful, but raw API calls don't "
            "solve business problems. We design and implement agent systems "
            "that integrate into your existing workflows and deliver "
            "measurable ROI.",
            size="4",
            color_scheme="gray",
            max_width="720px",
        ),
        rx.heading("Deliverables", size="4", weight="bold"),
        _deliverable_list(
            "Multi-agent architecture design and implementation",
            "Tool and API integration for autonomous agent workflows",
            "Evaluation frameworks and quality benchmarks",
            "Prompt engineering and LLM selection strategy",
            "RAG pipelines and knowledge management systems",
            "Production deployment with monitoring and guardrails",
        ),
        cta_button("Discuss your AI project", "/contact"),
        title="Agentic AI Consulting",
        subtitle="From prototype to production-grade agent systems.",
        id="agentic-ai",
    )


def agile() -> rx.Component:
    return section(
        rx.text(
            "Most Agile transformations fail because they focus on ceremony "
            "instead of outcomes. We embed with your teams, coach through "
            "real sprints, and leave behind practices that stick — because "
            "they actually work.",
            size="4",
            color_scheme="gray",
            max_width="720px",
        ),
        rx.heading("Deliverables", size="4", weight="bold"),
        _deliverable_list(
            "Sprint structure design and hands-on coaching",
            "Retrospective facilitation and continuous improvement",
            "Metrics that matter: cycle time, throughput, quality",
            "Team topology and collaboration pattern reviews",
            "Stakeholder alignment and roadmap workshops",
            "Agile leadership coaching for engineering managers",
        ),
        cta_button("Transform your delivery", "/contact"),
        title="Agile Transformation",
        subtitle="Practical coaching that moves teams from ceremony to delivery.",
        bg=LIGHT_GRAY,
        id="agile",
    )


def cloud() -> rx.Component:
    return section(
        rx.text(
            "Cloud migrations stall when architecture decisions are made in "
            "isolation. We bring a systems perspective — aligning cost, "
            "reliability, and velocity so your platform enables the business "
            "instead of constraining it.",
            size="4",
            color_scheme="gray",
            max_width="720px",
        ),
        rx.heading("Deliverables", size="4", weight="bold"),
        _deliverable_list(
            "Cloud architecture reviews and modernisation roadmaps",
            "Migration planning and execution support",
            "Cost optimisation and FinOps practices",
            "Cloud-native application patterns and container strategies",
            "Infrastructure as Code and CI/CD pipeline design",
            "Resilience engineering and disaster recovery planning",
        ),
        cta_button("Plan your cloud strategy", "/contact"),
        title="Cloud Strategy",
        subtitle="Architecture decisions that balance cost, reliability, and speed.",
        id="cloud",
    )


def services_page() -> rx.Component:
    return page_layout(
        section(
            rx.text(
                "Deep expertise across three domains that define "
                "modern software delivery.",
                size="5",
                color_scheme="gray",
                max_width="640px",
            ),
            title="Our Services",
            padding_y="5em",
        ),
        agentic_ai(),
        agile(),
        cloud(),
    )
