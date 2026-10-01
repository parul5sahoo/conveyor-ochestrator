# NIOSH Lifting Risk Calculator
def evaluate_lifting_risk(weight_lbs: float, horizontal_distance_in: float = 10, frequency_per_min: float = 4):
    rwl = 51.0 * (10 / max(10, horizontal_distance_in)) * (1.0 - (0.0075 * min(100, frequency_per_min * 10)))
    lifting_index = weight_lbs / max(1.0, rwl)
    is_safe = lifting_index <= 1.0
    return {
        "actual_weight_lbs": weight_lbs,
        "recommended_weight_limit_lbs": round(rwl, 1),
        "lifting_index": round(lifting_index, 2),
        "risk_level": "LOW (ACCEPTABLE)" if is_safe else "HIGH (TEAM LIFT OR HOIST REQUIRED)",
        "action_required": "Proceed with single operator" if is_safe else "Engage 2-person team lift or vacuum hoist"
    }
