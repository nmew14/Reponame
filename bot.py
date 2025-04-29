import os
from pyrogram import Client, filters
from app.uploader import handle_txt_upload

API_ID = int(os.getenv("28748671"))
API_HASH = os.getenv("f53ec7c41ce34e6d585674ed9ce6167c")
BOT_TOKEN = os.getenv("7820500746:AAHJXoIVZH750objwgQAcVtbr4BFK8Au8GU")
USER_ID = int(os.getenv("1169394017"))

app = Client("drm_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.document & filters.user(USER_ID))
async def txt_handler(client, message):
    await handle_txt_upload(client, message)

@app.on_message(filters.command("start") & filters.private & filters.user(USER_ID))
async def start(client, message):
    await message.reply_text("Welcome! Send me a .txt file to upload.")

app.run()
