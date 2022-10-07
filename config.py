from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "10411557"))
API_HASH = getenv("API_HASH", "cfca2614e8c5a0375c389f36c2b89cd8")
BOT_TOKEN = getenv("BOT_TOKEN","5497787737:AAH4dhYSpLdXLAkYK_Pf0fmEk2xE_TgjCS0")
BOT_NAME = getenv("BOT_NAME","Smoker")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
SESSION_NAME = getenv("SESSION_NAME", "BQB9A53qtWtUC83la8kja5OB6FNohfcGR5f13YNNGHmiK9NF4DSRLGLxU5Nt5pATKzrskiJ7rPVXRjhSVqLRPj_erFarzIUF_LGfDUl9vHi6kXslNY23_6zxmK6sREbvy40khCHy6YXcvchaO5oc9mBFqQ3ZSO_gvkDnObLflJmgxT5DTRoNTMAdEuQvve5SJifSUtcaQn54L-kY709U-A05kagVsOoxiOER3MF1WzRq4dlIXEhPUUXGtfjeJN3e2jEpibFPXjSGy-AHfBYs26WEchZsPbX1OTMt9pT9a8HgDSE_197V2MRSwLqnByMPiAwuBl9Ywp7FN55dJSRhcT-sAAAAATuJ4lMA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . ?").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5080607590").split()))
