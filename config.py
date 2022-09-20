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
SESSION_NAME = getenv("SESSION_NAME", "BQCwvUFs5wuek2cfFEw76NxUzlHvX_V9M3jN2tq_I__BpoC2v16_SWY_BNV12QlPEYTDTKGrla10VZLEM24h7HF5Ox5Iptnp2EglkqIh9WYuZUHlRjeGXUcMiNDFAhDgasDEnA0jAJIgyD05LFetOEA2FH_e_4th6GvwsKyXOLYHwlYNgxca58vP9S80s1_l-ysH0xjYeOWsjmaPNizJ7ToCfHA6brc7YmpcCwUAs0jCwjMnufTj2hInqLN2ob3eQk-zI7HeQnJYjNYU49Wa5CUi9zdhDmf75eB4DdFMjeewPeYsboQ8bNBZDIyu2LZ4uRCAF3zA606sonk3CyNgBCVqdxJEnwA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . ?").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5080607590").split()))
