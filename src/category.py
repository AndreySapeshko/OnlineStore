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


    def add_product(self, product: Product) -> None:
        self._products.append(product)


    @property
    def products(self) -> list[Product]:
        for product in self._products:
            print(f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.')
        return self._products

categ = Category(
        name='Смартфоны',
        description='Смартфоны, как средство не только коммуникации, '
                    'но и получения дополнительных функций для удобства жизни',
        products=[
            Product('Iphone 15', '512GB, Gray space', 210000.0, 8),
            Product('Xiaomi Redmi Note 11', '1024GB, Синий', 31000.0, 14)
        ]
    )

categ.add_product(Product('Samsung Galaxy S23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0, 5))
categ.products
