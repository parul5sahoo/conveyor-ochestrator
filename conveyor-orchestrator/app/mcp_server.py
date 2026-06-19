import json
import sys
from mcp.server.fastmcp import FastMCP

# Define a FastMCP server named "AGV Telemetry Server"
mcp = FastMCP("AGV Telemetry Server")

# Simulated Dynamic AGV Fleet Telemetry database
AGV_FLEET = {
    "PickerBot-Alpha": {
        "bot_id": "PickerBot-Alpha",
        "status": "IDLE",
        "battery": 12,
        "location": "Aisle 2",
        "notes": "CRITICAL WARNING: Battery low (12%). Below 20% safety threshold. Do not dispatch."
    },
    "PickerBot-Beta": {
        "bot_id": "PickerBot-Beta",
        "status": "IDLE",
        "battery": 88,
        "location": "Aisle 6",
        "notes": "Optimal battery level (88%). Highly recommended and safe for dispatch."
    },
    "PickerBot-Gamma": {
        "bot_id": "PickerBot-Gamma",
        "status": "BUSY",
        "battery": 95,
        "location": "Aisle 1",
        "notes": "Currently handling a heavy pallet sorting task in Aisle 1."
    }
}

@mcp.tool()
def list_available_agvs() -> str:
    """Retrieve the real-time status and battery levels of all active Automated Guided Vehicles (AGVs) in the fleet.
    
    Use this tool to see the current locations, operational states, and battery percentages of the vehicles.
    
    Returns:
        A JSON string containing the list of all active AGVs on the floor.
    """
    return json.dumps(list(AGV_FLEET.values()), indent=2)

@mcp.tool()
def get_agv_vitals(bot_id: str) -> str:
    """Retrieve detailed real-time health, battery status, and notes for a specific Automated Guided Vehicle (AGV).
    
    Args:
        bot_id: The unique identifier of the AGV (e.g. 'PickerBot-Alpha', 'PickerBot-Beta', 'PickerBot-Gamma').
        
    Returns:
        A JSON string containing the detailed vitals of the requested AGV.
    """
    bot = AGV_FLEET.get(bot_id)
    if not bot:
        return json.dumps({"error": f"AGV '{bot_id}' not found in the fleet registry."}, indent=2)
    return json.dumps(bot, indent=2)

if __name__ == "__main__":
    mcp.run()
