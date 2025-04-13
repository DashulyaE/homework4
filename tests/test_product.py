import unittest

from src.product import Product
from unittest import mock


def test_product_init(products):
    assert products.name == '55" QLED 4K'
    assert products.description == "Фоновая подсветка"
    assert products.price == 123000.0
    assert products.quantity == 7


def test_new_product_addition():
    """Тестирование добавления нового продукта в список."""
    Product.products_list.clear()  # Очищаем список перед тестом
    new_product_info = {"name": "Товар1", "description": "Описание товара 1", "price": 100.0, "quantity": 5}
    product = Product.new_product(new_product_info)
    assert isinstance(product, Product)
    assert product.quantity == 5

    new_product_info = {"name": "Товар1", "description": "Описание товара 1", "price": 120.0, "quantity": 10}
    product = Product.new_product(new_product_info)
    assert product.quantity == 15
    assert product.price == 120.0


def test_price_setter():
    """Тестирование установки цены продукта."""
    Product.products_list.clear()  # Очищаем список перед тестом
    product = Product("Товар2", "Описание товара 2", 100.0, 10)

    product.price = 150.0
    assert product.price == 150.0

    with unittest.mock.patch("builtins.input", return_value="y"):
        product.price = 50.0
        assert product.price == 50.0

    with unittest.mock.patch("builtins.input", return_value="no"):
        product.price = 40.0
        assert product.price == 50.0


def test_invalid_new_product():
    """Тест на проверку исключения при некорректных ключах."""
    Product.products_list.clear()
    new_product_info = {"name": "Товар2", "description": "Описание товара 2", "price": 100.0}
    try:
        Product.new_product(new_product_info)
    except ValueError:
        pass
    else:
        assert False, "ValueError не было вызвано"


def test_product_add(products2, products3):
    assert products2 + products3 == 2114000.0


def test_str_prod(products2):
    print(products2)
