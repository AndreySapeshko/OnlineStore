from src.category import Category

class IteratorCategory:
    category: Category
    index_category: int = 0

    def __init__(self, category) -> None:
        self.category = category

    def __iter__(self):
        self.current_value = -1
        return self

    def __next__(self):
        if self.current_value + 1 < len(self.category.products):
            self.current_value += 1
            return self.category.products[self.current_value]
        else:
            raise StopIteration
