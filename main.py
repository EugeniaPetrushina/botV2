import json
from gettext import find
from io import BytesIO

import bs4
import telebot
from telebot import types
import requests
from menuBot import Menu
import DZ
import BotGames

bot = telebot.TeleBot('5205850102:AAF93gC5k5FoDVQOmZU3BFdN4GkE7rMtZTc')

game21 = None


@bot.message_handler(commands=["start"])
def start(message, res=False):
    chat_id = message.chat.id


def command(message, res=False):
    txt_message = f"Привет, {message.from_user.first_name}! Я тестовый бот для курса программирования на языке Пайтон"
    bot.send_message(message.chat.id, text=txt_message, reply_markup=Menu.getMenu("Главное меню").markup)


@bot.message_handler(content_types=['text'])
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
                goto_menu(chat_id, "Выход")
                return
            text_game = game21.get_cards(1)
            bot.send_message(chat_id, text=text_game)
            if game21.status != None:
                goto_menu(chat_id, "Выход")
                return
            elif ms_text == "Стоп!":
                game21 = None
                goto_menu(chat_id, "Выход")
                return

            elif ms_text == "Задание 1":
                DZ.dz1(bot, chat_id)

            elif ms_text == "Задание 2":
                DZ.dz2(bot, chat_id)

            elif ms_text == "Задание 3":
                DZ.dz3(bot, chat_id)

            elif ms_text == "Задание 4-5":
                DZ.dz45(bot, chat_id)

            elif ms_text == "Задание 6":
                DZ.dz6(bot, chat_id)
        else:
            bot.send_message(chat_id, text="Извините, я не понимаю вашу команду: " + ms_text)
            goto_menu(chat_id, "Главное меню")


# ----------------------------------------------------------------------------------------------------------------------
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call): # передать параметры
    pass


# ----------------------------------------------------------------------------------------------------------------------
def goto_menu(chat_id, name_menu):
    if name_menu == "Выход" and Menu.cur_menu != None and Menu.cur_menu.parent != None:
        target_menu = Menu.cur_menu(not Menu.cur_menu.parent.name)
    else:
        target_menu = Menu.getMenu(name_menu)
    if target_menu != None:
        bot.send_message(chat_id, text=target_menu.name, reply_markup=target_menu.markup)
        if target_menu.name == "Игра в 21":
            global game21
            game21 = BotGames.Game21()  # новый экземпляр игры
            text_game = game21.get_cards(2)  # просим 2 карты
            bot.send_media_group(chat_id, media=getMediaCards(game21))
            bot.send_message(chat_id, text=text_game)

        return True
    else:
        return False

def getMediaCards(game21):
    medias = []
    for url in game21.arr_carda_URL:
        medias.append(types.InputMediaPhoto(url))
        return medias


def send_help(chat_id):
    global bot
    bot.send_message(chat_id, "Автор: Петрушина Евгения")
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Напишите автору", url="https://t.me/evgptr")
    markup.add(btn1)
    img = open('кот1.jpg', 'rb')
    bot.send_photo(chat_id, img, reply_markup=markup)


def send_film(chat_id):
    bot.send_message(chat_id, text="еще не готово")


def get_ManOrNot(chat_id):
    bot.send_message(chat_id, text="еще не готово")


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


def get_dogURL():
    url = ""
    req = requests.get('https://random.dog/woof.json')
    if req.status_code == 200:
        r_json = req.json()
        url = r_json['url']
    return url


# ----------------------------------------------------------------------------------------------------------------------
bot.polling(none_stop=True, interval=0)
print()
