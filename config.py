import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()
# ===============================================

API_ID = int(getenv("API_ID", None))
API_HASH = getenv("API_HASH", None)
BOT_TOKEN = getenv("BOT_TOKEN", None)

# ===============================================

OWNER_ID = int(getenv("OWNER_ID", 7473021518))
OWNER_USERNAME = getenv("OWNER_USERNAME", "liar_neo")
LOGGER_ID = int(getenv("LOGGER_ID", None))

# ===============================================

BOT_USERNAME = getenv("BOT_USERNAME", "columbinaxMusicBot")
BOT_NAME = getenv("BOT_NAME", "𝐂ꪮʟᴜꪑʙɪꪀꪖ")

# ===============================================

MONGO_DB_URI = getenv("MONGO_DB_URI", None)
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))

# ===============================================

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

# ===============================================

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/txsn4x/sn4xy")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)  

# ===============================================

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/aniweb_bots")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/aniweb_nexus")

# ===============================================

AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# ===============================================

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

# ===============================================

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))   
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))     

# ===============================================

STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

# ===============================================

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# ===============================================

START_IMG_URL = getenv("START_IMG_URL", "https://graph.org/file/e2ccdc8f93a67b995072c-37cdfd36f3dd2f4dbb.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://graph.org/file/95e7a771b14e2da41d7c7-54f29bec291e2ad228.jpg")

PLAYLIST_IMG_URL = "https://graph.org/file/01f6bff76d899c77153ba-112d924074f9890051.jpg"
STATS_IMG_URL = "https://graph.org/file/e8d2d4c10a317e3b62bcf-f5e9bf6e7ad41e222c.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/e8d2d4c10a317e3b62bcf-f5e9bf6e7ad41e222c.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/e8d2d4c10a317e3b62bcf-f5e9bf6e7ad41e222c.jpg"
STREAM_IMG_URL = "https://graph.org/file/e8d2d4c10a317e3b62bcf-f5e9bf6e7ad41e222c.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/e8d2d4c10a317e3b62bcf-f5e9bf6e7ad41e222c.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/e8d2d4c10a317e3b62bcf-f5e9bf6e7ad41e222c.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/e8d2d4c10a317e3b62bcf-f5e9bf6e7ad41e222c.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/e8d2d4c10a317e3b62bcf-f5e9bf6e7ad41e222c.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/e8d2d4c10a317e3b62bcf-f5e9bf6e7ad41e222c.jpg"

# ===============================================

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# ===============================================

if SUPPORT_CHANNEL and not re.match("(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - Invalid SUPPORT_CHANNEL URL. Must start with https://")

if SUPPORT_CHAT and not re.match("(?:http|https)://", SUPPORT_CHAT):
    raise SystemExit("[ERROR] - Invalid SUPPORT_CHAT URL. Must start with https://")
# ===============================================
