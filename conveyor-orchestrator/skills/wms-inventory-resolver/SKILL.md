---
name: wms-inventory-resolver
display_name: "WMS Inventory & Velocity Resolution"
category: "INVENTORY"
hierarchy_level: 1
level_name: "ROOT_DOMAIN"
version: "1.0.0"
description: "3-tier inventory discrepancy and velocity management suite covering cycle counts, high-velocity SKU-991, quarantine triage, and RFID triangulation."
tags: ["inventory", "cycle count", "sku-991", "high velocity", "wms", "quarantine", "rfid", "shrinkage"]
disciplines: ['inventory-discrepancy-resolution', 'rfid-iot-rack-tracking']
---

# WMS Inventory & Velocity Resolution (Level 1 Root Domain Skill)

3-tier inventory discrepancy and velocity management suite covering cycle counts, high-velocity SKU-991, quarantine triage, and RFID triangulation.

## Specialist Disciplines (Level 2)
- **[`inventory-discrepancy-resolution`](./disciplines/inventory-discrepancy-resolution/SKILL.md)**: Executes ABC stratification cycle counting, shrinkage investigation, and quarantined tote release.
- **[`rfid-iot-rack-tracking`](./disciplines/rfid-iot-rack-tracking/SKILL.md)**: Leverages UHF RFID sensors and optical barcode cameras to locate misplaced high-value inventory.
