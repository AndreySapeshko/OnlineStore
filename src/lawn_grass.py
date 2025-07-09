from src.product import Product


class LawnGrass(Product):
    """ Описывает продукт "газонная трава" помимо полей наследуемых от Product
     добавлены страна происхождения, период роста и цвет """

    country: str
    germination_period: str
    color: str

    def __init__(self, name: str, description: str, price: float, quantity: int, country: str,
                 germination_period: str, color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
