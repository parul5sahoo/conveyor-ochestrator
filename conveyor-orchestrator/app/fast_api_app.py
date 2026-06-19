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
import os
import logging as standard_logging

import google.auth
from fastapi import FastAPI
from google.adk.cli.fast_api import get_fast_api_app
from google.cloud import logging as google_cloud_logging

from app.app_utils.telemetry import setup_telemetry
from app.app_utils.typing import Feedback

setup_telemetry()

# Configure standard fallback logger
std_logger = standard_logging.getLogger(__name__)
use_gcp_logging = False
logger = std_logger

try:
    if os.getenv("INTEGRATION_TEST") == "TRUE":
        raise google.auth.exceptions.DefaultCredentialsError("Using fallback logger for integration tests.")
    _, project_id = google.auth.default()
    logging_client = google_cloud_logging.Client()
    logger = logging_client.logger(__name__)
    use_gcp_logging = True
except Exception as e:
    std_logger.warning(f"GCP Cloud Logging client initialization failed or bypassed: {e}. Falling back to standard logger.")
allow_origins = (
    os.getenv("ALLOW_ORIGINS", "").split(",") if os.getenv("ALLOW_ORIGINS") else None
)

# Artifact bucket for ADK (created by Terraform, passed via env var)
logs_bucket_name = os.environ.get("LOGS_BUCKET_NAME")

# Create a dedicated agent isolation directory to prevent ADK from scanning non-agent folders like tests/ or artifacts/
_app_dir = os.path.dirname(os.path.abspath(__file__))
AGENT_DIR = _app_dir
# In-memory session configuration - no persistent storage
session_service_uri = None

artifact_service_uri = f"gs://{logs_bucket_name}" if logs_bucket_name else None

# Disable cloud trace exporter for local environments to prevent opentelemetry dependency crashes
is_integration_test = os.getenv("INTEGRATION_TEST") == "TRUE"
otel_to_cloud = False

app: FastAPI = get_fast_api_app(
    agents_dir=AGENT_DIR,
    web=True,
    artifact_service_uri=artifact_service_uri,
    allow_origins=allow_origins,
    session_service_uri=session_service_uri,
    otel_to_cloud=otel_to_cloud,
)
app.title = "conveyor-orchestrator"
app.description = "API for interacting with the Agent conveyor-orchestrator"


@app.post("/feedback")
def collect_feedback(feedback: Feedback) -> dict[str, str]:
    """Collect and log feedback.

    Args:
        feedback: The feedback data to log

    Returns:
        Success message
    """
    if use_gcp_logging:
        try:
            logger.log_struct(feedback.model_dump(), severity="INFO")
        except Exception as e:
            std_logger.warning(f"Failed to log struct to GCP Logging: {e}. Falling back to standard logging.")
            std_logger.info(f"Feedback: {feedback.model_dump()}")
    else:
        std_logger.info(f"Feedback: {feedback.model_dump()}")
    return {"status": "success"}


from fastapi.responses import HTMLResponse

@app.get("/dashboard", response_class=HTMLResponse)
def get_dashboard():
    """Serve the warehouse orchestration dashboard."""
    static_file_path = os.path.join(os.path.dirname(__file__), "static", "index.html")
    if os.path.exists(static_file_path):
        with open(static_file_path, "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>StackBox Conveyor Orchestrator</h1><p>Dashboard static file not found.</p>"


# Main execution
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8555)
