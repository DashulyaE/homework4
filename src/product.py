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
        self.price = price
        self.quantity = quantity
