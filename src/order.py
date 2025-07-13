from src.receiver import Receiver
from src.product import Product

import datetime

class Order(Receiver):
    count_order: int = 0
    id_order: int
    user_name: str
    date_order: datetime
    __products: list[Product]

    def __init__(self, user_name, products=None):
        self.user_name = user_name
        self.__products = products if products else []
        self.date_order = datetime.datetime.now()
        Order.count_order += 1
        self.id_order = Order.count_order


    def add_product(self, product: Product) -> None:
        self.__products.append(product)
