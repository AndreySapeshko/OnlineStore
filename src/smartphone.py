from src.product import Product


class Smartphone(Product):
    """ Класс описывает продукт смартфон помимо наследуемых полей добавлены
     эффективность, модель, память и цвет """

    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(self, name: str, description: str, price: float, quantity: int, efficiency: float, model: str,
                 memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
