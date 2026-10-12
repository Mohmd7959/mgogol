import os

API_ID = 36802286
API_HASH = "a1d2bafc62a0b0eb6246cd0a85ae79a9"
BOT_TOKEN = "8973651211:AAF37likBOB0RNrk0c7Rp_7sERDjQD5mQjI"

DEV_ID = 8777227942
DEV_LINK = "https://t.me/rkpkk"

BASE = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE, "data")
DB_PATH = os.path.join(DATA_DIR, "bot.db")
SESSIONS_DIR = os.path.join(BASE, "sessions")
VIDEOS_DIR = os.path.join(BASE, "download")

for d in [DATA_DIR, SESSIONS_DIR, VIDEOS_DIR]:
    os.makedirs(d, exist_ok=True)

MAX_ACCOUNTS_FREE = 5
MAX_ACCOUNTS_SUB = 10