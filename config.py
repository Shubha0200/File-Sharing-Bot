#(©)CodeXBotz

import os
import logging
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv()

# Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7532458641:AAHJgXb9LoeVbtPMRlLhHe-v4F-V_176gJ4")

# Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "21459238"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "0cef1924d139587654bc18402d2b512d")

# Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002448726887"))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1782088532"))

# Port
PORT = os.environ.get("PORT", "8080")

# Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://shubhashankar246:nEWTylzLZpiuysRh@cluster0.kpecd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "shubhashankar246")

# Helper function to convert string to boolean
def str_to_bool(value):
    return str(value).strip().lower() in ("true", "1", "yes")

# Force Sub Channels
FORCE_SUB_CHANNELS = [
    int(channel) for channel in [
        os.environ.get("FORCE_SUB_CHANNEL_1", "-1002343164262"),
        os.environ.get("FORCE_SUB_CHANNEL_2", "-1002262591479"),
        os.environ.get("FORCE_SUB_CHANNEL_3", "-1002383034992")
    ] if channel and channel.lstrip('-').isdigit()
]

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Start Message
START_PIC = os.environ.get("START_PIC", "")
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in a specified channel, and other users can access them via a special link.")

# Admins List
try:
    ADMINS = [int(x) for x in os.environ.get("ADMINS", "1782088532").split() if x.lstrip('-').isdigit()]
except ValueError:
    raise Exception("Your ADMINS list contains invalid values. Ensure all IDs are numbers.")

# Ensure OWNER_ID is in the admins list without duplication
ADMINS = list(set(ADMINS + [OWNER_ID]))

# Force Sub Message
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel to use me\n\nKindly Please join Channel</b>")

# Set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = str_to_bool(os.environ.get("PROTECT_CONTENT", "False"))

# Auto delete time in seconds
AUTO_DELETE_TIME = int(os.environ.get("AUTO_DELETE_TIME", "1800"))
AUTO_DELETE_MSG = os.environ.get("AUTO_DELETE_MSG", "This file will be automatically deleted in {time} seconds. Please ensure you have saved any necessary content before this time.")
AUTO_DEL_SUCCESS_MSG = os.environ.get("AUTO_DEL_SUCCESS_MSG", "Your file has been successfully deleted. Thank you for using our service. ✅")

# Set true if you want to disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = str_to_bool(os.environ.get("DISABLE_CHANNEL_BUTTON", "False"))

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

# Log File Handling
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE_NAME = os.path.join(LOG_DIR, "filesharingbot.txt")

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
