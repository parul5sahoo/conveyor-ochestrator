---
name: evacuation-headcount-audit
parent_domain: warehouse-ehs-safety
parent_discipline: hazmat-emergency-response
display_name: "Muster Point Headcount & Missing Personnel Audit"
hierarchy_level: 3
level_name: "OPERATIONAL_MICRO_SKILL"
description: "Reconciles live badge RFID swipes at external assembly muster zones against active shift roster."
tags: ["evacuation", "muster point", "headcount", "fire drill", "missing person"]
---

# Muster Point Headcount & Missing Personnel Audit (Level 3 Operational Micro-Skill)

**Hierarchy Path**: `warehouse-ehs-safety` ➔ `hazmat-emergency-response` ➔ `evacuation-headcount-audit`

## Description
Reconciles live badge RFID swipes at external assembly muster zones against active shift roster.

### Standard Operating Procedure: Muster Point Headcount Audit
1. **Active Roster Ingestion**: Query warehouse turnstile database for active employees on site.
2. **Muster Portal Verification**: Cross-reference employees who badged into Muster Points Alpha, Beta, and Gamma within 300 seconds of alarm.
3. **Search & Rescue Dispatch**: Auto-generate list of unaccounted personnel and last-seen zone sensors for Fire Department command.

## Executable Helper Script
Executable implementation available at `scripts/tool.py`.
