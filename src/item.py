import csv


class InstantiateCSVError(Exception):
    def __init__(self, *args, **kwargs):
        self.message = "Файл повреждён"

    def __str__(self):
        return self.message

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса Item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __add__(self, other):
        """Складывает количество товаров в магазине с проверкой"""
        if not isinstance(other, Item):
            raise ValueError ("Можно складывать только экземпляры классов 'Phone или `Item` и их дочерние")
        return self.quantity + other.quantity


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        """Проверяем длину наименования товара - не более 10 символов"""
        if len(name) > 10:
            self.__name = name[:10]
        else:
            self.__name = name

    @classmethod
    def instantiate_from_csv(cls, csvfile):
        """Получение экземпляров классов из .csv файла"""
        try:
            cls.all = []
            with open(csvfile, newline='', encoding='windows-1251') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    cls(str(row["name"]), int(row["price"]), int(row["quantity"]))
        except FileNotFoundError:
            raise FileNotFoundError(f"Отсутствует файл{csvfile}")
        except KeyError:
            raise InstantiateCSVError


    @staticmethod
    def string_to_number(str_number):
        """Возвращает число из строки"""
        number = str(str_number)
        return int(float(number))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.name}'
