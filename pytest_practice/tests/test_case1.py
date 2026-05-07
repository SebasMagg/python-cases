import pytest 
from cases.case1 import total_xp

@pytest.mark.parametrize("level, xp, expected",[
    (1, 200, 300),
    (2, 50, 250),
    (0, 0, 0),
    (0, 200, 200),
    (176, 350, 17950),
    (250, 100, 25100),
])

def test_total_xp(level, xp, expected):
    assert total_xp(level, xp) == expected