from src.base_product import BaseProduct

import pytest


class Product1(BaseProduct):

    def __str__(self) -> str:
        return self.__class__.__name__

    def __add__(self, other):
        return self.__class__.__name__ + ' + ' + other.__class__.__name__


class Product2(BaseProduct):

    def __str__(self):
        return self.__class__.__name__


def test_base_product() -> None:
    with pytest.raises(TypeError) as exc_info:
        Product2()
    assert str(exc_info.value) == ("Can't instantiate abstract class Product2 without an "
                                   "implementation for abstract method '__add__'")
    prod1 = Product1()
    assert str(prod1) == 'Product1'
    assert prod1 + prod1 == 'Product1 + Product1'
