from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "8557622"))
API_HASH = getenv("API_HASH", "d33c3ed0c253f1bc5bb7166ac0da4d73")
BOT_TOKEN = getenv("BOT_TOKEN","5497787737:AAH-vPHnNvQt0AJ2XzTwl5AsMz4URNkna7U")
BOT_NAME = getenv("BOT_NAME","Smoker")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
SESSION_NAME = getenv("SESSION_NAME", "BQBfG4RGqij2Mrh-BCSilB4TBFJ7Or8smn3hnfr9yQx2hk28UtBEBqb44E-tHGRGsB0sSnwIOqfnU4VPSp280biBOdt1dzUK8plaOuyonzzUaC2vpCjPhfbSK5GvaioX0mUefwnHjChyckOAauhwSkE1yoYjXWGokbOgc0eCkseP7pS-v59dlgqb3lp0tgZlgMtIcaB6orSQhdxN81UotcQT4yZQ_98JRzI2Gnc9GlO44hMNIBjgHpqMTABuPJ7bcUFBIVWjfGF66uKjIFjoIIY7Cl-tnPF-oXtLpx6YRyonHVbgA-vJ3yeYdbAIpZiHobmqAXBYxnlBM30QSo9m7sS6dxJEnwA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . ?").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5080607590").split()))
