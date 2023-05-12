from aiogram import types
from aiogram.types import ContentTypes

from loader import dp, bot
from filters import Guruh

# Echo bot
@dp.message_handler(Guruh(),commands='start')
async def bot_echo(message: types.Message):
    await message.answer(text="Guruhga hush kelibsiz")


@dp.message_handler(Guruh(),text="Salom")
async def bot_echo(message: types.Message):
    await message.answer(text="Assalomu alaykum guruhga hush kelibsiz")


@dp.message_handler(Guruh(),content_types=ContentTypes.NEW_CHAT_MEMBERS)
async def bot_echo(message: types.Message):
    ism = message.new_chat_members[0].full_name
    chat_id = message.chat.id
    message_id = message.message_id
    await bot.send_message(chat_id=chat_id,text=f"{ism} Guruhga hush kelibsiz")
    await bot.delete_message(chat_id=chat_id,message_id=message_id)

@dp.message_handler(Guruh(),content_types=ContentTypes.LEFT_CHAT_MEMBER)
async def bot_echo(message: types.Message):
    ism = message.left_chat_member.full_name
    chat_id = message.chat.id
    message_id = message.message_id
    await bot.send_message(chat_id=chat_id,text=f"{ism} Guruhni tark etdi")
    await bot.delete_message(chat_id=chat_id, message_id=message_id)


@dp.message_handler(Guruh())
async def bot_echo(message: types.Message):
    text = message.text
    if 'https:' in text:
        ism = message.from_user.full_name
        chat_id = message.chat.id
        user_id = message.from_user.id
        message_id = message.message_id
        await bot.kick_chat_member(chat_id=chat_id,user_id=user_id,)
        await bot.send_message(chat_id=chat_id,text=f"{ism} Guruhni tark etdi guruhda reklama tarqatmang")

        await bot.delete_message(chat_id=chat_id, message_id=message_id)