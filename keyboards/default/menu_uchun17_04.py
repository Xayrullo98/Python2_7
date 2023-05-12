from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menu_buttons = ReplyKeyboardMarkup(
    keyboard=[
         [
            KeyboardButton(text="Taomlar"),
            KeyboardButton(text="Ichimliklar")
         ],
        [
            KeyboardButton(text="Shirinliklar"),
            KeyboardButton(text="Fast food")
        ],
        [
            KeyboardButton(text="Adminga murojaat" )

        ]
    ],
    resize_keyboard=True
)