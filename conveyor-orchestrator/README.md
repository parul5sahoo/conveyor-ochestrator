# Conveyor Orchestrator (GEAP & ADK 2.0 Agent)

Multi-agent warehouse orchestration backend, local sandbox diagnostic coordinator, and operational control surface.

## Web Dashboards & UI Endpoints

When running locally or deployed on Cloud Run, the application serves:

- **`/dashboard`**: Real-time warehouse conveyor belt SVG monitor, dynamic AGV telemetry tracking, CCTV posture and PPE inspection feed, live fault injector, and interactive incident dispatch console.
- **`/playground`**: Enterprise testing ground with pre-configured demonstration prompts, hierarchical skill progressive disclosure (Root Suites $\to$ Disciplines $\to$ Micro-Skills), real-time token reduction and cost reactor (~122 tokens in, ₹0.0089/op), and direct telemetry sandbox audit.
- **`/admin`**: Executive & IT Admin Console with Latency & Performance HUD (P50 284ms, sub-tool profiling), Sessions & Memory Banks, SecOps Threat Matrix (SAIF/SGP denial `SEC-8821`), and Hillclimbing Scorecards ($3.70 \to 4.30$).
- **`/api/agent_metadata`**: JSON telemetry endpoint exposing active agent graphs, models, and reasoning engines.

---

## Quick Start (Local Run)

1. **Install dependencies**:
   ```bash
   uv sync
   ```

2. **Run the FastAPI server**:
   ```bash
   uv run uvicorn app.fast_api_app:app --host 0.0.0.0 --port 8080 --reload
   ```

3. **Open the browser**:
   Navigate to `http://localhost:8080/dashboard` or `http://localhost:8080/playground`.

---

## Cloud Run Deployment

To build and deploy the container image to Google Cloud Run:

```bash
bash scratch/deploy_public_app.sh
```

This automates:
1. Building the Docker image via Google Cloud Build (`gcloud builds submit`).
2. Deploying to Cloud Run with public unauthenticated ingress on port 8080.
3. Injecting `GOOGLE_CLOUD_PROJECT` and `GOOGLE_CLOUD_LOCATION`.

Refer to the main [Repository README](../README.md) for full architectural documentation, evaluation guides, and interactive demo scenarios.
