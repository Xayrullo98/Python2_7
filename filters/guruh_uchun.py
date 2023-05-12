from aiogram.dispatcher.filters import BoundFilter
from aiogram import types

class Guruh(BoundFilter):
    async def check (self,message:types.Message):
        return message.chat.type == types.ChatType.SUPERGROUP