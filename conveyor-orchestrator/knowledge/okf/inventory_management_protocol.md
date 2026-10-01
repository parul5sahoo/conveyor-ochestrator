---
doc_id: "DOC-OPS-INV-005"
title: "Warehouse Inventory Management & Stock Reconciliation Protocol"
domain: "INVENTORY"
category: "SOP"
version: "5.2"
tier: "LEVEL_2"
last_updated: "2026-08-01"
author: "Logistics Engineering & Inventory Control"
tags: ["inventory", "cycle count", "quarantine", "wms", "blocked sku", "hazmat", "reconciliation"]
available_sections:
  - "Cycle Count Schedules & Inventory Audits"
  - "Discrepancy Tolerances & Escalation Thresholds"
  - "Quarantined Stock & Blocked SKU Handling"
  - "Hazardous Materials (Hazmat) Storage & Tracking"
  - "WMS Status Codes & Real-Time Sync Protocols"
---

# Warehouse Inventory Management & Stock Reconciliation Protocol

## 1. Cycle Count Schedules & Inventory Audits
To maintain >99.8% physical inventory accuracy across the facility:
* **High-Velocity Velocity-A SKUs (e.g. SKU-991):** Counted on a weekly rotating schedule.
* **Standard Velocity-B SKUs (e.g. SKU-502):** Counted monthly.
* **Low-Velocity Velocity-C SKUs:** Counted quarterly.
* **Automated Cycle Counts:** AGVs equipped with RFID and optical LiDAR scanners run autonomous nightly cycle counts between 01:00 and 04:00 in non-active aisles.

## 2. Discrepancy Tolerances & Escalation Thresholds
* **Acceptable Variance:** Count variances within **±0.5%** or less than $50 in value are auto-reconciled with automated WMS audit log entries.
* **Level 1 Escalation:** Any variance between 0.5% and 2.0% requires a blind recount by a secondary inventory specialist within 4 hours.
* **Level 2 Escalation (Variance >2.0% or >$1,000 value):** Requires formal investigation by the Inventory Control Manager and temporary freeze of the affected bin location.

## 3. Quarantined Stock & Blocked SKU Handling
When an item is flagged with status `BLOCKED` in the WMS (such as defective packaging, barcode scanning failure, or mechanical conveyor incident):
1. **Immediate System Hold:** The WMS automatically marks the SKU as unpickable and inhibits automated fulfillment allocation.
2. **Physical Isolation:** The Floor Dispatcher commands a picker bot (e.g., PickerBot-Beta) to transfer the blocked pallet or bin to the **Quarantine Staging Area (Aisle 9, Bay Q-1 through Q-8)**.
3. **Safety Inspection:** The QA inspector reviews the blocked inventory within 24 hours:
   - If cleared: Status updated to `AVAILABLE` and returned to active storage bins.
   - If damaged or expired: Flagged for Return to Vendor (RTV) or authorized scrap.
4. **Bypass Routing:** While an item is blocked in Aisle 4, active sorting conveyors must be rerouted to alternate bypass lines (e.g. CV-12) via AGV transfer.

## 4. Hazardous Materials (Hazmat) Storage & Tracking
* All lithium-ion battery packs, combustible aerosols, and chemical cleaning solvents must be segregated into **Zone H (Flame-Retardant Bunker, Building 2)**.
* Maximum allowable storage height for Hazmat pallets is two (2) tiers.
* Real-time thermal sensors must monitor Zone H ambient temperatures; automated alarms trigger if temperature exceeds 28°C (82.4°F).

## 5. WMS Status Codes & Real-Time Sync Protocols
* `AVAILABLE`: Ready for picker allocation and automated sortation.
* `ALLOCATED`: Reserved for active packing order.
* `BLOCKED`: Held under QA inspection or mechanical line obstruction.
* `IN_TRANSIT`: Assigned to an AGV or conveyor transit node.
* `QUARANTINED`: Moved to physical containment bay Q.
