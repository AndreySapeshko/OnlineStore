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



