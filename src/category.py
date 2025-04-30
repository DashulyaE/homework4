import typing

from src.base_product import ProductOrder
from src.product import Product
from src.exceptions import ZeroProduct

class Category(ProductOrder):
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

    def __str__(self):
        product_total = 0
        for product in self.__products:
            product_total += product.quantity

        return f"{self.name}, количество продуктов: {product_total} шт."

    @property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str += f"{str(product)}\n"
        return product_str

    def add_product(self, product: Product):
        if isinstance(product, Product):
            try:
                if product.quantity == 0:
                    raise ZeroProduct("Нельзя добавить продукт с нулевым кол-вом")
            except ZeroProduct as e:
                print(str(e))
            else:
                self.__products.append(product)
                Category.category_count += 1
                Category.product_count += 1
                print("Продукт добавлен успешно")
            finally:
                print("Обработка товара завершена")
        else:
            raise TypeError

    @property
    def product_lst(self):
        return self.__products


    def middle_price(self):
        try:
            return sum([product.price for product in self.__products])/sum(product.quantity for product in self.__products)
        except ZeroDivisionError:
            return 0
