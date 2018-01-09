import requests

#base variables
token = '254723372:AAGru9_7irj2mvg1QERwwbvo-iNNKgdvTew/'
URL = 'https://api.telegram.org/bot' + token

def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    return r.json()

def get_message():
    data = get_updates()
    chat_id = data['result'][-1]['message']['chat']['id']
    message_text = data['result'][-1]['message']['text']
    message = {'chat_id' : chat_id,
               'message_text' : message_text}
    return message

def send_message(chat_id, text='wait a second'):
    url = URL + 'sendMessage?chat_id={}&text={}'.format(chat_id, text)
    r = requests.get(url)


def main():
    answer = get_message()
    chat_id = answer['chat_id']
    text = answer['message_text']

    send_message(chat_id, 'чо нада')

main()
