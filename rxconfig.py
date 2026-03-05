import reflex as rx

config = rx.Config(
    app_name="website",
    telemetry_enabled=False,
    plugins=[
        rx.plugins.TailwindV4Plugin(),
    ],
)
