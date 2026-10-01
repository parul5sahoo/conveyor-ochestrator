---
name: rfid-iot-rack-tracking
parent_skill: wms-inventory-resolver
display_name: "RFID & IoT Rack Tracking"
hierarchy_level: 2
level_name: "SPECIALIST_DISCIPLINE"
description: "Leverages UHF RFID sensors and optical barcode cameras to locate misplaced high-value inventory."
micro_skills: ['rfid-triangulation-localization', 'barcode-symbology-recoder']
---

# RFID & IoT Rack Tracking (Level 2 Specialist Discipline)

**Parent Domain**: `wms-inventory-resolver`

Leverages UHF RFID sensors and optical barcode cameras to locate misplaced high-value inventory.

## Operational Micro-Skills (Level 3)
- **[`rfid-triangulation-localization`](./micro-skills/rfid-triangulation-localization/SKILL.md)**: Calculates spatial coordinates of misplaced totes using Received Signal Strength Indicator (RSSI) from fixed antenna arrays.
- **[`barcode-symbology-recoder`](./micro-skills/barcode-symbology-recoder/SKILL.md)**: Regenerates high-density GS1-128 and 2D Datamatrix labels for degraded or unreadable packaging.
