# HardwareSwap Listing Scraper

This README isn't anything amazing but everything you need should be here.

# Getting up and running with the script
## Prerequisites

Make sure you have the following installed before proceeding:
- A recent release of [Python](https://python.org)
- A recent release of [Git](https://git-scm.com/downloads)
- `pip` (comes with Python)

Optional but recommended:
- An editor with syntax highlighting such as Notepad++
- An IDE like Visual Studio Code (if you know what you're doing)

## Script Download Instructions
### Windows
1. Open up a PowerShell window. (You can do this by pressing the Windows key, and searching for "PowerShell" - it will be called "Windows PowerShell" or "PowerShell 7".) **Do not open PowerShell as administrator!**
2. Ensure you're in your user profile by typing `cd $env:userprofile`. 
3. Type in `git clone https://github.com/PowerPCFan/hardwareswap-listing-scraper.git` to download all of the necessary files.
4. Once that's done, type `cd hardwareswap-listing-scraper` to enter the folder for HardwareSwap Listing Scraper.  
**IMPORTANT: DO NOT CLOSE THIS POWERSHELL WINDOW! You will need it later.**

### Linux
Haven't written Linux instructions yet, sorry!

### macOS
Haven't written macOS instructions yet, sorry!

## Preparing the script
1. Go to [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps). Press **"are you a developer? create an app..."**
2. Name it **"HardwareSwap Listing Scraper"** and set the app type to **Script**. 
3. Leave the description blank.
4. Set the redirect URI to **http://localhost:8080** (this is just a placeholder URL - you could probably use google.com as well and it should still work!). 
5. Complete the reCaptcha and press **create app**.
6. Rename the file `example_config.json` to `config.json`.
7. Fill in your config.json using the "Configuring the script" instructions below. **Make sure that you fill in every value properly.**

## Configuring the script
### Reddit Secret Setup (REQUIRED)
- Go to [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps).
- Locate the app 'HardwareSwap Listing Scraper' you created earlier.
- Find your secret and ID using this example photo (you may have to press "edit" to view the secret):  
![Example image for how to find the ID and secret](https://raw.githubusercontent.com/PowerPCFan/hardwareswap-listing-scraper/refs/heads/main/assets/1.png)
- Open your config.json and find `"reddit_secret"` and `"reddit_id"`.
- Between the quotation marks after `"reddit_secret"`, paste in your reddit secret.
- Do the same but for `"reddit_id"`.

### Reddit Username Setup (REQUIRED)
1. In your config.json file, find `"reddit_username"`.
2. Just like you did for the secret and ID, insert your Reddit username between the quotes. 
3. DO NOT INCLUDE THE `u/` - if your username is `u/SuperCoolRedditUsername` just put in `SuperCoolRedditUsername`.

### Mode Setup (REQUIRED)
1. Open your config.json file and find the keys `"firehose"` and `"match"`.
2. There are two modes: 
    - Firehose Mode
      - Gives you a stream of every new post that comes in.
      - To use firehose mode (default), make sure the keys look like this:
        ```json
        "firehose": true,
        "match": false,
        ```
    - Match Mode
      - Only displays posts that meet your criteria.
      - To use match mode, make sure the keys look like this:
        ```json
        "firehose": false,
        "match": true,
        ```
### Author Has and Author Wants Setup (ONLY IF USING MATCH MODE)
- Since you're using Match Mode, you need to define what you're looking for. 
- In the config.json file, I provided examples on how to properly define the `"author_has"` and `"author_wants"` keys - just change my examples to whatever you want.
- You can have as many or as little strings in the `"author_has"` and `"author_wants"` lists, as long as they have at least one. So, both of these are valid, as long as the last string doesn't have a comma after it:
  ```json
    "author_has": [
      "4090",
      "4080",
      "4070",
      "4060",
      "3090 Ti",
      "1660 Super",
      "Intel i5-12600K"
    ],
  ```
  - 
  ```json
    "author_has": [
      "4090"
    ],
  ```

### retrieve_older_posts (Optional)
- If set to `true`, the script will retrieve the last 100 posts (firehose mode) or the posts that meet your criteria within the last 100 posts (match mode). 
- If set to `false` (default), the script will only retrieve new posts that are posted while the script is running. 

### tinyurl (Optional)
- If set to `true`, the URLs used in notifications, SMS messages, and console output will be tinyurl.com links made with the TinyURL URL shortener.
  - Note: Some carriers may flag SMS messages containing shortened URLs as spam. If you set up SMS and you have TinyURL enabled, and your messages aren't going through, try disabling it.
- If set to `false` (default), the script will use reddit.com URLs.

### Receive Push Notifications for posts (Optional, but recommended!)
To set up the script so you get push notifications for every new HWS post (firehose mode) or every new HWS post that matches your criteria (match mode), follow these steps:
1. In your config.json, change the `push_notifications` key from `false` to `true`, so `"push_notifications": false` becomes `"push_notifications": true`.
2. Download the ntfy app on your phone. Links: 
   - [Apple App Store](https://apps.apple.com/us/app/ntfy/id1625396347)
   - [Google Play Store](https://play.google.com/store/apps/details?id=io.heckel.ntfy)
   - [Web App (no downloads required)](https://ntfy.sh/app)
      - Note: If you would like Markdown support on mobile (clickable links, formatted text, etc), use the ntfy Web App, and add it to your Home Screen to receive notifications. 
3. Open the app, and allow notifications.
4. Press the plus button to create a topic. Name it something randomized and secure. 
5. In your config.json, insert your topic name between the quotes after `"topic_name"`. 
6. That's all! Whenever a new post is printed to your terminal, it'll send you a notification as well! Here's what a notification looks like (screenshot taken on iOS, but it probably looks similar on Android or other platforms):
![Listing notification on iOS](https://raw.githubusercontent.com/PowerPCFan/hardwareswap-listing-scraper/refs/heads/main/assets/2.jpg)

### Receive SMS message for posts (Optional)
To set up the script so you get SMS texts for every new HWS post (firehose mode) or every new HWS post that matches your criteria (match mode), follow these steps:
1. In your config.json, change the `"sms"` key from `false` to `true`, so `"sms": false` becomes `"sms": true`.
2. Sign into your Google account, or make one if you don't have one. 
3. Make sure 2FA (Two-Factor Authentication) is enabled - this won't work unless you enable it.
4. In your config.json, insert your Google account's Gmail address under the `"gmail_address"` key.
5. Visit [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords).
6. Create a new App Password with the name "HardwareSwap Listing Scraper", copy the App Password, and paste it in your config.json under the `"app_password"` key. Make sure that the formatting is correct, sometimes when you copy your app password it might mess up the formatting of config.json. 
7. Fill in your phone number in your config.json. Make sure the formatting is correct - for example, if your phone number was `+1 (123) 456-7890` you would do `"phone_number": "1234567890"` - note that I removed the country code and the parentheses and dashes. 
8. Insert your phone carrier's SMS gateway in your config.json. Do not include your phone number or the "at" (`@`) symbol. For example, I use Verizon, so I'm going to put `"sms_gateway": "vzwpix.com"`. If you don't know what yours is, try googling "carrier-name SMS gateway" or "carrier-name MMS gateway". 
9.  That's all! Whenever a new post is printed to your terminal, it'll send you an SMS text.

## Script Run Instructions
### Windows
***Note: For the following commands, if `py` doesn't work, try `python` or `python3`.***
1. In the PowerShell terminal you left open from earlier, run these commands:
   1. `py -m venv venv`
   2. `venv\Scripts\Activate.ps1`
   3. `pip install -r requirements.txt`
2. And finally to start the script, run `py scraper.py`.
Pro Tip: If you're looking for a specific item, enable Push Notifications and Match Mode (Follow the instructions in section "Configuring the script"), and leave the script running in the background, so you get notified when a listing gets posted that meets your criteria!

### Linux
Haven't written Linux instructions yet but if you're running linux you probably know what to do based on the Windows instructions. 

# Issues
If something's broken, confusing, or just not working right, [open an issue!](https://github.com/PowerPCFan/hardwareswap-listing-scraper/issues).

Make sure to include these details so it's easier to debug:
- What OS you're using
- What you were trying to do
- If there was an error, what error you saw (copy-paste the full message and put it in a codeblock)
- Your config.json file (be sure to remove sensitive information like your Gmail username and password, phone number, Reddit credentials, and ntfy topic name before sharing!)

I’ll try to respond quickly, but if you know the fix already and want to contribute, feel free to submit a pull request instead, explaining the fix and what you changed.

# Contributing
Want to help improve this script? Go for it!  
Just fork the repo, make your changes, and open a pull request. Please try your best to explain what you changed so it's easier for me to review. 
