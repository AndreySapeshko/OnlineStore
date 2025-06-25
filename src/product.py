from itertools import product


class Product:
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity


    @property
    def price(self) -> float:
        return self.__price


    @price.setter
    def price(self, new_price: float) -> None:
        if new_price > 0:
            if self.__price > new_price:
                answer = input('Подтверждаете понижение цены? Да введите "Y", нет введите "N" ')
                if answer.lower() != 'y':
                    return
            self.__price = new_price
        else:
            print('Цена не должна быть нулевая или отрицательная')


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
