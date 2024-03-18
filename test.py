import pytest

# Тесты для структуры данных str

def test_str_length():
    assert len("hello") == 5

def test_str_concatenation():
    assert "hello" + " " + "world" == "hello world"

def test_str_lower():
    assert "HELLO".lower() == "hello"


# Тесты для структуры данных tuple

def test_tuple_length():
    assert len((1, 2, 3)) == 3

def test_tuple_indexing():
    t = (1, 2, 3)
    assert t[0] == 1
    assert t[1] == 2
    assert t[2] == 3

@pytest.mark.parametrize("number", [-100, -1, 0, 1, 100])
def test_even_number(number):
    assert number % 2 == 0


def test_negative_division_by_zero():
    try:
        assert 1 / 0
    except ZeroDivisionError:
        pass

