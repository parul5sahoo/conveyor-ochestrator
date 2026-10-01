# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from google.adk.tools import FunctionTool


def check_wms_stock(sku: str) -> dict:
    """Verify stock status and block condition for a specific SKU in the Warehouse Management System (WMS).

    Args:
        sku: The unique Stock Keeping Unit identifier to check in the WMS.

    Returns:
        A dictionary containing the SKU, its current blocking status, quantity, and physical warehouse location.
    """
    sku_cleaned = sku.strip().upper()
    if sku_cleaned == "SKU-991":
        return {
            "sku": sku_cleaned,
            "status": "BLOCKED",
            "quantity": 15,
            "location": "Aisle 4",
        }
    elif sku_cleaned == "SKU-502":
        return {
            "sku": sku_cleaned,
            "status": "AVAILABLE",
            "quantity": 42,
            "location": "Aisle 2",
        }
    return {
        "sku": sku_cleaned,
        "status": "UNKNOWN",
        "quantity": 0,
        "location": "Unknown",
    }


def query_runbooks(error_code: str) -> dict:
    """Query the maintenance Vector Search database for repair instructions matching the error code.

    Args:
        error_code: The machine error or warning code reported by the conveyor telemetry.

    Returns:
        A dictionary containing matched repair instructions, error code, and urgency level.
    """
    err_cleaned = error_code.strip()
    if err_cleaned == "Error 4042":
        return {
            "error_code": err_cleaned,
            "instructions": "Calibrate the main belt speed sensor and reset controller C-3.",
            "urgency": "HIGH",
        }
    elif err_cleaned == "Error 5011":
        return {
            "error_code": err_cleaned,
            "instructions": "Clear debris from diverter flap and manual cycle standard restart.",
            "urgency": "MEDIUM",
        }
    return {
        "error_code": err_cleaned,
        "instructions": "Perform standard conveyor belt safety inspection and reboot system.",
        "urgency": "LOW",
    }


def dispatch_agv(aisle: str, task: str, bot_id: str = "PickerBot-Alpha") -> dict:
    """Command an Autonomous Guided Vehicle (AGV) or picker bot to perform a bypass task in a specific aisle.

    Args:
        aisle: The warehouse aisle where the AGV must perform the bypass.
        task: The specific bypass instruction or route for the AGV.
        bot_id: The unique identifier of the AGV to dispatch (e.g. 'PickerBot-Beta').

    Returns:
        A dictionary confirming the AGV's dispatched status, assigned bot ID, and routing details.
    """
    return {
        "aisle": aisle,
        "task": task,
        "status": "DISPATCHED",
        "bot_id": bot_id,
    }


check_wms_stock_tool = FunctionTool(func=check_wms_stock)
query_runbooks_tool = FunctionTool(func=query_runbooks)
dispatch_agv_tool = FunctionTool(func=dispatch_agv)


import os
import subprocess
import sys

# Configure local sandbox directory path inside the workspace
SANDBOX_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "sandbox"))

def _ensure_telemetry_in_sandbox() -> None:
    """Helper to ensure that fleet_telemetry_dump.json is always present and populated in the sandbox directory."""
    os.makedirs(SANDBOX_DIR, exist_ok=True)
    target_telemetry = os.path.join(SANDBOX_DIR, "fleet_telemetry_dump.json")
    if not os.path.exists(target_telemetry) or os.path.getsize(target_telemetry) == 0:
        source_telemetry = os.path.join(os.path.dirname(__file__), "fleet_telemetry_dump.json")
        if os.path.exists(source_telemetry) and os.path.getsize(source_telemetry) > 0:
            import shutil
            shutil.copy(source_telemetry, target_telemetry)
        else:
            workspace_source = os.path.join(os.path.dirname(__file__), "..", "mock_data", "fleet_telemetry_dump.json")
            if os.path.exists(workspace_source) and os.path.getsize(workspace_source) > 0:
                import shutil
                shutil.copy(workspace_source, target_telemetry)

def write_file_to_sandbox(filename: str, content: str) -> str:
    """Write or create a file containing script code, text, or reports inside the secure agent sandbox.

    Args:
        filename: The name of the file to save (e.g. 'diagnose_stress.py', 'report.md').
        content: The text content or code to write to the file.

    Returns:
        A confirmation message indicating the file was written successfully and its absolute path.
    """
    _ensure_telemetry_in_sandbox()
    target_path = os.path.join(SANDBOX_DIR, os.path.basename(filename))
    
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    return f"File successfully written to secure sandbox path: {filename}"



def read_file_from_sandbox(filename: str) -> str:
    """Read and retrieve the raw contents of a specific file located inside the secure agent sandbox.

    Args:
        filename: The name of the file to read (e.g. 'reports/stress_audit.md').

    Returns:
        A string containing the raw contents of the file, or an error message if the file doesn't exist.
    """
    _ensure_telemetry_in_sandbox()
    target_path = os.path.join(SANDBOX_DIR, os.path.basename(filename))
    
    if not os.path.exists(target_path):
        return f"Error: The requested file '{filename}' was not found in the sandbox."
        
    with open(target_path, "r", encoding="utf-8") as f:
        return f.read()


def execute_python_in_sandbox(script_name: str) -> str:
    """Execute a python script securely in the isolated sandbox terminal environment using the bash tool.

    Use this tool to run analytical, statistical, or data-parsing scripts that you have written to process
    large telemetry dumps (e.g. 'fleet_telemetry_dump.json') and output consolidated reports.

    Args:
        script_name: The name of the python script to run (e.g. 'diagnose_stress.py').

    Returns:
        A string containing the standard output (stdout) and standard error (stderr) of the executed script.
    """
    _ensure_telemetry_in_sandbox()
    target_path = os.path.join(SANDBOX_DIR, os.path.basename(script_name))
    
    if not os.path.exists(target_path):
        return f"Error: Script '{script_name}' not found. Please write the file to the sandbox first."
        
    try:
        # Run python subprocess inside the sandbox directory
        result = subprocess.run(
            [sys.executable, os.path.basename(script_name)],
            cwd=SANDBOX_DIR,
            capture_output=True,
            text=True,
            timeout=30,  # 30 seconds timeout to prevent hanging
        )
        output = []
        if result.stdout:
            output.append(f"[STDOUT]\n{result.stdout}")
        if result.stderr:
            output.append(f"[STDERR]\n{result.stderr}")
            
        if not output:
            return "Script executed successfully with no output."
        return "\n".join(output)
    except subprocess.TimeoutExpired:
        return f"Error: Script execution timed out (limit: 30s)."
    except Exception as e:
        return f"Error executing script: {str(e)}"


write_file_to_sandbox_tool = FunctionTool(func=write_file_to_sandbox)
read_file_from_sandbox_tool = FunctionTool(func=read_file_from_sandbox)
execute_python_in_sandbox_tool = FunctionTool(func=execute_python_in_sandbox)


# ---------------------------------------------------------------------------
# Open Knowledge Format (OKF) & Progressive Disclosure Catalog Tools
# ---------------------------------------------------------------------------
KNOWLEDGE_BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "knowledge"))
OKF_DOCS_DIR = os.path.join(KNOWLEDGE_BASE_DIR, "okf")
OKF_INDEX_PATH = os.path.join(KNOWLEDGE_BASE_DIR, "okf_catalog_index.json")


def discover_okf_catalog(query: str, domain: str = None) -> list[dict]:
    """Level 1 Discovery: Search the Open Knowledge Format (OKF) catalog index to find relevant policy documents and available sections.

    Use this tool FIRST before retrieving full policy documents. It inspects metadata, document IDs, summaries,
    and available section titles, allowing you to identify which document and specific section contains the answer
    without overloading the LLM context window with thousands of lines of text.

    Args:
        query: Keywords or questions regarding HR policies, payroll, employee benefits, healthcare, inventory, or floor safety (e.g., 'night shift differential', 'sick leave doctor note', 'quarantined stock').
        domain: Optional domain filter: 'HR', 'PAYROLL', 'HEALTHCARE', 'GOVERNANCE', 'INVENTORY', or 'SAFETY'.

    Returns:
        A list of matching document catalog entries with doc_id, title, domain, summary, available_sections, and gcs_uri.
    """
    import json
    if not os.path.exists(OKF_INDEX_PATH):
        return [{"error": f"OKF Catalog index not found at {OKF_INDEX_PATH}"}]

    try:
        with open(OKF_INDEX_PATH, "r", encoding="utf-8") as f:
            catalog = json.load(f)
    except Exception as e:
        return [{"error": f"Failed to load OKF Catalog index: {str(e)}"}]

    documents = catalog.get("documents", [])
    query_lower = query.lower().strip()
    query_words = set(query_lower.split())
    domain_upper = domain.upper().strip() if domain else None

    matches = []
    for doc in documents:
        if domain_upper and doc.get("domain", "").upper() != domain_upper:
            continue

        # Score relevance based on title, summary, tags, and available sections
        title = doc.get("title", "").lower()
        summary = doc.get("summary", "").lower()
        tags = [t.lower() for t in doc.get("tags", [])]
        sections = [s.lower() for s in doc.get("available_sections", [])]

        score = 0
        if query_lower in title:
            score += 10
        if query_lower in summary:
            score += 8
        for word in query_words:
            if word in title:
                score += 3
            if word in summary:
                score += 2
            if any(word in tag for tag in tags):
                score += 4
            if any(word in sec for sec in sections):
                score += 4

        if score > 0 or not query_words:
            matches.append((score, {
                "doc_id": doc.get("doc_id"),
                "title": doc.get("title"),
                "domain": doc.get("domain"),
                "category": doc.get("category"),
                "summary": doc.get("summary"),
                "available_sections": doc.get("available_sections", []),
                "gcs_uri": doc.get("gcs_uri"),
                "relevance_score": score
            }))

    matches.sort(key=lambda x: x[0], reverse=True)
    results = [m[1] for m in matches]

    # Return top 3 matches or all if few
    return results[:3] if results else [{"message": f"No direct OKF document match found for query '{query}'. Try searching for broader terms (e.g. 'leave', 'payroll', 'health', 'inventory', 'safety')."}]


def fetch_okf_document_section(doc_id: str, section: str = None) -> dict:
    """Level 2/3 Progressive Disclosure: Retrieve a targeted section or full policy document from the OKF knowledge repository.

    Use this tool AFTER discovering the relevant document using `discover_okf_catalog`. Specifying a specific `section`
    name retrieves only the designated policy clauses, calculations, or procedure steps, implementing progressive disclosure.

    Args:
        doc_id: The unique document identifier discovered in the catalog (e.g., 'DOC-HR-LEAVE-001', 'DOC-PAY-COMP-002', 'DOC-MED-HEALTH-003', 'DOC-OPS-INV-005', 'DOC-SAF-PPE-006').
        section: Optional name of the specific section to retrieve (e.g., 'Shift Differential Rates (Day, Evening, Night)', 'Sick Leave & Medical Certification Rules', 'Quarantined Stock & Blocked SKU Handling'). If omitted or 'ALL', the full document is returned.

    Returns:
        A dictionary containing the document metadata, the targeted section name, and the exact policy content text.
    """
    import json
    import re

    # Locate document metadata from index
    doc_meta = None
    if os.path.exists(OKF_INDEX_PATH):
        try:
            with open(OKF_INDEX_PATH, "r", encoding="utf-8") as f:
                catalog = json.load(f)
            for d in catalog.get("documents", []):
                if d.get("doc_id", "").upper() == doc_id.upper().strip():
                    doc_meta = d
                    break
        except Exception:
            pass

    file_name = doc_meta.get("file_name") if doc_meta else None
    if not file_name:
        # Fallback mapping
        id_map = {
            "DOC-HR-LEAVE-001": "hr_leave_policy.md",
            "DOC-PAY-COMP-002": "payroll_compensation_policy.md",
            "DOC-MED-HEALTH-003": "healthcare_facilities_policy.md",
            "DOC-GOV-CONDUCT-004": "workplace_code_of_conduct.md",
            "DOC-OPS-INV-005": "inventory_management_protocol.md",
            "DOC-SAF-PPE-006": "warehouse_safety_ppe_loto.md",
        }
        file_name = id_map.get(doc_id.upper().strip())

    if not file_name:
        return {
            "error": f"Document ID '{doc_id}' not found in OKF catalog.",
            "suggestion": "Call discover_okf_catalog first to find valid doc_ids."
        }

    file_path = os.path.join(OKF_DOCS_DIR, file_name)
    if not os.path.exists(file_path):
        return {
            "error": f"OKF document file '{file_name}' not found locally at {file_path}.",
            "gcs_uri": doc_meta.get("gcs_uri") if doc_meta else f"gs://ce-testing-465204-conveyor-orchestrator-knowledge/okf/{file_name}"
        }

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            full_text = f.read()
    except Exception as e:
        return {"error": f"Failed reading file '{file_name}': {str(e)}"}

    # Separate YAML frontmatter and body
    frontmatter = {}
    body = full_text
    if full_text.startswith("---"):
        parts = full_text.split("---", 2)
        if len(parts) >= 3:
            body = parts[2].strip()

    # If full document requested or section is None
    if not section or section.strip().upper() == "ALL":
        return {
            "doc_id": doc_id,
            "title": doc_meta.get("title") if doc_meta else file_name,
            "disclosure_tier": "LEVEL_3_FULL_SPECIFICATION",
            "section_requested": "ALL",
            "gcs_uri": doc_meta.get("gcs_uri") if doc_meta else None,
            "content": body
        }

    # Progressive Disclosure: Extract the specific requested section
    section_query = section.lower().strip()
    # Normalize markdown header parsing (e.g. ## 2. Shift Differential Rates or ## Shift Differential Rates)
    # Split by level-2 markdown headers
    header_pattern = re.compile(r'^(##\s+(?:\d+\.\s*)?([^\n]+))', re.MULTILINE)
    sections_found = []
    
    matches = list(header_pattern.finditer(body))
    for i, match in enumerate(matches):
        sec_header = match.group(2).strip()
        start_pos = match.start()
        end_pos = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        sec_content = body[start_pos:end_pos].strip()
        sections_found.append({
            "title": sec_header,
            "content": sec_content
        })

    # Find the best matching section
    matched_section = None
    for sec in sections_found:
        if section_query in sec["title"].lower() or sec["title"].lower() in section_query:
            matched_section = sec
            break

    if not matched_section:
        # Word-based similarity fallback
        for sec in sections_found:
            words = set(section_query.split())
            if any(w in sec["title"].lower() for w in words if len(w) > 3):
                matched_section = sec
                break

    if matched_section:
        return {
            "doc_id": doc_id,
            "title": doc_meta.get("title") if doc_meta else file_name,
            "disclosure_tier": "LEVEL_2_TARGETED_SECTION",
            "section_requested": section,
            "section_matched": matched_section["title"],
            "gcs_uri": doc_meta.get("gcs_uri") if doc_meta else None,
            "content": matched_section["content"]
        }

    # If no specific section matched, return list of available sections for progressive disclosure
    available = [s["title"] for s in sections_found]
    return {
        "warning": f"Section '{section}' not found in '{doc_id}'.",
        "available_sections": available,
        "disclosure_tier": "LEVEL_1_INDEX_FALLBACK",
        "doc_id": doc_id,
        "title": doc_meta.get("title") if doc_meta else file_name
    }


discover_okf_catalog_tool = FunctionTool(func=discover_okf_catalog)
fetch_okf_document_section_tool = FunctionTool(func=fetch_okf_document_section)


# ---------------------------------------------------------------------------
# 3-Tier Hierarchical Agent Skills & OKF Progressive Disclosure Tools
# ---------------------------------------------------------------------------
SKILLS_INDEX_PATH = os.path.join(KNOWLEDGE_BASE_DIR, "skills_catalog_index.json")
SKILLS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "skills"))


def discover_skill_catalog(query: str, domain: str = None) -> list[dict]:
    """Level 1 Discovery: Search the 3-tier hierarchical skills catalog for relevant parent domains and disciplines.

    Use this tool FIRST when encountering operational queries, technical diagnostics, floor safety,
    inventory reconciliation, AGV routing, or HR workforce policies (e.g., 'cycle count SKU-991',
    '3-day sick leave policy', 'night shift differential', 'LOTO lockout', 'conveyor motor vibration').

    Args:
        query: Operational keywords or user prompt terms.
        domain: Optional filter ('HUMAN_RESOURCES', 'INVENTORY', 'MAINTENANCE', 'SAFETY', 'ROBOTICS').

    Returns:
        List of matching parent skill suites and their specialist disciplines with relevance scoring.
    """
    import json
    if not os.path.exists(SKILLS_INDEX_PATH):
        return [{"error": f"Skills index not found at {SKILLS_INDEX_PATH}"}]

    try:
        with open(SKILLS_INDEX_PATH, "r", encoding="utf-8") as f:
            catalog = json.load(f)
    except Exception as e:
        return [{"error": f"Failed to load skills catalog index: {str(e)}"}]

    suites = catalog.get("suites", [])
    query_lower = query.lower().strip()
    query_words = set(query_lower.split())
    domain_upper = domain.upper().strip() if domain else None

    matches = []
    for suite in suites:
        if domain_upper and suite.get("category", "").upper() != domain_upper:
            continue

        suite_id = suite.get("suite_id", "").lower()
        title = suite.get("display_name", "").lower()
        desc = suite.get("description", "").lower()
        tags = [t.lower() for t in suite.get("tags", [])]

        score = 0
        if query_lower in title or query_lower in suite_id:
            score += 12
        if query_lower in desc:
            score += 8
        for word in query_words:
            if word in title or word in suite_id:
                score += 4
            if word in desc:
                score += 2
            if any(word in t for t in tags):
                score += 5

        # Also search disciplines and micro-skills
        matched_disciplines = []
        for disc in suite.get("disciplines", []):
            disc_title = disc.get("display_name", "").lower()
            disc_desc = disc.get("description", "").lower()
            disc_matched = False
            for word in query_words:
                if word in disc_title or word in disc_desc:
                    score += 3
                    disc_matched = True

            for micro in disc.get("micro_skills", []):
                micro_title = micro.get("display_name", "").lower()
                micro_id = micro.get("micro_skill_id", "").lower()
                micro_tags = [t.lower() for t in micro.get("tags", [])]
                if query_lower in micro_title or query_lower in micro_id:
                    score += 15
                    disc_matched = True
                for word in query_words:
                    if word in micro_title or word in micro_id or any(word in t for t in micro_tags):
                        score += 5
                        disc_matched = True

            if disc_matched or not query_words:
                matched_disciplines.append({
                    "discipline_id": disc.get("discipline_id"),
                    "display_name": disc.get("display_name"),
                    "available_micro_skills": [m["micro_skill_id"] for m in disc.get("micro_skills", [])]
                })

        if score > 0 or not query_words:
            matches.append((score, {
                "disclosure_level": "LEVEL_1_ROOT_DOMAIN",
                "suite_id": suite.get("suite_id"),
                "display_name": suite.get("display_name"),
                "category": suite.get("category"),
                "version": suite.get("version"),
                "relevance_score": score,
                "summary": suite.get("description"),
                "matched_disciplines": matched_disciplines or [
                    {"discipline_id": d["discipline_id"], "display_name": d["display_name"]}
                    for d in suite.get("disciplines", [])
                ],
                "next_step": f"Call fetch_skill_manifest(skill_id='{suite.get('suite_id')}', discipline_id=...) to inspect specialist discipline."
            }))

    matches.sort(key=lambda x: x[0], reverse=True)
    return [m[1] for m in matches[:3]] if matches else [
        {"message": f"No skills found for '{query}'. Try broader terms like 'hr', 'cycle count', 'vibration', 'loto', 'agv'."}
    ]


def fetch_skill_manifest(skill_id: str, discipline_id: str = None) -> dict:
    """Level 2 Progressive Disclosure: Retrieve the specialist discipline manifest and micro-skill roster.

    Use this tool AFTER discovering the root skill suite using `discover_skill_catalog`.
    It returns the discipline parameters, operational scope, and list of available micro-skills.

    Args:
        skill_id: Root skill identifier (e.g. 'hr-workforce-governance', 'wms-inventory-resolver', 'conveyor-diagnostics').
        discipline_id: Optional specialist discipline ID (e.g. 'employee-leave-attendance', 'inventory-discrepancy-resolution').

    Returns:
        Structured manifest containing operational scope and available micro-skills for Level 3 activation.
    """
    import json
    if not os.path.exists(SKILLS_INDEX_PATH):
        return {"error": f"Skills index not found at {SKILLS_INDEX_PATH}"}

    try:
        with open(SKILLS_INDEX_PATH, "r", encoding="utf-8") as f:
            catalog = json.load(f)
    except Exception as e:
        return {"error": f"Failed to load skills catalog: {str(e)}"}

    suite = next((s for s in catalog.get("suites", []) if s.get("suite_id", "").lower() == skill_id.lower().strip()), None)
    if not suite:
        return {
            "error": f"Skill suite '{skill_id}' not found.",
            "available_suites": [s["suite_id"] for s in catalog.get("suites", [])]
        }

    disciplines = suite.get("disciplines", [])
    target_disc = None
    if discipline_id:
        target_disc = next((d for d in disciplines if d.get("discipline_id", "").lower() == discipline_id.lower().strip()), None)

    if not target_disc and len(disciplines) > 0:
        target_disc = disciplines[0]

    return {
        "disclosure_level": "LEVEL_2_SPECIALIST_DISCIPLINE",
        "suite_id": suite["suite_id"],
        "suite_display_name": suite["display_name"],
        "discipline_id": target_disc["discipline_id"] if target_disc else None,
        "discipline_display_name": target_disc["display_name"] if target_disc else None,
        "scope_description": target_disc["description"] if target_disc else suite["description"],
        "micro_skills": target_disc.get("micro_skills", []) if target_disc else [],
        "next_step": f"Call activate_skill(skill_id='{suite['suite_id']}', discipline_id='{target_disc['discipline_id'] if target_disc else ''}', micro_skill_id=...) to activate SOP rules and scripts."
    }


def activate_skill(skill_id: str, discipline_id: str, micro_skill_id: str, action: str = None) -> dict:
    """Level 3 Progressive Disclosure: Activate operational micro-skill to retrieve procedural SOPs, checklists, and scripts.

    Use this tool to disclose the full step-by-step SOP text, verification formulas, and execution
    parameters for a specific operational task (e.g. 'sku-991-velocity-cycle-count', 'medical-certification-fmla-audit',
    'night-shift-differential-calc', 'breaker-lockout-tagout-verification', 'fft-vibration-harmonic-analysis').

    Args:
        skill_id: Root skill suite (e.g. 'wms-inventory-resolver', 'hr-workforce-governance', 'conveyor-diagnostics').
        discipline_id: Specialist discipline (e.g. 'inventory-discrepancy-resolution', 'employee-leave-attendance').
        micro_skill_id: Target micro-skill (e.g. 'sku-991-velocity-cycle-count', 'medical-certification-fmla-audit').
        action: Optional operational action flag.

    Returns:
        Complete operational procedure, compliance rules, and executable code payload.
    """
    skill_clean = skill_id.strip().lower()
    disc_clean = discipline_id.strip().lower()
    micro_clean = micro_skill_id.strip().lower()

    micro_dir = os.path.join(SKILLS_DIR, skill_clean, "disciplines", disc_clean, "micro-skills", micro_clean)
    skill_md_path = os.path.join(micro_dir, "SKILL.md")
    script_path = os.path.join(micro_dir, "scripts", "tool.py")

    if not os.path.exists(skill_md_path):
        # Fallback search across any discipline in the suite
        suite_path = os.path.join(SKILLS_DIR, skill_clean, "disciplines")
        if os.path.exists(suite_path):
            for d in os.listdir(suite_path):
                candidate = os.path.join(suite_path, d, "micro-skills", micro_clean)
                if os.path.exists(os.path.join(candidate, "SKILL.md")):
                    micro_dir = candidate
                    skill_md_path = os.path.join(candidate, "SKILL.md")
                    script_path = os.path.join(candidate, "scripts", "tool.py")
                    disc_clean = d
                    break

    if not os.path.exists(skill_md_path):
        return {
            "error": f"Micro-skill '{micro_skill_id}' not found under {skill_id}/{discipline_id}.",
            "suggestion": f"Call fetch_skill_manifest(skill_id='{skill_id}') to inspect valid micro-skills."
        }

    with open(skill_md_path, "r", encoding="utf-8") as f:
        sop_text = f.read()

    script_code = None
    if os.path.exists(script_path):
        with open(script_path, "r", encoding="utf-8") as f:
            script_code = f.read()

    return {
        "disclosure_level": "LEVEL_3_OPERATIONAL_ACTIVATION",
        "hierarchy_path": f"{skill_clean} ➔ {disc_clean} ➔ {micro_clean}",
        "skill_id": skill_clean,
        "discipline_id": disc_clean,
        "micro_skill_id": micro_clean,
        "sop_content": sop_text,
        "executable_script": script_code,
        "status": "ACTIVATED",
        "compliance_guarantee": "Validated against Cymbal Enterprise Warehouse SOP and OSHA/EHS Standards"
    }


discover_skill_catalog_tool = FunctionTool(func=discover_skill_catalog)
fetch_skill_manifest_tool = FunctionTool(func=fetch_skill_manifest)
activate_skill_tool = FunctionTool(func=activate_skill)


