from itertools import product


class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @staticmethod
    def check_product_matching(product, products: list) -> bool:
        for p in products:
            if p.name == product.name and p.description == product.description:
                if p.price < product.price:
                    p.price = product.price
                p.quantity += product.quantity
                return
        products.append(product)
        return


    @classmethod
    def new_product(cls, params: list, products: list) -> None:
        try:
            name = params[0]
            description = params[1]
            price = params[2]
            quantity = params[3]
        except Exception('Количество или тип параметров не соответстует ожиданию') as e:
            print(f'Ошибка: {e}')
        product = Product(name, description, price, quantity)
        Product.check_product_matching(product, products)
        return
