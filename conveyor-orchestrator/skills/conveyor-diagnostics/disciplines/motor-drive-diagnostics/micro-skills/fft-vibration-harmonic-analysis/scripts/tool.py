# FFT Vibration Severity Classifier
def evaluate_vibration_severity(rms_velocity_mms: float, peak_frequency_hz: float, motor_rpm: float = 1750):
    motor_freq = motor_rpm / 60.0
    fault_type = "NORMAL"
    if 4.5 <= rms_velocity_mms < 7.1:
        severity = "WARNING"
        fault_type = "BEARING_DEGRADATION" if peak_frequency_hz > 3 * motor_freq else "MISALIGNMENT"
    elif rms_velocity_mms >= 7.1:
        severity = "CRITICAL_TRIP"
        fault_type = "IMMINENT_BEARING_FAILURE"
    else:
        severity = "ACCEPTABLE"
    return {"rms_velocity_mms": rms_velocity_mms, "severity": severity, "diagnosed_fault": fault_type}
