from itertools import product

from src.category import Category
from src.exceptions import ZeroProduct
from src.lawngrass import LawnGrass
from src.product import Product, Order
from src.smartphone import Smartphone

if __name__ == "__main__":  # pragma: no cover
        try:
                product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
        except ValueError as e:
                print(
                        "Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт с нулевым количеством")
        else:
                print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")

        product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

        category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2])

        print(category1.middle_price())

        category_empty = Category("Пустая категория", "Категория без продуктов", [])
        print(category_empty.middle_price())

        print(category1)
        order1 = Order(product1, 3)
        order2 = Order(product2, 1)

        category1.add_product(product3)

        #product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 0)
        #category1.add_product(product3)
