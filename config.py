import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
class Config(object):
    log = True
    APP_ID = getenv("API_ID", "6435225")
    API_HASH = getenv("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    TOKEN = getenv("TOKEN", "6107040564:AAFf27c69JZkbmxVajttlf7iaTaNff2idvY0")
    OWNER_ID = getenv("OWNER_ID", "1981344911")
    ASSISTANT_ID = getenv("ASSISTANT_ID", "5968775445")
    STRING_SESSION = getenv("STRING_SESSION", "1BVtsOKIBu5L8yd8gDHp4RJarwqj5mWI6mEWuE62x1wPxUQsLO1rt-Gr4ABVtD-a-Goi7XHUM5XfsCAdOANSFyQTI4O-osrMHfGXsQwvjLeldtE7izpxSXJr-28wYIiJIUfJE4U7cMBPJ4UNAqKzJZOPdQ2Ehlfy8jEfxVcuZ5tYfiljAs2M0bAsFjw47d0xIVV0igVDSPyRBXsuPQo59b8zCAn1Bzo8rWWQqd20z47xbTlvaZMC3nXtFGqbJvFRnDFbPmLYFgcn1uk7H7BXgm4q5rrvmD4b1rWaTLCEH45Ox-NMbbnXzhEzTrAumRr_M9U8a0FPQzHGfUaqELMvCd4VfDBhW2Fw=") #telethon
    OWNER_USERNAME = getenv("OWNER_USERNAME", "Shoshuke")
    DB_URI = getenv("DATABASE_URL", "")
    DB_URI = DB_URI.replace("postgres", "postgresql")
    MESSAGE_DUMP = getenv("MESSAGE_DUMP", "-1001509525202")
    GBAN_LOGS = getenv("GBAN_LOGS", "-1001509525202")
    SYS_ADMIN = getenv("SYS_ADMIN", "1669178360")
    DEV_USERS = getenv("DEV_USERS", "1669178360")
    LOAD = getenv("LOAD")
    WEBHOOK = False
    SPB_MODE = True
    DROP_UPDATES = False
    DEBUG = False
    URL = None
    INFOPIC = True
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True
    STRICT_GBAN = True
    BAN_STICKER = getenv("BAN_STICKER", "")
    ALLOW_EXCL = True
    CUSTOM_CMD = False
    CHANNEL = getenv("CHANNEL", "TheUpdatesChannel")
    SUPPORT = getenv("SUPPORT", "TheSupportChat")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    CASH_API_KEY = getenv("CASH_API_KEY", "https://www.alphavantage.co/support/#api-key")
    TIME_API_KEY = getenv("TIME_API_KEY", "https://timezonedb.com/api")
    WALL_API = getenv("WALL_API", "https://wall.alphacoders.com/api.php")
    spamwatch_api = getenv("spamwatch_api", "https://t.me/SpamWatchBot")
    SPAMMERS = getenv("SPAMMERS", "")
    LASTFM_API_KEY = getenv("LASTFM_API_KEY", "https://www.last.fm/api/account/create")
    CF_API_KEY = getenv("CF_API_KEY", "coffehouse.intellivoid.net")
    BOT_API_URL = getenv("BOT_API_URL", "https://api.telegram.org/bot")
    BOT_API_FILE_URL = getenv("BOT_API_FILE_URL", "https://api.telegram.org/file/bot")
    SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1669178360").split()))
    ZAID_USER = list(map(int, getenv("DEV_USERS", "1669178360").split()))
    NO_LOAD = list(map(int, getenv("NO_LOAD", "").split()))
