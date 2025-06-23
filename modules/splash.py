def print_splash_text(WHITE: str, BLUE: str, RESET: str, color: bool):
    fg, bg = (f"{WHITE}▓{RESET}", f"{BLUE}▓{RESET}") if color else (f"#", f".")

    splash = f"""
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{fg}{fg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{fg}{fg}{fg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{fg}{fg}{fg}{fg}{fg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{fg}{fg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{fg}{fg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{fg}{fg}{fg}{fg}{fg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{fg}{fg}{fg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{fg}{fg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
"""

    print(splash)