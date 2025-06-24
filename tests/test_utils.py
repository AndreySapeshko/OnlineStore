from src.utils import created_category_with_products, read_from_json


def test_read_from_json(categories_json_file: list) -> None:
    expected_list = categories_json_file[0]
    file_name = categories_json_file[1]
    data_from_json = read_from_json(file_name)
    assert len(data_from_json) == len(expected_list)
    for i in range(len(data_from_json)):
        assert data_from_json[i].get('name') == expected_list[i].get('name')
        assert data_from_json[i].get('description') == expected_list[i].get('description')
        assert len(data_from_json[i].get('products')) == len(expected_list[i].get('products'))


def test_created_category_with_product(categories_json_file: list) -> None:
    expected_list = categories_json_file[0]
    file_name = categories_json_file[1]
    categories_from_json = created_category_with_products(file_name)
    assert len(categories_from_json) == len(expected_list)
    for i in range(len(categories_from_json)):
        assert categories_from_json[i].name == expected_list[i].get('name')
        assert categories_from_json[i].description == expected_list[i].get('description')
        assert len(categories_from_json[i].products) == len(expected_list[i].get('products'))
