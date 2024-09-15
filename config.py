#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7002754834:AAH8gQMRpVHh9JiG2v4YSx2EiBC_hp6V7gM")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "2737672"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "f4aae49f836134236a19d434f8597c45")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002079972903"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1675155069"))

#Port
PORT = os.environ.get("PORT", "7100")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://JJUSTANIME:teamjxg@cluster0.nncsv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "My_Anime_Store_Bot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001621032259"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4000"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI am File Store Bot. I can provide you Anime Files with With Special Link Generated By Admin.\n\n🌐 Visit Our Base @Team_JXG For More Stuff")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1865103287 6369860260 1675155069").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>Aapko file tabhi milegi jab aap neeche diye gaye channels ko join karenge. Jab aap ye kar lenge, ""Try Again"" par click karna\n\nThanks You 🙏</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only Work For @Team_JXG"

ADMINS.append(OWNER_ID)
ADMINS.append(1675155069)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
