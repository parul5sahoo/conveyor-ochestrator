---
name: splice-wear-tracking
parent_domain: conveyor-diagnostics
parent_discipline: belt-mechanical-integrity
display_name: "Conveyor Belt Splice Wear & Joint Integrity"
hierarchy_level: 3
level_name: "OPERATIONAL_MICRO_SKILL"
description: "Inspects mechanical vulcanized splice seams via high-speed line scan cameras to prevent catastrophic belt parting."
tags: ["splice", "vulcanized", "joint", "line scan", "belt parting"]
---

# Conveyor Belt Splice Wear & Joint Integrity (Level 3 Operational Micro-Skill)

**Hierarchy Path**: `conveyor-diagnostics` ➔ `belt-mechanical-integrity` ➔ `splice-wear-tracking`

## Description
Inspects mechanical vulcanized splice seams via high-speed line scan cameras to prevent catastrophic belt parting.

### Standard Operating Procedure: Splice Wear Tracking
1. **Camera Inspection**: High-speed line scan camera inspects splice markers every complete belt revolution.
2. **Separation Limits**: Splice gap widening > 3.0 mm triggers an urgent maintenance order for cold vulcanization re-bonding.

## Executable Helper Script
Executable implementation available at `scripts/tool.py`.
