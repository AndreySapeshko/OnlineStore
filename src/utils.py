import json
import os


from src.product import Product
from src.category import Category

def read_from_json(file_name: str) -> list[dict]:
    data = []
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as file:
            data = json.load(file)
    return data

def created_category_with_products(file_name: str) -> list[Category]:
    data = read_from_json(file_name)
    categories = []
    if len(data) != 0:
        for category in data:
            products = []
            if category.get('products'):
                products = [Product(
                    x.get('name'),
                    x.get('description'),
                    x.get('price'),
                    x.get('quantity')
                ) for x in category.get('products')]
            categories.append(Category(category.get('name'), category.get('description'), products= products))
    return categories


# categories = created_category_with_products('../data/products.json')
# for category in categories:
#     print(f'name: {category.name}, description: {category.description}, products: {len(category.products)}')
