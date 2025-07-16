import pytest
from pytest import CaptureFixture

from src.category import Category
from src.product import Product


def test_category(category: Category) -> None:
    assert category.name == 'Смартфоны'
    assert category.description == ('Смартфоны, как средство не только коммуникации, '
                                    'но и получения дополнительных функций для удобства жизни')
    assert len(category.products) == 2
    assert category.category_count == 1
    assert category.product_count == 2


def test_category_add_product(category: Category) -> None:
    category.add_product(Product('Samsung Galaxy S23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0, 5))
    assert len(category.products) == 3
    with pytest.raises(TypeError) as exc_info:
        category.add_product('not product')
        assert str(exc_info.value) == 'Добавлять можно только объекты класса Product и его наследники'


def test_category_products(category: Category, capsys: CaptureFixture[str]) -> None:
    category.products
    captured = capsys.readouterr()
    assert captured.out == ('Iphone 15, 210000.0 руб. Остаток: 8 шт.\n'
                            'Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n')


def test_str_category(category: Category) -> None:
    assert str(category) == 'Смартфоны, количество продуктов: 22 шт.'


def test_avg_price_product(category: Category) -> None:
    category_0 = Category(
        name='Смартфоны',
        description='Смартфоны, как средство не только коммуникации, '
                    'но и получения дополнительных функций для удобства жизни'
    )
    assert category.avg_price_product() == 10954.55
    assert category_0.avg_price_product() == 0.0
