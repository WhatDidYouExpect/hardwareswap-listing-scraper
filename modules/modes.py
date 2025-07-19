import time
from modules.config.configuration import config
from modules.utils import parse_have_want, print_new_post

def firehose(subreddit):
    for submission in subreddit.stream.submissions(skip_existing = not config.retrieve_older_posts):
        h, w = parse_have_want(submission.title)
        print_new_post(subreddit, submission.author, h, w, submission.url, submission.created_utc, submission.author_flair_text, submission.title)

def match(subreddit):
    post_stream = subreddit.stream.submissions(skip_existing = not config.retrieve_older_posts)
    
    author_has_lower = [s.lower() for s in config.author_has]
    author_wants_lower = [s.lower() for s in config.author_wants]
    
    for submission in post_stream:
        h, w = parse_have_want(submission.title)
        if any(s in h.lower() for s in author_has_lower) and any(s in w.lower() for s in author_wants_lower):
            print_new_post(subreddit, submission.author, h, w, submission.url, submission.created_utc, submission.author_flair_text, submission.title)
