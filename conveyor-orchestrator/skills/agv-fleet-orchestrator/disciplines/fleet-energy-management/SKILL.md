---
name: fleet-energy-management
parent_skill: agv-fleet-orchestrator
display_name: "Fleet Energy & Payload Optimization"
hierarchy_level: 2
level_name: "SPECIALIST_DISCIPLINE"
description: "Dispatches opportunity charging to floor inductive pads and audits pallet center-of-gravity stabilization."
micro_skills: ['opportunity-charging-dispatch', 'load-capacity-weight-balancing']
---

# Fleet Energy & Payload Optimization (Level 2 Specialist Discipline)

**Parent Domain**: `agv-fleet-orchestrator`

Dispatches opportunity charging to floor inductive pads and audits pallet center-of-gravity stabilization.

## Operational Micro-Skills (Level 3)
- **[`opportunity-charging-dispatch`](./micro-skills/opportunity-charging-dispatch/SKILL.md)**: Routes AGVs with < 35% battery to available inductive floor pads during shift change or task idle cycles.
- **[`load-capacity-weight-balancing`](./micro-skills/load-capacity-weight-balancing/SKILL.md)**: Calculates payload mass distribution to prevent AGV tip-over during high-speed turns.
