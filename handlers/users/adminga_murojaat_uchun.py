from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp,bot
from states.holatlar import Murojaat
from keyboards.default.tasdiqlash_uchun import tasdiqlash_buttons
from keyboards.default.menu_uchun17_04 import menu_buttons
# Echo bot
@dp.message_handler(text="Adminga murojaat", )
async def bot_echo(message: types.Message):
    await message.answer(text="Ismni kiriting")
    await Murojaat.ism_qabul_qilish.set()


@dp.message_handler(state=Murojaat.ism_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    matn = message.text
    await state.update_data({"ism":matn})
    await message.answer(text="Familyani kiriting")
    await Murojaat.familya_qabul_qilish.set()


@dp.message_handler(state=Murojaat.familya_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    matn  = message.text
    await state.update_data({"fam":matn})
    await message.answer(text="Yoshni kiriting")
    await Murojaat.yosh_qabul_qilish.set()

@dp.message_handler(state=Murojaat.yosh_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    matn  = message.text
    await state.update_data({"yosh":matn})
    await message.answer(text="No'merni kiriting")
    await Murojaat.tel_qabul_qilish.set()

@dp.message_handler(state=Murojaat.tel_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    matn  = message.text
    await state.update_data({"tel":matn})
    await message.answer(text="Manzilni kiriting")
    await Murojaat.manzil_qabul_qilish.set()

@dp.message_handler(state=Murojaat.manzil_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    matn  = message.text
    await state.update_data({"manzil":matn})
    await message.answer(text="Murojaat kiriting")
    await Murojaat.murojaat_qabul_qilish.set()

@dp.message_handler(state=Murojaat.murojaat_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    matn  = message.text
    await state.update_data({"murojaat":matn})

    malumot = await state.get_data()
    ismi = malumot.get('ism')
    familya = malumot.get('fam')
    yoshi = malumot.get('yosh')
    nomer = malumot.get('tel')
    manzil = malumot.get('manzil')
    text = malumot.get('murojaat')

    ekranga_chiqarish = f"Ism : {ismi} \n" \
                        f"Familya : {familya} \n" \
                        f"Yosh : {yoshi}\n" \
                        f"Tel : {nomer} \n" \
                        f"Manzil : {manzil} \n" \
                        f"Murojaat : {text} \n"
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id,text=ekranga_chiqarish,reply_markup=tasdiqlash_buttons)
    await Murojaat.tasdiqlash_holati.set()

@dp.message_handler(state=Murojaat.tasdiqlash_holati,text="Bekor qilish")
async def bot_echo(message: types.Message,state:FSMContext):
    await bot.send_message(chat_id=message.from_user.id,text="Bekor qilindi !!!",reply_markup=menu_buttons
    )
    await state.finish()

@dp.message_handler(state=Murojaat.tasdiqlash_holati,text="Tasdiqlash")
async def bot_echo(message: types.Message,state:FSMContext):
    malumot = await state.get_data()
    ismi = malumot.get('ism')
    familya = malumot.get('fam')
    yoshi = malumot.get('yosh')
    nomer = malumot.get('tel')
    manzil = malumot.get('manzil')
    text = malumot.get('murojaat')

    ekranga_chiqarish = f"Ism : {ismi} \n" \
                        f"Familya : {familya} \n" \
                        f"Yosh : {yoshi}\n" \
                        f"Tel : {nomer} \n" \
                        f"Manzil : {manzil} \n" \
                        f"Murojaat : {text} \n"
    await bot.send_message(chat_id='5883029982',text=ekranga_chiqarish)
    await bot.send_message(chat_id=message.from_user.id,text="Adminga yuborildi")
    await state.finish()