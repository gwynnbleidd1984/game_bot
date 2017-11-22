# import modules
import time
import datetime
import pandas as pd
from telegram.ext import Updater, CommandHandler

'------------------------------------------------------'

# setting global variables
updater = Updater('254723372:AAGru9_7irj2mvg1QERwwbvo-iNNKgdvTew')
dp = updater.dispatcher
start_time = None
stop_time = None


# admins
admins_list = ("gwynnbleidd")

# starting the game itself
admin_code_start = "погнали"

# stop game
admins_code_stop = "приехали"
'------------------------------------------------------'

# setting player start code
start_code = "пилидавай"

# codes list
codes = ("d1r1",
         "r2d2",
         "dr13",
         "rd6",
         "d13r666")

# setting player game over code
stop_code = "аявсё"
'------------------------------------------------------'

# players list
player_list = list()


# starting the game as admin
def game_start(bot, update):
    player_id = update.message.from_user.username
    if player_id in admins_list:
        update.message.reply_text('Пошла Жара! Время {}'.format(time.ctime()))
        global start_time
        start_time = time.time()
    else:
        update.message.reply_text('А сюда ли ты зашёл, {}? В логах всё будет видно!'.format(player_id))


# stop game as admin
def game_stop(bot, update):
    player_id = update.message.from_user.username
    if player_id in admins_list:
        global stop_time
        stop_time = time.time()
        #duration = stop_time - start_time
        update.message.reply_text('Всё, приехали. Время окончания игры: {}'.format(time.ctime()))
        game_duration = stop_time - start_time
        update.message.reply_text('Игра длилась{}'.format((datetime.timedelta(seconds=game_duration))))
    else:
        update.message.reply_text('А вот это не тебе решать, {}? В логах всё будет видно!'.format(player_id))


# add player to list and start the search
def user_append(bot, update):
    # add user to game by entering start code
    # getting username
    global player_list
    new_player = update.message.from_user.username
    player_start_time = time.time()
    time_delay = player_start_time - start_time #checking if game duration is already > 2 minutes
    if time_delay < 120:
        if new_player in player_list:
            update.message.reply_text('Вы уже вводили стартовый код, {}! Будьте внимательнее.'.format(new_player))
        else:
            update.message.reply_text('Добро пожаловать в Игру, {}!'.format(new_player))
            update.message.reply_text('Когда ты всё спилишь или просто решишь, что с тебя достаточно - вбей код /{} И всё кончится'.format(stop_code))
            player_list.append(new_player)
    else:
        if new_player in player_list:
            update.message.reply_text('Вы уже вводили стартовый код, {}! Будьте внимательнее.'.format(new_player))
        else:
            update.message.reply_text('Ну и где мы гуляли, когда началсаь игра? Извини, {}, сегодня не твой день :('.format(new_player))


def test(bot, update):
    if code in codes:
        update.message.reply_text('маладца!')



dp.add_handler(CommandHandler(admin_code_start, game_start))
dp.add_handler(CommandHandler(admins_code_stop, game_stop))
dp.add_handler(CommandHandler(start_code, user_append))
#dp.add_handler(CommandHandler(code, test))

updater.start_polling()
updater.idle()