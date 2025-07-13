from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __add__(self, other) -> Any:
        pass
