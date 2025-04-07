import typing


class Product:
    """Класс для представления продукта"""

    name: str
    description: str
    price: float
    quantity: int
    products_list = []

    @typing.no_type_check
    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Product.products_list.append(self)


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
        if float(new_price) == 0 or float(new_price) < 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

