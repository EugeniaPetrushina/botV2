from telebot import types


class Menu:
    hash = {}
    cur_menu = None
    extendedParameters = {}

    def __init__(self, name, buttons=None, parent=None, action=None):
        self.parent = parent
        self.name = name
        self.buttons = buttons
        self.action = action

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=5)
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

m_dz = Menu("ДЗ", buttons=["з. 1", "з. 2", "з. 3", "з. 4", "з. 5", "з. 6", "Выход"], parent=m_main)
m_fun = Menu("Развлечения", buttons=["Прислать собаку", "Прислать анекдот", "Прислать фильм", "Выход"], parent=m_main)
