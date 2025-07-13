from abc import ABC, abstractmethod
from src.product import Product


class Receiver(ABC):

    @abstractmethod
    def add_product(self, product: Product) -> None:
        pass