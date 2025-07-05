from src.iterator_category import IteratorCategory
from src.category import Category


def test_iterator_categories(category: Category) -> None:
    count_products = 0
    for product in category.products:
        count_products += 1
    assert count_products == len(category.products)