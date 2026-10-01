---
name: tension-ultrasonic-calibration
parent_domain: conveyor-diagnostics
parent_discipline: belt-mechanical-integrity
display_name: "Ultrasonic Belt Tension & Load Cell Calibration"
hierarchy_level: 3
level_name: "OPERATIONAL_MICRO_SKILL"
description: "Measures belt resonant vibration frequency to calibrate take-up carriage tension without stopping line."
tags: ["belt tension", "ultrasonic", "load cell", "resonant frequency", "slack"]
---

# Ultrasonic Belt Tension & Load Cell Calibration (Level 3 Operational Micro-Skill)

**Hierarchy Path**: `conveyor-diagnostics` ➔ `belt-mechanical-integrity` ➔ `tension-ultrasonic-calibration`

## Description
Measures belt resonant vibration frequency to calibrate take-up carriage tension without stopping line.

### Standard Operating Procedure: Ultrasonic Belt Tension Calibration
1. **Frequency Sensing**: Deploy optical/acoustic laser vibrometer over span between pulleys.
2. **Target Frequency**: Target resonant span frequency is 42.0 Hz +/- 2.5 Hz (corresponding to 180 N/mm belt tension).
3. **Take-up Actuation**: Adjust hydraulic tensioner cylinder if frequency drops below 36.0 Hz.

## Executable Helper Script
Executable implementation available at `scripts/tool.py`.
