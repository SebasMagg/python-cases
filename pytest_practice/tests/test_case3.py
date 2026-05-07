import pytest 
from cases.case3 import calculate_damage

@pytest.mark.parametrize("sword, arrow, spear, dagger, fireball, expected_output", [
    (3, 5, 2, 1, 4, (15, 3.0)),
    (5, 5, 5, 5, 5, (25, 5.0)),
    (1, 2, 3, 4, 5, (15, 3.0)),
    (0, 0, 0, 0, 10, (10, 2.0)),
    (0, 0, 0, 0, 0, (0, 0.0)),
    (10, 20, 30, 40, 50, (150, 30.0)),
    (2, 2, 2, 2, 2, (10, 2.0)),
    (1, 1, 1, 1, 1, (5, 1.0))
])

def test_calculate_damage(sword, arrow, spear, dagger, fireball, expected_output):
    assert calculate_damage(sword, arrow, spear, dagger, fireball) == expected_output