import os
from pyrogram import Client, filters
from app.uploader import handle_txt_upload

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
USER_ID = int(os.getenv("USER_ID"))

app = Client("drm_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.document & filters.user(USER_ID))
async def txt_handler(client, message):
    await handle_txt_upload(client, message)

@app.on_message(filters.command("start") & filters.private & filters.user(USER_ID))
async def start(client, message):
    await message.reply_text("Welcome! Send me a .txt file to upload.")

app.run()
