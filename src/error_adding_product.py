class ErrorAddingProduct(Exception):
    """ Класс исключение применяемый при добавлении продуктов в заказы и категории """

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Ошибка добавления продукта.'

    def __str__(self):
        return self.message