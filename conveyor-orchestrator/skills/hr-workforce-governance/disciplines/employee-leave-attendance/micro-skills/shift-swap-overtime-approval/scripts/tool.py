# Shift Swap Rest Period Validator
def validate_shift_swap(end_prev_shift_hour: float, start_next_shift_hour: float):
    rest_gap = (start_next_shift_hour - end_prev_shift_hour) % 24
    is_valid = rest_gap >= 8.0
    return {
        "rest_interval_hours": rest_gap,
        "minimum_required": 8.0,
        "approved": is_valid,
        "warning": None if is_valid else "FATIGUE ALERT: Less than 8 hours rest between shifts!"
    }
