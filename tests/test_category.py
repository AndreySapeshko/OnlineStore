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


def test_category_products(category: Category, capsys: CaptureFixture[str]) -> None:
    category.products
    captured = capsys.readouterr()
    assert captured.out == ('Iphone 15, 210000.0 руб. Остаток: 8 шт.\n'
                            'Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n')
