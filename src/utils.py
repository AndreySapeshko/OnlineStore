import json
import os

from src.category import Category
from src.product import Product


def read_from_json(file_name: str) -> list[dict]:
    """ Функция читает из файла в формате json данные и возвращает в виде списка словарей """

    data = []
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as file:
            data = json.load(file)
    return data


def created_category_with_products(file_name: str) -> list[Category]:
    """ Функция принимает имя json файла в котором указаны категории и соответствующие
    им списки продуктов. На основе этих данных создает объекты категорий с списками продуктов
     и возвращает их в списке. """

    data = read_from_json(file_name)
    categories = []
    if len(data) != 0:
        for category in data:
            products = [Product(
                x.get('name'),
                x.get('description'),
                x.get('price'),
                x.get('quantity')
            ) for x in category.get('products') if category.get('products')]
            categories.append(Category(category.get('name'), category.get('description'), products=products))
    return categories
