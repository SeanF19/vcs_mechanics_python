import pytest

from src.fibonacci import fibonacci


@pytest.mark.parametrize(
    'n, expected',
    [
        pytest.param(0, 0, id='zero'),
        pytest.param(1, 1, id='one'),
        pytest.param(2, 1, id='two'),
    ]
)
def test_fibonacci(n, expected):
    assert fibonacci(n) == expected
