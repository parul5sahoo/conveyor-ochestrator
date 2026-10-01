---
name: breaker-lockout-tagout-verification
parent_domain: warehouse-ehs-safety
parent_discipline: energy-isolation-loto
display_name: "Electrical Breaker Lockout & Zero-Energy Verification"
hierarchy_level: 3
level_name: "OPERATIONAL_MICRO_SKILL"
description: "Verifies physical breaker lock placement, calibrated multimeter zero-voltage checks, and LOTO permit issuance."
tags: ["loto", "breaker", "zero energy", "multimeter", "voltage", "lockout hasp"]
---

# Electrical Breaker Lockout & Zero-Energy Verification (Level 3 Operational Micro-Skill)

**Hierarchy Path**: `warehouse-ehs-safety` ➔ `energy-isolation-loto` ➔ `breaker-lockout-tagout-verification`

## Description
Verifies physical breaker lock placement, calibrated multimeter zero-voltage checks, and LOTO permit issuance.

### Standard Operating Procedure: Breaker LOTO Zero-Energy Verification
1. **Notify Affected Personnel**: Broadcast audible chime and notify supervisory dispatch that Line CV-101 is entering LOTO isolation.
2. **Switch De-energization**: Open primary 480V 3-phase molded-case circuit breaker.
3. **Lockout Hasp Application**: Affix OSHA-compliant red padlock and danger tag containing technician employee ID and contact.
4. **Zero-Energy Multimeter Test**:
   - Verify calibrated CAT III multimeter on live voltage source (known good test).
   - Test Phase-to-Phase and Phase-to-Ground on isolated side. Must read strictly 0.00V.
   - Re-verify multimeter on known live source (live-dead-live testing protocol).

## Executable Helper Script
Executable implementation available at `scripts/tool.py`.
