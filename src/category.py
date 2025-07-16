from src.product import Product
from src.receiver import Receiver


class Category(Receiver):
    """ Класс описыавет категорию каких то продуктов, у нее есть имя,
    опесание и список входящих в категорию продуктов. В классе есть две переменные,
    одна отражает сколько всего категорий созданно, вторая сколко продуктов в этих категориях """

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
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError('Добавлять можно только объекты класса Product и его наследники')

    @property
    def products(self) -> list[Product]:
        for product in self.__products:
            print(str(product))
        return self.__products
