from telebot import types
class Menu:
    hash = {}
    cur_menu = None
    extendedParameters = {}
    def __init__(self, name, buttons=None, parent=None, action=None):
        self.parent = parent
        self.name = name
        self.buttons = buttons
        self.action - action

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_wigth=5)
        markup.add(*buttons)
        self.markup = markup
        self.__class__.hash[name] = self

    @classmethod
    def getExtPar(cls, id):
        return cls.extendedParameters.pop(id, None)

    @classmethod
    def setExtPar(cls, parameter):
        import uuid
        id = uuid.uuid4().hex
        cls.extendedParameters[id] = parameter
        return id
    @classmethod
    def getMenu(cls, name):
        menu = cls.hash.get(name)
        if menu != None:
            cls.cur_menu = menu
        return menu

m_main = Menu("Главное меню", buttons=["Развлечения", "Игры", "ДЗ", "Помощь"])
m_games = Menu("Игры", buttons=["Камень, ножницы, бумага", "Игра в 21", "Угадай кто?", "Выход"], parent=m_main)
m_game_21 = Menu("Игра в 21", buttons=["Карту!", "Стоп!", "Выход"], parent=m_games, action=game_21)
m_game_rsp = Menu("Игра в 21", buttons=["Карту!", "Стоп!", "Выход"], parent=m_games, action=game_21)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Главное меню")
    btn2 = types.KeyboardButton("❓ Помощь")
    markup.add(btn1, btn2)