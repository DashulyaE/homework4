def test_product_init(products):
    assert products.name == '55" QLED 4K'
    assert products.description == "Фоновая подсветка"
    assert products.price == 123000.0
    assert products.quantity == 7
