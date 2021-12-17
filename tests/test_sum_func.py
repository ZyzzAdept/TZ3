from functions import sum_of_numbers
import pytest


@pytest.mark.parametrize("num_list, expected_result", [([1.0, 2.5, 0.35, -6.0, 10.0], 7.85),
                                                       ([-10, 0, -1, -0.5, 0.5], -11.0)])
def test_sum(num_list, expected_result):
    assert sum_of_numbers(num_list) == expected_result
