from __future__ import annotations

from typing import Any

from src.base_product import BaseProduct
from src.report_by_create_object import ReportByCreateObject


class Product(BaseProduct, ReportByCreateObject):
    """ Класс описыает общеие свойства для любого продукта
    имеет поля: имя, описание, цена и количество """

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError('Товар с нулевым количеством не может быть добавлен')
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self) -> str:
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other: Product) -> Any:
        if isinstance(other, type(self)):
            return self.__price * self.quantity + other.price * other.quantity
        else:
            raise TypeError('Товары разных типов складывать нельзя')

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price > 0:
            if self.__price > new_price:
                answer = input('Подтверждаете понижение цены? Да введите "Y", нет введите "N" ')
                if answer.lower() != 'y':
                    return
            self.__price = new_price
        else:
            print('Цена не должна быть нулевая или отрицательная')

    @staticmethod
    def check_product_matching(product: Product, products: list) -> None:
        for p in products:
            if p.name == product.name and p.description == product.description:
                if p.price < product.price:
                    p.price = product.price
                p.quantity += product.quantity
                return
        products.append(product)
        return

    @classmethod
    def new_product(cls, params: dict, products: list) -> Product:
        try:
            name = params['name']
            description = params['description']
            price = params['price']
            quantity = params['quantity']
        except Exception('Количество или тип параметров не соответстует ожиданию') as e:
            print(f'Ошибка: {e}')
        product_new = Product(name, description, price, quantity)
        Product.check_product_matching(product_new, products)
        return product_new
