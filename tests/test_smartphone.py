from src.smartphone import Smartphone


def test_smartphone(smartphone: Smartphone) -> None:
    assert smartphone.name == 'Samsung Galaxy S23 Ultra'
    assert smartphone.description == '256GB, Серый цвет, 200MP камера'
    assert smartphone.price == 180000.0
    assert smartphone.quantity == 5
    assert smartphone.efficiency == 95.5
    assert smartphone.model == 'S23 Ultra'
    assert smartphone.memory == 256
    assert smartphone.color == 'Серый'
