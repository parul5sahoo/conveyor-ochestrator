---
name: sku-991-velocity-cycle-count
parent_domain: wms-inventory-resolver
parent_discipline: inventory-discrepancy-resolution
display_name: "High-Velocity SKU-991 Perpetual Cycle Count Protocol"
hierarchy_level: 3
level_name: "OPERATIONAL_MICRO_SKILL"
description: "Executes ABC Class-A velocity cycle count procedures specifically for high-velocity items like SKU-991, performing automated WMS ledger reconciliation and variance root cause analysis."
tags: ["sku-991", "cycle count", "high velocity", "class a", "perpetual count", "wms reconciliation"]
---

# High-Velocity SKU-991 Perpetual Cycle Count Protocol (Level 3 Operational Micro-Skill)

**Hierarchy Path**: `wms-inventory-resolver` ➔ `inventory-discrepancy-resolution` ➔ `sku-991-velocity-cycle-count`

## Description
Executes ABC Class-A velocity cycle count procedures specifically for high-velocity items like SKU-991, performing automated WMS ledger reconciliation and variance root cause analysis.

### Standard Operating Procedure: High-Velocity SKU-991 Cycle Count Protocol
1. **Velocity Stratification**:
   - SKU-991 is categorized as **ABC Class-A (High-Velocity / Critical Turnover)**.
   - Frequency: Counted **daily on a perpetual rolling basis** during shift handover (07:30 and 15:30) or immediately when stock variance triggers >= 2 units.
2. **Cycle Count Execution Workflow**:
   - Step 1: Lock the target pick bin (`BIN-04-A-12` for SKU-991) to pause active AGV pick dispatches.
   - Step 2: Use handheld terminal (RF gun) to scan the bin location barcode and perform a blind physical barcode count of SKU-991 units.
   - Step 3: Transmit physical count to WMS Inventory Engine.
3. **Variance Thresholds & Root-Cause Escalation**:
   - If Physical Count == System Ledger: Unlock bin, mark cycle count as `PASSED_VERIFIED`.
   - If Variance is within +/- 1% (< $50 threshold): Auto-adjust WMS inventory ledger and log adjustment code `ADJ-VAR-CYCLE-AUTO`.
   - If Variance > 1% (e.g. >= 2 units for SKU-991): Escalate to Floor Supervisor, trigger automated conveyor chute CCTV replay, and initiate RFID rack triangulation to locate misplaced units.

## Executable Helper Script
Executable implementation available at `scripts/tool.py`.
