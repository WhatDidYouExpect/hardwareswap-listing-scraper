import os
import shutil
import subprocess
import requests
from packaging.version import Version
from modules.ansi import ansi_supported, ansi_codes

RESET, RED, GREEN, BLUE, YELLOW, WHITE, PURPLE, CYAN, LIGHT_CYAN, SUPER_LIGHT_CYAN, ORANGE = ansi_codes() if ansi_supported() else ("",) * 11

GITHUB_VERSION_URL = "https://raw.githubusercontent.com/PowerPCFan/hardwareswap-listing-scraper/refs/heads/main/version.txt"
BACKUP_FOLDER_PREFIX = "version-"
VERSION_FILE = "version.txt"

def read_local_version():
    with open(VERSION_FILE, "r") as f:
        return Version(f.read().strip())

def fetch_remote_version():
    response = requests.get(GITHUB_VERSION_URL, timeout=10)
    response.raise_for_status()
    return Version(response.text.strip())

def create_backup(local_version):
    backup_folder = f"{BACKUP_FOLDER_PREFIX}{local_version}-backup"
    os.makedirs(backup_folder, exist_ok=True)

    for item in os.listdir("."):
        if item == backup_folder:
            continue
        if item.startswith(BACKUP_FOLDER_PREFIX):
            continue # Skips backup folders

        if os.path.isdir(item):
            shutil.copytree(item, os.path.join(backup_folder, item), dirs_exist_ok=True)
        else:
            shutil.copy2(item, os.path.join(backup_folder, item))
            
    print(f"{GREEN}Backup created at {backup_folder}{RESET}")

def update_repo():
    # git reset
    subprocess.run(["git", "reset", "--hard", "origin/main"], check=True)
    # git pull
    subprocess.run(["git", "pull"], check=True)
    print(f"{GREEN}Update Successful!{RESET}\nPlease restart the script by running `python scraper.py`.")

def check_for_updates():
    print(f"{BLUE}Checking for updates...{RESET}")
    
    try:
        local_version = read_local_version()
        remote_version = fetch_remote_version()

        if remote_version > local_version:
            print(f"{YELLOW}Update available: {local_version} → {remote_version}. Updating...{RESET}")
            create_backup(local_version)
            update_repo()
        else:
            print(f"Script is already up to date.")

    except Exception as e:
        print(f"{RED}Error: Update failed:{RESET} {e}")
