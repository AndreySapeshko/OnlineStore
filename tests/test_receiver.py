from src.receiver import Receiver
from src.product import Product

import pytest


class Basket(Receiver):
    products: list[Product]

    def __init__(self, products=None):
        if products:
            self.products = products
        else:
            self.products = []

    def add_product(self, product: Product) -> None:
        self.products.append(product)


class Warehouse(Receiver):

    def __init__(self):
        self.name = 'Warehouse'


def test_receiver(product: Product) -> None:
    basket = Basket()
    basket.add_product(product)
    assert len(basket.products) == 1
    with pytest.raises(TypeError) as exc_info:
        Warehouse()
    assert str(exc_info.value) == ("Can't instantiate abstract class Warehouse without "
                                   "an implementation for abstract method 'add_product'")
