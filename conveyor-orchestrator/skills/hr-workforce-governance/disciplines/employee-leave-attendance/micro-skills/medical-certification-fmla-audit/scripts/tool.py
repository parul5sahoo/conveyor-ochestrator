# Medical Certification & FMLA Verification Script
def verify_medical_certification(absence_consecutive_days: int, hours_worked_past_year: int = 1300):
    requires_doctor_note = absence_consecutive_days >= 3
    fmla_eligible = hours_worked_past_year >= 1250
    return {
        "absence_days": absence_consecutive_days,
        "requires_medical_note": requires_doctor_note,
        "policy_rule": "SOP-HR-LEAVE-SEC-3: Doctor note required for >= 3 consecutive days." if requires_doctor_note else "Self-certified short illness.",
        "fmla_eligible": fmla_eligible,
        "status": "CLEARANCE_REQUIRED" if requires_doctor_note else "APPROVED"
    }
