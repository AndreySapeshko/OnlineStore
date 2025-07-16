from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    """ Абстрактный класс задающий обязательную функциональность для всех продуктов """

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __add__(self, other: Any) -> Any:
        pass
