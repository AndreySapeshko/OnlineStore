from typing import Any

import pytest
from pytest import CaptureFixture

from src.report_by_create_object import ReportByCreateObject
from src.product import Product


class TestClass(ReportByCreateObject):

    def __init__(self, arg1: Any, arg2: Any, arg3: Any) -> None:
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        super().__init__()

@pytest.mark.parametrize('arg1, arg2, arg3, expected', [
    ('One', 'Two', 'Three', 'TestClass(One, Two, Three)\n'),
    ('One', 2, 3.0, 'TestClass(One, 2, 3.0)\n')
])
def test_report_by_create_object(arg1: Any, arg2: Any, arg3: Any, expected: str, capsys: CaptureFixture[str]) -> None:
    TestClass(arg1, arg2, arg3)
    captured = capsys.readouterr()
    assert captured.out == expected


def test_report_with_product(capsys: CaptureFixture[str]) -> None:
    Product('Samsung Galaxy S23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0, 5)
    captured = capsys.readouterr()
    assert captured.out == 'Product(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)\n'
