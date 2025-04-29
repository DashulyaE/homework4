import typing

from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    """Класс для представления продукта"""

    name: str
    description: str
    price: float
    quantity: int
    products_list: list = []

    @typing.no_type_check
    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        if quantity != 0:
            Product.products_list.append(self)
        else:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__()

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) is Product:
            return self.__price * self.quantity + other.__price * other.quantity
        raise TypeError

    @classmethod
    def new_product(cls, new_product: dict):
        if list(new_product.keys()) != ["name", "description", "price", "quantity"]:
            raise ValueError("Ключи не совпадают")

        name, description, price, quantity = new_product.values()

        for existing_product in cls.products_list:
            if existing_product.name == name and existing_product.description == description:
                existing_product.quantity += quantity
                existing_product.price = max(existing_product.price, price)  # Выбираем более высокую цену
                return existing_product

        return cls(name, description, price, quantity)

    @classmethod
    def get_products(cls):
        return cls.products_list

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        new_price = float(new_price)
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            confirmation = input(
                f"Цена товара {self.name} понижается с {self.__price} "
                f"до {new_price}. Подтверждаете понижение цены? (y/n): "
            )
            if confirmation.lower() == "y":
                self.__price = new_price
                print("Цена успешно изменена.")
            else:
                print("Изменение цены отменено.")
        else:
            self.__price = new_price
