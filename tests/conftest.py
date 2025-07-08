import json

import pytest

from src.category import Category
from src.product import Product
from src.smartphone import Smartphone
from src.lawn_grass import LawnGrass
from tests.config import PATH_PRODUCTS
from src.iterator_category import IteratorCategory


@pytest.fixture
def product() -> Product:
    return Product(
        name='Samsung Galaxy S23 Ultra',
        description='256GB, Серый цвет, 200MP камера',
        price=180000.0,
        quantity=5
    )


@pytest.fixture
def category() -> Category:
    return Category(
        name='Смартфоны',
        description='Смартфоны, как средство не только коммуникации, '
                    'но и получения дополнительных функций для удобства жизни',
        products=[
            Product('Iphone 15', '512GB, Gray space', 210000.0, 8),
            Product('Xiaomi Redmi Note 11', '1024GB, Синий', 31000.0, 14)
        ]
    )


@pytest.fixture
def categories_json_file() -> tuple:
    file_name = PATH_PRODUCTS
    with open(file_name, 'r', encoding='utf-8') as file:
        categories = json.load(file)
    return categories, file_name


@pytest.fixture
def iterator_category() -> IteratorCategory:
    return IteratorCategory(
        Category(
            name='Смартфоны',
            description='Смартфоны, как средство не только коммуникации, '
                        'но и получения дополнительных функций для удобства жизни',
            products=[
                Product('Iphone 15', '512GB, Gray space', 210000.0, 8),
                Product('Xiaomi Redmi Note 11', '1024GB, Синий', 31000.0, 14)
            ]
        )
    )


@pytest.fixture
def smartphone() -> Smartphone:
    return Smartphone(
        'Samsung Galaxy S23 Ultra',
        '256GB, Серый цвет, 200MP камера',
        180000.0, 5, 95.5,
        'S23 Ultra', 256, 'Серый'
    )


@pytest.fixture
def lawn_grass() -> LawnGrass:
    return LawnGrass(
        'Газонная трава', 'Элитная трава для газона',
        500.0, 20, 'Россия',
        '7 дней', 'Зеленый'
    )
