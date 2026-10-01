---
name: rfid-triangulation-localization
parent_domain: wms-inventory-resolver
parent_discipline: rfid-iot-rack-tracking
display_name: "RFID RSSI Rack Triangulation & Tote Localization"
hierarchy_level: 3
level_name: "OPERATIONAL_MICRO_SKILL"
description: "Calculates spatial coordinates of misplaced totes using Received Signal Strength Indicator (RSSI) from fixed antenna arrays."
tags: ["rfid", "rssi", "triangulation", "lost tote", "localization"]
---

# RFID RSSI Rack Triangulation & Tote Localization (Level 3 Operational Micro-Skill)

**Hierarchy Path**: `wms-inventory-resolver` ➔ `rfid-iot-rack-tracking` ➔ `rfid-triangulation-localization`

## Description
Calculates spatial coordinates of misplaced totes using Received Signal Strength Indicator (RSSI) from fixed antenna arrays.

### Standard Operating Procedure: RFID RSSI Triangulation
1. **Antenna Array Sweep**: Engage fixed Impinj Speedway R420 readers across Aisle 4.
2. **Signal Filtering**: Apply Kalman filtering to RSSI signals across 4 antenna portals to eliminate multipath reflections.
3. **Coordinate Calculation**: Resolve spatial (X, Y, Z) coordinates down to rack shelf level (+/- 15 cm accuracy).

## Executable Helper Script
Executable implementation available at `scripts/tool.py`.
