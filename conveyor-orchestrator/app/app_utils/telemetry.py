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

import logging
import os


def setup_telemetry() -> str | None:
    """Configure OpenTelemetry and GenAI telemetry with span and event message content."""
    os.environ.setdefault("GOOGLE_CLOUD_AGENT_ENGINE_ENABLE_TELEMETRY", "true")
    os.environ["ADK_CAPTURE_MESSAGE_CONTENT_IN_SPANS"] = "true"
    os.environ["OTEL_INSTRUMENTATION_GENAI_CAPTURE_MESSAGE_CONTENT"] = "SPAN_AND_EVENT"
    os.environ["OTEL_INSTRUMENTATION_GENAI_EMIT_EVENT"] = "true"
    os.environ.setdefault("OTEL_SEMCONV_STABILITY_OPT_IN", "gen_ai_latest_experimental")

    commit_sha = os.environ.get("COMMIT_SHA", "dev")
    os.environ.setdefault(
        "OTEL_RESOURCE_ATTRIBUTES",
        f"service.name=cymbal-warehouse-automation,service.namespace=conveyor-orchestrator,service.version={commit_sha}",
    )

    # Disable external GCS completion upload hook to avoid gcsfs 401 authentication errors
    os.environ.pop("OTEL_INSTRUMENTATION_GENAI_COMPLETION_HOOK", None)
    os.environ.pop("OTEL_INSTRUMENTATION_GENAI_UPLOAD_BASE_PATH", None)

    bucket = os.environ.get("LOGS_BUCKET_NAME", "ce-testing-465204-cctv-media")
    logging.info(
        "Prompt-response logging enabled in SPAN_AND_EVENT mode with span content enabled for Agent Platform evaluations."
    )
    return bucket

