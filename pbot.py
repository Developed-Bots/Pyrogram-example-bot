import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

Developedbots = Client(
    "Pyrogram-example-bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)


START_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('SOURCE CODE', url="https://github.com/Developed-Bots/Pyrogram-example-bot")
        ]]
    ) 
@Developedbots.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_photo("https://telegra.ph/file/47d44ef6072f170652ef0.jpg")
    await update.reply_text(
        f""" Hai {update.from_user.mention} am just a pyrogram example bot""", 
        disable_web_page_preview=True,
        reply_markup=START_BUTTON
    )

Developedbots.run()
