import pytest
from controllers import operation


@pytest.mark.parametrize('a, b, expected', [
    (1, 2, 3),
    (5, -4, 1),
    (7, 8, 15),
    (0, 0, 0),
    (-10, 5, -5)
])
def test_operation(a: int, b: int, expected: int) -> None:
    received = operation(a, b)
    assert received == expected


def test_operation_with_none():
    assert operation(None, 5) is None
    assert operation(5, None) is None
    assert operation(None, None) is None