from src.lawn_grass import LawnGrass


def test_lawn_grass(lawn_grass: LawnGrass) -> None:
    assert lawn_grass.name == 'Газонная трава'
    assert lawn_grass.description == 'Элитная трава для газона'
    assert lawn_grass.price == 500.0
    assert lawn_grass.quantity == 20
    assert lawn_grass.country == 'Россия'
    assert lawn_grass.germination_period == '7 дней'
    assert lawn_grass.color == 'Зеленый'
