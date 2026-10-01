---
name: opportunity-charging-dispatch
parent_domain: agv-fleet-orchestrator
parent_discipline: fleet-energy-management
display_name: "State-of-Charge (SoC) Opportunity Charging Dispatch"
hierarchy_level: 3
level_name: "OPERATIONAL_MICRO_SKILL"
description: "Routes AGVs with < 35% battery to available inductive floor pads during shift change or task idle cycles."
tags: ["battery", "soc", "inductive charging", "opportunity charging", "fleet energy"]
---

# State-of-Charge (SoC) Opportunity Charging Dispatch (Level 3 Operational Micro-Skill)

**Hierarchy Path**: `agv-fleet-orchestrator` ➔ `fleet-energy-management` ➔ `opportunity-charging-dispatch`

## Description
Routes AGVs with < 35% battery to available inductive floor pads during shift change or task idle cycles.

### Standard Operating Procedure: Opportunity Charging Dispatch
1. **Battery Threshold**:
   - SoC < 20%: Immediate task cancellation, emergency high-priority dock at Pad CP-01.
   - 20% <= SoC <= 35%: Opportunity charge assignment when current tote drop-off concludes.
   - SoC > 80%: Release back to active fleet dispatch queue.
2. **Inductive Pad Alignment**: Laser guidance aligns AGV coils within +/- 5 mm for 94% power transfer efficiency.

## Executable Helper Script
Executable implementation available at `scripts/tool.py`.
