from src.product import Product


class Category:
    name: str
    description: str
    __products: list[Product]
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product] = None) -> None:
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self) -> str:
        count_products = 0
        for product in self.__products:
            count_products += product.quantity
        return f'{self.name}, количество продуктов: {count_products} шт.'

    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> list[Product]:
        for product in self.__products:
            print(str(product))
        return self.__products
