from src.category import Category
from src.product import Product


def test_product_init(products):
    assert products.name == '55" QLED 4K'
    assert products.description == "Фоновая подсветка"
    assert products.price == 123000.0
    assert products.quantity == 7


def test_add_product(category1, products, products2):
    Category.product_count = 0  # Очищаем список перед тестом
    category = category1
    product1 = products

    category.add_product(product1)  # Добавляем первый продукт
    assert Category.product_count == 1

    product2 = Product("Телевизор", "Смарт-телевизор", 30000, 3)
    category.add_product(product2)  # Добавляем тот же продукт
    assert Category.product_count == 2  # Увеличение общего количества


def test_str_category(category1):
    print(category1)
