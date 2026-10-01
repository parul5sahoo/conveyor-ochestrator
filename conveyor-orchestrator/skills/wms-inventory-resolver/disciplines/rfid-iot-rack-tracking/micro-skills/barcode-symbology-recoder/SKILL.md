---
name: barcode-symbology-recoder
parent_domain: wms-inventory-resolver
parent_discipline: rfid-iot-rack-tracking
display_name: "Barcode Symbology Recoding & Cross-Dock Routing"
hierarchy_level: 3
level_name: "OPERATIONAL_MICRO_SKILL"
description: "Regenerates high-density GS1-128 and 2D Datamatrix labels for degraded or unreadable packaging."
tags: ["barcode", "gs1-128", "datamatrix", "cross-dock", "label reprint"]
---

# Barcode Symbology Recoding & Cross-Dock Routing (Level 3 Operational Micro-Skill)

**Hierarchy Path**: `wms-inventory-resolver` ➔ `rfid-iot-rack-tracking` ➔ `barcode-symbology-recoder`

## Description
Regenerates high-density GS1-128 and 2D Datamatrix labels for degraded or unreadable packaging.

### Standard Operating Procedure: Barcode Symbology Recoding
1. **OCR Verification**: Use optical camera feed to read human-readable SKU numbers when barcode scan fails.
2. **Format Verification**: Re-encode into GS1-128 with Application Identifiers (AI 01 = GTIN, AI 10 = Batch, AI 21 = Serial).
3. **Automated Print & Apply**: Direct pneumatic applicator at Station 3 to print and stamp replacement label.

## Executable Helper Script
Executable implementation available at `scripts/tool.py`.
