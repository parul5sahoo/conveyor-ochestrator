---
name: pneumatic-residual-bleed-off
parent_domain: warehouse-ehs-safety
parent_discipline: energy-isolation-loto
display_name: "Pneumatic Accumulator Bleed-Off & Pressure Dump"
hierarchy_level: 3
level_name: "OPERATIONAL_MICRO_SKILL"
description: "Verifies discharge of stored kinetic energy in pneumatic pusher cylinders and pressure vessels."
tags: ["pneumatic", "pressure dump", "bleed-off", "accumulator", "air pressure"]
---

# Pneumatic Accumulator Bleed-Off & Pressure Dump (Level 3 Operational Micro-Skill)

**Hierarchy Path**: `warehouse-ehs-safety` ➔ `energy-isolation-loto` ➔ `pneumatic-residual-bleed-off`

## Description
Verifies discharge of stored kinetic energy in pneumatic pusher cylinders and pressure vessels.

### Standard Operating Procedure: Pneumatic Residual Bleed-Off
1. **Air Supply Isolation**: Close ball valve on main 90 PSI pneumatic supply header.
2. **Pressure Relief**: Manually actuate yellow safety bleed dump valve.
3. **Gauge Verification**: Confirm mechanical Bourdon tube pressure gauge registers 0.0 PSI.

## Executable Helper Script
Executable implementation available at `scripts/tool.py`.
