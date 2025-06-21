import requests
from modules.ansi import ansi_supported, ansi_codes

RESET, RED, GREEN, BLUE, YELLOW, WHITE, PURPLE, CYAN, LIGHT_CYAN, SUPER_LIGHT_CYAN, ORANGE = ansi_codes() if ansi_supported() else ("",) * 11    

class TinyURL:
    def __init__(self):
        pass
    
    def shorten(self, url, timeout) -> str:
        try:
            api_url = f"http://tinyurl.com/api-create.php?url={url}"
            response = requests.get(api_url, timeout=timeout)
            if response.status_code == 200:
                return response.text
            else:
                raise Exception("Error shortening URL.")
        except Exception as e:
            print(f"{RED}ERROR: {e}{RESET}")
            return url
