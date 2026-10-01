# Shift Differential Calculation Tool
def calculate_shift_differential(base_rate: float, hours_worked: float, shift_type: str = "NIGHT"):
    rates = {"DAY": 0.0, "EVENING": 0.15, "NIGHT": 0.22, "GRAVEYARD": 0.22}
    diff_rate = rates.get(shift_type.upper(), 0.0)
    effective_hourly = base_rate * (1.0 + diff_rate)
    total_comp = effective_hourly * hours_worked
    return {
        "base_hourly_rate": base_rate,
        "shift_type": shift_type.upper(),
        "differential_pct": f"{diff_rate * 100}%",
        "effective_hourly_rate": round(effective_hourly, 2),
        "total_compensation": round(total_comp, 2)
    }
