# VFD Thermal Monitor
def check_vfd_thermal_limits(temp_celsius: float):
    if temp_celsius > 95:
        return {"action": "EMERGENCY_SHUTDOWN", "derate_pct": 100, "status": "OVERHEAT_PROTECTION_TRIPPED"}
    elif temp_celsius > 80:
        return {"action": "DERATE_SPEED", "derate_pct": 15, "status": "THERMAL_WARNING_ACTIVE"}
    return {"action": "NORMAL_OPERATION", "derate_pct": 0, "status": "NOMINAL"}
