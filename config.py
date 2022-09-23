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
SESSION_NAME = getenv("SESSION_NAME", "BQC9bS4i9llfJmUMdcnFyqPtXrpnhcT3VzIZttxlzyOoDF9HXyK0PlvC8OWubkpdlqcOgEarP-ucT0pElUdznvOaDe5HbOr-yuOdnOYLz9pGsko8G7HLYc8i2A_w5ZcljX2SofBjTQYYozOjsXOjVocE0N9KPiM9eg_90bG7EN2oZojWnqGVglgVpZtnV717_i5NB5BjwIQSO3bEitagOIxTysu8wRCVKdbYlcEkAuTgAWrHilFmCibxSJyU3173OCpXdo4_Ijk4MKRlBp9Dk9rN3JBWddt6Bd6WdMlv3p1_i6H-OYlexnzmWwFcoLqJfNtf7NAZPPIrjzSbKxg9sdtrdxJEnwA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . ?").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5080607590").split()))
