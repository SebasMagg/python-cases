import pytest 
from cases.case4 import binary_string_to_int

@pytest.mark.parametrize("input1, input2, input3, expected_output", [
    ("1", "10", "1010", (1, 2, 10)),
    ("101", "11", "10100", (5, 3, 20)),
    ("111", "1011", "11010", (7, 11, 26)),
    ("0", "0", "0", (0, 0, 0)),
    ("1111", "1111", "1111", (15, 15, 15)),
    ("101010", "110011", "101010", (42, 51, 42))
])

def test_binary_string_to_int(input1, input2, input3, expected_output):
    assert binary_string_to_int(input1, input2, input3) == expected_output