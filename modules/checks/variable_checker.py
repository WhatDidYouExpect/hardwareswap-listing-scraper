import sys
from modules.config.configuration import config
from modules.colors.ansi_codes import RESET, RED, GREEN, BLUE, YELLOW, WHITE, PURPLE, CYAN, LIGHT_CYAN, SUPER_LIGHT_CYAN, ORANGE, ansi_is_supported

def check():
    print(f"{BLUE}Initializing variables...{RESET}")
    
    try:
        if not config.reddit_id or not config.reddit_secret or not config.reddit_username:
            raise ValueError("There are missing variables in your config.json.\nPlease ensure all values are filled in using the instructions found in the README.")
        if config.mode == "match" and not (config.author_has or not config.author_wants):
            raise ValueError("You have match mode enabled, but have not specified any values for the author_has or author_wants keys.\nPlease switch to firehose mode to view all posts, or insert values in your config.json.")
        if config.push_notifications and not config.topic_name:
            raise ValueError("You have push notifications enabled, but have not specified a topic name.\nPlease set a topic name in your config.json file - see the README for instructions.")
        if config.sms and (not config.gmail_address or not config.app_password or not config.sms_gateway or not config.phone_number):
            raise ValueError("You have SMS notifications enabled but have not specified all of the required values.\nPlease ensure your config.json has all the proper values filled in.")
        if sum(bool(x) for x in [config.tinyurl, config.sl_expect_ovh, config.sl_powerpcfan_xyz]) > 1:
            raise ValueError("You cannot have more than one URL shortener enabled at once.\nPlease choose one and disable the others in your config.json file.")
        if config.mode not in ["firehose", "match", "match_llm"]:
            raise ValueError(f"Invalid mode specified in config.json. Allowed values are: 'firehose', 'match', 'match_llm'.")
        
        print("")
    except ValueError as e:
        print(f"\n{RED}{e}{RESET}\n")
        sys.exit(1)