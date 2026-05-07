def unlock_achievement(before_xp, ach_xp, ach_name):
    final_xp = before_xp + ach_xp
    alert = f"Achievement Unlocked: {ach_name}"
    return final_xp, alert