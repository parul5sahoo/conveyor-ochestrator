---
name: agv-routing-navigation
parent_skill: agv-fleet-orchestrator
display_name: "AGV Dynamic Navigation & Traffic Control"
hierarchy_level: 2
level_name: "SPECIALIST_DISCIPLINE"
description: "Calculates graph detour routes around blocked conveyor lines and negotiates right-of-way at four-way intersections."
micro_skills: ['dynamic-conveyor-bypass-pathing', 'aisle-intersection-collision-avoidance']
---

# AGV Dynamic Navigation & Traffic Control (Level 2 Specialist Discipline)

**Parent Domain**: `agv-fleet-orchestrator`

Calculates graph detour routes around blocked conveyor lines and negotiates right-of-way at four-way intersections.

## Operational Micro-Skills (Level 3)
- **[`dynamic-conveyor-bypass-pathing`](./micro-skills/dynamic-conveyor-bypass-pathing/SKILL.md)**: Computes A* shortest detour trajectories through secondary staging aisles when a conveyor zone is halted.
- **[`aisle-intersection-collision-avoidance`](./micro-skills/aisle-intersection-collision-avoidance/SKILL.md)**: Arbitrates priority tokens between loaded AGVs, empty AGVs, and human-operated order pickers at blind aisle intersections.
