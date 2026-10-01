import os
import json

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
KNOWLEDGE_DIR = os.path.join(BASE_DIR, "knowledge", "okf")
os.makedirs(KNOWLEDGE_DIR, exist_ok=True)

docs = {
    "hr_leave_policy.md": """---
doc_id: "DOC-HR-LEAVE-001"
title: "Employee Leave & Time Off Policy"
domain: "HR"
category: "POLICY"
version: "2.4"
tier: "LEVEL_2"
last_updated: "2026-06-15"
author: "Corporate Human Resources & Warehouse Operations"
tags: ["pto", "sick leave", "bereavement", "parental leave", "accrual", "fmla", "vacation"]
available_sections:
  - "Overview & Scope"
  - "Paid Time Off (PTO) Accrual Schedules"
  - "Sick Leave & Medical Certification Rules"
  - "Parental, Family & Medical Leave (FMLA)"
  - "Bereavement & Compassionate Leave"
  - "Approval Workflows & Emergency Absence Protocol"
---

# Employee Leave & Time Off Policy

## 1. Overview & Scope
This policy governs all full-time, part-time, and contracted warehouse operations personnel, logistics technicians, and maintenance engineers across all StackBox logistics centers. Compliance with scheduled attendance is vital to maintaining uninterrupted continuous sorting operations.

## 2. Paid Time Off (PTO) Accrual Schedules
All regular full-time operations engineers and warehouse associates accrue PTO on a bi-weekly basis starting from their first day of active employment:
* **Years 0 to 2 of Service:** 4.62 hours accrued per 80-hour pay period (equivalent to 15 days / 120 hours annually).
* **Years 3 to 5 of Service:** 6.15 hours accrued per 80-hour pay period (equivalent to 20 days / 160 hours annually).
* **Years 6+ of Service:** 7.69 hours accrued per 80-hour pay period (equivalent to 25 days / 200 hours annually).
* **Maximum Carryover:** Associates may carry over a maximum of 40 hours of unused PTO across calendar year boundaries into the next calendar year. Any excess hours beyond 40 are automatically cashed out at 100% of the employee's base hourly rate on December 31st.

## 3. Sick Leave & Medical Certification Rules
* **Allotted Sick Days:** Full-time staff receive 8 dedicated Paid Sick Days (64 hours) at the start of each calendar year, independent of standard PTO.
* **Documentation Threshold:** 
  - For absences lasting **up to two (2) consecutive scheduled shifts**, self-certification via the Employee Mobile Portal is sufficient.
  - For absences of **three (3) or more consecutive work days**, a formal medical certificate signed by a licensed medical practitioner must be uploaded to the HR portal within 48 hours of returning to duty.
* **Return-to-Work Clearance:** If the medical leave is due to a musculoskeletal strain or workplace physical injury, the employee must undergo an on-site evaluation by the occupational health nurse in Building 3 before resuming heavy lifting (>25 lbs) or operating machinery.

## 4. Parental, Family & Medical Leave (FMLA)
* **Primary Caregiver Leave:** Up to 16 weeks of 100% fully paid parental leave for birth, adoption, or foster placement.
* **Secondary Caregiver Leave:** Up to 6 weeks of 100% fully paid parental leave.
* **FMLA Eligibility:** Employees with at least 12 months of service and 1,250 hours worked are entitled to up to 12 weeks of unpaid, job-protected leave for serious medical conditions affecting the employee or immediate family members.

## 5. Bereavement & Compassionate Leave
* **Immediate Family (Spouse, Child, Parent, Sibling):** Up to 5 consecutive paid working days.
* **Extended Family (Grandparent, In-laws, Grandchild):** Up to 3 consecutive paid working days.
* **Additional Travel Days:** Up to 2 additional unpaid travel days may be granted for funerals requiring international or interstate travel exceeding 300 miles.

## 6. Approval Workflows & Emergency Absence Protocol
* **Planned Vacation (>2 Days):** Must be requested via the HR Portal at least 14 days in advance and approved by the Warehouse Shift Supervisor.
* **Emergency or Unplanned Same-Day Absence:**
  1. Call the automated Warehouse Absence Hotline (ext. 4400) at least **two (2) hours prior** to shift start.
  2. Input Employee Badge ID and designated reason code (Code 01: Illness, Code 02: Family Emergency, Code 03: Transit Failure).
  3. The system automatically alerts the active Shift Dispatcher to adjust robot and personnel routing.
""",

    "payroll_compensation_policy.md": """---
doc_id: "DOC-PAY-COMP-002"
title: "Shift Differentials, Overtime & Payroll Policy"
domain: "PAYROLL"
category: "POLICY"
version: "3.1"
tier: "LEVEL_2"
last_updated: "2026-07-01"
author: "Payroll & Compensation Department"
tags: ["payroll", "overtime", "shift differential", "pay cycle", "holiday multiplier", "bonus"]
available_sections:
  - "Payroll Cycles & Direct Deposit"
  - "Shift Differential Rates (Day, Evening, Night)"
  - "Overtime Rules & Calculation Multipliers"
  - "Holiday Work Premiums"
  - "Performance & Hazard Bonuses"
---

# Shift Differentials, Overtime & Payroll Policy

## 1. Payroll Cycles & Direct Deposit
All warehouse employees, technicians, and floor supervisors are paid on a **bi-weekly schedule** (every alternate Friday). 
* Direct deposit takes effect immediately and can be split between up to three (3) designated bank accounts.
* Paystubs and tax withholdings are accessible 24/7 through the StackBox Employee Self-Service (ESS) platform.

## 2. Shift Differential Rates (Day, Evening, Night)
To compensate staff working off-peak and continuous 24/7 sorting operations, StackBox pays premium shift differentials over base hourly rates:
* **Shift 1 (Day Shift: 06:00 - 14:30):** Base rate (no differential).
* **Shift 2 (Evening / Twilight Shift: 14:30 - 23:00):** **+15% differential** applied to all active hours worked during the shift.
* **Shift 3 (Graveyard / Night Shift: 23:00 - 06:30):** **+22% differential** applied to all active hours worked.
* **Weekend Premium:** Any hours worked between Friday 23:00 and Monday 06:00 receive an additional **+$3.50/hour flat premium**, stackable on top of shift differentials.

## 3. Overtime Rules & Calculation Multipliers
* **Standard Overtime (1.5x):** Paid for all hours worked in excess of forty (40) non-overtime hours within a defined workweek (Sunday 00:00 to Saturday 23:59).
* **Double Time (2.0x):** Paid for:
  - All hours worked on the seventh consecutive day of a workweek.
  - Any hours worked in excess of twelve (12) consecutive hours in a single twenty-four (24) hour operational window.
* **Pre-Approval Mandate:** Overtime shifts must be pre-authorized by the Warehouse Dispatcher or Floor Superintendent.

## 4. Holiday Work Premiums
Associates required to staff operations during recognized corporate holidays (e.g., New Year's Day, Memorial Day, Labor Day, Thanksgiving, Christmas) receive:
* **Holiday Base Pay:** 8 hours of holiday pay at base rate.
* **Holiday Worked Multiplier:** **2.0x base rate + applicable shift differential** for all actual hours worked on the floor during the holiday.

## 5. Performance & Hazard Bonuses
* **Monthly Sort-Accuracy Bonus:** Up to $450/month per team for zero mis-picks and zero conveyor jams resulting in downtime exceeding 15 minutes.
* **Emergency Dispatch Callout Allowance:** A flat $120 call-out allowance plus guaranteed 3 hours minimum overtime pay for maintenance technicians called in for emergency mechanical belt restorations outside standard scheduled shifts.
""",

    "healthcare_facilities_policy.md": """---
doc_id: "DOC-MED-HEALTH-003"
title: "Healthcare Facilities & Occupational Wellness Guide"
domain: "HEALTHCARE"
category: "BENEFITS"
version: "1.9"
tier: "LEVEL_2"
last_updated: "2026-05-20"
author: "Occupational Safety & Employee Health Services"
tags: ["healthcare", "first aid", "clinic", "health insurance", "ergonomics", "mental health", "eap", "injury"]
available_sections:
  - "On-Site Warehouse Healthcare Facilities"
  - "Emergency Medical Response Protocol"
  - "Medical Insurance Tiers & Coverage"
  - "Occupational Health & Ergonomic Support"
  - "Mental Health & Employee Assistance Program (EAP)"
---

# Healthcare Facilities & Occupational Wellness Guide

## 1. On-Site Warehouse Healthcare Facilities
StackBox maintains certified occupational healthcare stations on-site to provide immediate care, triage, and health maintenance:
* **Building 3 Central Health Clinic (Room HC-104):**
  - Staffed 24/7 by a certified Occupational Health Nurse (OHN) and Paramedic.
  - Services: Immediate laceration treatment, acute musculoskeletal triage, vital signs monitoring, ergonomic ice/heat therapy, prescription wellness supplies.
* **Aisle 1 Satellite First Aid Pod (Pod SF-01):**
  - Equipped with an Automated External Defibrillator (AED), emergency eye-wash station, burn treatment kits, and spine-board splints.
  - Direct rapid-call button linking directly to the central dispatch console.
* **Quiet Rest & Lactation Suites (Building 1, Room 112 & Building 3, Room 108):**
  - Sound-dampened spaces equipped with refrigerators, private hygiene sinks, and ergonomic resting recliners.

## 2. Emergency Medical Response Protocol
In the event of an acute injury, conveyor pinch accident, or medical event on the warehouse floor:
1. **Immediate Halt:** Hit the nearest Emergency E-Stop button on the conveyor line.
2. **Code Red Alert:** Dial extension 911 on internal warehouse landlines or push the red SOS button on your operator scanner terminal.
3. **Dispatch Response:** Central clinic personnel respond to the designated aisle within **90 seconds**.
4. **Off-Site Ambulance Triage:** St. Jude Memorial Hospital (located 2.4 miles away, Level 1 Trauma) is the contracted facility for off-site ambulance transfers.

## 3. Medical Insurance Tiers & Coverage
Full-time employees are eligible for company-subsidized healthcare coverage effective on the first day of the calendar month following 30 days of employment:
* **Tier 1 (Core PPO):** $500 individual deductible / $1,000 family. 90% in-network coinsurance. Low co-pays ($20 primary care, $35 specialist).
* **Tier 2 (High Deductible Health Plan with HSA):** $1,500 deductible with $1,000 annual employer HSA contribution match.
* **Preventive Care:** 100% covered at zero out-of-pocket cost across all tiers (annual physicals, vaccinations, ergonomic wellness consultations).
* **Dental & Vision:** Comprehensive preventative dental (2 cleanings/year covered 100%) and annual vision exam allowance ($200 frame/contacts credit).

## 4. Occupational Health & Ergonomic Support
* **Ergonomic Assessment:** Any engineer or floor picker experiencing persistent back, neck, or wrist fatigue may request a workstation ergonomic audit by the safety team within 5 business days.
* **Support Gear:** Anti-fatigue matting, lumbar support braces, and impact-absorbing safety footwear allowances ($150 annually) are provided at company expense.

## 5. Mental Health & Employee Assistance Program (EAP)
* **24/7 EAP Hotline:** Free, 100% confidential counseling support available via phone at 1-800-555-EAP-HELP.
* **In-Person Counseling:** Up to six (6) free in-person or telehealth counseling sessions per year per issue for employees and immediate household family members.
""",

    "workplace_code_of_conduct.md": """---
doc_id: "DOC-GOV-CONDUCT-004"
title: "Warehouse Workplace Standards & Ethics Code"
domain: "GOVERNANCE"
category: "POLICY"
version: "4.0"
tier: "LEVEL_2"
last_updated: "2026-04-10"
author: "Legal Compliance & Corporate Security"
tags: ["code of conduct", "ethics", "safety rules", "harassment", "whistleblower", "substance abuse"]
available_sections:
  - "Core Workplace Principles"
  - "Zero-Tolerance Safety Infractions"
  - "Substance Abuse & Fit-for-Duty Mandate"
  - "Anti-Harassment & Equal Opportunity"
  - "Whistleblower Protection & Reporting Channels"
---

# Warehouse Workplace Standards & Ethics Code

## 1. Core Workplace Principles
All employees, contractors, and visitors must uphold the highest standards of integrity, mutual respect, and physical safety. In an automated robotics warehouse, strict adherence to operating parameters is critical to personal safety and collective operational excellence.

## 2. Zero-Tolerance Safety Infractions
The following actions constitute severe infractions and lead to **immediate suspension and potential termination of employment**:
* Intentionally bypassing or defeating safety interlocks, optical light curtains, or conveyor emergency stops.
* Operating an AGV, forklift, or automated pallet jack without active certified authorization.
* Entering an active robot transit cell or conveyor enclosure without performing Lockout-Tagout (LOTO) zero-energy verification.
* Tampering with security CCTV cameras or sensor telemetry units.

## 3. Substance Abuse & Fit-for-Duty Mandate
* StackBox is a drug-free and alcohol-free operating environment.
* Employees must report to work physically and mentally fit to perform their safety-sensitive duties.
* Random screening is conducted in accordance with federal DOT and OSHA industrial regulations. Post-incident drug and alcohol testing is mandatory following any recordable safety incident or equipment collision.

## 4. Anti-Harassment & Equal Opportunity
* Discrimination or harassment based on race, gender, religion, national origin, sexual orientation, disability, or age is strictly prohibited.
* Respectful communication is required at all times across radios, internal chats, and in-person shift hand-offs.

## 5. Whistleblower Protection & Reporting Channels
Employees who observe ethical violations, safety circumventions, or harassment may report confidentially without fear of retaliation:
* **Anonymous Ethics Hotline:** 1-800-ETHICS-LINE (Available 24/7).
* **Secure Web Intake:** `https://compliance.stackbox.internal/report`
* **Zero Retaliation Policy:** StackBox strictly prohibits retaliation against any individual who reports a safety hazard or policy violation in good faith.
""",

    "inventory_management_protocol.md": """---
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
""",

    "warehouse_safety_ppe_loto.md": """---
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
"""
}

# 1. Write documents
for fname, content in docs.items():
    fpath = os.path.join(KNOWLEDGE_DIR, fname)
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created OKF document: {fpath}")

# 2. Build catalog index
catalog = {
    "catalog_name": "StackBox Enterprise Open Knowledge Catalog (OKF)",
    "specification_version": "OKF-0.1",
    "updated_at": "2026-09-18T16:55:00Z",
    "total_documents": len(docs),
    "documents": [
        {
            "doc_id": "DOC-HR-LEAVE-001",
            "title": "Employee Leave & Time Off Policy",
            "domain": "HR",
            "category": "POLICY",
            "version": "2.4",
            "file_name": "hr_leave_policy.md",
            "gcs_uri": "gs://ce-testing-465204-conveyor-orchestrator-knowledge/okf/hr_leave_policy.md",
            "summary": "Governs PTO accrual rates (15-25 days/year), sick leave guidelines, 3-day medical certificate rules, 16-week paid parental leave, and bereavement leave.",
            "tags": ["pto", "sick leave", "bereavement", "parental leave", "accrual", "fmla", "vacation"],
            "available_sections": [
                "Overview & Scope",
                "Paid Time Off (PTO) Accrual Schedules",
                "Sick Leave & Medical Certification Rules",
                "Parental, Family & Medical Leave (FMLA)",
                "Bereavement & Compassionate Leave",
                "Approval Workflows & Emergency Absence Protocol"
            ]
        },
        {
            "doc_id": "DOC-PAY-COMP-002",
            "title": "Shift Differentials, Overtime & Payroll Policy",
            "domain": "PAYROLL",
            "category": "POLICY",
            "version": "3.1",
            "file_name": "payroll_compensation_policy.md",
            "gcs_uri": "gs://ce-testing-465204-conveyor-orchestrator-knowledge/okf/payroll_compensation_policy.md",
            "summary": "Defines bi-weekly pay cycles, off-peak shift differentials (+15% for evening, +22% for night/graveyard), overtime calculation (1.5x / 2.0x), and holiday work multipliers.",
            "tags": ["payroll", "overtime", "shift differential", "pay cycle", "holiday multiplier", "bonus"],
            "available_sections": [
                "Payroll Cycles & Direct Deposit",
                "Shift Differential Rates (Day, Evening, Night)",
                "Overtime Rules & Calculation Multipliers",
                "Holiday Work Premiums",
                "Performance & Hazard Bonuses"
            ]
        },
        {
            "doc_id": "DOC-MED-HEALTH-003",
            "title": "Healthcare Facilities & Occupational Wellness Guide",
            "domain": "HEALTHCARE",
            "category": "BENEFITS",
            "version": "1.9",
            "file_name": "healthcare_facilities_policy.md",
            "gcs_uri": "gs://ce-testing-465204-conveyor-orchestrator-knowledge/okf/healthcare_facilities_policy.md",
            "summary": "Details 24/7 on-site health clinics in Building 3 and satellite first aid in Aisle 1, acute emergency medical protocols, healthcare insurance tiers, ergonomics, and 24/7 mental health EAP.",
            "tags": ["healthcare", "first aid", "clinic", "health insurance", "ergonomics", "mental health", "eap", "injury"],
            "available_sections": [
                "On-Site Warehouse Healthcare Facilities",
                "Emergency Medical Response Protocol",
                "Medical Insurance Tiers & Coverage",
                "Occupational Health & Ergonomic Support",
                "Mental Health & Employee Assistance Program (EAP)"
            ]
        },
        {
            "doc_id": "DOC-GOV-CONDUCT-004",
            "title": "Warehouse Workplace Standards & Ethics Code",
            "domain": "GOVERNANCE",
            "category": "POLICY",
            "version": "4.0",
            "file_name": "workplace_code_of_conduct.md",
            "gcs_uri": "gs://ce-testing-465204-conveyor-orchestrator-knowledge/okf/workplace_code_of_conduct.md",
            "summary": "Sets standards of integrity, mutual respect, zero-tolerance for bypassing safety interlocks, drug-free fit-for-duty mandates, and confidential whistleblower protections.",
            "tags": ["code of conduct", "ethics", "safety rules", "harassment", "whistleblower", "substance abuse"],
            "available_sections": [
                "Core Workplace Principles",
                "Zero-Tolerance Safety Infractions",
                "Substance Abuse & Fit-for-Duty Mandate",
                "Anti-Harassment & Equal Opportunity",
                "Whistleblower Protection & Reporting Channels"
            ]
        },
        {
            "doc_id": "DOC-OPS-INV-005",
            "title": "Warehouse Inventory Management & Stock Reconciliation Protocol",
            "domain": "INVENTORY",
            "category": "SOP",
            "version": "5.2",
            "file_name": "inventory_management_protocol.md",
            "gcs_uri": "gs://ce-testing-465204-conveyor-orchestrator-knowledge/okf/inventory_management_protocol.md",
            "summary": "Covers cycle count schedules for velocity SKUs, count discrepancy tolerances (±0.5%), quarantine protocols for blocked items (SKU-991 in Aisle 4), hazmat Zone H storage, and WMS state codes.",
            "tags": ["inventory", "cycle count", "quarantine", "wms", "blocked sku", "hazmat", "reconciliation"],
            "available_sections": [
                "Cycle Count Schedules & Inventory Audits",
                "Discrepancy Tolerances & Escalation Thresholds",
                "Quarantined Stock & Blocked SKU Handling",
                "Hazardous Materials (Hazmat) Storage & Tracking",
                "WMS Status Codes & Real-Time Sync Protocols"
            ]
        },
        {
            "doc_id": "DOC-SAF-PPE-006",
            "title": "Lockout-Tagout (LOTO) & PPE Floor Safety Mandate",
            "domain": "SAFETY",
            "category": "SOP",
            "version": "6.0",
            "file_name": "warehouse_safety_ppe_loto.md",
            "gcs_uri": "gs://ce-testing-465204-conveyor-orchestrator-knowledge/okf/warehouse_safety_ppe_loto.md",
            "summary": "Mandates ANSI Class 2 vests and ASTM boots, 10m buffer zone for active AGVs, 6-step Lockout-Tagout (LOTO) energy isolation, and Conveyor CV-11 specific maintenance safety procedures.",
            "tags": ["safety", "ppe", "loto", "lockout tagout", "vest", "hard hat", "conveyor maintenance"],
            "available_sections": [
                "Personal Protective Equipment (PPE) Matrix",
                "Active AGV & Autonomous Transit Zone Rules",
                "Lockout-Tagout (LOTO) 6-Step Protocol",
                "Conveyor CV-11 Specific Maintenance Safety",
                "Audit Penalties & Compliance Verification"
            ]
        }
    ]
}

index_path = os.path.join(BASE_DIR, "knowledge", "okf_catalog_index.json")
with open(index_path, "w", encoding="utf-8") as f:
    json.dump(catalog, f, indent=2)

print(f"Successfully generated OKF Catalog Index at: {index_path}")
