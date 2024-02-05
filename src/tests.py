import pytest

from src.fibonacci import fibonacci


@pytest.mark.parametrize(
    'n, expected',
    [
        pytest.param(0, 0, id='zero'),
    ]
)
def test_fibonacci(n, expected):
    assert fibonacci(n) == expected
