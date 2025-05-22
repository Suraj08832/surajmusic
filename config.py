import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# --- HARDCODED CONFIG VALUES ---
API_ID = 28053244
API_HASH = "a7d745be7c8ba465750bfad1e7abc075"
BOT_TOKEN = "8021590989:AAGIu2WS30kjBpXIvWqXUCkrCt3E3yIG9Ak"
MONGO_DB_URI = "mongodb://localhost:27017/destinymusic"
LOGGER_ID = -1002638427943
OWNER_ID = 8015044785
STRING1 = "BQGsDvwAMQDTveLse1-q03wcBgeh1LglX21pIEO-C_-TwE_UCfBt4qsmrBqoO5t5N-bKG6kddrv5c61LHXCB6Wha4ci5R1V3IIeANtwrUCJ87esez_FyugrbMEwv1p2nbEoJrFsMW6n6AtVvX1gGuMar0VT_ajnhj_PzWKZC_RfE1_Hhh3s0czyLWrYtAtgOZQBHURW5GpxCEOXLjoc_9jF7Yt48XYhDqcpdWZg7p2WHKMYQriLDSvSVJeKL97kkzD6aBLAEvjNqh6zvUFZXV4fsFpvenze-njzJQBtFYBRB-HXX5zEU7bPJacFfUeRdd4O8ma7sAwtEO7F-UzS9Im4ZbqUj8wAAAAHdu-CxAA"
STRING2 = "BQF-ZJIASbBrsfbXzsMEEC55i41nyJvns68ouL_lVZby_cZwhIa9heE5HZdvGePA4j7x4J8AVcoj76FnywPaJnehPa7cVCDCyHJE5axDNkH7XVAMja1FNA2OCH-z1tyfemSNWCR4T53B479H0u-QbE6vDKoSzrEvRonv7XkAL5ZL59-vTAfSqc30VpfXs9JLEhNIrSPJepVZFXiOdfNiqi3NYMcbBZsKxqQhd_yGLEHwCeMCqjhA95BNADUL3b-X383zZTVkLVsD95WGiGqni7g7BRXj1u82-C532G3zGHyx4b7u_XkXx9vgMRnH23rfDsZYxhjt9CrS60BDR_dElllvOpW9xQAAAAHNQBbEAA"
# --- END HARDCODED CONFIG VALUES ---

# Get your token from @BotFather on Telegram.
# -------------------------------------------------------
OWNER_USERNAME = getenv("OWNER_USERNAME","ANURAGMOD")
# --------------------------------------------------------
BOT_USERNAME = getenv("BOT_USERNAME","@MAHI_X_MUSIC_BOT")
# --------------------------------------------------------
BOT_NAME = getenv("BOT_NAME")
# ---------------------------------------------------------


# Get your mongo url from cloud.mongodb.com
# --------------------------------------------------------
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 900))

# Chat id of a group for logging bot's activities
# --------------------------------------------------------

# Get this value from @PURVI_HELP_BOT on Telegram by /id
# --------------------------------------------------------


# make your bots privacy from telegra.ph and put your url here 
PRIVACY_LINK = getenv("PRIVACY_LINK", "https://graph.org/PRIVACY-FOR-TEAM-PURVI-BOTS-09-18")

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/ANURAGSONG/ANURAG_music",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/chamber_of_heart1")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+AzKGhJreNmhiZTll")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://files.catbox.moe/gjbdmi.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://files.catbox.moe/gjbdmi.jpg"
)
PLAYLIST_IMG_URL = "https://files.catbox.moe/gjbdmi.jpg"
STATS_IMG_URL = "https://files.catbox.moe/gjbdmi.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/gjbdmi.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/gjbdmi.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/gjbdmi.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/gjbdmi.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/gjbdmi.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/gjbdmi.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/gjbdmi.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/gjbdmi.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
