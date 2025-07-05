import pytest

from unittest.mock import patch

from src.product import Product
from src.category import Category


def test_product(product: Product) -> None:
    assert product.name == 'Samsung Galaxy S23 Ultra'
    assert product.description == '256GB, Серый цвет, 200MP камера'
    assert product.price == 180000.0
    assert product.quantity == 5


def test_check_product_matching(product: Product, category: Category) -> None:
    number_of_pieces = sum([x.quantity for x in category.products])
    number_products = len(category.products)
    Product.check_product_matching(product, category.products)
    assert sum([x.quantity for x in category.products]) == number_of_pieces + product.quantity
    assert len(category.products) == number_products + 1


def test_new_product(category: Category) -> None:
    number_of_pieces = sum([x.quantity for x in category.products])
    Product.new_product(
        {'name': 'Xiaomi Redmi Note 11', 'description': '1024GB, Синий', 'price': 31000.0, 'quantity': 14},
        category.products
    )
    assert sum([x.quantity for x in category.products]) == number_of_pieces + 14


def test_new_product_except() -> None:
    with pytest.raises(Exception) as exc_info:
        Product.new_product({'name': 'Xiaomi Redmi Note 11', 'description': '1024GB, Синий'}, [])
        assert str(exc_info.value) == 'Количество или тип параметров не соответстует ожиданию'


def test_set_price(product: Product, capsys) -> None:
    product.price = 190000.0
    assert product.price == 190000.0
    product.price = 0
    captured = capsys.readouterr()
    assert captured.out == 'Цена не должна быть нулевая или отрицательная\n'
    with patch('builtins.input', side_effect=['n', 'y']):
        product.price = 100000.0
        assert product.price == 190000.0
        product.price = 110000.0
        assert product.price == 110000.0


def test_str_product(product: Product) -> None:
    assert str(product) == 'Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.'


def test_add_product(product: Product) -> None:
    product_for_add = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    assert product + product_for_add == 2580000.0
