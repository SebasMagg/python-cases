import pytest 
from cases.case5 import player_status

@pytest.mark.parametrize("health, expected_status", [
    (0, "dead"),
    (4, "injured"),
    (6, "healthy"),
    (5, "injured"),
    (1, "injured"),
    (10, "healthy"),
    (-1, "dead")
])

def test_player_status(health, expected_status):
    assert player_status(health) == expected_status