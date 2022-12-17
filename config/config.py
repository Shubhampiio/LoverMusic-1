import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "18960528"))
API_HASH = getenv("API_HASH", "cc0fff577b677c9b2b4de5dd5bc5dfd1")
BOT_TOKEN = getenv("BOT_TOKEN", "5983601762:AAFu5qJs4CKj3DhQz77_Fe9kPHuxK9kBhV4")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://hnyx:wywyw2@cluster0.9dxlslv.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001715071938"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "『˹𝑳𝒐𝒗𝒆𝒓 ✘ ℳ𝓾𝓼𝓲c͢˼』")
OWNER_ID = list(map(int, getenv("OWNER_ID", "1548904516").split()))
SUPPORT_CHANNEL = getenv(
    "SUPPORT_CHANNEL", "https://t.me/t_c_c_network")
SUPPORT_GROUP = getenv(
    "SUPPORT_GROUP", "https://t.me/the_chatting")

DURATION_LIMIT_MIN = int(
    getenv("DURATION_LIMIT", "59006")
)

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "10998")
)

HEROKU_API_KEY = getenv("HEROKU_API_KEY")

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/SPARTENX-OP/VirusMusicBot",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

GIT_TOKEN = getenv("GIT_TOKEN", None)

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")

AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", "False")

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "6"))

GITHUB_REPO = getenv("GITHUB_REPO", "https://t.me/shubhamsah1")

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "50"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "5")
)

TG_AUDIO_FILESIZE_LIMIT = int(
    getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600")
)
TG_VIDEO_FILESIZE_LIMIT = int(
    getenv("TG_VIDEO_FILESIZE_LIMIT", "2073741824")
)


STRING1 = getenv("STRING_SESSION", "BQAtDFZrnjlHKvo-JMCFcD2iKg9OUpUKqq9fj-iv2VGadftLDjICXFsx9AIW1fuTAF9pAtag2vvZQfhTetwZqEqCBp781cxk03vN6lh_hDHpxga_vIuc-yJk1Gx4fEXUOe11k1w1p-QjrO9RfaiP4QQxuhPQqSPOcYvKKszKMn1wYS3E5S5X6W7baEZ7whec7QL1CLBA3lpHsaUIzjAnjMPKo9aUCh0F-lqUWEhEtA91FwnxQEdmFHBl97uWdwGkcvjpRHVO7i_hxmfm-cU_snuoR9wdnQsdYjJCOMdt7a93XpD3YQY0MaWlkZsb2ROwDLXHA0PjOKY98lLKd_ouE-_DAAAAAVUVXdEA")
STRING2 = getenv("STRING_SESSION2", "AQAmze89KCvwMG5Z63NObTXvhJn2cje4McXmuw1A5MkKMYXOAQA2F-qt3XM57FhUcOuJDW7brfZqg4Z3lMNwHI8PRXrHOW76-81DYCmsyBdHRhH-D7eAvwpDzaEbi0o8gA0VIanF7zZ2ABaQbxBhrM8auRIpPHMohjYjLYShQURITnq085QrV8IqeSHEgg9w5X-e2UDH6mNRoejma3E2v3VNt6u4dRawv7paojZ8or0PztHdaPY0Q1mcTgJvoQ3zyNeoiwiJw436vdJLkXhSIy9WDuGjkTRcnbio8cSS2e72yiabmta_NhNQ1TtPlQl3jcjjN_c7EbE2jTY6pEyyviAvAAAAAWQmw70A")
STRING3 = getenv("STRING_SESSION3", "BQADXae9k934aDMrGgU8PKf0ytQ_Op0mc6eImkW0UOJwyvIZkqcPjP0ofeaAoKT6hKIKa2WEqUaRGxymPPeqqE5p_uNcgPbkc6O5q2yWMRnFX0M0y6RlZwn5ciCb8m4DlEgrgTIsTB-pscpvmB3i_-t3W6Ex9I6mVRJHPurEn0_wX8zS0jIqubOofLQw2boFQjVGtzpK1OqxH0QXPBMSZn42tJA3cGZAC5qBUHyFHhpJoUrxheLnpeOwYvkGlDTpTMgbcpPyoiqwyeNOx5PrIU1oFPMYgr08DNDS_wJycPQRVfzP-uW3jyr4DzS3XW-Otk2K5NqyMMhy_TNI_03WS5O5c1rR6wA")
STRING4 = getenv("STRING_SESSION4" None)
STRING5 = getenv("STRING_SESSION5" None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "viruslogs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/file/8d4c08fb054f205e0061e.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://telegra.ph/file/8d4c08fb054f205e0061e.jpg",
)

PLAYLIST_IMG_URL = getenv(
    "PLAYLIST_IMG_URL",
    "assets/Playlist.jpeg",
)

GLOBAL_IMG_URL = getenv(
    "GLOBAL_IMG_URL",
    "https://te.legra.ph/file/354711e8d255477308a2d.jpg",
)

STATS_IMG_URL = getenv(
    "STATS_IMG_URL",
    "https://te.legra.ph/file/354711e8d255477308a2d.jpg",
)

TELEGRAM_AUDIO_URL = getenv(
    "TELEGRAM_AUDIO_URL",
    "https://te.legra.ph/file/354711e8d255477308a2d.jpg",
)

TELEGRAM_VIDEO_URL = getenv(
    "TELEGRAM_VIDEO_URL",
    "https://te.legra.ph/file/354711e8d255477308a2d.jpg",
)

STREAM_IMG_URL = getenv(
    "STREAM_IMG_URL",
    "assets/Stream.jpeg",
)

SOUNCLOUD_IMG_URL = getenv(
    "SOUNCLOUD_IMG_URL",
    "assets/Soundcloud.jpeg",
)

YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL",
    "assets/Youtube.jpeg",
)

SPOTIFY_ARTIST_IMG_URL = getenv(
    "SPOTIFY_ARTIST_IMG_URL",
    "assets/SpotifyArtist.jpeg",
)

SPOTIFY_ALBUM_IMG_URL = getenv(
    "SPOTIFY_ALBUM_IMG_URL",
    "assets/SpotifyAlbum.jpeg",
)

SPOTIFY_PLAYLIST_IMG_URL = getenv(
    "SPOTIFY_PLAYLIST_IMG_URL",
    "assets/SpotifyPlaylist.jpeg",
)


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)

if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            print(
                "[ERROR] - Your PING_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if PLAYLIST_IMG_URL:
    if PLAYLIST_IMG_URL != "assets/Playlist.jpeg":
        if not re.match("(?:http|https)://", PLAYLIST_IMG_URL):
            print(
                "[ERROR] - Your PLAYLIST_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if GLOBAL_IMG_URL:
    if GLOBAL_IMG_URL != "https://te.legra.ph/file/354711e8d255477308a2d.jpg":
        if not re.match("(?:http|https)://", GLOBAL_IMG_URL):
            print(
                "[ERROR] - Your GLOBAL_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STATS_IMG_URL:
    if STATS_IMG_URL != "https://te.legra.ph/file/354711e8d255477308a2d.jpg":
        if not re.match("(?:http|https)://", STATS_IMG_URL):
            print(
                "[ERROR] - Your STATS_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_AUDIO_URL:
    if TELEGRAM_AUDIO_URL != "https://te.legra.ph/file/354711e8d255477308a2d.jpg":
        if not re.match("(?:http|https)://", TELEGRAM_AUDIO_URL):
            print(
                "[ERROR] - Your TELEGRAM_AUDIO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STREAM_IMG_URL:
    if STREAM_IMG_URL != "assets/Stream.jpeg":
        if not re.match("(?:http|https)://", STREAM_IMG_URL):
            print(
                "[ERROR] - Your STREAM_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if SOUNCLOUD_IMG_URL:
    if SOUNCLOUD_IMG_URL != "assets/Soundcloud.jpeg":
        if not re.match("(?:http|https)://", SOUNCLOUD_IMG_URL):
            print(
                "[ERROR] - Your SOUNCLOUD_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if YOUTUBE_IMG_URL:
    if YOUTUBE_IMG_URL != "assets/Youtube.jpeg":
        if not re.match("(?:http|https)://", YOUTUBE_IMG_URL):
            print(
                "[ERROR] - Your YOUTUBE_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_VIDEO_URL:
    if TELEGRAM_VIDEO_URL != "https://te.legra.ph/file/354711e8d255477308a2d.jpg":
        if not re.match("(?:http|https)://", TELEGRAM_VIDEO_URL):
            print(
                "[ERROR] - Your TELEGRAM_VIDEO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()
