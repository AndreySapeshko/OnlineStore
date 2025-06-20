import json

import pytest


from src.product import Product
from src.category import Category


@pytest.fixture
def product():
    return Product(
        name= 'Samsung Galaxy S23 Ultra',
        description= '256GB, Серый цвет, 200MP камера',
        price= 180000.0,
        quantity= 5
    )


@pytest.fixture
def category():
    return Category(
        name= 'Смартфоны',
        description= 'Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни',
        products= [
            Product('Iphone 15', '512GB, Gray space', 210000.0, 8),
            Product('Xiaomi Redmi Note 11', '1024GB, Синий', 31000.0, 14)
        ]
    )


@pytest.fixture
def categories_json_file():
    categories = []
    file_name = '../data/products.json'
    with open(file_name, 'r', encoding='utf-8') as file:
        categories = json.load(file)
    return categories, file_name
