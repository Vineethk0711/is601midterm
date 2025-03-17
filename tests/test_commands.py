import pytest
from calculator.commands import add, subtract, multiply, divide

def test_add():
    assert add.run(3, 2) == 5

def test_subtract():
    assert subtract.run(3, 2) == 1

def test_multiply():
    assert multiply.run(3, 2) == 6

def test_divide():
    assert divide.run(6, 2) == 3

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide.run(6, 0)
