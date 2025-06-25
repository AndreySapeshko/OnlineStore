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


    @classmethod
    def new_product(cls, params: list) -> None:
        try:
            name = params[0]
            description = params[1]
            price = params[2]
            quantity = params[3]
        except Exception('Количество или тип параметров не соответстует ожиданию') as e:
            print(f'Ошибка: {e}')
        return Product(name, description, price, quantity)


    @staticmethod
    def check_product_matching(products: list) -> None:
        pass
