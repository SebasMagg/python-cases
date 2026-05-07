import pytest
from cases.case2 import unlock_achievement

@pytest.mark.parametrize("before_xp, ach_xp, ach_name, expected_output",[
    (100, 20, "Speedster",   (120, "Achievement Unlocked: Speedster")),
    (200, 50, "Killer",      (250, "Achievement Unlocked: Killer")),
    (100, 50, "Unstoppable", (150, "Achievement Unlocked: Unstoppable")),
    (400, 75, "Gnarly",      (475, "Achievement Unlocked: Gnarly"))
])

def test_unlock_achievement(before_xp, ach_xp, ach_name, expected_output):
    assert unlock_achievement(before_xp, ach_xp, ach_name) == expected_output