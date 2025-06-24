from src.product import Product


class Category:
    name: str
    description: str
    _products: list[Product]
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]=None) -> None:
        self.name = name
        self.description = description
        self._products = products if products else []
        Category.category_count += 1
        Category.product_count += len(self._products)


    def add_product(self, product: Product):
        self._products.append(product)


    @property
    def products(self):
        for product in self._products:
            print(f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.')
        return self._products
