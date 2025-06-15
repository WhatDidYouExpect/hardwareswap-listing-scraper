import config as c
import praw
import re as regexp
import time
import ansi
import sys
import requests

ansi_is_supported = ansi.ansi_supported()

if ansi_is_supported:
    # ansi escape codes for colors in console output 
    ANSI = "\033["
    RESET = f"{ANSI}0m"
    RED = f"{ANSI}31m"
    GREEN = f"{ANSI}32m"
    BLUE = f"{ANSI}34m"
    YELLOW = f"{ANSI}33m"
    WHITE = f"{ANSI}37m"
    PURPLE = f"{ANSI}35m"
    CYAN = f"{ANSI}36m"
    LIGHT_CYAN = f"{ANSI}96m"
    SUPER_LIGHT_CYAN = f"{ANSI}38;5;153m"
    ORANGE = f"{ANSI}38;5;208m"
else:
    print("Note: Your terminal does not support ANSI colors. Output will appear without color.")

    ANSI = ""
    RESET = ""
    RED = ""
    GREEN = ""
    BLUE = ""
    YELLOW = ""
    WHITE = ""
    PURPLE = ""
    CYAN = ""
    LIGHT_CYAN = ""
    SUPER_LIGHT_CYAN = ""
    ORANGE = ""

def strip_trades_prefix(flair):
    if flair and flair.startswith("Trades: "):
        return flair.removeprefix("Trades: ")
    return flair

def get_karma_string(author):
    j = reddit_account_age_timestamp_generator(author.created_utc)
    pk = author.link_karma
    ck = author.comment_karma
    
    return j, pk, ck

def send_notification(text, url):
    headers={
        "Click": url, # notification click action
        "Title": f"New listing on r/hardwareswap",
        "Priority": "3" # 1 = min, 2 = low, 3 = default, 4 = high, 5 = max
    }
    
    requests.post(
        "https://ntfy.sh/" + c.topic_name,
        data=text.encode(encoding='utf-8'),
        headers=headers
    )

def print_new_post(subreddit, author, h, w, url, utc_date, flair, title):
    j, pk, ck = get_karma_string(author)
    
    trades = strip_trades_prefix(flair)
    trades = "0" if trades == "None" else trades
    
    print(f"New post by {BLUE}u/{author.name}{RESET} ({YELLOW}{trades}{RESET} trades | joined {CYAN}{j}{RESET} | post karma {ORANGE}{pk}{RESET} | comment karma {PURPLE}{ck}{RESET}):")
    print(f"[H]: {GREEN}{h}{RESET}\n[W]: {RED}{w}{RESET}\nURL: {SUPER_LIGHT_CYAN}{url}{RESET}")
    print(f"Posted {WHITE}{reddit_timestamp_creator(utc_date)}{RESET}\n")
    
    if c.push_notifications and c.topic_name:
        text = title
        send_notification(text, url)

def reddit_timestamp_creator(unix_epoch):
    now = int(time.time())
    diff = now - int(unix_epoch)
    if diff < 60:
        return "just now"
    elif diff < 3600:
        minutes = diff // 60
        return f"{minutes} minute{'s' if minutes != 1 else ''} ago"
    elif diff < 86400:
        hours = diff // 3600
        return f"{hours} hour{'s' if hours != 1 else ''} ago"
    elif diff < 2592000:
        days = diff // 86400
        return f"{days} day{'s' if days != 1 else ''} ago"
    elif diff < 31536000:
        months = diff // 2592000
        return f"{months} month{'s' if months != 1 else ''} ago"
    else:
        years = diff // 31536000
        return f"{years} year{'s' if years != 1 else ''} ago"

def reddit_account_age_timestamp_generator(unix_epoch):
    return time.strftime("%B %d, %Y", time.localtime(unix_epoch))

def print_welcome_text():
    welcome = f"Welcome to the HardwareSwap Listing Scraper, "
    username = f"u/{c.reddit_username}!"
    dashes = "-" * (len(welcome) + len(username))
    print(f"\n{dashes}")
    print(f"{welcome}{BLUE}{username}{RESET}")
    print(f"Mode: {WHITE}{'Firehose' if c.firehose else 'Match'}{RESET}")
    print(f"Press {YELLOW}Ctrl+C{RESET} to exit.")
    print(f"{dashes}\n")

def parse_have_want(title):
    h_match = regexp.search(r'\[H\](.*?)\[W\]', title, regexp.IGNORECASE)
    w_match = regexp.search(r'\[W\](.*)', title, regexp.IGNORECASE)

    h = h_match.group(1).strip() if h_match else ""
    w = w_match.group(1).strip() if w_match else ""
    return h, w

def firehose_mode(subreddit):    
    for submission in subreddit.stream.submissions(skip_existing = not c.retrieve_older_posts):
        h, w = parse_have_want(submission.title)
        print_new_post(subreddit, submission.author, h, w, submission.url, submission.created_utc, submission.author_flair_text, submission.title)

def match_mode(subreddit):
    # for submission in subreddit.stream.submissions(skip_existing=True):
    for submission in subreddit.stream.submissions(skip_existing = not c.retrieve_older_posts):
        h, w = parse_have_want(submission.title)
        author_has_lower = [s.lower() for s in c.author_has]
        author_wants_lower = [s.lower() for s in c.author_wants]

        if any(s in h.lower() for s in author_has_lower) and any(s in w.lower() for s in author_wants_lower):
            print_new_post(subreddit, submission.author, h, w, submission.url, submission.created_utc, submission.author_flair_text, submission.title)

def main():
    print(f"{YELLOW}Initializing variables...{RESET}")
    if not c.reddit_id or not c.reddit_secret or not c.reddit_username:
        print(f"{RED}Error: There are missing variables in your config.py.\nPlease ensure all values are filled in using the instructions found in the README.{RESET}")
        return
    if c.firehose == c.match:
        print(f"{RED}Error: You cannot have both firehose and match mode enabled or disabled at the same time.{RESET}")
        return
    if c.match and (c.author_has == [] or c.author_wants == []):
        print(f"{RED}Error: You have match mode enabled, but have not specified any author_has or author_wants values.\nPlease switch to firehose mode to view all posts, or insert values in your config.py.{RESET}")
        return
    
    print(f"{YELLOW}Connecting to Reddit...{RESET}")

    reddit = praw.Reddit(
        client_id=c.reddit_id,
        client_secret=c.reddit_secret,
        user_agent=f"script:hardwareswap-listing-scraper (by u/{c.reddit_username})"
    )
    
    subreddit = reddit.subreddit("hardwareswap")

    print(f"{GREEN}Connected successfully.{RESET}")

    print_welcome_text()

    if c.firehose:
        firehose_mode(subreddit)
    elif c.match:
        match_mode(subreddit)
    else:
        print(f"{RED}\nError: An unknown error occurred. Please ensure that your config.py file is properly set up. {RESET}")
        return
    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"{YELLOW}Exiting...{RESET}")
        sys.exit(0)
    except Exception as e:
        print(f"{'-' * 36}\n{RED}ERROR: An unexpected error occurred:{RESET}\n{'-' * 36}\n{e}")
        sys.exit(1)
