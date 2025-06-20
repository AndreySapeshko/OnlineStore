from src.category import Category
from src.product import Product
from src.utils import read_from_json, created_category_with_products


def test_read_from_json(categories_json_file) -> None:
    expected_list = categories_json_file[0]
    file_name = categories_json_file[1]
    data_from_json = read_from_json(file_name)
    assert len(data_from_json) == len(expected_list)
    for i in range(len(data_from_json)):
        assert data_from_json[i].get('name') == expected_list[i].get('name')
        assert data_from_json[i].get('description') == expected_list[i].get('description')
        assert len(data_from_json[i].get('products')) == len(expected_list[i].get('products'))