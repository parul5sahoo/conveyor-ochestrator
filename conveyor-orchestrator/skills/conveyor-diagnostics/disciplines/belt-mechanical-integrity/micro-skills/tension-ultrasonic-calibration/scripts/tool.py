# Belt Tension Calculator
def evaluate_belt_tension(measured_freq_hz: float):
    target = 42.0
    variance = measured_freq_hz - target
    return {
        "measured_hz": measured_freq_hz,
        "status": "OPTIMAL" if abs(variance) <= 2.5 else ("SLACK_WARNING" if variance < -2.5 else "OVERTIGHT_WARNING"),
        "hydraulic_adjustment_mm": round(-variance * 1.8, 1)
    }
