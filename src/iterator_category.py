from typing import Any
from src.category import Category
from __future__ import annotations

class IteratorCategory:
    category: Category
    index_category: int = 0

    def __init__(self, category: Category) -> None:
        self.category = category

    def __iter__(self) -> IteratorCategory:
        self.current_value = -1
        return self

    def __next__(self) -> Any:
        if self.current_value + 1 < len(self.category.products):
            self.current_value += 1
            return self.category.products[self.current_value]
        else:
            raise StopIteration
