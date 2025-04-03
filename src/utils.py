import json
import typing

from src.category import Category
from src.product import Product


def read_json(operations_path_json: str) -> typing.Any:
    """Функция чтения файла JSON с информацией о категориях и продуктах"""

    with open(operations_path_json, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def create_category_json(data: typing.Any) -> list:
    """Функция создания экземпляров классов категорий и продуктов"""

    category_product = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        category_product.append(Category(**category))
    return category_product
