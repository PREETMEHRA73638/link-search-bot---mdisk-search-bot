import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 25830285))
    API_HASH = os.environ.get("API_HASH", "0cbcabbf1b9c56a4dfc4b8950d584a2a")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6443763987:AAFqZrFnJHux_0pHRddE5xtmZEIY89RmOK0")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "LinkSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "1BVtsOHgBu5IpvJ8J1rP2SYxwJdmYYqL38SNtrUQKYJiGPAsOewvpmW6cxU2NjStpiIrjDftyMKhh6HRkTvTegP6mJ_6c0jcqGajMwbTwsNijQi3oF-fxoLyM0nxPu41xUdUT6R4h4ZpyPQ8C7rQvexyHi-YO0grkcDndQ22hESAi-wGds4b-YXFbFBJUna7vphuV_aDqL7mwTX4gTeA5U5UXkUuo3Itg1SkpzRvjJZVEytksWW_1FMn_t_Rqzfrk45ZoRL9bv3p0bNTCiMe5DTAyI7rra9XzIfvHb4Ak37N3H0aktX-MdcgA2yvYvsk3s-CmdGJazxdlYwCs7juDb9_9rGDO_nE=")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001855434571"))
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "MOVIES_VILLA_SEARCH_BOT")
    BOT_OWNER = int(os.environ.get("BOT_OWNER", "6339699671"))
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://LinkSearchBot:mongodb786@cluster0.gwbtuaj.mongodb.net/?retryWrites=true&w=majority")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001896148531")
    ABOUT_BOT_TEXT = """<b>This is Link Search Bot.
    
    
    
🤖 My Name: <a href='https://t.me/MOVIES_VILLA_SEARCH_BOT'>ᴹᴼᵛᴵᴱˢ ᵛᴵᴸᴸᴬ ˢᴱᴬᴿᶜᴴ ᴮᴼᵀ</a>

📝 Language : <a href='https://www.python.org'>ᴾᵞᵀᴴᴼᴺ ᵛ3</a>

📚 Library: <a href='https://docs.pyrogram.org'>ᴾᵞᴿᴼᴳᴿᴬᴹ</a>

📡 Server: <a href='heroku.com'>ᴴᴱᴿᴼᴷᵁ</a>

👨‍💻 Created By: <a href='https://t.me/Hindi_movies_villa'>ᴹᴼᵛᴵᴱˢ ᵛᴵᴸᴸᴬ</a></b>
"""

    ABOUT_HELP_TEXT = """<b>👨‍💻 Creator : <a href='https://t.me/Hindi_movies_villa'>ᴹᴼᵛᴵᴱˢ ᵛᴵᴸᴸᴬ</a>
If You Want Your Own Bot Like This Then You Can Contact Our Creator.</b>
"""

    HOME_TEXT = """
<b>Hey! {}😅,

I'm Link Search Bot.🤖

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @ROYAL_OSM_MEHRAp</a></b>
"""


    START_MSG = """
<b>Hey! {}😅,

I'm Link Search Bot.🤖

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @ROYAL_OSM_MEHRA</a></b>
"""

