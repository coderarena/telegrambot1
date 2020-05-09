from telegram.ext import Updater ,CommandHandler, MessageHandler

updater = Updater(token='TOKEN HERE')
dispatcher = updater.dispatcher

def start(bot, update):
    update.message.reply_text("im abot")

start_handler = CommandHandler('start',start)
dispatcher.add_handler(start_handler)

updater.start_polling()
