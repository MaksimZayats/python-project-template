import pytest

from application import utils


@pytest.mark.parametrize("a, b, result", ((1, 2, 3), (-1, 1, 0), (2, 0, 2)))
def test_sum(a: float, b: float, result: float):
    assert utils.sum_over_two_values(a, b) == result
