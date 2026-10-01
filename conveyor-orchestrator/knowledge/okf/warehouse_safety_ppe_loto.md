---
doc_id: "DOC-SAF-PPE-006"
title: "Lockout-Tagout (LOTO) & PPE Floor Safety Mandate"
domain: "SAFETY"
category: "SOP"
version: "6.0"
tier: "LEVEL_2"
last_updated: "2026-07-15"
author: "EHS Division & Safety Engineering"
tags: ["safety", "ppe", "loto", "lockout tagout", "vest", "hard hat", "conveyor maintenance"]
available_sections:
  - "Personal Protective Equipment (PPE) Matrix"
  - "Active AGV & Autonomous Transit Zone Rules"
  - "Lockout-Tagout (LOTO) 6-Step Protocol"
  - "Conveyor CV-11 Specific Maintenance Safety"
  - "Audit Penalties & Compliance Verification"
---

# Lockout-Tagout (LOTO) & PPE Floor Safety Mandate

## 1. Personal Protective Equipment (PPE) Matrix
All personnel entering the warehouse floor must wear required PPE calibrated to their work zone:
* **Zone 1 (General Logistics & Packing):**
  - High-visibility safety vest (ANSI/ISEA 107-2020 Class 2).
  - Steel-toed or composite-toed protective safety boots (ASTM F2413).
  - Safety glasses with side shields (ANSI Z87.1).
* **Zone 2 (Conveyor Lines & Maintenance Bays):**
  - All Zone 1 gear plus:
  - Hard hat (ANSI Z89.1 Type I, Class E).
  - Cut-resistant level A4 mechanical work gloves.
  - Hearing protection (NRR 25dB minimum) when operating in high-decibel sortation bays (>85 dBA).

## 2. Active AGV & Autonomous Transit Zone Rules
* **Pedestrian Distance Buffer:** Technicians must maintain a minimum **10-meter clearance distance** from active Autonomous Guided Vehicles (AGVs).
* **High-Visibility Requirement:** CCTV safety audit cameras cross-verify high-visibility vests. Any personnel detected without a vest near active AGVs will trigger an automated audible alarm and reduce AGV transit speed to crawl mode (<0.5 m/s).
* **Crosswalks:** Pedestrians must only cross designated robotics transit lanes at marked yellow zebra crossings after visually verifying AGV warning beacons.

## 3. Lockout-Tagout (LOTO) 6-Step Protocol
Before any maintenance, belt clearing, sensor replacement, or motor servicing on conveyors:
1. **Preparation:** Notify all affected operators and active floor supervisors.
2. **Shutdown:** Power down equipment using normal stopping procedures.
3. **Isolation:** Disconnect all main electrical switches and pneumatic air pressure lines.
4. **Lock & Tag:** Apply personal red padlock and completed yellow identification tag to the energy isolation switch.
5. **Stored Energy Dissipation:** Bleed hydraulic pressure, discharge electrical capacitors, and mechanically block gravity-fed belt rollers.
6. **Zero-Energy Verification:** Attempt to restart equipment using standard controls to ensure zero mechanical movement or electrical voltage before initiating work.

## 4. Conveyor CV-11 Specific Maintenance Safety
When clearing mechanical jams or resetting Error 4042 on Conveyor CV-11:
* Perform standard LOTO on Main Disconnect C-3.
* Dispatch an AGV (e.g. PickerBot-Beta) to divert upstream carton flow before opening diverter guards.
* Never place hands or tools into belt nip points without physically inserting the mechanical roller stop bar.

## 5. Audit Penalties & Compliance Verification
* Regular safety audits are conducted continuously via AI vision cameras and safety officers.
* Non-compliance with PPE or LOTO results in immediate stop-work order, mandatory re-certification training, and formal disciplinary documentation under SOP-0100.
