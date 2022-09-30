from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "8557622"))
API_HASH = getenv("API_HASH", "d33c3ed0c253f1bc5bb7166ac0da4d73")
BOT_TOKEN = getenv("BOT_TOKEN","5497787737:AAH4dhYSpLdXLAkYK_Pf0fmEk2xE_TgjCS0")
BOT_NAME = getenv("BOT_NAME","Smoker")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
SESSION_NAME = getenv("SESSION_NAME", "BQBxe3BH_sDCY72dTNriOBj3a4zAq5sI-F6d7Fpioca-JjXFFZ1iSmRjZfyhDFOLew4Wg4GxoSgV6ZFLep9w_l4yXP1aFXN62FVCiSNqy0zAOP28fz7K6xKHfvs3iJ1uk4GC9FjfgbudvJOXj6QKbmHxZhO4YMf24fdzWodrMVdUWNT3HYcu0mFBoEwAfFtfgK-ehxfYKyi6iDbeAjqXfLAwLdqEKZSTUfuP_SZu8Ojsbx9v8504LPdEUi017fRx2X_MEAp-8sQcP105Aoc2VluajDF2mNHTy1ehsQJdgVgweYraULED85cCjZRJcJZVIvZ6E8mj_EF2NeohkPipY32-dxJEnwA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . ?").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5080607590").split()))
