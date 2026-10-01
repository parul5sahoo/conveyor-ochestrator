---
name: aisle-intersection-collision-avoidance
parent_domain: agv-fleet-orchestrator
parent_discipline: agv-routing-navigation
display_name: "Blind-Spot LiDAR & Intersection Right-of-Way"
hierarchy_level: 3
level_name: "OPERATIONAL_MICRO_SKILL"
description: "Arbitrates priority tokens between loaded AGVs, empty AGVs, and human-operated order pickers at blind aisle intersections."
tags: ["lidar", "collision avoidance", "intersection", "right of way", "safety"]
---

# Blind-Spot LiDAR & Intersection Right-of-Way (Level 3 Operational Micro-Skill)

**Hierarchy Path**: `agv-fleet-orchestrator` ➔ `agv-routing-navigation` ➔ `aisle-intersection-collision-avoidance`

## Description
Arbitrates priority tokens between loaded AGVs, empty AGVs, and human-operated order pickers at blind aisle intersections.

### Standard Operating Procedure: Intersection Collision Avoidance
1. **Priority Hierarchy**: Human Pedestrian > Manual Forklift > Heavy Loaded AGV > Empty AGV.
2. **Virtual Token Negotiation**: AGVs approach intersection at decelerated speed (0.5 m/s) and exchange ultra-wideband (UWB) tokens.
3. **Clearance Confirmation**: Proceed only after LiDAR 270-degree scan confirms 2.0-meter clear clearance envelope.

## Executable Helper Script
Executable implementation available at `scripts/tool.py`.
