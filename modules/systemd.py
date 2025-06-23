# lol this is so stupid
# it prints out messages that look like systemd startup logs or something 

from modules.ansi import ansi_supported, ansi_codes

RESET, RED, GREEN, BLUE, YELLOW, WHITE, PURPLE, CYAN, LIGHT_CYAN, SUPER_LIGHT_CYAN, ORANGE = ansi_codes() if ansi_supported() else ("",) * 11

class Logger:
    def __init__(self):
        pass

    def ok(self, message):
        print(f"[{GREEN} OK {RESET}] {message}")

    def failed(self, message):
        print(f"[{RED} FAILED {RESET}] {message}")
        
    def warn(self, message):
        print(f"[{YELLOW} WARN {RESET}] {message}")