from aiogram import Bot

async def tekshirish1(user_id,kanal_link):
    user = Bot.get_current()

    malumot = await user.get_chat_member(chat_id=kanal_link,user_id=user_id)
    return malumot.is_chat_member()