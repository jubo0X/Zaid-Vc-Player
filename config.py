## What's up Kangers
## Don't Kang without Creadits else I will rape your mom

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}

SESSION_NAME = getenv("SESSION_NAME")

if str(getenv("STRING_SESSION2")).strip() == "AQAxvsvCS1gUoRQaRXN4wk0RcAz5mI_X6W3CjI_z0zZGzAfV9li-bqmhypOCT69nQ0F2xvF9_il9UaAvSrT5GMB1ldF61fvUOoV3fwjhOuXyOEqwZh79xDSsWrfx3eol6xXApOUH81nYAyBeVSLbyrHxV4S3q9rArcdN8c9_-DEaL4POCpe5duyHXBrhCSJ8sADWff__Bu54s5NwVtXLbDHu5X7VtYvCGj5uBzsZ8lM8rv-ZxSDoImac6cV1O8IgLsfZ13xrcPpftPJWwRQKZ1MwSYUeLQ3DTuA8CesOyz5R32QfReXdffy_nQnTk2nATyOH8B6D5z69QfqNl04EXcM-AAAAAVDdpxEA":
    SESSION2 = str(None)
else:
    SESSION2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "AQAxvsvCS1gUoRQaRXN4wk0RcAz5mI_X6W3CjI_z0zZGzAfV9li-bqmhypOCT69nQ0F2xvF9_il9UaAvSrT5GMB1ldF61fvUOoV3fwjhOuXyOEqwZh79xDSsWrfx3eol6xXApOUH81nYAyBeVSLbyrHxV4S3q9rArcdN8c9_-DEaL4POCpe5duyHXBrhCSJ8sADWff__Bu54s5NwVtXLbDHu5X7VtYvCGj5uBzsZ8lM8rv-ZxSDoImac6cV1O8IgLsfZ13xrcPpftPJWwRQKZ1MwSYUeLQ3DTuA8CesOyz5R32QfReXdffy_nQnTk2nATyOH8B6D5z69QfqNl04EXcM-AAAAAVDdpxEA":
    SESSION3 = str(None)
else:
    SESSION3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "AQAxvsvCS1gUoRQaRXN4wk0RcAz5mI_X6W3CjI_z0zZGzAfV9li-bqmhypOCT69nQ0F2xvF9_il9UaAvSrT5GMB1ldF61fvUOoV3fwjhOuXyOEqwZh79xDSsWrfx3eol6xXApOUH81nYAyBeVSLbyrHxV4S3q9rArcdN8c9_-DEaL4POCpe5duyHXBrhCSJ8sADWff__Bu54s5NwVtXLbDHu5X7VtYvCGj5uBzsZ8lM8rv-ZxSDoImac6cV1O8IgLsfZ13xrcPpftPJWwRQKZ1MwSYUeLQ3DTuA8CesOyz5R32QfReXdffy_nQnTk2nATyOH8B6D5z69QfqNl04EXcM-AAAAAVDdpxEA":
    SESSION4 = str(None)
else:
    SESSION4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "AQAxvsvCS1gUoRQaRXN4wk0RcAz5mI_X6W3CjI_z0zZGzAfV9li-bqmhypOCT69nQ0F2xvF9_il9UaAvSrT5GMB1ldF61fvUOoV3fwjhOuXyOEqwZh79xDSsWrfx3eol6xXApOUH81nYAyBeVSLbyrHxV4S3q9rArcdN8c9_-DEaL4POCpe5duyHXBrhCSJ8sADWff__Bu54s5NwVtXLbDHu5X7VtYvCGj5uBzsZ8lM8rv-ZxSDoImac6cV1O8IgLsfZ13xrcPpftPJWwRQKZ1MwSYUeLQ3DTuA8CesOyz5R32QfReXdffy_nQnTk2nATyOH8B6D5z69QfqNl04EXcM-AAAAAVDdpxEA":
    SESSION5 = str(None)
else:
    SESSION5 = str(getenv("STRING_SESSION5"))

BOT_TOKEN = getenv("BOT_TOKEN", "5004985412:AAEpITTke1e8mWg9uaNr8fmtfRP3GlK8Ab8")
BOT_NAME = getenv("BOT_NAME", "Red Zone")

API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://redzone:redzone@cluster0.usrv3w1.mongodb.net/?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME", "RED ZONE")
OWNER_USERNAME = getenv("OWNER_USERNAME", "MiNdX69")
ALIVE_NAME = getenv("ALIVE_NAME", "RED ZONE")
BOT_USERNAME = getenv("BOT_USERNAME", "VideoXRobot")
OWNER_ID = getenv("OWNER_ID", "1844303560")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "RED ZONE_Assistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "TheSupportChat")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "TheUpdatesChannel")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5181756679").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/a414e2cdfeaa7d4414b89.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ZAID/Zaid-Vc-Player")
PLAY_IMG = getenv("PLAY_IMG", "https://telegra.ph/file/10b1f781170b1e1867f68.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/b95c13eef1ebd14dbb458.png")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
VIDEO_IMG = getenv("VIDEO_IMG", "https://telegra.ph/file/6213d2673486beca02967.png")
SKIP_IMG = getenv("SKIP_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
NEXT_IMG = getenv("NEXT_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
HEROKU_MODE = getenv("HEROKU_MODE", None)
