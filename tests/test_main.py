from _pytest.capture import CaptureFixture

from src.category import Category
from src.main import main

expected_main = ('Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт с нулевым количеством\n'
                 'Product(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)\n'
                 'Product(Iphone 15, 512GB, Gray space, 210000.0, 8)\n'
                 'Product(Xiaomi Redmi Note 11, 1024GB, Синий, 31000.0, 14)\n'
                 '15592.59\n'
                 '0.0\n'
                 )


def test_main(capsys: CaptureFixture[str]) -> None:
    main()
    captured = capsys.readouterr()
    assert captured.out == expected_main
