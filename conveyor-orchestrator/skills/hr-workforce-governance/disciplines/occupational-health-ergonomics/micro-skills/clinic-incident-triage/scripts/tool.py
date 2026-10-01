# Clinic Incident Triage Router
def triage_clinic_incident(injury_type: str, severity: str, lost_workdays: int = 0):
    is_osha_recordable = severity.upper() in ["CRITICAL", "MAJOR"] or lost_workdays > 0
    return {
        "injury_type": injury_type,
        "severity": severity.upper(),
        "osha_300_recordable": is_osha_recordable,
        "protocol": "Immediate ER Escort & Executive Notification" if severity.upper() == "CRITICAL" else "Station 1 First Aid Treatment",
        "dispatch_clinic": True
    }
