from dotenv import load_dotenv
from os import getenv

load_dotenv()

# Required Variables
API_ID = int(getenv("API_ID", "29869097"))
API_HASH = getenv("API_HASH", "b011037acfaf24f5dd4b5dda104c55fe")
BOT_TOKEN = getenv("BOT_TOKEN", "7944281902:AAE8DEXG9mEtvTgC3PCdPYYDLMJ7FvWgW74")
STRING_SESSION = getenv("STRING_SESSION", None)
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002028213552"))


# Optional Variables
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", ". !").split())


# Don't Change After This Line.
COMMAND_HANDLERS = []
for x in COMMAND_PREFIXES:
    COMMAND_HANDLERS.append(x)
COMMAND_HANDLERS.append('')
