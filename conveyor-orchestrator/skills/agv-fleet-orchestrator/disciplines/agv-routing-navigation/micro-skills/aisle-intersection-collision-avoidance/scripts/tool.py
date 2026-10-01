# Intersection Priority Arbitrator
def arbitrate_intersection_token(vehicle_a: str, is_loaded_a: bool, vehicle_b: str, is_loaded_b: bool):
    # Loaded vehicles have right of way over unloaded to prevent momentum shift
    winner = vehicle_a if is_loaded_a and not is_loaded_b else (vehicle_b if is_loaded_b and not is_loaded_a else vehicle_a)
    return {"granted_vehicle": winner, "waiting_vehicle": vehicle_b if winner == vehicle_a else vehicle_a, "yield_seconds": 4.0}
