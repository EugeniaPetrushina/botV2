import json
from gettext import find
from io import BytesIO

import bs4
import telebot
from telebot import types
import requests
import menuBot
from menuBot import Menu, Users
import DZ
import BotGames


bot = telebot.TeleBot('5185233102:AAHj6OgBdQhnpEiBBQhsN-bddiftKYkbBZE')

game21 = None

#команды

@bot.message_handler(commands="start")
def command(message, res=False):
    chat_id = message.chat.id
    bot.send_sticker(chat_id, "CAACAgIAAxkBAAEEkq9iaT_FQTC2XiYqEMXDaZicoSlafQACmxIAAkesoUshgGwRAAF2MPYkBA")
    txt_message = f"Привет, {message.from_user.first_name}! Я тестовый бот для курса программирования на языке Python"
    bot.send_message(chat_id, text=txt_message, reply_markup=Menu.getMenu(chat_id, "Главное меню").markup)

#получение

@bot.message_handler(content_types=['sticker'])
def get_messages(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Это " + message.content_type)

    sticker = message.sticker
    bot.send_message(message.chat.id, sticker)
    # глубокая инспекция объекта
    # import inspect,pprint
    # i = inspect.getmembers(sticker)
    # pprint.pprint(i)

@bot.message_handler(content_types=['audio'])
def get_messages(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Это " + message.content_type)

    audio = message.audio
    bot.send_message(chat_id, audio)

@bot.message_handler(content_types=['voice'])
def get_messages(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Это " + message.content_type)

    voice = message.voice
    bot.send_message(message.chat.id, voice)

@bot.message_handler(content_types=['photo'])
def get_messages(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Это " + message.content_type)

    photo = message.photo
    bot.send_message(message.chat.id, photo)

@bot.message_handler(content_types=['video'])
def get_messages(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Это " + message.content_type)

    video = message.video
    bot.send_message(message.chat.id, video)

@bot.message_handler(content_types=['document'])
def get_messages(message):
    chat_id = message.chat.id
    mime_type = message.document.mime_type
    bot.send_message(chat_id, "Это " + message.content_type + " (" + mime_type + ")")

    document = message.document
    bot.send_message(message.chat.id, document)
    if message.document.mime_type == "video/mp4":
        bot.send_message(message.chat.id, "This is a GIF!")

@bot.message_handler(content_types=['location'])
def get_messages(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Это " + message.content_type)

    location = message.location
    bot.send_message(message.chat.id, location)

    from Weather import WeatherFromPyOWN
    pyOWN = WeatherFromPyOWN()
    bot.send_message(chat_id, pyOWN.getWeatherAtCoords(location.latitude, location.longitude))
    bot.send_message(chat_id, pyOWN.getWeatherForecastAtCoords(location.latitude, location.longitude))

@bot.message_handler(content_types=['contact'])
def get_messages(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Это " + message.content_type)

    contact = message.contact
    bot.send_message(message.chat.id, contact)



@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    chat_id = message.chat.id
    ms_text = message.text

    cur_user = Users.getUser(chat_id)
    if cur_user == None:
        cur_user = Users(chat_id, message.json["from"])

    # проверка = мы нажали кнопку подменю, или кнопку действия
    subMenu = menuBot.goto_menu(bot, chat_id, ms_text)  # попытаемся использовать текст как команду меню, и войти в него
    if subMenu != None:
        # Проверим, нет ли обработчика для самого меню. Если есть - выполним нужные команды
        if subMenu.name == "Игра в 21":
            game21 = BotGames.newGame(chat_id, BotGames.Game21(jokers_enabled=True))  # создаём новый экземпляр игры
            text_game = game21.get_cards(2)  # просим 2 карты в начале игры
            bot.send_media_group(chat_id, media=getMediaCards(game21))  # получим и отправим изображения карт
            bot.send_message(chat_id, text=text_game)

        elif subMenu.name == "Камень, ножницы, бумага":
            gameRSP = BotGames.newGame(chat_id, BotGames.GameRPS())  # создаём новый экземпляр игры и регистрируем его
            text_game = "<b>Победитель определяется по следующим правилам:</b>\n" \
                        "1. Камень побеждает ножницы\n" \
                        "2. Бумага побеждает камень\n" \
                        "3. Ножницы побеждают бумагу\n" \
                        "подробная информация об игре: <a href='https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D0%BC%D0%B5%D0%BD%D1%8C,_%D0%BD%D0%BE%D0%B6%D0%BD%D0%B8%D1%86%D1%8B,_%D0%B1%D1%83%D0%BC%D0%B0%D0%B3%D0%B0'>Wikipedia</a>"
            bot.send_photo(chat_id, photo="https://i.ytimg.com/vi/Gvks8_WLiw0/maxresdefault.jpg", caption=text_game,
                           parse_mode='HTML')

        return  # мы вошли в подменю, и дальнейшая обработка не требуется

    # проверим, является ли текст текущий команды кнопкой действия
    cur_menu = Menu.getCurMenu(chat_id)
    if cur_menu != None and ms_text in cur_menu.buttons:  # проверим, что команда относится к текущему меню

        if ms_text == "Помощь":
            send_help(chat_id)

        # ======================================= Развлечения
        elif ms_text == "Прислать собаку":
            bot.send_photo(chat_id, photo=get_dogURL(), caption="Вот тебе собачка!")

        elif ms_text == "Прислать лису":
            bot.send_photo(chat_id, photo=get_foxURL(), caption="Вот тебе лисичка!")

        elif ms_text == "Прислать анекдот":
            bot.send_message(chat_id, text=get_anekdot())

        elif ms_text == "Прислать новости":
            bot.send_message(chat_id, text=get_news())

        elif ms_text == "Прислать фильм":
            send_film(chat_id)

        elif ms_text == "Угадай кто?":
            get_ManOrNot(chat_id)

        # ======================================= реализация игры в 21
        elif ms_text == "Карту!":
            game21 = BotGames.getGame(chat_id)
            if game21 == None:  # если мы случайно попали в это меню, а объекта с игрой нет
                menuBot.goto_menu(bot, chat_id, "Выход")
                return

            text_game = game21.get_cards(1)
            bot.send_media_group(chat_id, media=getMediaCards(game21))  # получим и отправим изображения карт
            bot.send_message(chat_id, text=text_game)

            if game21.status != None:  # выход, если игра закончена
                BotGames.stopGame(chat_id)
                menuBot.goto_menu(bot, chat_id, "Выход")
                return

        elif ms_text == "Стоп!":
            BotGames.stopGame(chat_id)
            menuBot.goto_menu(bot, chat_id, "Выход")
            return

        # ======================================= реализация игры Камень-ножницы-бумага
        elif ms_text in BotGames.GameRPS.values:
            gameRSP = BotGames.getGame(chat_id)
            if gameRSP == None:  # если мы случайно попали в это меню, а объекта с игрой нет
                menuBot.goto_menu(bot, chat_id, "Выход")
                return
            text_game = gameRSP.playerChoice(ms_text)
            bot.send_message(chat_id, text=text_game)
            gameRSP.newGame()

        # ======================================= реализация игры Камень-ножницы-бумага Multiplayer
        elif ms_text == "КНБ Multiplayer":
            keyboard = types.InlineKeyboardMarkup()
            btn = types.InlineKeyboardButton(text="Создать новую игру", callback_data="GameRPSm|newGame")
            keyboard.add(btn)
            numGame = 0
            for game in BotGames.activeGames.values():
                if type(game) == BotGames.GameRPS_Multiplayer:
                    numGame += 1
                    btn = types.InlineKeyboardButton(text="Игра КНБ-" + str(numGame) + " игроков: " + str(len(game.players)), callback_data="GameRPSm|Join|" + menuBot.Menu.setExtPar(game))
                    keyboard.add(btn)
            btn = types.InlineKeyboardButton(text="Вернуться", callback_data="GameRPSm|Exit")
            keyboard.add(btn)

            bot.send_message(chat_id, text=BotGames.GameRPS_Multiplayer.name, reply_markup=types.ReplyKeyboardRemove())
            bot.send_message(chat_id, "Вы хотите начать новую игру, или присоединиться к существующей?", reply_markup=keyboard)


        # ======================================= модуль ДЗ
        elif ms_text == "Задание-1":
            DZ.dz1(bot, chat_id)

        elif ms_text == "Задание-2":
            DZ.dz2(bot, chat_id)

        elif ms_text == "Задание-3":
            DZ.dz3(bot, chat_id)

        elif ms_text == "Задание-4":
            DZ.dz4(bot, chat_id)

        elif ms_text == "Задание-5":
            DZ.dz5(bot, chat_id)

        elif ms_text == "Задание-6":
            DZ.dz6(bot, chat_id)
        # ======================================= случайный текст
    else:
        bot.send_message(chat_id, text="Мне жаль, я не понимаю вашу команду: " + ms_text)
        menuBot.goto_menu(bot, chat_id, "Главное меню")



# ----------------------------------------------------------------------------------------------------------------------
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call): # передать параметры
    pass


# ----------------------------------------------------------------------------------------------------------------------
def goto_menu(chat_id, name_menu):
    if name_menu == "Выход" and Menu.cur_menu != None and Menu.cur_menu.parent != None:
        target_menu = Menu.cur_menu(not Menu.cur_menu.parent.name)
    else:
        target_menu = Menu.getMenu(chat_id, name_menu)
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


bot.polling(none_stop=True, interval=0)
print()
