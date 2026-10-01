# Payload Balancer
def audit_pallet_payload(weight_kg: float, offset_x_mm: float, offset_y_mm: float):
    import math
    dist = math.sqrt(offset_x_mm**2 + offset_y_mm**2)
    is_safe = weight_kg <= 1200.0 and dist <= 400.0
    return {
        "weight_kg": weight_kg,
        "cog_offset_mm": round(dist, 1),
        "is_safe": is_safe,
        "curve_speed_factor": 0.75 if weight_kg > 800 else 1.0,
        "warning": None if is_safe else "UNBALANCED CARGO OR OVERWEIGHT: Re-stack pallet before AGV transport"
    }
