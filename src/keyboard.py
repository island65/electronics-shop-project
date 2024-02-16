from src.item import Item


class Mixin:
    def __init__(self):
        self._language = 'EN'

    @property
    def language(self) -> str:
        return self._language

    def change_lang(self) -> None:
        if self._language == "EN":
            self._language = "RU"
        else:
            self._language = 'EN'


class Keyboard (Item, Mixin):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        Mixin.__init__(self)
