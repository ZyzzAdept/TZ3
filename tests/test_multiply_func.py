from functions import numbers_multiply
import pytest


@pytest.mark.parametrize("num_list, expected_result", [([1.0, 2.5, 0.35, -6.0, 10.0], -52.5),
                                                       ([1, 2.5, 100, 0, 5, 2.5], 0)])
def test_multiply(num_list, expected_result):
    assert numbers_multiply(num_list) == expected_result
