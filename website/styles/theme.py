"""Theme configuration for projectious.work."""

import reflex as rx

# Color palette
NAVY = "#0f172a"       # Dark navy (primary backgrounds)
SLATE = "#1e293b"      # Slate (card backgrounds)
TEAL = "#0d9488"       # Teal accent
ELECTRIC = "#06b6d4"   # Electric blue accent
WHITE = "#ffffff"
LIGHT_GRAY = "#f8fafc"
MUTED = "#94a3b8"      # Muted text

# Font stack
FONT_FAMILY = "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"

# Shared style values
SECTION_PADDING_Y = "6em"
MAX_WIDTH = "1200px"
BORDER_RADIUS = "12px"


def get_theme() -> rx.Component:
    """Return the rx.theme component for the app."""
    return rx.theme(
        appearance="light",
        accent_color="teal",
        gray_color="slate",
        radius="medium",
        scaling="100%",
    )
