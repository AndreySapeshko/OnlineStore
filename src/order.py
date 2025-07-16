import datetime

from src.product import Product
from src.receiver import Receiver
from src.error_adding_product import ErrorAddingProduct


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
        try:
            if isinstance(product, Product):
                if product.quantity == 0:
                    raise ErrorAddingProduct('Нельзя добавлять продукты с нулевым количеством.')
                self.__products.append(product)
            else:
                raise TypeError('Добавлять можно только объекты класса Product и его наследники')
        except ErrorAddingProduct as e:
            print(e)
        except TypeError as e:
            print(e)
        else:
            print('Продукт успешно добавлен.')
        finally:
            print('Обработка добавления продукта завершена.')

    def get_products(self) -> list:
        result = self.__products
        return result
