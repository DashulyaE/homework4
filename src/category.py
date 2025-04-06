import typing


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
        self.products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products)
