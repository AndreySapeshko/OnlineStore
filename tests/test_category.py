from src.product import Product


def test_category(category):
    assert category.name == 'Смартфоны'
    assert category.description == 'Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни'
    assert len(category.products) == 2
    assert category.categories_count == 1
    assert category.products_count == 2