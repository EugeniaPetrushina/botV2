import requests
from gettext import find
import bs4
import telebot
from telebot import types

import requests
from gettext import find
import bs4

activeGames = {}

def newGame(chatID, newGame):
    activeGames.update({chatID: newGame})
    return newGame

def getGame(chatID):
    return activeGames.get(chatID)

def stopGame(chatID):
    activeGames.pop(chatID)

class New_word:

    def __init__(self):
        self.word = None


    def get_word(self):
        url = "https://calculator888.ru/random-generator/sluchaynoye-slovo"
        req_word = requests.get(url)
        soup = bs4.BeautifulSoup(req_word.text, "html.parser")
        self.word = soup.find('div', class_="blok_otvet").getText().upper()

        return self.word


class Word_game:
    def __init__(self, bot, chat_id):
        self.bot = bot
        self.chat_id = chat_id
        self.word = New_word().get_word
        self.word_length = len(self.word)
        self.lives = 9
        self.used_letters = []
        self.guess_word = ""

    def word_start(self):
        self.guess_word = "_" * self.word_length
        info_word = "Бот загадывает слово\n" \
                    "Игрок должен угадывать его либо, по одной букве, либо все слово сразу" \
                    "Если игрок называет букву, которое есть в слова, она появляется" \
                    "Если нет, то это приближает игрока к казни" \
                    "Есть 8 шансов на ошибку, после чего игра заканчивается."
        message_word = self.guess_word + "  - " + self.word_length +  " букв(ы)"
        self.bot.send_message(self.chat_id, text=message_word)

    def input_letter(self):
        sent = bot.send_message(self.chat_id, text="Ведите букву: ")
        bot.register_next_step_handler(sent, self.letter)


    def letter(self):
        playerChoice = sent.text.upper()
        guess_word = self.guess_word
        bot.send_message(chat_id, text=playerChoice)
        word = self.word
        used_letters = self.used_letters
        print(word)

        if len(playerChoice) > 1:
            if user_input.upper() == word:
                self.bot.send_message(self.chat_id, "Ты победил!")
            else:
                self.bot.send_message(self.chat_id, f"Ты проиграл \nСлово было - '{word}'")
        elif len(playerChoice) == 1:
            if playerChoice in word:
                index = -1
                for letter in word:
                    if user_input == letter:
                        index = word.index(playerChoice, index + 1)
                        guess_word = guess_word[:index] + playerChoice + guess_word[index + 1:]
                self.guess_word = guess_word
                used = ', '.join(used_letters)
        else:
            self.lives -= 1
            if self.lives < 0:
                self.bot.send_message(self.chat_id, f"You lose!!!\n{word}")
                # restart_game()
            else:
                self.used_letters.append(user_input)
                used = ', '.join(used_letters)
                text = "❌\n" + "Wrong letters: " + used + "\n" + guess_word + "\n\n" + hearts(self.lives)
                self.bot.send_message(self.chat_id, text=text)





if __name__ == "__main__":
    print("Этот код должен использоваться только в качестве модуля!")