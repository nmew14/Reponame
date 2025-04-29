import os

async def handle_txt_upload(client, message):
    if message.document.mime_type != "text/plain":
        await message.reply_text("Only .txt files are allowed.")
        return

    file_path = await message.download()
    await message.reply_text(f"File '{message.document.file_name}' uploaded successfully!")
    os.remove(file_path)  # Remove after confirming receipt
