from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

taomlar_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Osh"),
            KeyboardButton(text="Lag'mon")
        ],
        [
           KeyboardButton(text="Sho'rva"),
            KeyboardButton(text="Mastava")
        ]
    ],
    resize_keyboard=True
)