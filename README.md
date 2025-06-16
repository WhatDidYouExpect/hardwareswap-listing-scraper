# HardwareSwap Listing Scraper

This README isn't anything amazing but everything you need should be here.

# Getting up and running with the script
## Prerequisites
Make sure you have these installed before proceeding:
- [Python](https://python.org)
- [git](https://git-scm.com/downloads)
- pip (comes with Python)

## Script Download Instructions
### Windows
1. Open up a PowerShell window. (You can do this by pressing the Windows key, and searching for "PowerShell" - it will be called "Windows PowerShell" or "PowerShell 7".)
2. Type in `git clone https://github.com/PowerPCFan/hardwareswap-listing-scraper.git`
3. Type `cd hardwareswap-listing-scraper` when that's done.  
**IMPORTANT: DO NOT CLOSE THIS POWERSHELL WINDOW!**

### Linux
Haven't written Linux instructions yet lmao

### macOS
Haven't written macOS instructions yet lmao

## Preparing the script
1. Go to [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps). Press **"are you a developer? create an app..."**
2. Name it **"HardwareSwap Listing Scraper"** and set the app type to **Script**. 
3. Leave the description blank.
4. Set the redirect URI to **http://localhost:8080** (placeholder URL). 
5. Complete the reCaptcha and press **create app**.
6. Rename the file `example_config.py` to `config.py`.
7. Fill in your config.py using the instructions below. **Make sure that you fill in every value properly.**

## Configuring the script
### Reddit Secret Setup (REQUIRED)
- Go to [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps).
- Find your secret and ID using this example (you may have to press edit to view the secret):  
![Example image for how to find the ID and secret](https://raw.githubusercontent.com/PowerPCFan/hardwareswap-listing-scraper/refs/heads/main/assets/1.png)
- Open your config.py and find `reddit_secret` and `reddit_id`.
- Between the quotation marks after `reddit_secret = `, paste in your reddit secret.
- Do the same but for `reddit_id`.

### Reddit Username Setup (REQUIRED)
1. In your config.py file, find `reddit_username`.
2. Just like the secret and ID, insert your Reddit username between the quotes. 
3. DO NOT INCLUDE THE `u/` - if your username is `u/SuperCoolRedditUsername` just put in `SuperCoolRedditUsername`.

### Mode Setup (REQUIRED)
1. Open your config file and find the variables `firehose` and `match`.
2. There are two modes: 
    - Firehose Mode
      - Gives you a stream of every new post that comes in.
      - To use firehose mode (default), make sure the variables look like this:
        ```python
        firehose = True
        match = False
        ```
    - Match Mode
      - Only displays posts that meet your criteria.
      - To use firehose mode, make sure the variables look like this:
        ```python
        firehose = False
        match = True
        ```
### Author Has and Author Wants Setup (ONLY IF USING MATCH MODE)
- Since you're using Match Mode, you need to define what you're looking for. 
- In the config.py file, I provided examples on how to properly define the `author_has` and `author_wants` variables - just change my examples to whatever you want.
- You can have as many or as little strings in the `author_has` and `author_wants` lists, as long as they have at least one. So, both of these are valid, as long as the last string doesn't have a comma after it:
  ```python
    author_has = [
      "4090",
      "4080",
      "4070",
      "4060",
      "3090 Ti",
      "1660 Super",
      "Intel i5-12600K"
    ]
  ```
  - 
  ```python
    author_has = [
      "4090"
    ]
  ```

### retrieve_older_posts (Optional)
- If set to `True`, the script will retrieve the last 100 posts (firehose mode) or the posts that meet your criteria within the last 100 posts (match mode). 
- If set to `False`, the script will only retrieve new posts that are posted while the script is running. 

### Receive Push Notifications for posts (Optional, but recommended!)
To set up the script so you get push notifications for every new HWS post (firehose mode) or every new HWS post that matches your criteria (match mode), follow these steps:
1. In your config.py, uncomment (remove the `#`) the line `push_notifications = True`.
2. Download the ntfy app on your phone. Links: [Apple App Store](https://apps.apple.com/us/app/ntfy/id1625396347) &nbsp;&nbsp; [Google Play Store](https://play.google.com/store/apps/details?id=io.heckel.ntfy)
3. Open the app, and allow notifications.
4. Press the plus button to create a topic. Name it something randomized and secure. 
5. In your config.py, insert your topic name between the quotes after `topic_name`. 
6. That's all! Whenever a new post is printed to your terminal, it'll send you a notification as well! Here's what a notification looks like (at least on iOS):
![Listing notification on iOS](https://raw.githubusercontent.com/PowerPCFan/hardwareswap-listing-scraper/refs/heads/main/assets/2.jpg)

## Script Run Instructions
### Windows
1. In the PowerShell terminal you left open from earlier, run these commands:
   1. `python -m venv venv`
   2. `venv\Scripts\Activate.ps1`
   3. `pip install -r requirements.txt`
2. And finally to start the script, run `python scraper.py`.
Pro Tip: If you're looking for a specific item, enable Push Notifications and Match Mode (Follow the instructions in section "Configuring the script"), and leave the script running in the background, so you get notified when a listing gets posted that meets your criteria!

### Linux
Haven't written Linux instructions yet but if you're running linux you probably know what to do based on the Windows instructions. 

# Issues
If something's broken, confusing, or just not working right, [open an issue!](https://github.com/PowerPCFan/hardwareswap-listing-scraper/issues).

Make sure to include these details so it's easier to debug:
- What OS you're using
- What you were trying to do
- If there was an error, what error you saw (copy-paste the full message and put it in a codeblock)
- Your config.py file (be sure to remove your `REDDIT_SECRET`, `REDDIT_ID`, and `topic_name` before sharing!!)

I’ll try to respond quickly, but if you know the fix already and want to contribute, feel free to submit a pull request instead, explaining the fix and what you changed.

# Contributing
Want to help improve this script? Go for it!  
Just fork the repo, make your changes, and open a pull request. Please try your best to explain what you changed so it's easier for me to review. 
