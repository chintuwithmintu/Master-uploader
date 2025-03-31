import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7703142204:AAFjjhJTkQVsU7drBWd733F6lH357mz-JVE")  # Ensure correct key name
    API_ID = int(os.environ.get("API_ID", "29940750"))  # Added key name and default value
    API_HASH = os.environ.get("API_HASH", "33412ad3b366ca991309d1bcbb472c32")  # Added key name for consistency

    AUTH_USER = os.environ.get("AUTH_USERS", "7618270428").split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]  # Ensuring list of integers

    HOST = os.environ.get("HOST", "https://api.masterapi.tech")  # Keeping HOST configurable
    CREDIT = os.environ.get("CREDIT", "𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎")  # Making CREDIT an environment variable for flexibility
