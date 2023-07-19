class Product:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, quantity) -> bool:
        """
        TODO Верните True если количество продукта больше или равно запрашиваемому
            и False в обратном случае
        """
        if quantity <= self.quantity:
            print('Товара достаточно.')
            return True
        elif quantity > self.quantity:
            return False
        raise NotImplementedError

    def buy(self, quantity):
        """
        TODO реализуйте метод покупки
            Проверьте количество продукта используя метод check_quantity
            Если продуктов не хватает, то выбросите исключение ValueError
        """
        if self.check_quantity(quantity):
            self.quantity -= quantity
            print(f'Куплено {self.name} - {quantity}\nОстаток - {self.quantity}')
        elif self.check_quantity(quantity) is False:
            print('Не хватает товара.')
            raise ValueError
        else:
            raise NotImplementedError

    def __hash__(self):
        return hash(self.name + self.description)


class Cart:
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    TODO реализуйте все методы класса
    """

    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}

    def print_cart(self):
        if len(self.products)== 0:
            print('Корзина пуста')
        else:
            print('Корзина:')
            for i_key, i_value in self.products.items():
                print(f'{i_key.name} - {i_value} шт.')

    def add_product(self, product: Product, buy_count=1):
        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество
        """
        if product in self.products:
            self.products[product] += buy_count
        else:
            self.products[product] = buy_count
        print(f'добавлен {product.name} в количестве {buy_count} шт.')
        #  raise NotImplementedError

    def remove_product(self, product: Product, remove_count=None):
        """
        Метод удаления продукта из корзины.
        Если remove_count не передан, то удаляется вся позиция
        Если remove_count больше, чем количество продуктов в позиции, то удаляется вся позиция
        """
        if product in self.products:
            if None == remove_count or remove_count > self.products[product]:
                self.products.pop(product)
            else:
                self.products[product] -= remove_count
        else:
            print("Product not in cart")
            raise NotImplementedError

    def clear(self):
        self.products.clear()
        # raise NotImplementedError

    def get_total_price(self) -> float:
        total_price = 0
        for i_key, i_value in self.products.items():
            total_price += i_key.price * i_value
        print('Сумма', total_price)
        return total_price
        # raise NotImplementedError

    def buy(self):
        self.get_total_price()
        print('Куплено')
        self.clear()
        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """
        # raise NotImplementedError


# potato = Product('potato', 20, "good", 2)
# apple = Product('apple', 22, "fruit", 5)
# my_cart = Cart()
# my_cart.add_product(potato, 2)
# my_cart.remove_product(potato,1)
# my_cart.print_cart()
# my_cart.clear()
# my_cart.print_cart()
# my_cart.add_product(apple, 2)
# my_cart.add_product(potato)
# my_cart.print_cart()
# my_cart.get_total_price()