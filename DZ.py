name = "Евгения"
age = 19

def dz1(bot, chat_id):
    bot.send_message(chat_id, text = name)
def dz2(bot, chat_id):
    bot.send_message(chat_id, text = f"Здравствуйте! Меня зовут {name}, мне {age} лет.")
def dz3(bot, chat_id):
    bot.send_message(chat_id, text = name + name + name )
    bot.send_message(chat_id, text = name * 5)
def dz4(bot, chat_id):
    bot.send_message(chat_id, text="Доделать")
def dz5(bot, chat_id):
    bot.send_message(chat_id, text="Доделать")
def dz6(bot, chat_id):
    bot.send_message(chat_id, text="Доделать")