# copyright 2025 © | https://github.com/Kingmaker-art

import logging, json
from uvloop import install
from pyrogram.client import Client

# Read the dictionary from the txt file
with open("/content/TeleDriveBot/credentials.json", "r") as file:
    credentials = json.loads(file.read())

API_ID = credentials["API_ID"]
API_HASH = credentials["API_HASH"]
BOT_TOKEN = credentials["BOT_TOKEN"]
OWNER = credentials["USER_ID"]
DUMP_ID = credentials["DUMP_ID"]
GROUP_ID = credentials["GROUP_ID"]
THREAD_ID = credentials["THREAD_ID"]

logging.basicConfig(level=logging.INFO)

install()

colab_bot = Client("tg_drivebot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
