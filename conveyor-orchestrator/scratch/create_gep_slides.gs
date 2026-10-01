/**
 * Google Apps Script Automation: Stackbox Conveyor Orchestrator GEP Slide Deck
 *
 * How to use:
 * 1. Go to https://script.google.com/ and create a new project.
 * 2. Paste this entire script into `Code.gs`.
 * 3. Run the `createGEPSlideDeck()` function.
 * 4. Authorize Google Drive / Slides permissions when prompted.
 * 5. A brand new 12-slide Google Slides presentation will be created in your Drive root.
 */

function createGEPSlideDeck() {
  var presentation = SlidesApp.create("Stackbox Conveyor Orchestrator - GEP Features Showcase");
  var slides = presentation.getSlides();
  
  // Remove default blank/title slide to build cleanly from scratch
  if (slides.length > 0) {
    slides[0].remove();
  }

  var slidesData = [
    {
      title: "Stackbox Conveyor Orchestrator",
      subtitle: "Enterprise Autonomous Warehouse Control Powered by GEP & ADK 2.0",
      pillar: "TITLE SLIDE",
      bullets: [
        "Presenter: Engineering & Architecture Team",
        "Repository: stackbox-conveyor-orchestrator",
        "Highlighting 9 Core Pillars of the Gemini Enterprise Platform"
      ],
      notes: "Welcome everyone. Today we are showcasing the Stackbox Conveyor Orchestrator—a production-grade multi-agent warehouse automation system designed to handle critical industrial conveyor belt malfunctions deterministically. Rather than a simple chat wrapper, this codebase demonstrates how we have embedded all nine foundational pillars of the Gemini Enterprise Platform (GEP) to achieve enterprise reliability, strict safety compliance, and zero-latency hardware coordination."
    },
    {
      title: "Executive Summary & Architecture",
      subtitle: "Architecting Autonomous Industrial Operations",
      pillar: "SYSTEM TOPOLOGY",
      bullets: [
        "The Challenge: Warehouse conveyor stoppages cause compounding supply chain delays and hazardous manual bypass picking.",
        "The GEP Solution: A hybrid graph-directed agentic architecture combining deterministic code execution with reasoning models.",
        "Ingest: Telemetry parsing and severity classification (CRITICAL vs. RECOVERABLE).",
        "Hardware Routing: Parallel vector SOP lookup and real-time fleet stock queries.",
        "Synthesis: Autonomous picker bot rerouting and authoritative engineering audit reports."
      ],
      notes: "In mission-critical warehouse environments, pure LLM loops introduce unacceptable latency and probabilistic failure risks. By leveraging GEP's Agent Development Kit (ADK) 2.0 Workflow architecture, we enforce strict Directed Acyclic Graph (DAG) boundaries where physical hardware operations execute in parallel and converge deterministically before any AI dispatching occurs."
    },
    {
      title: "ADK 2.0 Workflow Routing",
      subtitle: "Deterministic DAGs & Conditional Control Flows",
      pillar: "PILLAR 1: WORKFLOW API",
      bullets: [
        "Core Construct: Graph-based orchestration built via ADK 2.0 Workflow and FunctionNodes in agent.py.",
        "Parallel Branches: Simultaneous routing to RunbookLookup and WMSAccess upon detecting CRITICAL fault codes.",
        "State Synchronization: JoinNode aggregates asynchronous hardware payloads before transferring context to downstream LlmAgent.",
        "Jittered Backoff: Hardware-facing nodes utilize RetryConfig with exponential backoff (2.0x) and randomized jitter (0.5s)."
      ],
      notes: "Pillar 1 focuses on our core workflow routing defined in agent.py. When telemetry streams report a belt jam, TelemetryIngest evaluates the error severity. If critical, it forks execution across two parallel branches. To protect programmable logic controllers (PLCs) from stampede errors during network blips, every hardware node is wrapped in an exponential retry configuration with randomized jitter."
    },
    {
      title: "Enterprise Vector RAG & SOPs",
      subtitle: "Grounding Agent Decisions in Discovery Engine Datastores",
      pillar: "PILLAR 2: DISCOVERY ENGINE",
      bullets: [
        "Vector Datastore: Seamless integration with Google Cloud Discovery Engine vector search indexes.",
        "Semantic Grounding: Ingests raw PLC fault codes (e.g., ERR-CONV-MTR-09) and extracts mechanical repair walkthroughs.",
        "Safety Priority: Automatically surfaces mandatory OSHA Lockout-Tagout (LOTO) de-energization procedures.",
        "Zero Hallucination: Grounded SOP retrieval ensures repair instructions adhere strictly to manufacturer tolerances."
      ],
      notes: "When a mechanical failure occurs, technicians need exact manufacturer runbooks rather than generic LLM advice. In Pillar 2, our agent queries an enterprise Discovery Engine vector datastore. It translates cryptic sensor fault codes into step-by-step repair runbooks, specifically ensuring that required electrical Lockout-Tagout safety warnings are injected into the technician's dispatch orders."
    },
    {
      title: "Real-Time Fleet MCP Connectors",
      subtitle: "Standardized Tooling Architecture via Model Context Protocol",
      pillar: "PILLAR 3: MCP SERVER",
      bullets: [
        "Stdio Transport: Host dedicated stdio MCP server (mcp_server.py) tracking active warehouse robotic bot states.",
        "Live Telemetry: Exposes stock availability, AGV battery percentages, warehouse coordinates, and active tasks.",
        "Autonomous Bypass Rerouting: Dynamically coordinates physical AGV picker bot bypasses around damaged conveyor zones.",
        "Decoupled Architecture: Standardized MCP schemas eliminate custom ad-hoc hardware integration scripts."
      ],
      notes: "Pillar 3 highlights our use of the modern Model Context Protocol, or MCP. Rather than building fragile, custom REST wrappers for every warehouse bot, we host a dedicated MCP server in mcp_server.py. The orchestrator inspects real-time picker bot battery levels and physical locations, dynamically re-routing AGVs to bypass broken conveyor zones without human intervention."
    },
    {
      title: "Multimodal CCTV Vision Auditing",
      subtitle: "Real-Time Visual Posture & Safety Inspection",
      pillar: "PILLAR 4: MULTIMODAL VISION",
      bullets: [
        "Native Multimodality: Powered by Gemini 1.5 Pro visual reasoning engines.",
        "Live CCTV Ingest: Directly inspects streaming camera feeds and snapshots across active repair aisles.",
        "Automated Safety Infraction Logging: Audits repair zones to verify technician PPE compliance.",
        "Immediate Interlock: Halts autonomous AGV movement if operators are detected without safety hard hats or vests."
      ],
      notes: "Pillar 4 brings physical eyesight to our orchestrator. Using Gemini's native multimodal vision capabilities, the system connects directly to warehouse CCTV camera streams. Before authorizing AGVs to enter a repair aisle, it verifies that human technicians are wearing required safety gear. If an operator is detected without PPE, the workflow immediately halts autonomous bot movement and logs an infraction."
    },
    {
      title: "Cross-Session Long-Term Memory",
      subtitle: "Persistent Operator Profile Recollection via Memory Bank",
      pillar: "PILLAR 5: VERTEX AI MEMORY BANK",
      bullets: [
        "Memory Bank Binding: Integrates Vertex AI Session Service long-term context retention across runs.",
        "Shift Continuity: Recalls technician Dave's identity, certs (LOTO Level 3), and auditing goals across multi-day shifts.",
        "Contextual Personalization: Automatically adjusts technical explanation depth based on logged-in operator credentials.",
        "Zero Onboarding Overhead: Eliminates repetitive shift-handoff briefing prompts."
      ],
      notes: "Industrial warehouse shifts rotate constantly. Pillar 5 solves context loss across shift changes using Vertex AI Memory Bank. By embedding preload_memory_tool, the orchestrator remembers technician Dave's qualifications and active audit tasks from previous days. When Dave logs back in, the agent skips redundant onboarding questions and immediately resumes active maintenance workflows."
    },
    {
      title: "Isolated Secure Agent Sandbox",
      subtitle: "Sandboxed Python Code Execution for Telemetry Stress Profiling",
      pillar: "PILLAR 6: GEP AGENT SANDBOX",
      bullets: [
        "GEP Agent Sandbox: Spawns isolated container execution runtimes decoupled from core SCADA/PLC networks.",
        "Data Science Toolchain: Equipped with write_file_to_sandbox, execute_python_in_sandbox, and read_file_from_sandbox.",
        "On-the-Fly Calculation: Synthesizes pandas/numpy scripts to compute Thermal Heat Stress Indices across motor bearings.",
        "Air-Gapped Security: Protects physical motor controllers from untrusted dynamic code execution."
      ],
      notes: "Allowing AI agents to run arbitrary code on production PLCs is a major security hazard. In Pillar 6, we utilize GEP's secure Agent Sandbox. When analyzing heavy telemetry logs for thermal overheating, the orchestrator delegates the task to a specialized sandbox subagent. It writes and executes pandas scripts inside an isolated container, returning only clean statistical insights back to the main controller."
    },
    {
      title: "Enterprise Governance Guardrails",
      subtitle: "Zero-Trust AI Enforcement via Model Armor & SPIFFE",
      pillar: "PILLAR 7: GOVERNANCE & SECURITY",
      bullets: [
        "Model Armor Sanitization: Intercepts inbound prompts and outbound LLM responses to prevent prompt injection exploits.",
        "Physical Ceiling Enforcement: Hard-bans instructions attempting to override motor speeds beyond physical tolerances.",
        "SPIFFE Workload Identity: Enforces cryptographic service identifiers (spiffe://stackbox.internal/...) for mTLS authentication.",
        "Immutable Audit Logging: Cryptographically binds every robotic dispatch order to authenticated technician credentials."
      ],
      notes: "Pillar 7 represents our defense-in-depth security governance. In model_armor_config.yaml, we configure strict Model Armor guardrails. Even if an attacker injects a malicious prompt attempting to force conveyor motors beyond maximum physical RPMs, Model Armor intercepts and terminates the instruction. Furthermore, all service-to-robotic dispatches are authenticated via SPIFFE mutual TLS certificates."
    },
    {
      title: "Automated Quality Flywheel",
      subtitle: "Continuous Evaluation via LLM-as-a-Judge & ADK Eval",
      pillar: "PILLAR 8: EVALUATION SUITE",
      bullets: [
        "Custom GEAP Metrics: Evaluates trajectories against multi_turn_task_success, multi_turn_tool_use_quality, and hallucination.",
        "Synthetic Dataset Synthesis: Automatically generates complex multi-turn warehouse failure test scenarios.",
        "Automated Grading Loop: Regression tests agent traces to guarantee prompt updates never degrade safety compliance.",
        "Prompt Auto-Optimization: Utilizes grade feedback clusters to automatically fine-tune agent system prompts."
      ],
      notes: "How do we prove our agent is safe before deploying to a live warehouse? Pillar 8 highlights our automated Quality Flywheel. We define custom LLM-as-a-judge metrics in GEP console tracking hallucination rates and tool-calling accuracy. Every code change runs through an automated grading loop against synthetic industrial disaster datasets."
    },
    {
      title: "Production Cloud Deployment",
      subtitle: "Vertex AI Reasoning Engines & Enterprise Observability",
      pillar: "PILLAR 9: CLOUD RUNTIME",
      bullets: [
        "Reasoning Engine Packaging: One-click remote deployment to Vertex AI Agent Runtime via agents-cli deploy.",
        "Live Telemetry UI: Hosts real-time FastAPI web dashboard with interactive SVG monitoring of AGV routes and CCTV states.",
        "Distributed GenAI Tracing: Fully instrumented with OpenTelemetry prompt-response tracking and Google Cloud Logging.",
        "Enterprise Scalability: Serverless infrastructure scaling automatically under heavy warehouse telemetry bursts."
      ],
      notes: "Finally, Pillar 9 showcases production operations. Using agent_runtime_app.py, the entire multi-agent DAG packages into a serverless Vertex AI Reasoning Engine with a single CLI command. In production, operators monitor live robotic fleet movements via our real-time FastAPI SVG dashboard, backed by full OpenTelemetry distributed trace logging in Google Cloud."
    },
    {
      title: "Conclusion & Summary",
      subtitle: "Delivering Deterministic Industrial Agentic Systems",
      pillar: "CONCLUSION & QA",
      bullets: [
        "Summary: Achieved zero-trust industrial automation combining ADK 2.0 DAG determinism with Gemini reasoning multimodality.",
        "Operational Impact: Eliminated hazardous manual conveyor bypass picking and minimized downtime.",
        "Next Steps: Expand MCP fleet connectors to high-reach turret trucks and thermal CCTV feeds.",
        "Open Q&A: Thank you for your time. Questions are welcome."
      ],
      notes: "To wrap up: the Stackbox Conveyor Orchestrator proves that agentic AI can safely operate heavy industrial machinery when built on the Gemini Enterprise Platform. By wrapping powerful reasoning models inside deterministic workflows, real-time MCP fleet connectors, and zero-trust guardrails, we achieve true autonomous warehouse resilience. We will now open the floor to any questions."
    }
  ];

  for (var i = 0; i < slidesData.length; i++) {
    var data = slidesData[i];
    var slide = presentation.appendSlide(SlidesApp.PredefinedLayout.BLANK);
    
    // Set dark background (Slate 900)
    slide.getBackground().setSolidFill("#0F172A");

    // Pillar Header Badge Textbox
    var badgeBox = slide.insertTextBox(data.pillar, 50, 40, 300, 30);
    var badgeStyle = badgeBox.getText().getTextStyle();
    badgeStyle.setForegroundColor("#38BDF8");
    badgeStyle.setFontSize(12);
    badgeStyle.setBold(true);

    // Title Textbox
    var titleBox = slide.insertTextBox(data.title, 50, 75, 860, 50);
    var titleStyle = titleBox.getText().getTextStyle();
    titleStyle.setForegroundColor("#F8FAFC");
    titleStyle.setFontSize(32);
    titleStyle.setBold(true);

    // Subtitle Textbox
    var subBox = slide.insertTextBox(data.subtitle, 50, 130, 860, 40);
    var subStyle = subBox.getText().getTextStyle();
    subStyle.setForegroundColor("#4ADE80");
    subStyle.setFontSize(18);

    // Content Box
    var contentBox = slide.insertTextBox("", 50, 190, 860, 320);
    contentBox.getFill().setSolidFill("#1E293B");
    
    var bulletText = "";
    for (var j = 0; j < data.bullets.length; j++) {
      bulletText += "•   " + data.bullets[j] + (j < data.bullets.length - 1 ? "\n\n" : "");
    }
    contentBox.getText().setText(bulletText);
    var contentStyle = contentBox.getText().getTextStyle();
    contentStyle.setForegroundColor("#F8FAFC");
    contentStyle.setFontSize(16);

    // Add Speaker Notes
    slide.getNotesPage().getSpeakerNotesShape().getText().setText(data.notes);
  }

  Logger.log("Created presentation URL: " + presentation.getUrl());
}
