import datetime

from src.product import Product
from src.receiver import Receiver


class Order(Receiver):
    """ Класс описывает заказ клиента у объекта есть поля
    id_заказа, имя пользователя, дата. У класса ест поле счетчик заказов """

    count_order: int = 0
    id_order: int
    user_name: str
    date_order: datetime.datetime
    __products: list[Product]

    def __init__(self, user_name: str, products: list = None) -> None:
        self.user_name = user_name
        self.__products = products if products else []
        self.date_order = datetime.datetime.now()
        Order.count_order += 1
        self.id_order = Order.count_order

    def add_product(self, product: Product) -> None:
        self.__products.append(product)

    def get_products(self) -> list:
        result = self.__products
        return result
