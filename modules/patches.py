import sys
from packaging.version import Version
from modules.ansi import ansi_supported, ansi_codes

# load ANSI codes if the console supports it
RESET, RED, GREEN, BLUE, YELLOW, WHITE, PURPLE, CYAN, LIGHT_CYAN, SUPER_LIGHT_CYAN, ORANGE = ansi_codes() if ansi_supported() else ("",) * 11

# get the current script version from version.txt
def get_version():
    with open("version.txt", "r") as file:
        return Version(file.read().strip())

current_version: Version = get_version()

# PATCH: config.py push_notifications handling
def patch_config():
    name = "Config.py Patch"

    if current_version <= Version("1.1.3"):
        return None

    config_file = "config.py"

    with open(config_file, "r") as file:
        lines = file.readlines()

    def has_uncommented_push_var(lines):
        for line in lines:
            stripped = line.strip()
            if stripped.startswith("push_notifications") and "=" in stripped and not stripped.startswith("#"):
                return True
        return False

    if not has_uncommented_push_var(lines):
        for i, line in enumerate(lines):
            stripped = line.strip()
            if (stripped.startswith("#")) and (("push_notifications=True" in stripped.replace(" ", "")) or ("push_notifications=False" in stripped.replace(" ", ""))):
                lines[i] = "push_notifications = False\n"
                break
        else:
            lines.append("\npush_notifications = False\n")

        with open(config_file, "w", newline="\n") as file:
            file.writelines(lines)

        return name  # Patch was applied

    return None  # Patch not needed

def apply_patches():
    print(f"{BLUE}Checking for patches...{RESET}")

    patches = [patch_config]

    for patch in patches:
        result = patch()
        if result:
            print(f"{GREEN}Patch {result} applied successfully! Please restart HardwareSwap Listing Scraper.{RESET}")
            sys.exit(0)

    print(f"{GREEN}No patches necessary.{RESET}\n")
