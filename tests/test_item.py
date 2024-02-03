from src.item import Item
import pytest
from config import PATH

@pytest.fixture
def item():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 200000
    assert item.quantity == 20


def test_apply_discount(item):
    item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 8000


def test_name():
    """Проверка длины наименования товара (не более 10 символов)"""
    item1 = Item("Смартфон", 10000, 20)
    assert item1.name == "Смартфон"
    item1.name = "Посудомойка"
    assert item1.name == "Посудомойк"


def test_instantiate_from_csv():
    """Проверка добавления экземпляров класс из .csv файла"""
    Item.instantiate_from_csv(PATH)
    assert len(Item.all) == 5


def test_string_to_number():
    """Проверка возвращения числа из строки"""
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('2.5') == 2
