# Stackbox Conveyor Orchestrator (GEAP & ADK 2.0 Agent)

An advanced multi-agent warehouse orchestration system designed to automate critical conveyor belt fault resolution, fleet telemetry tracking, and multimodal safety auditing. Built on the **Gemini Enterprise Agent Platform (GEAP)** using the **Agent Development Kit (ADK) 2.0** and Vertex AI Reasoning Engines.

---

## 🌟 Key Capabilities

1. **Intelligent Workflow Routing**: Operates as a deterministic Directed Acyclic Graph (DAG) using ADK 2.0 Workflow APIs to ingest, parse, and route warehouse telemetry based on severity (Critical vs. Recoverable).
2. **Multi-Agent RAG & SOP Search**: Seamlessly retrieves lockout-tagout (LOTO), conveyor maintenance, and physical compliance safety SOPs from a Google Cloud Discovery Engine vector datastore.
3. **AGV Fleet Telemetry & Battery Monitoring**: Integrates a custom **Model Context Protocol (MCP)** server interface providing real-time telemetry on automated guided vehicles (battery, location, active tasks) to coordinate bypass routing.
4. **Multimodal CCTV Safety Auditing**: Connects Gemini 1.5 Pro multimodal capabilities to inspect safety posture, verify personal protective equipment (PPE), and log safety infractions.
5. **Vertex AI Memory Bank**: Implements cross-session operator profile recollection so that the orchestrator remembers technician identities, certifications, and active auditing goals across separate runs.
6. **Custom LLM-as-a-Judge Evaluation**: Fully integrated with GEAP console metrics supporting task success, tool-calling hygiene, and hallucination checks.

---

## 📁 Repository Layout

```text
stackbox-conveyer-demo/
├── README.md                          # Main repository guide (This file)
├── DESIGN_SPEC.md                     # Technical architecture, DAG specs, and tool definitions
├── conveyor-orchestrator/
│   ├── app/                           # Core Agent Source
│   │   ├── agent.py                   # Main workflow definition, agent graph routing, and tools
│   │   ├── agent_runtime_app.py       # Reasoning Engine entrypoint for Vertex AI deployment
│   │   ├── fast_api_app.py            # Local FastAPI server
│   │   ├── mcp_server.py              # Fleet Telemetry MCP Server (stdio-based)
│   │   ├── tools.py                   # Custom tool wrappers (WMS, runbooks, bypass dispatches)
│   │   └── static/                    # Frontend files
│   │       └── index.html             # Web dashboard, SVG flowchart, and CCTV visualization
│   ├── tests/                         # Test suites
│   │   ├── unit/                      # Mocked logic and graph validation tests
│   │   └── integration/               # Multi-agent routing and safety RAG validation tests
│   ├── scratch/                       # Helpful administration & cloud helper scripts
│   │   ├── configure_memory_bank.py   # Script to configure and bind Vertex AI Memory Bank
│   │   ├── create_mock_datastore.py   # RAG data source generation script
│   │   └── test_memory_deployed.py    # Deployed multi-session memory validator
│   ├── toolspec.json                  # Standalone MCP telemetry tool definitions
│   └── pyproject.toml                 # Modern python project specifications (uv managed)
```

---

## 🛠️ Prerequisites & Local Setup

To run, test, and deploy this project in your own GCP sandbox environment, you will need:

### 1. System Requirements & CLI Tools
- **Python**: Version `3.10` to `3.11`
- **uv**: Fast python package manager. [Install uv](https://docs.astral.sh/uv/getting-started/installation/)
- **gcloud CLI**: For Google Cloud authentication. [Install Google Cloud SDK](https://cloud.google.com/sdk/docs/install)
- **google-agents-cli**: GEAP development client tool. Install globally using:
  ```bash
  uv tool install google-agents-cli
  ```

### 2. Configure GCP Authentication
Log in to your Google Cloud Account and set up Application Default Credentials (ADC):
```bash
gcloud auth login
gcloud auth application-default login
gcloud config set project <your-gcp-project-id>
```

---

## 🚀 How to Run the App Locally

### Step 1: Install Dependencies
Navigate to the project subdirectory and trigger installation of the virtual environment and locked dependencies:
```bash
cd conveyor-orchestrator
agents-cli install
```

### Step 2: Launch the Agent Interactive Playground
Start the local GEAP agent emulator. This launches a development server with live reload and an interactive chat playground:
```bash
agents-cli playground
```
- Open `http://localhost:8000` (or the console output link) to chat with the agent locally.

### Step 3: Run the Interactive Web Dashboard
The project includes a custom real-time SVG monitor dashboard tracking AGV paths and CCTV posture analysis.
To view it:
1. Run the local development server:
   ```bash
   uv run uvicorn app.fast_api_app:app --reload --port 8080
   ```
2. Open `http://localhost:8080/static/index.html` in your web browser.

---

## 🧪 Testing the Agent

The repository comes with pre-configured unit and integration test suites utilizing mock data to prevent real API costs during localized loops.

To execute tests:
```bash
# Run unit tests
uv run pytest tests/unit

# Run full integration tests (routes, RAG searches, and tool validations)
uv run pytest tests/integration
```

---

## ☁️ Deploying to Google Cloud (GEAP)

When you are ready to deploy your orchestrator as a remote cloud Reasoning Engine in GEAP:

### Step 1: Create a Google Cloud Secret for Gemini
The agent requires a secret key stored in **Secret Manager** to run calls remotely:
```bash
# Enable the Secret Manager API
gcloud services enable secretmanager.googleapis.com

# Create the secret for your Gemini API Key
gcloud secrets create GEMINI_API_KEY --data-file=- <<< "AIzaSy..."
```

### Step 2: Deploy the Agent
Run the standard deployment command to package your code and deploy it to Vertex AI Agent Runtime:
```bash
agents-cli deploy
```
This builds your container, registers your runtime app under Vertex AI, and outputs a deployed **Reasoning Engine ID** (e.g. `projects/12345/locations/us-central1/reasoningEngines/8594036320127418368`).

---

## 🧠 Optional: Binding Vertex AI Memory Bank

To configure persistent, cross-session operator profile recollection on your deployed engine:

1. Update the target parameters at the top of the helper script `conveyor-orchestrator/scratch/configure_memory_bank.py`:
   - `PROJECT_ID`: Your GCP project ID.
   - `RE_ID`: The Reasoning Engine ID outputted during deployment.
2. Execute the configuration script:
   ```bash
   uv run scratch/configure_memory_bank.py
   ```
This activates the context spec on Vertex AI. To test, open the GEAP Playground console, introduce yourself (e.g. *"Hello, I am operator Dave auditing LOTO today"*), reset the session, and query *"What am I doing today and what is my name?"* to see the cross-session recall in action.

---

## 📊 Optional: Setting Up Custom Evaluation Metrics

In the **GEAP Console -> Optimize -> Evaluation -> Custom Metrics** tab, you can add custom evaluation metrics using these optimized settings:

| Metric Name | Critique Prompt Purpose | Python Parse Output Schema |
| :--- | :--- | :--- |
| **`multi_turn_task_success`** | Evaluates whether the operator's end-goal is successfully answered. | `{"score": float, "explanation": str}` |
| **`multi_turn_tool_use_quality`** | Inspects parameter correctness on safety tools (`list_available_agvs`, etc.). | `{"score": float, "explanation": str}` |
| **`hallucination`** | Ensures safety protocols match reference RAG contexts exactly. | `{"score": float, "explanation": str}` |

*Detailed markdown prompts and parsing logic scripts can be found inside your custom metrics documentation logs.*

---

## 📜 License
This project is released under the **MIT License**. Check out `DESIGN_SPEC.md` for specific architectural nodes and algorithmic specs.
