from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_kd= ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='СОздать группу'),
            KeyboardButton(text='Редакт группы')
        ],[

            KeyboardButton(text='Удалитэ')],
            KeyboardButton(text='Отмена')
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)