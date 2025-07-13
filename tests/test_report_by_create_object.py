from pytest import CaptureFixture

from src.report_by_create_object import ReportByCreateObject


class TestClass(ReportByCreateObject):

    def __init__(self, arg1: str, arg2: str, arg3: str) -> None:
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        super().__init__()


def test_report_by_create_object(capsys: CaptureFixture[str]) -> None:
    TestClass('One', 'Two', 'Three')
    captured = capsys.readouterr()
    assert captured.out == 'TestClass(One, Two, Three)\n'
