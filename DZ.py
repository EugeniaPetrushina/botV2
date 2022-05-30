import requests
from gettext import find
import bs4
import telebot
from telebot import types






def dz1(bot, chat_id):
    name = "Евгения"
    bot.send_message(chat_id, text = name)
def dz2(bot, chat_id):
    name = "Евгения"
    age = 19
    bot.send_message(chat_id, text = f"Здравствуйте! Меня зовут {name}, мне {age} лет.")
def dz3(bot, chat_id):
    name = "Евгения"
    bot.send_message(chat_id, text = name + name + name )
    bot.send_message(chat_id, text = name * 5)
def dz4(bot, chat_id):
    sent = bot.send_message(chat_id, text="Введите имя: ")
    bot.register_next_step_handler(sent, f4, bot, chat_id)
def f4(sent, bot, chat_id):
    sent2 = bot.send_message(chat_id, text="Введите возраст: ")
    bot.register_next_step_handler(sent2, f42, bot, chat_id, sent)
def f42(sent, sent2, bot, chat_id):
    bot.send_message(chat_id, text=sent.text + sent2.text)
    #bot.send_message(chat_id, text=sent2.text)

def dz5(bot, chat_id):
    bot.send_message(chat_id, text="Доделать")
def dz6(bot, chat_id):
    bot.send_message(chat_id, text="Доделать")



