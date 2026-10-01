---
name: load-capacity-weight-balancing
parent_domain: agv-fleet-orchestrator
parent_discipline: fleet-energy-management
display_name: "Pallet Payload Capacity & Center-of-Gravity Balancer"
hierarchy_level: 3
level_name: "OPERATIONAL_MICRO_SKILL"
description: "Calculates payload mass distribution to prevent AGV tip-over during high-speed turns."
tags: ["payload", "center of gravity", "tip over", "weight limit", "pallet balance"]
---

# Pallet Payload Capacity & Center-of-Gravity Balancer (Level 3 Operational Micro-Skill)

**Hierarchy Path**: `agv-fleet-orchestrator` ➔ `fleet-energy-management` ➔ `load-capacity-weight-balancing`

## Description
Calculates payload mass distribution to prevent AGV tip-over during high-speed turns.

### Standard Operating Procedure: Payload Balance
1. **Weight Limit**: Maximum AGV deck capacity is 1,200 kg (2,645 lbs).
2. **Center of Gravity (CoG)**: CoG must remain within central 400 mm radius of vehicle chassis.
3. **Turn Deceleration**: Payload > 800 kg auto-applies 25% curve speed reduction.

## Executable Helper Script
Executable implementation available at `scripts/tool.py`.
