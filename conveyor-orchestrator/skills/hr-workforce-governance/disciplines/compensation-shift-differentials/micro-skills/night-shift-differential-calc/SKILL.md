---
name: night-shift-differential-calc
parent_domain: hr-workforce-governance
parent_discipline: compensation-shift-differentials
display_name: "Evening & Night Shift Differential Calculator"
hierarchy_level: 3
level_name: "OPERATIONAL_MICRO_SKILL"
description: "Applies +15% evening shift (16:00-00:00) and +22% graveyard/night shift (00:00-08:00) differential calculations to base hourly wages."
tags: ["shift differential", "night shift", "evening shift", "payroll", "differential rate"]
---

# Evening & Night Shift Differential Calculator (Level 3 Operational Micro-Skill)

**Hierarchy Path**: `hr-workforce-governance` ➔ `compensation-shift-differentials` ➔ `night-shift-differential-calc`

## Description
Applies +15% evening shift (16:00-00:00) and +22% graveyard/night shift (00:00-08:00) differential calculations to base hourly wages.

### Standard Operating Procedure: Shift Differential Rates
1. **Day Shift (08:00 - 16:00)**: Standard Base Hourly Wage (1.0x).
2. **Evening Shift (16:00 - 00:00)**: Base Wage + **15% Shift Differential** (1.15x).
3. **Night / Graveyard Shift (00:00 - 08:00)**: Base Wage + **22% Shift Differential** (1.22x).
4. **Overtime Compounding**: Shift differential applies to the base rate BEFORE overtime multipliers are calculated.

## Executable Helper Script
Executable implementation available at `scripts/tool.py`.
