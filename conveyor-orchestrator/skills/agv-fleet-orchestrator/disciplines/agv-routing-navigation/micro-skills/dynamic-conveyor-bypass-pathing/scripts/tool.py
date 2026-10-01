# AGV Graph Bypass Router
def calculate_agv_conveyor_detour(blocked_conveyor_zone: str):
    detour_map = {
        "ZONE-1": ["AISLE-A01", "AISLE-B04", "TRANSFER-BAY-02"],
        "ZONE-2": ["AISLE-B08", "AISLE-C02", "INDUCTION-STATION-01"],
        "ZONE-3": ["CROSS-AISLE-NORTH", "AISLE-D10", "DISPATCH-SPUR-04"]
    }
    path = detour_map.get(blocked_conveyor_zone.upper(), ["MAIN-CORRIDOR-WEST", "BAY-DEFAULT"])
    return {"blocked_zone": blocked_conveyor_zone, "detour_path": path, "estimated_added_seconds": 38.5, "speed_limit_ms": 1.2}
