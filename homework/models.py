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

    def add_product(self, product: Product, buy_count=1):
        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество
        """
        if product in self.products:
            self.products[product] += 1
        else:
            self.products[product] = buy_count
        print(f'добавлен{self.products[product]} в количестве {buy_count}')
            # raise NotImplementedError

    def remove_product(self, product: Product, remove_count=None):
        """
        Метод удаления продукта из корзины.
        Если remove_count не передан, то удаляется вся позиция
        Если remove_count больше, чем количество продуктов в позиции, то удаляется вся позиция
        """
        if Product in product:
            if remove_count is None or remove_count > product[Product]:
                product.pop(Product)
            else:
                product[Product] -= remove_count
        else:
            print("Product not in cart")
        raise NotImplementedError

    def clear(self):
        self.clear()
        raise NotImplementedError

    def get_total_price(self) -> float:
        total_price = 0
        for i_key, i_value in self.items:
            total_price += i_key.prise * i_value
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

potato = Product('potato', 20, "good",2)
my_cart =Cart
my_cart.add_product(potato, 2)
