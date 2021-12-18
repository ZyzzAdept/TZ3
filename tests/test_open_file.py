from functions import open_file
import pytest


@pytest.mark.parametrize("file_name, expected_list", [("open_file_test.txt", [12.9, 14.0, 0, 5.1]),
                                                      ("open_file_test_2.txt", [0, 1.1, 1.0, 1847.822])])
def test_open_file(file_name, expected_list):
    assert open_file(file_name) == expected_list
