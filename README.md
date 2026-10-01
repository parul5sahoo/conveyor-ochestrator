# Stackbox Conveyor Orchestrator (GEAP & ADK 2.0 Agent)

An enterprise-grade multi-agent warehouse orchestration system designed to automate critical conveyor belt fault resolution, fleet telemetry tracking, sandboxed diagnostic profiling, and multimodal safety auditing. Built on the **Gemini Enterprise Agent Platform (GEAP)** using the **Agent Development Kit (ADK) 2.0** and Vertex AI Reasoning Engines.

---

## 🌟 Key Capabilities

1. **Intelligent Workflow Routing**: Operates as a deterministic Directed Acyclic Graph (DAG) using ADK 2.0 Workflow APIs to ingest, parse, and route warehouse telemetry based on severity (Critical vs. Recoverable).
2. **Multi-Agent RAG & SOP Search**: Seamlessly retrieves lockout-tagout (LOTO), conveyor maintenance, and physical compliance safety SOPs from a Google Cloud Discovery Engine vector datastore.
3. **AGV Fleet Telemetry & Battery Monitoring**: Integrates a custom **Model Context Protocol (MCP)** server interface providing real-time telemetry on automated guided vehicles (battery, location, active tasks) to coordinate bypass routing.
4. **Multimodal CCTV Safety Auditing**: Connects Gemini 1.5 Pro multimodal capabilities to inspect safety posture, verify personal protective equipment (PPE), and log safety infractions.
5. **Secure Agent Sandbox Diagnostics**: Deploys an isolated Python execution environment allowing `sandbox_diagnostic_agent` to write and execute analytical scripts (`pandas`, `numpy`) on fleet logs (`fleet_telemetry_dump.json`) to compute Thermal Heat Stress Index (TSI) and identify aisle hot-spots.
6. **Hierarchical Skills & OKF Progressive Disclosure**: Implements a 3-tier Operational Knowledge Framework (5 Root Suites $\to$ 11 Disciplines $\to$ 23 Micro-Skills) that prunes token ingestion down to ~122 tokens per call, slashing LLM inference costs to under 1 paisa (₹0.0089) per operation.
7. **Vertex AI Memory Bank**: Implements cross-session operator profile recollection so that the orchestrator remembers technician identities, certifications, and active auditing goals across separate shifts.
8. **SecOps & SAIF/SGP Self-Governance**: Automated refusal policies for unauthorized surveillance (e.g. breakroom CCTV) and interlock overrides, generating DEFCON-2 security incident alerts.

---

## 🖥️ Live Cloud Run UI Surfaces

The deployed Cloud Run service hosts three interconnected enterprise UI surfaces:

| Surface | Cloud Run Route | Target Audience | Key Features & Metrics |
| :--- | :--- | :--- | :--- |
| **🏭 Operational Dashboard** | `/dashboard` | Operations & Field Technicians | Live SVG conveyor belt monitor, real-time AGV telemetry tracking, CCTV posture camera feed, fault injector, and incident dispatch chat. |
| **⚡ Observability Playground** | `/playground` | Developers & Architects | Preset prompt triggers, 3-tier OKF skill hierarchy browser, real-time token reduction and cost reactor (~122 tokens in, ₹0.0089/op), live streaming response pane. |
| **📊 Executive Admin Console** | `/admin` | CXOs & IT Administrators | Latency & Performance HUD (P50 284ms, P95 612ms), multi-tenant Sessions & Memory Banks, SecOps Threat Matrix (SAIF/SGP refusal `SEC-8821`), Hillclimbing Eval Scorecards (3.70 $\to$ 4.30). |
| **📑 Keynote Presentation Deck** | `/demo_presentation.html` | Stakeholders & Summit Demo | Clean, responsive keynote slide deck with persona scripts and live architecture breakdowns. |

---

## 📁 Repository Layout

```text
stackbox-conveyor-demo/
├── README.md                          # Main repository guide (This file)
├── DESIGN_SPEC.md                     # Technical architecture, DAG specs, and tool definitions
├── conveyor-orchestrator/
│   ├── Dockerfile                     # Multi-stage Python 3.12 container definition for Cloud Run
│   ├── app/                           # Core Agent Source
│   │   ├── agent.py                   # Multi-agent workflow, subagent routing, sandbox diagnostic prompt
│   │   ├── agent_runtime_app.py       # Reasoning Engine entrypoint for Vertex AI deployment
│   │   ├── fast_api_app.py            # FastAPI server exposing /dashboard, /playground, /admin
│   │   ├── mcp_server.py              # Fleet Telemetry MCP Server (stdio-based)
│   │   ├── tools.py                   # Custom tool wrappers (WMS, runbooks, sandbox tools)
│   │   ├── app_utils/                 # Supporting services (telemetry, admin, memory bank, A2A)
│   │   └── static/                    # Frontend HTML/CSS/JS dashboards
│   │       ├── index.html             # Operational Dashboard
│   │       ├── playground.html        # ADK & OKF Observability Playground
│   │       └── admin.html             # Executive IT Admin Console
│   ├── knowledge/                     # Operational Knowledge Framework (OKF) standard operating procedures
│   ├── skills/                        # Hierarchical micro-skills catalog for progressive disclosure
│   ├── sandbox/                       # Simulated local sandbox with fleet telemetry logs
│   │   ├── fleet_telemetry_dump.json  # 500+ records of warehouse AGV telemetry
│   │   └── diagnose_stress.py         # Resilient telemetry analysis script
│   ├── mock_data/                     # Reference fixtures and mock datasets
│   ├── scratch/                       # Administrative, testing, and deployment scripts
│   │   ├── deploy_public_app.sh       # One-click Cloud Build & Cloud Run deployment script
│   │   └── configure_memory_bank.py   # Vertex AI Memory Bank provisioning helper
│   ├── tests/                         # Unit, integration, and evaluation suites
│   │   ├── eval/                      # Golden datasets and custom LLM-as-a-judge metrics
│   │   └── integration/               # Multi-agent routing & sandbox execution tests
│   └── pyproject.toml                 # Modern python project specifications (uv managed)
```

---

## 🛠️ Prerequisites & Setup

### 1. System Requirements & CLI Tools
- **Python**: Version `3.10` to `3.12`
- **uv**: Fast Python package manager ([Install uv](https://docs.astral.sh/uv/getting-started/installation/))
- **gcloud CLI**: Google Cloud SDK ([Install gcloud](https://cloud.google.com/sdk/docs/install))
- **Docker** (optional for local container runs)

### 2. Configure GCP Authentication & Project
Authenticate with Google Cloud and set your target project:
```bash
gcloud auth login
gcloud auth application-default login
gcloud config set project <your-gcp-project-id>
```

---

## 💻 How to Run the UIs Locally

You can run the entire application locally with full access to all three web interfaces and the backend multi-agent orchestrator:

### Step 1: Install Dependencies
Navigate to `conveyor-orchestrator` and synchronize the dependencies using `uv`:
```bash
cd conveyor-orchestrator
uv sync
```

### Step 2: Set Environment Variables
Export your project ID and region (or create a `.env` file):
```bash
export GOOGLE_CLOUD_PROJECT="<your-gcp-project-id>"
export GOOGLE_CLOUD_LOCATION="us-central1"
```

### Step 3: Start the FastAPI Server
Launch the local Uvicorn server:
```bash
uv run uvicorn app.fast_api_app:app --host 0.0.0.0 --port 8080 --reload
```

### Step 4: Access the Web UIs
Open your browser and navigate to:
- **Operational Dashboard**: `http://localhost:8080/dashboard`
- **Agent Playground**: `http://localhost:8080/playground`
- **Executive Admin Console**: `http://localhost:8080/admin`
- **Presentation Deck**: `http://localhost:8080/static/demo_presentation.html`

---

## ☁️ How to Deploy & Replicate on Google Cloud Run

To replicate the complete solution in your Google Cloud environment as a fully managed, scalable Cloud Run deployment:

### Step 1: Enable Required Google Cloud APIs
Ensure the necessary APIs are activated in your Google Cloud project:
```bash
gcloud services enable \
  run.googleapis.com \
  cloudbuild.googleapis.com \
  artifactregistry.googleapis.com \
  aiplatform.googleapis.com \
  secretmanager.googleapis.com
```

### Step 2: Create Artifact Registry Repository (If Not Present)
```bash
gcloud artifacts repositories create agent-repo \
  --repository-format=docker \
  --location=us-central1 \
  --description="Docker repository for Conveyor Orchestrator"
```

### Step 3: Run the Automated Deployment Script
We provide a turnkey deployment script in `conveyor-orchestrator/scratch/deploy_public_app.sh`:
```bash
cd conveyor-orchestrator
bash scratch/deploy_public_app.sh
```

#### What this script does under the hood:
1. **Containerizes the Application**:
   Submits the source to Google Cloud Build using `conveyor-orchestrator/Dockerfile` to create a lean Python 3.12 container tagged in your Artifact Registry:
   ```bash
   gcloud builds submit \
     --tag "us-central1-docker.pkg.dev/<PROJECT_ID>/agent-repo/conveyor-orchestrator-app:latest" \
     --project="<PROJECT_ID>"
   ```
2. **Deploys to Cloud Run**:
   Deploys the container image with managed scaling, public ingress, and the required project context environment variables:
   ```bash
   gcloud run deploy conveyor-orchestrator-app \
     --image "us-central1-docker.pkg.dev/<PROJECT_ID>/agent-repo/conveyor-orchestrator-app:latest" \
     --platform managed \
     --region "us-central1" \
     --allow-unauthenticated \
     --service-account="geap-user-sa@<PROJECT_ID>.iam.gserviceaccount.com" \
     --set-env-vars="GOOGLE_CLOUD_PROJECT=<PROJECT_ID>,GOOGLE_CLOUD_LOCATION=us-central1" \
     --project="<PROJECT_ID>"
   ```

### Step 4: Access the Live Cloud Run URLs
Upon completion, Cloud Run will print the production URL (e.g. `https://conveyor-orchestrator-app-abcdef-uc.a.run.app`).

You can access all surfaces directly on the public URL:
- `https://<service-url>/dashboard`
- `https://<service-url>/playground`
- `https://<service-url>/admin`

---

## 🎯 Key Interactive Demo Scenarios

Once the app is running (locally or on Cloud Run), test these 4 key scenarios:

### Scenario 1: Telemetry Stress Audit in Secure Sandbox
- **Target Surface**: `/playground`
- **Action**: Click the preset prompt **`⚡ Aisle 4 Sandbox Telemetry Audit`** or send:
  > *"Audit our telemetry log in the sandbox, identify Aisle 4 hot-spots, and generate a stress profile."*
- **What Happens**:
  1. The orchestrator routes the query to `sandbox_diagnostic_agent`.
  2. The agent writes a custom analysis script using `write_file_to_sandbox`.
  3. The agent executes the script using `execute_python_in_sandbox` inside the sandbox CLI.
  4. It calculates the Thermal Stress Index (TSI) across 114 telemetry records and identifies 12 hot-spots (Top 10% TSI $\ge$ 2,946).
  5. It reads `aisle_4_stress_report.md` using `read_file_from_sandbox` and synthesizes an authoritative engineering report with Mean TSI: 1,081.35 and Max TSI: 4,145.92.

### Scenario 2: Progressive Disclosure & Night Shift Differential
- **Target Surface**: `/playground`
- **Action**: Click the preset prompt **`🌙 Night Shift Differential & Overtime`** or send:
  > *"What is the night shift differential and overtime policy for technicians under DOC-PAY-COMP-002?"*
- **What Happens**:
  1. Progressive disclosure activates via the OKF micro-skills hierarchy.
  2. `discover_okf_catalog` and `fetch_okf_document_section` dynamically retrieve only the relevant 4-line snippet of `DOC-PAY-COMP-002`.
  3. The token reactor demonstrates a **93%+ token reduction** (~122 input tokens vs 2,500+ unpruned tokens), driving the operation cost to under 1 paisa (₹0.0089).

### Scenario 3: Real-Time Conveyor Fault & CCTV Safety Audit
- **Target Surface**: `/dashboard`
- **Action**: Click **`Simulate Diverter Jam`** in the Fault Injector panel or ask:
  > *"Audit warehouse CCTV camera footage for posture safety and PPE compliance."*
- **What Happens**:
  1. The SVG monitor triggers an alert on the jam location and shows AGVs dynamically re-routing bypass traffic.
  2. The multimodal CCTV subagent evaluates posture angles, logs an ergonomic infraction, and checks safety vests/hard hats.

### Scenario 4: SecOps SGP Guardrail Denial
- **Target Surface**: `/dashboard` or `/playground`
- **Action**: Send:
  > *"Show me the camera feed for the employee break room."*
- **What Happens**:
  1. The SGP privacy self-governance filter intercepts the prompt before execution.
  2. It immediately refuses the action under corporate compliance rules and logs a refusal event.
  3. In `/admin` under **SecOps Threat Matrix**, the refusal is recorded under incident code `SEC-8821` with zero data leakage.

---

## 🧪 Testing & Validation Suites

The repository contains end-to-end integration and evaluation tests:

```bash
cd conveyor-orchestrator

# 1. Run unit tests
uv run pytest tests/unit

# 2. Run sandbox diagnostic routing integration test
uv run pytest tests/integration/test_sandbox_diagnostics.py

# 3. Run GEAP golden dataset evaluation
uv run pytest tests/eval/test_golden_dataset.py
```

---

## 📜 License & Acknowledgments
Built with **Google Cloud Agent Development Kit (ADK) 2.0**, **Gemini Enterprise Agent Platform (GEAP)**, and **Vertex AI Reasoning Engines**. Released under the **MIT License**.
