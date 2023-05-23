import os
from typing import Tuple, Union
from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message, User, Chat
import random
from datetime import datetime, timedelta
from pyrogram.errors import UserNotParticipant
from pyrogram.enums import MessageEntityType

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
 "https://telegra.ph/file/cc4e670c97263c4984091.png"
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
      
# extract_user

def extract_user(message: Message) -> Tuple[int, str, Union[Chat, User]]:
    """extracts the user from a message"""
    user_id = None
    user_first_name = None
    aviyal = None

    if len(message.command) > 1:
        if (
            len(message.entities) > 1 and
            message.entities[1].type == MessageEntityType.TEXT_MENTION
        ):
            # 0: is the command used
            # 1: should be the user specified
            required_entity = message.entities[1]
            user_id = required_entity.user.id
            user_first_name = required_entity.user.first_name
            aviyal = required_entity.user
        else:
            user_id = message.command[1]
            # don't want to make a request -_-
            user_first_name = user_id
            aviyal = True

        try:
            user_id = int(user_id)
        except ValueError:
            pass

    elif message.reply_to_message:
        user_id, user_first_name, aviyal = _eufm(message.reply_to_message)

    elif message:
        user_id, user_first_name, aviyal = _eufm(message)

    return (user_id, user_first_name, aviyal)

# extract_time

def extract_time(time_val):
    if any(time_val.endswith(unit) for unit in ("s", "m", "h", "d")):
        unit = time_val[-1]
        time_num = time_val[:-1]  # type: str
        if not time_num.isdigit():
            return None

        if unit == "s":
            bantime = datetime.now() + timedelta(seconds=int(time_num))
        elif unit == "m":
            bantime = datetime.now() + timedelta(minutes=int(time_num))
        elif unit == "h":
            bantime = datetime.now() + timedelta(hours=int(time_num))
        elif unit == "d":
            bantime = datetime.now() + timedelta(days=int(time_num))
        else:
            # how even...?
            return None
        return bantime
    else:
        return None
   
# _enufm

def _eufm(message: Message) -> Tuple[int, str, Union[Chat, User]]:
    user_id = None
    user_first_name = None
    ithuenthoothengaa = None

    if message.from_user:
        ithuenthoothengaa = message.from_user
        user_id = ithuenthoothengaa.id
        user_first_name = ithuenthoothengaa.first_name

    elif message.sender_chat:
        ithuenthoothengaa = message.sender_chat
        user_id = ithuenthoothengaa.id
        user_first_name = ithuenthoothengaa.title

    return (user_id, user_first_name, ithuenthoothengaa)

# Ban Command Available in Groups

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
{user_first_name} is Banned ⚠"""
            )
            
# UnBan Command Available in Groups

@HRZ.on_message(filters.command(["unban"]) & filters.group)
async def unban(_, message):
    user_id, user_first_name, _ = extract_user(message)

    try:
        await message.chat.unban_member(user_id=user_id)
    except Exception as error:
        await message.reply_text(str(error))
    else:
        if str(user_id).lower().startswith("@"):
            await message.reply_text(f"""Ok, You are Unbanned Now ✔ 
{user_first_name} can Join the group..!"""
            )
# last_online

def last_online(from_user: User) -> str:
    time = ""
    if from_user.is_bot:
        time += "🤖 Bot :("
    elif from_user.status == "recently":
        time += "Recently"
    elif from_user.status == "within_week":
        time += "Within the last week"
    elif from_user.status == "within_month":
        time += "Within the last month"
    elif from_user.status == "long_time_ago":
        time += "A long time ago :("
    elif from_user.status == "online":
        time += "Currently Online"
    elif from_user.status == "offline":
        time += datetime.fromtimestamp(from_user.last_online_date).strftime(
            "%a, %d %b %Y, %H:%M:%S"
        )
    return time

#get_file_id

def get_file_id(msg):
    if msg.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            "sticker"
        ):
            obj = getattr(msg, message_type)
            if obj:
                setattr(obj, "message_type", message_type)
                return obj
# Markup

def markup():
    return InlineKeyboardMarkup

# Button

def button():
    return InlineKeyboardButton

            
# ShowId Command Available in PM and Groups
            
@HRZ.on_message("showid")
async def showid(client, message):
    chat_type = message.chat.type
    if chat_type == enums.ChatType.PRIVATE:
        user_id = message.chat.id
        first = message.from_user.first_name
        last = message.from_user.last_name or ""
        username = message.from_user.username
        dc_id = message.from_user.dc_id or ""
        await message.reply_text(
            f"<b>亗 First Name:</b> {first}\n<b>亗 Last Name:</b> {last}\n<b>亗 Username:</b> {username}\n<b>亗 Telegram ID:</b> <code>{user_id}</code>\n<b>亗 Data Centre:</b> <code>{dc_id}</code>",
            quote=True
        )

    elif chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        _id = ""
        _id += (
            "<b>亗 Chat ID</b>: "
            f"<code>{message.chat.id}</code>\n"
        )
        if message.reply_to_message:
            _id += (
                "<b>亗 User ID</b>: "
                f"<code>{message.from_user.id if message.from_user else 'Anonymous'}</code>\n"
                "<b>亗 Replied User ID</b>: "
                f"<code>{message.reply_to_message.from_user.id if message.reply_to_message.from_user else 'Anonymous'}</code>\n"
            )
            file_info = get_file_id(message.reply_to_message)
        else:
            _id += (
                "<b>亗 User ID</b>: "
                f"<code>{message.from_user.id if message.from_user else 'Anonymous'}</code>\n"
            )
            file_info = get_file_id(message)
        if file_info:
            _id += (
                f"<b>{file_info.message_type}</b>: "
                f"<code>{file_info.file_id}</code>\n"
            )
        await message.reply_text(
            _id,
            quote=True
        )

@HRZ.on_message("who_is")
async def who_is(client, message):
    status_message = await message.reply_text(
        "`Fetching user info...`"
    )
    await status_message.edit(
        "`Processing user info...`"
    )
    from_user = None
    from_user_id, _ = extract_user(message)
    try:
        from_user = await client.get_users(from_user_id)
    except Exception as error:
        await status_message.edit(str(error))
        return
    if from_user is None:
        return await status_message.edit("no valid user_id / message specified")
    message_out_str = ""
    message_out_str += f"<b>亗 First Name:</b> {from_user.first_name}\n"
    last_name = from_user.last_name or "<b>None</b>"
    message_out_str += f"<b>亗 Last Name:</b> {last_name}\n"
    message_out_str += f"<b>亗 Telegram ID:</b> <code>{from_user.id}</code>\n"
    username = from_user.username or "<b>None</b>"
    dc_id = from_user.dc_id or "[User Doesn't Have A Valid DP]"
    message_out_str += f"<b>亗 Data Centre:</b> <code>{dc_id}</code>\n"
    message_out_str += f"<b>亗 User Name:</b> @{username}\n"
    message_out_str += f"<b>亗 User 𝖫𝗂𝗇𝗄:</b> <a href='tg://user?id={from_user.id}'><b>Click Here</b></a>\n"
    if message.chat.type in ((enums.ChatType.SUPERGROUP, enums.ChatType.CHANNEL)):
        try:
            chat_member_p = await message.chat.get_member(from_user.id)
            joined_date = (
                chat_member_p.joined_date or datetime.now()
            ).strftime("%Y.%m.%d %H:%M:%S")
            message_out_str += (
                "<b>亗 Joined this Chat on:</b> <code>"
                f"{joined_date}"
                "</code>\n"
            )
        except UserNotParticipant:
            pass
    chat_photo = from_user.photo
    if chat_photo:
        local_user_photo = await client.download_media(
            message=chat_photo.big_file_id
        )
        buttons = [[
            button()('🔐 Close', callback_data='close_data')
        ]]
        reply_markup = markup()(buttons)
        await message.reply_photo(
            photo=local_user_photo,
            quote=True,
            reply_markup=reply_markup,
            caption=message_out_str,
            parse_mode=enums.ParseMode.HTML,
            disable_notification=True
        )
        os.remove(local_user_photo)
    else:
        buttons = [[
            button()('🔐 Close', callback_data='close_data')
        ]]
        reply_markup = markup()(buttons)
        await message.reply_text(
            text=message_out_str,
            reply_markup=reply_markup,
            quote=True,
            parse_mode=enums.ParseMode.HTML,
            disable_notification=True
        )
    await status_message.delete()
   


            
print("Bot Started..!") 
                                 
HRZ.run()
  
