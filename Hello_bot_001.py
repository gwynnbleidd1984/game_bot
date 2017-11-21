from telegram.ext import Updater, CommandHandler

def start(bot, update):
    update.message.reply_text('гвин хороший')

def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

updater = Updater('254723372:AAGru9_7irj2mvg1QERwwbvo-iNNKgdvTew')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('phello', hello))

updater.start_polling()
updater.idle()

