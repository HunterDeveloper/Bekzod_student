from turtle import update
from telegram.ext import *
import db_help
from db_help import *
from inline_btn import *
from conv import *
from telegram.ext import CallbackQueryHandler
db=db_help.royhat("royhat.db")

def start(up, ct):
    id=up.message.from_user.id
    if db.check_user(id):
        ct.bot.send_message(id, "Hafta kunini tanlang", reply_markup=btn)
        return STATE_INPUT_TUGASH
    else:
        db.add_product(id)
        up.message.reply_text('Введите ваше имя')
    return STATE_INPUT_NAME

def input_name(up,ct):
    up.message.reply_text('Введите вашу фамилию')
    id=up.message.from_user.id
    db.edit_name(id,up.message.text)
    return STATE_INPUT_SURNAME

def input_surname(up,ct):
    id=up.message.from_user.id
    db.edit_surname(id,up.message.text)
    up.message.reply_text('Введите свой номер телефона')
    return STATE_INPUT_PHONE

def input_phone(up,ct):
    id=up.message.from_user.id
    up.message.reply_text('Войдите в свою группу')
    # Telefon raqamni mosligini tekshirishingiz mumkin
    db.edit_phone(id, int(up.message.text))
    return STATE_INPUT_GROUP

def input_guruh(up,ct):
    id=up.message.from_user.id
    db.edit_group(id, up.message.text)
    up.message.reply_text('Спасибо за регистрацию',reply_markup=btn)
    return STATE_INPUT_TUGASH

def input_tugash(up,ct):
    query=up.callback_query
    id=query.message.chat.id
    if query.data=="понедельник":
        ct.bot.send_message(id, "понедельник")



def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    conv_hand = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            STATE_INPUT_NAME:[
                CommandHandler('start', start),
                MessageHandler(Filters.text, input_name),
               ],
            STATE_INPUT_SURNAME:[
                CommandHandler('start', start),
                MessageHandler(Filters.text, input_surname),
               ],
            STATE_INPUT_PHONE:[
                CommandHandler('start', start),
                MessageHandler(Filters.text, input_phone),
               ],
            STATE_INPUT_GROUP:[
                CommandHandler('start', start),
                MessageHandler(Filters.text, input_guruh),
            ],
            STATE_INPUT_TUGASH:[
                CommandHandler('start', start),
                CallbackQueryHandler(input_tugash)
            ]},
        fallbacks=[CommandHandler('start', start)]
    )
    dp.add_handler(conv_hand)
    updater.start_polling()
    updater.idle()


main()