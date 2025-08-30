from aiogram.types import ReplyKeyboardMarkup,KeyboardButton



reg_menu = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [KeyboardButton(text='Registration')]
    ]
)

main_menu = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [KeyboardButton(text='Tagamlar'),
         KeyboardButton(text='Ishimlikler')],
         [
             KeyboardButton(text='Biz haqqimizda'),
             KeyboardButton(text='Otziv qaldiriw')
         ]
    ]
)