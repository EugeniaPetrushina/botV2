"""markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton("👋 Главное меню")
btn2 = types.KeyboardButton("❓ Помощь")
markup.add(btn1, btn2)

bot.send_message(chat_id,
                 text="Привет, {0.first_name}! Я тестовый бот для курса программирования на языке Пайтон".format(
                     message.from_user))

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
"""
