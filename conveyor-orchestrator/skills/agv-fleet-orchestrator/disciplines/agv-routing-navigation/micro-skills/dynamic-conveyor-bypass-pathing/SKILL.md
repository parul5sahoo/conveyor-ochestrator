---
name: dynamic-conveyor-bypass-pathing
parent_domain: agv-fleet-orchestrator
parent_discipline: agv-routing-navigation
display_name: "Conveyor Outage Dynamic Graph Bypass Routing"
hierarchy_level: 3
level_name: "OPERATIONAL_MICRO_SKILL"
description: "Computes A* shortest detour trajectories through secondary staging aisles when a conveyor zone is halted."
tags: ["agv bypass", "detour", "a*", "stalled conveyor", "pathing", "graph"]
---

# Conveyor Outage Dynamic Graph Bypass Routing (Level 3 Operational Micro-Skill)

**Hierarchy Path**: `agv-fleet-orchestrator` ➔ `agv-routing-navigation` ➔ `dynamic-conveyor-bypass-pathing`

## Description
Computes A* shortest detour trajectories through secondary staging aisles when a conveyor zone is halted.

### Standard Operating Procedure: Conveyor Bypass Detour Routing
1. **Node Invalidation**: Mark conveyor transfer node `CV-TRANSFER-03` as blocked in the central AGV fleet graph.
2. **Detour Path Generation**: Calculate secondary corridor route via Aisle B-08 with speed restricted to 1.2 m/s.
3. **Fleet Reroute Broadcast**: Transmit updated trajectory coordinates to all dispatched AGVs carrying active totes.

## Executable Helper Script
Executable implementation available at `scripts/tool.py`.
