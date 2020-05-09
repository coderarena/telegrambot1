from telegram.ext import Updater ,CommandHandler, MessageHandler

updater = Updater(token='1208250636:AAEwo-dbUFGKePpx6O1DsA1m8iOcygiEYJs')
dispatcher = updater.dispatcher

def start(bot, update):
    update.message.reply_text("im abot")

start_handler = CommandHandler('start',start)
dispatcher.add_handler(start_handler)

updater.start_polling()