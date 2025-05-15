import pytest
from solution import sum_two

def test_sum_two_valid():
    """Корректные аргументы"""
    assert sum_two(1, 2) == 3

def test_sum_two_invalid_type():
    """Некорректный тип аргумента"""
    with pytest.raises(TypeError) as exc_info:
        sum_two(1, 2.4)

    assert "Argument 'b' must be int, not float" in str(exc_info.value)

def test_sum_two_both_invalid():
    """Оба аргумента некорректные"""
    with pytest.raises(TypeError) as exc_info:
        sum_two("1", "2")
    assert "Argument 'a' must be int, not str" in str(exc_info.value)
