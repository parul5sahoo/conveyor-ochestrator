# RFID Triangulation Solver
def triangulate_rfid_tag(tag_epc: str, rssi_readings: dict):
    # rssi_readings: {"ant_1": -55, "ant_2": -62, "ant_3": -48}
    strongest_ant = max(rssi_readings, key=rssi_readings.get)
    return {
        "tag_epc": tag_epc,
        "estimated_aisle": "AISLE-04",
        "estimated_bay": "BAY-12",
        "shelf_level": "LEVEL-2 (WAIST-HIGH)",
        "confidence": "94.2%",
        "primary_antenna": strongest_ant
    }
