

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


    bot.send_message(chat_id,
                     text="Привет, {0.first_name}! Я тестовый бот для курса программирования на языке Пайтон".format(
                         message.from_user))



@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    chat_id = message.chat.id
    ms_text = message.text

# ----------------------------------------------------------------------------------------------------------------------


    if ms_text == "👋 Главное меню" or ms_text == "Главное меню" or ms_text == "Вернуться в главное меню" \
            or ms_text == "главное меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Развлечения")
        btn2 = types.KeyboardButton("1 Урок")
        btn3 = types.KeyboardButton("Сгенерировать пароль")
        back = types.KeyboardButton("Помощь")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(chat_id, text="Вы в главном меню", reply_markup=markup)

    elif ms_text == "Развлечения":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Прислать собаку")
        btn2 = types.KeyboardButton("Прислать анекдот")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(chat_id, text="Развлечения", reply_markup=markup)

    elif ms_text == "1 Урок":
        bot.send_message(chat_id, text="еще не готово))")

    elif ms_text == "Сгенерировать пароль":
        bot.send_message(chat_id, text=get_fact())

    elif ms_text == "Помощь" or ms_text == "/help":
        bot.send_message(chat_id, text="Автор: Петрушина Евгения")
        key1 = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="Напишите автору", url="https://t.me/evgptr")
        key1.add(btn1)
        img = open('кот1.jpg', 'rb')
        bot.send_photo(message.chat.id, img, reply_markup=key1)

    # ----------------------------------------------------------------------------------------------------------------------

    # ----------------------------------------------------------------------------------------------------------------------

    elif ms_text == "/dog" or ms_text == "Прислать собаку":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Красивую")
        btn2 = types.KeyboardButton("Смешную")
        btn3 = types.KeyboardButton("Другую")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(chat_id, text="Какую собаку?", reply_markup=markup)

    elif ms_text == "Красивую":
        img = open('собака4.jpg', 'rb')
        bot.send_photo(message.chat.id, img)

    elif ms_text == "Смешную":
        img = open('собака1.jpg', 'rb')
        bot.send_photo(message.chat.id, img)

    elif ms_text == "Другую":
        contents = requests.get('https://random.dog/woof.json').json()
        urlDOG = contents['url']
        bot.send_photo(chat_id, photo=urlDOG, caption="Вот тебе собачка")
    # ----------------------------------------------------------------------------------------------------------------------

    # ----------------------------------------------------------------------------------------------------------------------

    elif ms_text == "Прислать анекдот":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Про слона")
        btn2 = types.KeyboardButton("Случайный анекдот")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(chat_id, text="Какой анекдот?", reply_markup=markup)
    elif ms_text == "Про слона":
        bot.send_message(chat_id, text="- Блин! - сказал слон, наступив на колобка.")
    elif ms_text == "Случайный анекдот":
        bot.send_message(chat_id, text=get_anekdot())
    else:
        bot.send_message(chat_id, text="Я тебя слышу!!! Ваше сообщение: "
                                       + ms_text)


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