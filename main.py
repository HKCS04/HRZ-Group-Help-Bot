from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import random
from pyrogram.errors import UserNotParticipant

HRZ = Client(
   "GroupHelpBot",
   api_id=API_ID,
   api_hash=API_HASH,
   bot_token=BOT_TOKEN
)

API_ID = int(os.environ.get("API_ID", ""))

API_HASH = os.environ.get("API_HASH", "")
             
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
             
PICS = os.environ.get("PICS", "")
             
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
@HRZ.on_message(filters.command(["help"]) & filters.private)
async def help(client, message):
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
async def ban(self, message):
        if not message.reply_to_message:
            return message.send_response('Use this command responding to a message written by the user to ban.')
        group_id = message.chat.id
        moderator = message.from_user
        banned = message.reply_to_message.from_user
        try:
            self.bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
        except ApiException as e:
            return send_error(message, e)
        msg = message.response('<code>{b} ({bi})</code> banned by <code>{m} ({mi})</code>'.format(
            **escape_items(b=get_name(banned), bi=banned.id, m=get_name(moderator), mi=moderator.id)),
            parse_mode='html')
        inline = msg.inline_keyboard()
        inline.add_button('Unban', callback=self.unban_button, callback_kwargs={'u': banned.id})
        msg.send()
        self.ban_db(group_id, moderator, banned)

            
print("Bot Started..!") 
                                 
HRZ.run()
  
