---
name: quarantined-stock-triage
parent_domain: wms-inventory-resolver
parent_discipline: inventory-discrepancy-resolution
display_name: "Quarantined Stock & Blocked SKU Handling"
hierarchy_level: 3
level_name: "OPERATIONAL_MICRO_SKILL"
description: "Inspects damaged packaging, hazardous material holds, and QA release certifications for quarantined inventory."
tags: ["quarantine", "damaged goods", "qa hold", "rtv", "blocked stock"]
---

# Quarantined Stock & Blocked SKU Handling (Level 3 Operational Micro-Skill)

**Hierarchy Path**: `wms-inventory-resolver` ➔ `inventory-discrepancy-resolution` ➔ `quarantined-stock-triage`

## Description
Inspects damaged packaging, hazardous material holds, and QA release certifications for quarantined inventory.

### Standard Operating Procedure: Quarantined Stock Triage
1. **Quarantine Zone Placement**: Items with illegible barcodes, broken seals, or hydraulic fluid contamination are flagged `STATUS_QUARANTINED` and routed to Zone Q-01.
2. **Inspection & Resolution**:
   - Relabeling: Print replacement 2D Datamatrix barcode if physical contents intact.
   - Return-to-Vendor (RTV): Generate vendor credit memo if manufacturing defect found.
   - Write-Off: Scrapped via Environmental Waste Disposal if contaminated.

## Executable Helper Script
Executable implementation available at `scripts/tool.py`.
