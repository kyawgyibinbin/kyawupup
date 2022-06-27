from pyrogram import Client
from database.access import kyawwa
from pyrogram.types import Message


async def AddUser(bot: Client, update: Message):
    if not await kyawwa.is_user_exist(update.from_user.id):
           await kyawwa.add_user(update.from_user.id)
