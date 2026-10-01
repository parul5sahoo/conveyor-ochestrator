---
name: thermal-overload-monitoring
parent_domain: conveyor-diagnostics
parent_discipline: motor-drive-diagnostics
display_name: "VFD Inverter Thermal Overload Monitoring"
hierarchy_level: 3
level_name: "OPERATIONAL_MICRO_SKILL"
description: "Monitors IGBT junction temperatures and calculates current derating to prevent motor winding insulation breakdown."
tags: ["thermal", "overload", "vfd", "igbt", "winding", "temperature"]
---

# VFD Inverter Thermal Overload Monitoring (Level 3 Operational Micro-Skill)

**Hierarchy Path**: `conveyor-diagnostics` ➔ `motor-drive-diagnostics` ➔ `thermal-overload-monitoring`

## Description
Monitors IGBT junction temperatures and calculates current derating to prevent motor winding insulation breakdown.

### Standard Operating Procedure: VFD Thermal Monitoring
1. **Thermal Thresholds**: Normal operating range is 45C - 70C. Above 80C initiates automated 15% speed derating.
2. **Shutdown Interlock**: Temperature exceeding 95C trips the emergency thermal overload relay.

## Executable Helper Script
Executable implementation available at `scripts/tool.py`.
