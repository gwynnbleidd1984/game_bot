# import modules
import time
import datetime
import pandas as pd
from telegram.ext import Updater, CommandHandler

# setting global variables
updater = Updater('254723372:AAGru9_7irj2mvg1QERwwbvo-iNNKgdvTew')
dp = updater.dispatcher

# setting start code
start_code = "zont"

# codes list
codes = ("d1r1",
         "r2d2",
         "dr13",
         "rd6",
         "d13r666")

# players list
player_list = list()

# add player to list
def user_append(bot, update):
    # add user to game by entering start code
    # getting username
    new_player = update.message.from_user.username  # first_name
    if new_player in player_list:
        update.message.reply_text('Вы уже вводили стартовый код, ' + new_player + "! Будьте внимательнее.")
    else:
        update.message.reply_text('Добро пожаловать в Игру, ' + new_player + "!")
        player_list.append(new_player)


dp.add_handler(CommandHandler(start_code, user_append))

updater.start_polling()
updater.idle()
