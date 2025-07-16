from _pytest.capture import CaptureFixture

from src.order import Order
from src.product import Product


def test_order(product: Product, order: Order) -> None:
    order.add_product(product)
    assert order.id_order == 1
    assert order.user_name == 'Sergey'
    assert len(order.get_products()) == 1


def test_order_add_product(product: Product, order: Order, capsys: CaptureFixture[str]) -> None:
    product_zero = Product('Product', 'without quantity', 1.0, 1)
    product_zero.quantity = 0
    order.add_product(product_zero)
    captured = capsys.readouterr()
    assert captured.out == ('Product(Product, without quantity, 1.0, 1)\n'
                            'Нельзя добавлять продукты с нулевым количеством.\n'
                            'Обработка добавления продукта завершена.\n')
    order.add_product(product)
    captured = capsys.readouterr()
    assert captured.out == 'Продукт успешно добавлен.\nОбработка добавления продукта завершена.\n'
