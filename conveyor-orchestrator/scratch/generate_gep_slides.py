# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "python-pptx>=1.0.0",
# ]
# ///
"""
Stackbox Conveyor Orchestrator - GEP Feature Presentation Generator

This script generates a professional PowerPoint presentation (.pptx) showcasing the
Gemini Enterprise Platform (GEP) features implemented in the conveyor orchestrator codebase.

Dependency Note:
`python-pptx` is required as an isolated script dependency to programmatically construct
the .pptx presentation file without altering core project dependencies.
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Theme Colors (Modern Dark Theme)
    BG_COLOR = RGBColor(0x0F, 0x17, 0x2A)       # Deep Navy / Slate 900
    CARD_BG = RGBColor(0x1E, 0x29, 0x3B)        # Slate 800
    ACCENT_BLUE = RGBColor(0x38, 0xBD, 0xF8)    # Sky 400
    ACCENT_GREEN = RGBColor(0x4A, 0xDE, 0x80)   # Emerald 400
    TEXT_WHITE = RGBColor(0xF8, 0xFA, 0xFC)     # Slate 50
    TEXT_MUTED = RGBColor(0x94, 0xA3, 0xB8)     # Slate 400

    slides_data = [
        {
            "title": "Stackbox Conveyor Orchestrator",
            "subtitle": "Enterprise Autonomous Warehouse Control Powered by GEP & ADK 2.0",
            "pillar": "TITLE SLIDE",
            "bullets": [
                "Presenter: Engineering & Architecture Team",
                "Repository: stackbox-conveyor-orchestrator",
                "Highlighting 9 Core Pillars of the Gemini Enterprise Platform"
            ],
            "notes": "Welcome everyone. Today we are showcasing the Stackbox Conveyor Orchestrator—a production-grade multi-agent warehouse automation system designed to handle critical industrial conveyor belt malfunctions deterministically. Rather than a simple chat wrapper, this codebase demonstrates how we have embedded all nine foundational pillars of the Gemini Enterprise Platform (GEP) to achieve enterprise reliability, strict safety compliance, and zero-latency hardware coordination."
        },
        {
            "title": "Executive Summary & Architecture",
            "subtitle": "Architecting Autonomous Industrial Operations",
            "pillar": "SYSTEM TOPOLOGY",
            "bullets": [
                "The Challenge: Warehouse conveyor stoppages cause compounding supply chain delays and hazardous manual bypass picking.",
                "The GEP Solution: A hybrid graph-directed agentic architecture combining deterministic code execution with reasoning models.",
                "Ingest: Telemetry parsing and severity classification (CRITICAL vs. RECOVERABLE).",
                "Hardware Routing: Parallel vector SOP lookup and real-time fleet stock queries.",
                "Synthesis: Autonomous picker bot rerouting and authoritative engineering audit reports."
            ],
            "notes": "In mission-critical warehouse environments, pure LLM loops introduce unacceptable latency and probabilistic failure risks. By leveraging GEP's Agent Development Kit (ADK) 2.0 Workflow architecture, we enforce strict Directed Acyclic Graph (DAG) boundaries where physical hardware operations execute in parallel and converge deterministically before any AI dispatching occurs."
        },
        {
            "title": "ADK 2.0 Workflow Routing",
            "subtitle": "Deterministic DAGs & Conditional Control Flows",
            "pillar": "PILLAR 1: WORKFLOW API",
            "bullets": [
                "Core Construct: Graph-based orchestration built via ADK 2.0 Workflow and FunctionNodes in agent.py.",
                "Parallel Branches: Simultaneous routing to RunbookLookup and WMSAccess upon detecting CRITICAL fault codes.",
                "State Synchronization: JoinNode aggregates asynchronous hardware payloads before transferring context to the downstream LlmAgent.",
                "Jittered Backoff: Hardware-facing nodes utilize RetryConfig with exponential backoff (2.0x) and randomized jitter (0.5s) to protect physical controllers."
            ],
            "notes": "Pillar 1 focuses on our core workflow routing defined in agent.py. When telemetry streams report a belt jam, TelemetryIngest evaluates the error severity. If critical, it forks execution across two parallel branches. To protect programmable logic controllers (PLCs) from stampede errors during network blips, every hardware node is wrapped in an exponential retry configuration with randomized jitter."
        },
        {
            "title": "Enterprise Vector RAG & SOPs",
            "subtitle": "Grounding Agent Decisions in Discovery Engine Datastores",
            "pillar": "PILLAR 2: DISCOVERY ENGINE",
            "bullets": [
                "Vector Datastore: Seamless integration with Google Cloud Discovery Engine vector search indexes.",
                "Semantic Grounding: Ingests raw PLC fault codes (e.g., ERR-CONV-MTR-09) and extracts high-context mechanical repair walkthroughs.",
                "Safety Priority: Automatically surfaces mandatory OSHA Lockout-Tagout (LOTO) de-energization procedures.",
                "Zero Hallucination: Grounded SOP retrieval ensures mechanical repair instructions adhere strictly to manufacturer tolerances."
            ],
            "notes": "When a mechanical failure occurs, technicians need exact manufacturer runbooks rather than generic LLM advice. In Pillar 2, our agent queries an enterprise Discovery Engine vector datastore. It translates cryptic sensor fault codes into step-by-step repair runbooks, specifically ensuring that required electrical Lockout-Tagout safety warnings are injected into the technician's dispatch orders."
        },
        {
            "title": "Real-Time Fleet MCP Connectors",
            "subtitle": "Standardized Tooling Architecture via Model Context Protocol",
            "pillar": "PILLAR 3: MCP SERVER",
            "bullets": [
                "Stdio Transport: Host dedicated stdio MCP server (mcp_server.py) tracking active warehouse robotic bot states.",
                "Live Telemetry: Exposes stock availability, AGV battery percentages, warehouse aisle coordinates, and active tasks.",
                "Autonomous Bypass Rerouting: Dynamically coordinates physical AGV picker bot picking bypasses around damaged conveyor zones.",
                "Decoupled Architecture: Standardized MCP schemas eliminate custom ad-hoc hardware integration scripts."
            ],
            "notes": "Pillar 3 highlights our use of the modern Model Context Protocol, or MCP. Rather than building fragile, custom REST wrappers for every warehouse bot, we host a dedicated MCP server in mcp_server.py. The orchestrator inspects real-time picker bot battery levels and physical locations, dynamically re-routing AGVs to bypass broken conveyor zones without human intervention."
        },
        {
            "title": "Multimodal CCTV Vision Auditing",
            "subtitle": "Real-Time Visual Posture & Safety Inspection",
            "pillar": "PILLAR 4: MULTIMODAL VISION",
            "bullets": [
                "Native Multimodality: Powered by Gemini 1.5 Pro visual reasoning engines.",
                "Live CCTV Ingest: Directly inspects streaming camera feeds and snapshots across active repair aisles.",
                "Automated Safety Infraction Logging: Audits repair zones to verify technician Personal Protective Equipment (PPE) compliance.",
                "Immediate Interlock: Halts autonomous AGV movement if operators are detected without safety hard hats or high-visibility vests."
            ],
            "notes": "Pillar 4 brings physical eyesight to our orchestrator. Using Gemini's native multimodal vision capabilities, the system connects directly to warehouse CCTV camera streams. Before authorizing AGVs to enter a repair aisle, it verifies that human technicians are wearing required safety gear. If an operator is detected without PPE, the workflow immediately halts autonomous bot movement and logs an infraction."
        },
        {
            "title": "Cross-Session Long-Term Memory",
            "subtitle": "Persistent Operator Profile Recollection via Memory Bank",
            "pillar": "PILLAR 5: VERTEX AI MEMORY BANK",
            "bullets": [
                "Memory Bank Binding: Integrates Vertex AI Session Service long-term context retention across runs.",
                "Shift Continuity: Recalls technician Dave's identity, certifications (e.g., LOTO Level 3), and historical auditing goals across multi-day shifts.",
                "Contextual Personalization: Automatically adjusts technical engineering explanation depth based on logged-in operator credentials.",
                "Zero Onboarding Overhead: Eliminates repetitive shift-handoff briefing prompts."
            ],
            "notes": "Industrial warehouse shifts rotate constantly. Pillar 5 solves context loss across shift changes using Vertex AI Memory Bank. By embedding preload_memory_tool, the orchestrator remembers technician Dave's qualifications and active audit tasks from previous days. When Dave logs back in, the agent skips redundant onboarding questions and immediately resumes active maintenance workflows."
        },
        {
            "title": "Isolated Secure Agent Sandbox",
            "subtitle": "Sandboxed Python Code Execution for Telemetry Stress Profiling",
            "pillar": "PILLAR 6: GEP AGENT SANDBOX",
            "bullets": [
                "GEP Agent Sandbox: Spawns isolated container execution runtimes decoupled from core warehouse SCADA/PLC networks.",
                "Data Science Toolchain: Equipped with write_file_to_sandbox, execute_python_in_sandbox, and read_file_from_sandbox.",
                "On-the-Fly Calculation: Synthesizes pandas and numpy diagnostic scripts to compute ambient Thermal Heat Stress Indices across motor bearings.",
                "Air-Gapped Security: Protects physical motor controllers from untrusted dynamic code execution."
            ],
            "notes": "Allowing AI agents to run arbitrary code on production PLCs is a major security hazard. In Pillar 6, we utilize GEP's secure Agent Sandbox. When analyzing heavy telemetry logs for thermal overheating, the orchestrator delegates the task to a specialized sandbox subagent. It writes and executes pandas scripts inside an isolated container, returning only clean statistical insights back to the main controller."
        },
        {
            "title": "Enterprise Governance Guardrails",
            "subtitle": "Zero-Trust AI Enforcement via Model Armor & SPIFFE",
            "pillar": "PILLAR 7: GOVERNANCE & SECURITY",
            "bullets": [
                "Model Armor Sanitization: Intercepts inbound prompts and outbound LLM responses to prevent prompt injection exploits.",
                "Physical Ceiling Enforcement: Hard-bans instructions attempting to override motor speeds beyond physical tolerances.",
                "SPIFFE Workload Identity: Enforces cryptographic service identifiers (spiffe://stackbox.internal/...) for mTLS authentication.",
                "Immutable Audit Logging: Cryptographically binds every robotic dispatch order to authenticated technician credentials."
            ],
            "notes": "Pillar 7 represents our defense-in-depth security governance. In model_armor_config.yaml, we configure strict Model Armor guardrails. Even if an attacker injects a malicious prompt attempting to force conveyor motors beyond maximum physical RPMs, Model Armor intercepts and terminates the instruction. Furthermore, all service-to-robotic dispatches are authenticated via SPIFFE mutual TLS certificates."
        },
        {
            "title": "Automated Quality Flywheel",
            "subtitle": "Continuous Evaluation via LLM-as-a-Judge & ADK Eval",
            "pillar": "PILLAR 8: EVALUATION SUITE",
            "bullets": [
                "Custom GEAP Metrics: Evaluates trajectories against multi_turn_task_success, multi_turn_tool_use_quality, and hallucination.",
                "Synthetic Dataset Synthesis: Automatically generates complex multi-turn warehouse failure test scenarios.",
                "Automated Grading Loop: Regression tests agent traces to guarantee prompt updates never degrade safety compliance.",
                "Prompt Auto-Optimization: Utilizes grade feedback clusters to automatically fine-tune agent system prompts."
            ],
            "notes": "How do we prove our agent is safe before deploying to a live warehouse? Pillar 8 highlights our automated Quality Flywheel. We define custom LLM-as-a-judge metrics in GEP console tracking hallucination rates and tool-calling accuracy. Every code change runs through an automated grading loop against synthetic industrial disaster datasets."
        },
        {
            "title": "Production Cloud Deployment",
            "subtitle": "Vertex AI Reasoning Engines & Enterprise Observability",
            "pillar": "PILLAR 9: CLOUD RUNTIME",
            "bullets": [
                "Reasoning Engine Packaging: One-click remote deployment to Vertex AI Agent Runtime via agents-cli deploy.",
                "Live Telemetry UI: Hosts real-time FastAPI web dashboard with interactive SVG monitoring of AGV routes and CCTV states.",
                "Distributed GenAI Tracing: Fully instrumented with OpenTelemetry prompt-response tracking and Google Cloud Logging.",
                "Enterprise Scalability: Serverless infrastructure scaling automatically under heavy warehouse telemetry bursts."
            ],
            "notes": "Finally, Pillar 9 showcases production operations. Using agent_runtime_app.py, the entire multi-agent DAG packages into a serverless Vertex AI Reasoning Engine with a single CLI command. In production, operators monitor live robotic fleet movements via our real-time FastAPI SVG dashboard, backed by full OpenTelemetry distributed trace logging in Google Cloud."
        },
        {
            "title": "Conclusion & Summary",
            "subtitle": "Delivering Deterministic Industrial Agentic Systems",
            "pillar": "CONCLUSION & QA",
            "bullets": [
                "Summary: Achieved zero-trust industrial automation combining ADK 2.0 DAG determinism with Gemini reasoning multimodality.",
                "Operational Impact: Eliminated hazardous manual conveyor bypass picking and minimized downtime.",
                "Next Steps: Expand MCP fleet connectors to high-reach turret trucks and thermal CCTV feeds.",
                "Open Q&A: Thank you for your time. Questions are welcome."
            ],
            "notes": "To wrap up: the Stackbox Conveyor Orchestrator proves that agentic AI can safely operate heavy industrial machinery when built on the Gemini Enterprise Platform. By wrapping powerful reasoning models inside deterministic workflows, real-time MCP fleet connectors, and zero-trust guardrails, we achieve true autonomous warehouse resilience. We will now open the floor to any questions."
        }
    ]

    for data in slides_data:
        slide = prs.slides.add_slide(blank_layout)

        # Background
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_COLOR
        bg.line.fill.background()

        # Pillar Header Badge
        badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.6), Inches(4.2), Inches(0.45))
        badge.fill.solid()
        badge.fill.fore_color.rgb = CARD_BG
        badge.line.color.rgb = ACCENT_BLUE
        badge.line.width = Pt(1.5)
        tf_b = badge.text_frame
        tf_b.text = data["pillar"]
        p_b = tf_b.paragraphs[0]
        p_b.font.size = Pt(12)
        p_b.font.bold = True
        p_b.font.color.rgb = ACCENT_BLUE
        p_b.alignment = PP_ALIGN.CENTER

        # Title
        txBox = slide.shapes.add_textbox(Inches(0.8), Inches(1.2), Inches(11.5), Inches(1.2))
        tf = txBox.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = data["title"]
        p.font.size = Pt(38)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE

        # Subtitle
        p2 = tf.add_paragraph()
        p2.text = data["subtitle"]
        p2.font.size = Pt(20)
        p2.font.color.rgb = ACCENT_GREEN

        # Content Card
        card = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(2.6), Inches(11.733), Inches(4.3))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.fill.background()

        tf_c = card.text_frame
        tf_c.word_wrap = True
        tf_c.margin_left = Inches(0.4)
        tf_c.margin_top = Inches(0.4)
        tf_c.margin_right = Inches(0.4)

        for i, bullet in enumerate(data["bullets"]):
            p_c = tf_c.paragraphs[0] if i == 0 else tf_c.add_paragraph()
            p_c.text = f"•   {bullet}"
            p_c.font.size = Pt(18)
            p_c.font.color.rgb = TEXT_WHITE
            p_c.space_after = Pt(14)

        # Speaker Notes
        notes_slide = slide.notes_slide
        text_frame = notes_slide.notes_text_frame
        text_frame.text = data["notes"]

    output_path = os.path.join(os.path.dirname(__file__), "stackbox_conveyor_gep_features.pptx")
    prs.save(output_path)
    print(f"Presentation saved successfully to {output_path}")

if __name__ == "__main__":
    create_deck()
