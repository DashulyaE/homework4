import typing

from src.product import Product


class Category:
    """Класс для представления категории продукта"""

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    @typing.no_type_check
    def __init__(self, name, description, products=None):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products)


    @property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return product_str


    def add_product(self, product: Product):
        self.__products.append(product)
        Category.category_count += 1
        Category.product_count += 1
