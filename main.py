

import bs4
import telebot
from telebot import types
import requests
from menuBot import Menu


bot = telebot.TeleBot('5205850102:AAF93gC5k5FoDVQOmZU3BFdN4GkE7rMtZTc')

game21 = None

@bot.message_handler(commands=["start"])
def start(message, res=False):
    chat_id = message.chat.id

def command(message, res=False):
    txt_message = f"Привет, {message.from_user.first_name}! Я тестовый бот для курса программирования на языке Пайтон"
    bot.send_message(message.chat.id, text=txt_message,
reply_markup=Menu.getMenu("Главное меню".markup)




@bot.message_handler(content_types=['text']))
def get_text_messages(message):
    global game21
    chat_id = message.chat.id
    ms_text = message.text

    result = goto_menu(chat_id, ms_text)
    if result == True:
        return
    if Menu.cur_menu != None and ms_text in Menu.cur_menu.buttons:
         if ms_text == "Помощь":
             send_help(chat_id)
         elif ms_text == "Прислать собаку":
             bot.send_photo(chat_id, photo=get_dogURL(), caption="Вот тебе собачка!")
         elif ms_text == "Прислать анекдот":
             bot.send_photo(chat_id, photo=get_anekdot())
         elif ms_text == "Прислать фильм":
             send_film(chat_id)
         elif ms_text == "Угадай кто?":
             get_ManOrNot(chat_id)
         elif ms_text == "Карту!":
             if game21 == None:
                 goto_menu(chat_id,"Выход")
                return
             text_game = game21.get_cards(1)
             bot.send_message(chat_id, text=text_game)
             if game21.status != None:
                 goto_menu(chat_id,"Выход")
                 return



# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------

def get_anekdot():
    array_anekdots = []
    req_anek = requests.get('http://anekdotme.ru/random')
    soup = bs4.BeautifulSoup(req_anek.text, "html.parser")
    result_find = soup.select('.anekdot_text')
    for result in result_find:
        array_anekdots.append(result.getText().strip())
    return array_anekdots[0]


def get_fact():
    array_facts = []
    req_fact = requests.get('https://randstuff.ru/password/')
    soup = bs4.BeautifulSoup(req_fact.text, "html.parser")
    result_find = soup.select('.cur')
    for result in result_find:
        array_facts.append(result.getText().strip())
    return array_facts[0]


# ----------------------------------------------------------------------------------------------------------------------
bot.polling(none_stop=True, interval=0)