# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Helper script to generate a large, highly structured warehouse telemetry log.

This generates fleet_telemetry_dump.json inside mock_data/ to represent log-plane
telemetry from 100+ AGVs and conveyor segments, including specific thermal anomalies.
"""

import json
import os
import random
from datetime import datetime, timedelta

def generate_logs():
    random.seed(42)  # For deterministic generation
    start_time = datetime(2026, 6, 22, 14, 0, 0)
    devices = [
        "PickerBot-Alpha",
        "PickerBot-Beta",
        "PickerBot-Gamma",
        "PickerBot-Delta",
        "Conveyor-CV11",
        "Conveyor-CV12",
        "Conveyor-CV15",
        "SorterBot-01",
        "SorterBot-02"
    ]
    
    entries = []
    
    # Generate 500 telemetry log entries spread across 1 hour
    for i in range(500):
        timestamp = start_time + timedelta(seconds=random.randint(0, 3600))
        device = random.choice(devices)
        
        # Default typical operating ranges
        aisle = f"Aisle {random.randint(1, 6)}"
        temperature = round(random.uniform(30.0, 70.0), 1)
        current_draw = round(random.uniform(2.0, 8.0), 1)
        speed = round(random.uniform(1.0, 2.0), 1)
        battery_level = random.randint(30, 100)
        
        # Inject deliberate high thermal stress anomalies around Aisle 4
        if i % 12 == 0:
            aisle = "Aisle 4"
            device = random.choice(["PickerBot-Beta", "PickerBot-Delta", "Conveyor-CV11"])
            temperature = round(random.uniform(85.0, 105.0), 1)  # Overheat
            current_draw = round(random.uniform(11.0, 16.0), 1) # High current draw
            speed = round(random.uniform(0.3, 0.8), 1)          # Sluggish speed
            battery_level = random.randint(10, 25)              # Low battery
            
        entries.append({
            "timestamp": timestamp.isoformat() + "Z",
            "device_id": device,
            "aisle": aisle,
            "temperature_c": temperature,
            "current_draw_a": current_draw,
            "speed_mps": speed,
            "battery_percent": battery_level
        })
        
    # Sort chronologically
    entries.sort(key=lambda x: x["timestamp"])
    
    output_dir = os.path.join(os.path.dirname(__file__), "..", "mock_data")
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "fleet_telemetry_dump.json")
    
    with open(output_file, "w") as f:
        json.dump(entries, f, indent=2)
        
    print(f"Successfully generated {len(entries)} telemetry entries at {output_file}")

if __name__ == "__main__":
    generate_logs()
