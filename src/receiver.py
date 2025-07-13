from abc import ABC, abstractmethod
from src.product import Product


class Receiver(ABC):
    """ Абстрактный класс задающий создание метода добовление
    продуктов для объектос содержащих список продуктов """

    @abstractmethod
    def add_product(self, product: Product) -> None:
        pass