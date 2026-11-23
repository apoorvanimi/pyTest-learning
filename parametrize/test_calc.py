import pytest

from parametrize.calc import add

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (-1, -4, -5),
    (0, 0, 0)
],ids=["positive numbers", "negative numbers", "zeroes"])
def test_add(a, b, expected):
    assert add(a, b) == expected    
    print(f"This is a test for add function with inputs: {a}, {b} and expected output: {expected}")