import json
import os
import typing

from config import DATA_DIR
from src.category import Category
from src.product import Product


def read_json(operations_path_json: str) -> typing.Any:
    with open(operations_path_json, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def create_category_json(data: typing.Any) -> list:
    category_product = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        category_product.append(Category(**category))
    return category_product


if __name__ == "__main__":
    operations_path_json = os.path.join(DATA_DIR, "products.json")
    category_data = read_json(operations_path_json)
    category_product = create_category_json(category_data)
    print(category_product[0].name)
    print(category_product[0].products)
