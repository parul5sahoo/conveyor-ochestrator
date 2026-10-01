# Holiday and Hazard Pay Calculator
def calculate_hazard_pay(base_rate: float, hours: float, is_holiday: bool = False, in_freezer_zone: bool = False):
    multiplier = 2.0 if is_holiday else 1.0
    stipend = 2.50 if in_freezer_zone else 0.0
    effective_rate = (base_rate * multiplier) + stipend
    return {
        "base_rate": base_rate,
        "is_holiday": is_holiday,
        "freezer_hazard_stipend": stipend,
        "effective_hourly_rate": round(effective_rate, 2),
        "total_gross": round(effective_rate * hours, 2)
    }
