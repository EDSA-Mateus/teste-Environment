from calculator import calculate


def test_calculate_basic():
    assert calculate(2, 3) == 5


def test_calculate_with_multiplier():
    assert calculate(2, 3, multiplier=2) == 10
