import typing

class Product:
    """Класс для представления продукта"""

    name: str
    description: str
    price: float
    quantity: int

    @typing.no_type_check
    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity


    @classmethod
    def new_product(cls, new_product: dict):
        if list(new_product.keys()) == ["name", "description", "price", "quantity"]:
            name, description, price, quantity = new_product.values()
            return cls(name, description, price, quantity)
        else:
            print("Входные данные не корректны")

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if float(new_price) == 0 or float(new_price) < 0:
            print("Цена не должна быть нулевая или отрицательная")

        self.__price = new_price

