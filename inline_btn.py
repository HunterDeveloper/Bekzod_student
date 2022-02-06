from telegram import InlineKeyboardButton, InlineKeyboardMarkup


btn = InlineKeyboardMarkup([
    [InlineKeyboardButton('Понедельник', callback_data='понедельник'),
     InlineKeyboardButton('Вторник', callback_data='вторник')],
    [InlineKeyboardButton('Среда', callback_data='среда'),
     InlineKeyboardButton('Четверг', callback_data='четверг')],
    [InlineKeyboardButton('Пятница', callback_data='пятница'),
     InlineKeyboardButton('Суббота', callback_data='суббота')],
])