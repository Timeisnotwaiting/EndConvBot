from pyrogram import Client, filters, idle
import os
from db import *

API_ID = int(os.getenv("API_ID", None))
API_HASH = os.getenv("API_HASH", None)
BOT_TOKEN = os.getenv("BOT_TOKEN", None)

yashu = Client(":alpha:", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@yashu.on_message(filters.command("add"))
async def add(_, m):
    to_add = int(m.text.split()[1])
    try:
        await add_user(to_add)
        await m.reply("added")
    except Exception as e:
        await m.reply(e)

@yashu.on_message(filters.command(["webp", "webm"]))
async def conv(_, m):
    if not m.reply_to_message:
        return await m.reply(f"<i>reply to a sticker..!</i>")
    if not m.reply_to_message.sticker:
        return await m.reply(f"<i>reply to a sticker..!</i>")
    command = m.text.split()[0][4]
    id = m.from_user.id
    if command.lower() == "p":
        await _.download_media(m.reply_to_message, file_name=f"{id}.webp")
        await _.send_document(m.chat.id, f"downloads/{id}.webp", force_document=True)
        return 
    else:
        await _.download_media(m.reply_to_message, file_name=f"{id}.webm")
        await _.send_document(m.chat.id, f"downloads/{id}.webm", force_document=True)
  
@yashu.on_message(filters.command("start"))
async def start(_, m):
    await add_user(m.from_user.id)
    await m.reply(f"Hello..! {m.from_user.first_name}, myself sticker converter bot..!\n\nhelps you to convert given sticker into WEBP and WEBM formats.\n\nFor queries @Timeisnotwaiting, hit /help to check commands out..!")

@yashu.on_message(filters.command("help"))
async def help(_, m):
    await m.reply("COMMANDS EXPLANATION\n\n/webp - to convert replied sticker into WEBP format.\n/webm - to convert replied sticker into WEBM format.")   

@yashu.on_message(group=1)
async def cwf(_, m):
    await add_chat(m.chat.id)

@yashu.on_message(filters.command("served") & filters.user(5429087029))
async def served(_, m):
    USERS = await get_users()
    CHATS = await get_chats()
    u_msg = ""
    for x in USERS:
        u_msg += f"{x}\n"
    c_msg = ""
    for y in CHATS:
        c_msg += f"{y}\n"
    await m.reply(f"Chats :-\n\n{c_msg}\nCount :- {len(CHATS)}\n\nUsers :-\n\n{u_msg}\nCount :- {len(USERS)}")


yashu.start()
get = yashu.get_me()
um = get.username
print(f"@{um} started successfully..!")
idle()
