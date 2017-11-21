
# coding: utf-8

# # Список игроков

# In[32]:

player_list = list()


# In[38]:

new_player = input('Введите имя:')
if new_player in player_list:
    print('Вы уже вводили этот код')
else:
    player_list.append(new_player)


# In[39]:

player_list


# # Список кодов

# In[4]:

codes = ('d1r1', 'r2d2', 'dr13', '6dr')


# In[20]:

code = str.lower(input())


# In[22]:

if code in codes:
    #number = codes.index(code)+1
    print('Код по метке {} принят'.format(codes.index(code)+1))
else:
    print('Ты втираешь мне какую-то дичь!')


# # Время

# In[49]:

import time


# In[52]:

beginning = time.time()
beginning


# In[53]:

ending = time.time()
ending


# In[54]:

game_duration = ending - beginning
game_duration


# In[68]:

import datetime


# In[70]:

print('игровое время {}'.format(datetime.timedelta(seconds=game_duration)))

