"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)

@pytest.fixture
def cart():
    return Cart()

class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        if product.check_quantity(1000):
            assert product.quantity >= 1000
        if product.check_quantity(1001) is False:
            assert product.quantity < 1001
        pass

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(2)
        assert product.quantity == 1000 - 2
        pass

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(1001)
        pass


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
    def test_add_new_product(self, cart, product):
        cart.add_product(product, 10)
        assert cart.products[product] == 10

    def test_add_not_new_product(self, cart, product):
        cart.add_product(product)
        cart.add_product(product, 10)
        assert len(cart.products) == 1
        assert cart.products[product] == 11
