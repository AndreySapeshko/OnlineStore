from _pytest.capture import CaptureFixture

from src.main import main

expected_main = ('Product(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)\n'
                 'Product(Iphone 15, 512GB, Gray space, 210000.0, 8)\n'
                 'Product(Xiaomi Redmi Note 11, 1024GB, Синий, 31000.0, 14)\n'
                 'Samsung Galaxy S23 Ultra\n'
                 '256GB, Серый цвет, 200MP камера\n'
                 '180000.0\n'
                 '5\n'
                 'Iphone 15\n'
                 '512GB, Gray space\n'
                 '210000.0\n'
                 '8\n'
                 'Xiaomi Redmi Note 11\n'
                 '1024GB, Синий\n'
                 '31000.0\n'
                 '14\n'
                 'True\n'
                 'Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни\n'
                 'Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n'
                 'Iphone 15, 210000.0 руб. Остаток: 8 шт.\n'
                 'Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n'
                 '3\n'
                 '1\n'
                 '3\n'
                 'Product(55" QLED 4K, Фоновая подсветка, 123000.0, 7)\n'
                 'Телевизоры\n'
                 'Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником\n'
                 '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.\n'
                 '1\n'
                 '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.\n'
                 '[Product(55" QLED 4K, Фоновая подсветка, 123000.0, 7)]\n'
                 '2\n'
                 '4\n')


def test_main(capsys: CaptureFixture[str]) -> None:
    main()
    captured = capsys.readouterr()
    assert captured.out == expected_main
