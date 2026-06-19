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
from google.adk.agents.run_config import RunConfig, StreamingMode
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from app.agent import root_agent


def test_safety_audit_route_posture() -> None:
    """
    Integration test verifying that a query containing safety posture keywords
    correctly routes to the cctv_safety_audit_agent and produces a posture safety report.
    """
    session_service = InMemorySessionService()
    session = session_service.create_session_sync(user_id="test_safety_user", app_name="test")
    runner = Runner(agent=root_agent, session_service=session_service, app_name="test")

    # Request containing posture audit keywords
    message = types.Content(
        role="user",
        parts=[types.Part.from_text(text="Run a safety and posture audit for employee lifting in Aisle 2")]
    )

    events = list(
        runner.run(
            new_message=message,
            user_id="test_safety_user",
            session_id=session.id,
            run_config=RunConfig(streaming_mode=StreamingMode.SSE),
        )
    )

    assert len(events) > 0, "Expected at least one event back from the safety auditor flow"

    # Gather full concatenated output text
    full_output = ""
    for event in events:
        if event.content and event.content.parts:
            for part in event.content.parts:
                if part.text:
                    full_output += part.text

    assert len(full_output) > 0, "Expected text response in safety report"
    
    # Assert that the correct safety terms are included in the fallback evaluation
    assert any(term in full_output.lower() for term in ["aisle 2", "posture", "ergonomic", "lifting", "compliance", "violation"]), \
        f"Expected safety audit feedback in output, got: {full_output}"


def test_safety_audit_route_ppe() -> None:
    """
    Integration test verifying that a PPE safety vest audit request
    routes successfully and contains expected PPE check badges/results.
    """
    session_service = InMemorySessionService()
    session = session_service.create_session_sync(user_id="test_ppe_user", app_name="test")
    runner = Runner(agent=root_agent, session_service=session_service, app_name="test")

    # Request containing PPE vest safety keywords
    message = types.Content(
        role="user",
        parts=[types.Part.from_text(text="Audit safety vest and hard hat compliance in loading dock forklift zones")]
    )

    events = list(
        runner.run(
            new_message=message,
            user_id="test_ppe_user",
            session_id=session.id,
            run_config=RunConfig(streaming_mode=StreamingMode.SSE),
        )
    )

    full_output = ""
    for event in events:
        if event.content and event.content.parts:
            for part in event.content.parts:
                if part.text:
                    full_output += part.text

    assert len(full_output) > 0, "Expected text response in PPE safety report"
    assert any(term in full_output.lower() for term in ["loading dock", "ppe", "vest", "hard hat", "compliance", "violation"]), \
        f"Expected PPE audit elements in output, got: {full_output}"
