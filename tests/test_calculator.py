import calculator


def test_add():
    assert calculator.add(2, 3) == 5


def test_divide():
    assert calculator.divide(10, 2) == 5


def test_divide_by_zero():
    assert calculator.divide(5, 0) is None
