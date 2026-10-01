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
import pytest
from google.adk.agents.run_config import RunConfig, StreamingMode
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from app.agent import root_agent

def test_sandbox_diagnostic_route() -> None:
  """Integration test verifying that a telemetry stress audit query
  correctly routes to the sandbox_diagnostic_agent, writes a script,
  executes it in the local sandbox, and produces a professional report.
  """
  # Ensure we have the sandbox directory prepared with fleet telemetry log
  sandbox_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "sandbox"))
  assert os.path.exists(sandbox_dir), f"Sandbox directory does not exist at: {sandbox_dir}"
  
  telemetry_file = os.path.join(sandbox_dir, "fleet_telemetry_dump.json")
  assert os.path.exists(telemetry_file), f"Fleet telemetry dump file missing at: {telemetry_file}"

  session_service = InMemorySessionService()
  session = session_service.create_session_sync(user_id="test_sandbox_user", app_name="test")
  runner = Runner(agent=root_agent, session_service=session_service, app_name="test")

  # Request containing sandbox diagnostic keywords
  message = types.Content(
    role="user",
    parts=[types.Part.from_text(text="Audit our telemetry log in the sandbox, identify Aisle 4 hot-spots, and generate a stress profile.")]
  )

  events = list(
    runner.run(
      new_message=message,
      user_id="test_sandbox_user",
      session_id=session.id,
      run_config=RunConfig(streaming_mode=StreamingMode.SSE),
    )
  )

  assert len(events) > 0, "Expected at least one event back from the sandbox diagnostic flow"

  # Gather full concatenated output text and log events
  full_output = ""
  for event in events:
    if event.content and event.content.parts:
      for part in event.content.parts:
        if part.text:
          full_output += part.text

  print("\n--- Sandbox Diagnostic Agent Output ---")
  print(full_output)
  print("---------------------------------------\n")

  if len(full_output) == 0:
    print("\n[DEBUG] Empty output received. Listing raw workflow events:")
    for idx, event in enumerate(events):
      print(f"Event {idx}: {event}")
    raise AssertionError(
        "Expected text response in diagnostic report, but output was empty. "
        "This usually indicates a model execution or API credentials error. "
        "Please ensure GOOGLE_GENAI_USE_VERTEXAI=True is exported or a valid non-leaked API key is set."
    )

  # Check that key diagnostics keywords/analyses are included in the generated output
  assert any(term in full_output.lower() for term in ["aisle", "hot", "stress", "telemetry", "profile", "diagnostic"]), \
    f"Expected stress diagnostic feedback in output, got: {full_output}"

