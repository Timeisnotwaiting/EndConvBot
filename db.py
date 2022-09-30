from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
import os

URL = os.environ["URL"]

mongo = MongoClient(URL)
db = mongo.WEB

chatsdb = db.chats

usersdb = db.users

async def add_chat(chat_id: int):
    find = await chatsdb.find_one({"chat_id": chat_id})
    if find:
        return
    await chatsdb.insert_one({"chat_id": chat_id})
    return

async def get_chats():
    all = chatsdb.find({"chat_id": {"$lt": 0}})
    if not all:
        return []
    CHATS = []
    for x in await all.to_list(length=1000000000):
        CHATS.append(x["chat_id"])
    return CHATS

async def add_user(user_id: int):
    find = usersdb.find_one({"user_id": user_id})
    if find:
        return
    await usersdb.insert_one({"user_id": user_id})
    return

async def get_users():
    all = usersdb.find({"user_id": {"gt": 0}})
    if not all:
        return []
    USERS = []
    for x in await all.to_list(length=1000000000):
        USERS.append(x["user_id"])
    return USERS
