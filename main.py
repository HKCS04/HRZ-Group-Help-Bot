import os
from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import random
from pyrogram.errors import UserNotParticipant
from bot.extract_user import extract_user
from bot.extract_time import extract_time

HRZ = Client(
   "GroupHelpBot",
   api_id=int(os.environ.get("API_ID", "")),
   api_hash=os.environ.get("API_HASH", ""),
   bot_token=os.environ.get("BOT_TOKEN", "")
)

API_ID = int(os.environ.get("API_ID", ""))

API_HASH = os.environ.get("API_HASH", "")
             
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
             
PICS = [
 "https://telegra.ph/file/736d8009b207d02a937bf.jpg"
]
             
force_channel = os.environ.get("FORCE_CHANNEL", "")
             
@HRZ.on_message(filters.command(["start"]) & filters.private)
async def start(client, message):
    if force_channel:
        try:
            user = await client.get_chat_member(force_channel, message.from_user.id)
            if user.status == "kicked out":
                await message.reply_text("You Are Banned")
                return
        except UserNotParticipant :
            await message.reply_text(
                text="🔊 𝗝𝗼𝗶𝗻 𝗢𝘂𝗿 𝗠𝗮𝗶𝗻 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 🤭\nPlease Join our Channel to use this Bot..!",
                reply_markup=InlineKeyboardMarkup( [[
                 InlineKeyboardButton("🔊 𝗝𝗼𝗶𝗻 𝗢𝘂𝗿 𝗠𝗮𝗶𝗻 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 🤭", url=f"t.me/{force_channel}")
                 ]]
                 )
            )
            return
    await message.reply_photo(
        photo=random.choice(PICS),
        caption=f"""**Hi {message.from_user.mention} 👋

I am [Group Help Bot](http://t.me/HRZGroupHelpBot) Created By [HRZ TG](t.me/TheHRZTG)... 😎
I can manage your group or supergroup with Powerful Features... 🔥

Add me to a group and make me Admin to show my powers... 😍

Just hit /help to see my commands and how they work... 😁**""",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("➕ Add me to your Group ➕", url="http://t.me/HRZGroupHelpBot?startgroup=start"),
            ],[
            InlineKeyboardButton("📢 Channel", url="t.me/TheHRZTG"),
            InlineKeyboardButton("👥 Support Group", url="t.me/HRZSupport"),
            ],[
            InlineKeyboardButton("🛠 Help", callback_data="help"),
            InlineKeyboardButton("🤠 About", callback_data="about")
            ]]
            )
        )
             
@HRZ.on_message(filters.command(["help"]) & filters.private)
async def help(client, message):
    await message.reply_photo(
        photo=random.choice(PICS),
        caption=f"""**Hey {message.from_user.mention} 👋

Welcome to Help menu of [Group Help Bot](http://t.me/HRZGroupHelpBot)..!**""",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("💁🏼‍♂️ Basic Commands", callback_data="commands"),
            ],[
            InlineKeyboardButton("🏡 Home", callback_data="start"),
            InlineKeyboardButton("🔙 Back", callback_data="start")
            ]]
            )
        )
@HRZ.on_message(filters.command(["about"]) & filters.private)
async def about(client, message):
    await message.reply_photo(
        photo=random.choice(PICS),
        caption=f"""**Hey {message.from_user.mention} 👋
        
Welcome to About menu of [Group Help Bot](http://t.me/HRZGroupHelpBot)..!

亗 Name      : [Group Help Bot](http://t.me/HRZGroupHelpBot)
亗 Developer : [HRZ 🇮🇳](t.me/HRZRobot)
亗 Language  : [Python](https://python.org)
亗 Library   : [Pyrogrsm](https://pyrogram.org)
亗 Channel   : [HRZ TG](t.me/TheHRZTG)
亗 Support   : [HRZ Support](t.me/HRZSupport)
亗 Server    : [Somewhere](t.me/HRZRobot)
亗 Source    : [Click Here](t.me/HRZRobot)**""",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("🏡 Home", callback_data="start"),
            InlineKeyboardButton("🔙 Back", callback_data="help")
            ]]
            )
        )

@HRZ.on_message(filters.command(["ban"]) & filters.group)
async def ban(_, message):
    user_id, user_first_name, _ = extract_user(message)

    try:
        await message.chat.ban_member(user_id=user_id)
    except Exception as error:
        await message.reply_text(str(error))
    else:
        if str(user_id).lower().startswith("@"):
            await message.reply_text(f"""**Someone is breaked the limit..!
{message.from_user.mention} is Banned ⚠"""
            )
        else:
            await message.reply_text(
                "Someone is also breaked the limit..! "
                f"<a href='tg://user?id={user_id}'>"
                f"{user_first_name}"
                "</a>"
                "Banned ⚠"
            )

@HRZ.on_message(filters.command(["unban"]) & filters.group)
async def unban(_, message):
    user_id, user_first_name, _ = extract_user(message)

    try:
        await message.chat.unban_member(user_id=user_id)
    except Exception as error:
        await message.reply_text(str(error))
    else:
        if str(user_id).lower().startswith("@"):
            await message.reply_text(
                "Ok, You are Unbanned Now ✔ "
                f"{user_first_name}"
                "You can Join the group..!"
            )
        else:
            await message.reply_text(
                "Ok, You are Unbanned Now ✔ "
                f"<a href='tg://user?id={user_id}'>"
                f"{user_first_name}"
                "You can Join the group..!"
            )

            
print("Bot Started..!") 
                                 
HRZ.run()
  
