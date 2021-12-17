from functions import maximum_number
import pytest


@pytest.mark.parametrize("num_list, expected_result", [([1.0, 2.5, 0.35, -6.0, 10.0], 10),
                                                       ([0, -3, -15, -100], 0)])
def test_maximum_num(num_list, expected_result):
    assert maximum_number(num_list) == expected_result
