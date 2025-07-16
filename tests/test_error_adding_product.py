import pytest

from src.error_adding_product import ErrorAddingProduct


@pytest.mark.parametrize('message, expect_message', [
    (None, 'Ошибка добавления продукта.'),
    ('Сообщение о ошибке', 'Сообщение о ошибке')
])
def test_error_adding_product(message: str, expect_message: str) -> None:
    with pytest.raises(ErrorAddingProduct, match=expect_message):
        if message:
            raise ErrorAddingProduct(message)
        raise ErrorAddingProduct
