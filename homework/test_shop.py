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

    def test_remove_product_with_count(self, product, cart):
        cart.add_product(product, 100)
        cart.remove_product(product, 10)
        assert cart.products[product] == 100 - 10

    def test_remove_product_without_count(self, product, cart):
        cart.add_product(product, 100)
        assert cart.products[product] == 100
        cart.remove_product(product)
        assert len(cart.products) == 0

    def test_clear(self,product, cart):
        cart.add_product(product, 100)
        assert cart.products[product] == 100
        cart.clear()
        assert len(cart.products) == 0

    def test_get_total_price(self, cart, product):
        cart.add_product(product)
        total_price = 0
        total_price = [total_price + i_key.price * i_value for i_key, i_value in cart.products.items()]
        assert cart.get_total_price() == total_price[0]

    def test_cart_buy(self, product, cart):
        cart.add_product(product, 10)
        assert product.quantity == 1000
        cart.buy()
        assert len(cart.products) == 0
        assert product.quantity == 1000 - 10

