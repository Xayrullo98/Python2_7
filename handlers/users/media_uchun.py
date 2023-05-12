from aiogram import types
from aiogram.types import ContentTypes

from loader import dp,bot


# Echo bot
@dp.message_handler(content_types=ContentTypes.DOCUMENT)
async def bot_echo(message: types.Message):
    await message.document.download()
    await message.answer(text="Dakument qabul qilindi")


@dp.message_handler(content_types=ContentTypes.STICKER)
async def bot_echo(message: types.Message):
    await message.sticker.download()
    await message.answer(text="Stiker qabul qilindi")


@dp.message_handler(content_types=ContentTypes.PHOTO)
async def bot_echo(message: types.Message):
    await message.photo[-1].download()
    await message.answer(text="Rasm qabul qilindi")