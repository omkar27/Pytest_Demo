# tests/test_math.py
import pytest
from src.math_operations import add, subtract, divide

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (5, 5, 10),
    (10, -10, 0)
])
def test_add(a, b, expected):
    assert add(a, b) == expected

def test_subtract():
    assert subtract(10, 5) == 5

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
