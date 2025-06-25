import pytest

from src.product import Product


def test_product(product: Product) -> None:
    assert product.name == 'Samsung Galaxy S23 Ultra'
    assert product.description == '256GB, Серый цвет, 200MP камера'
    assert product.price == 180000.0
    assert product.quantity == 5


def test_new_product() -> None:
    product = Product.new_product(['Xiaomi Redmi Note 11', '1024GB, Синий', 31000.0, 14])
    assert product.name == 'Xiaomi Redmi Note 11'
    assert product.description == '1024GB, Синий'
    assert product.price == 31000.0
    assert product.quantity == 14


def test_new_product_except() -> None:
    with pytest.raises(Exception) as exc_info:
        product = Product.new_product(['Xiaomi Redmi Note 11', '1024GB, Синий'])
        assert str(exc_info.value) == 'Количество или тип параметров не соответстует ожиданию'
