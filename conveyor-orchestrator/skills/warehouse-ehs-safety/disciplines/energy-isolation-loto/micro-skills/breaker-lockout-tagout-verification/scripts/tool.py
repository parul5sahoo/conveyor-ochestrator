# LOTO Zero Energy Verification Tool
def verify_loto_isolation(technician_id: str, measured_voltage_v: float, hasp_installed: bool):
    is_safe = hasp_installed and (measured_voltage_v <= 0.05)
    return {
        "technician_id": technician_id,
        "zero_energy_verified": is_safe,
        "measured_voltage": measured_voltage_v,
        "loto_permit_status": "APPROVED_ACTIVE" if is_safe else "REJECTED_HAZARD_PRESENT",
        "osha_compliance": "PASS" if is_safe else "VIOLATION"
    }
