from functions import minimum_number
import pytest


@pytest.mark.parametrize("num_list, expected_result", [([1.0, 2.5, 0.35, -6.0, 10.0], -6.0),
                                                       ([0, 0, 15, 3], 0)])
def test_minimum_num(num_list, expected_result):
    assert minimum_number(num_list) == expected_result

