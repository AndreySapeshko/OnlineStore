from src.order import Order
from src.product import Product


def test_order(product: Product, order: Order) -> None:
    order.add_product(product)
    assert order.id_order == 1
    assert order.user_name == 'Sergey'
    assert len(order.get_products()) == 1
