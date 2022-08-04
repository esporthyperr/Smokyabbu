from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "16011325"))
API_HASH = getenv("API_HASH", "8c423e5f86f7d9819ea96bb6d7d02a")
BOT_TOKEN = getenv("BOT_TOKEN","5497787737:AAufj5Mi04TgplsMS0BogvI0zz9IqNx-mg")
BOT_NAME = getenv("BOT_NAME","𝗛𝗲𝘅𝗼𝗿 𝗕𝗮𝗯𝗮 𝗥𝗲𝗮𝗱𝘆 𝗙𝗼𝗿 𝗙𝗶𝗿𝗲")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
SESSION_NAME = getenv("SESSION_NAME", "BQCrTGrrMMW_PjPTP54N5KLGrD_vpKHQ0XwbpUT-ba_-U2GvVRt8Cf9ep0iifFvLk0iuUULqbcoZJMaFZ7iCafGKOy2tJPp6HZK7LdZ8NEN7zP36OojsHlkAy53FXVevs_71-TQEbTgV-Q8ijR2KQEQ5jnymyO9rwd5JszmpNDITe8yOcOOhu-lzr0Z9wTgRVUL-q-x1VYncB-7YWKCblD3GRjzmcbCtQ-R7RuYslFdA9vgFW2NP4excbpBcTGbsgAH7YeOFE-lW49XXJG98QV_o4v01roDznNDIHFZsICWIV53Yv98bQ7OYnwV8Wn1KVOJJ5-bAEGWeOL6MYYcI5AAAAASx7CR8A")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5080607590").split()))
