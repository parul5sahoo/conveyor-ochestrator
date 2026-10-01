---
name: agv-fleet-orchestrator
display_name: "Autonomous AGV Fleet Orchestrator"
category: "ROBOTICS"
hierarchy_level: 1
level_name: "ROOT_DOMAIN"
version: "1.0.0"
description: "3-tier Automated Guided Vehicle coordination suite covering dynamic detour routing around stalled conveyors, LiDAR intersection arbitration, inductive opportunity charging, and payload balancing."
tags: ["agv", "amr", "detour", "routing", "battery", "inductive charging", "lidar", "collision avoidance"]
disciplines: ['agv-routing-navigation', 'fleet-energy-management']
---

# Autonomous AGV Fleet Orchestrator (Level 1 Root Domain Skill)

3-tier Automated Guided Vehicle coordination suite covering dynamic detour routing around stalled conveyors, LiDAR intersection arbitration, inductive opportunity charging, and payload balancing.

## Specialist Disciplines (Level 2)
- **[`agv-routing-navigation`](./disciplines/agv-routing-navigation/SKILL.md)**: Calculates graph detour routes around blocked conveyor lines and negotiates right-of-way at four-way intersections.
- **[`fleet-energy-management`](./disciplines/fleet-energy-management/SKILL.md)**: Dispatches opportunity charging to floor inductive pads and audits pallet center-of-gravity stabilization.
