from config import config
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
app = Client(
    api_id=config.API_ID, api_hash=config.API_HASH, session_name=str(config.SESSION)
)

calls = PyTgCalls(app)

if config.BOT_TOKEN:
    bot = Client(
        "Music",
        api_id=config.API_ID,
        api_hash=config.API_HASH,
        bot_token=config.BOT_TOKEN,
    )
    client = bot
else:
    client = app
