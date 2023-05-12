from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery, InputFile
from filters.shaxsiy_uchun import Shaxsiy
from keyboards.default.menu_uchun17_04 import menu_buttons
from loader import dp,bot
from keyboards.default.taomlar_uchun import taomlar_buttons
from keyboards.inline.tillar_uchun import tillar_buttons

@dp.message_handler(Shaxsiy(),CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=tillar_buttons)


@dp.callback_query_handler(text="til1")
async def bot_start(xabar: CallbackQuery):
    await xabar.message.answer(f"Assalomu alaykum botga hush kelibsiz!",reply_markup=menu_buttons)


@dp.message_handler(text="Taomlar")
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum botga hush kelibsiz!",reply_markup=taomlar_buttons)




@dp.message_handler(commands="boshlash")
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum botga hush kelibsiz!")




@dp.message_handler(text="Osh")
async def bot_start(message: types.Message):
    rasm_manzil ='https://t.me/UstozShogird/25032'
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzil,caption="""Yaponiyalik Masaru Ibuka degan tog‘aning “Uchdan keyin kech” degan kitobini o’qib ko’ring-a, bola tarbiyasi masalasidagi ko’p fikrlaringiz uyg’un kelishi, yoki umuman to‘g‘ri kelmasligi mumkin. Masalan, men bu borada xayoldan o‘tkazganlarimni shu kitob orqali shuchaki tasdiqlab oldim. Har bir yosh yoki bo‘lajak ota-onalar uchun chindan hayotiy, zarur qo‘llanma ekan. Qo‘llanma ham emas, suhbat deylik, yaxshisi. Chunki, farzand tarbiysidek dunyodagi eng nozik masalada ma’lum kitob, qo’llanma yoki qonun-qoidalar inson tomonidan hech qachon mukammal yaratilgan emas. Ibuka tog‘a ham buni bot-bot takrorlaydi. Siz buni o’qish jarayonida muallif bilan dildan suhbatlashasiz, kezi kelsa bahslashasiz.
Kitobdagi qiziq ma’lumoqtlar va iqtiboslarni siz bilan ham ulashgim keldi:""")

































