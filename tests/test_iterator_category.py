from src.category import Category
from src.iterator_category import IteratorCategory


def test_iterator_categories(category: Category) -> None:
    count_products = 0
    iterator_category = IteratorCategory(category)
    for product in iterator_category:
        count_products += 1
    assert count_products == 2
