---
name: shift-swap-overtime-approval
parent_domain: hr-workforce-governance
parent_discipline: employee-leave-attendance
display_name: "Shift Swap & Overtime Rest Period Approval"
hierarchy_level: 3
level_name: "OPERATIONAL_MICRO_SKILL"
description: "Verifies 8-hour mandatory rest intervals between consecutive shifts and collective bargaining overtime fairness."
tags: ["shift swap", "overtime", "rest period", "fatigue", "scheduling"]
---

# Shift Swap & Overtime Rest Period Approval (Level 3 Operational Micro-Skill)

**Hierarchy Path**: `hr-workforce-governance` ➔ `employee-leave-attendance` ➔ `shift-swap-overtime-approval`

## Description
Verifies 8-hour mandatory rest intervals between consecutive shifts and collective bargaining overtime fairness.

### Standard Operating Procedure: Shift Swap & Overtime Rest Interval
1. **Mandatory Rest Period**:
   - Operators must have a minimum of 8 consecutive hours of rest between consecutive shifts.
   - Clopening (closing evening shift followed by opening morning shift with <8 hours interval) is strictly blocked by the scheduling engine.
2. **Overtime Allocation**:
   - Daily overtime (>8 hours) paid at 1.5x base rate.
   - Weekly overtime (>40 hours) paid at 1.5x base rate. Double time (2.0x) applies to hours worked on the 7th consecutive day.

## Executable Helper Script
Executable implementation available at `scripts/tool.py`.
