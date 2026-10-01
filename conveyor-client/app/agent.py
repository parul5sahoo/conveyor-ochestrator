# ruff: noqa
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

import datetime
from zoneinfo import ZoneInfo

from google.adk.agents import Agent
from google.adk.apps import App
from google.adk.models import Gemini
from google.adk.tools import LongRunningFunctionTool
from google.genai import types
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent

import os
import google.auth

_, project_id = google.auth.default()
os.environ["GOOGLE_CLOUD_PROJECT"] = project_id
os.environ["GOOGLE_CLOUD_LOCATION"] = "global"
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "True"


def get_weather(query: str) -> str:
    """Simulates a web search. Use it get information on weather.

    Args:
        query: A string containing the location to get weather information for.

    Returns:
        A string with the simulated weather information for the queried location.
    """
    if "sf" in query.lower() or "san francisco" in query.lower():
        return "It's 60 degrees and foggy."
    return "It's 90 degrees and sunny."


def get_current_time(query: str) -> str:
    """Simulates getting the current time for a city.

    Args:
        city: The name of the city to get the current time for.

    Returns:
        A string with the current time information.
    """
    if "sf" in query.lower() or "san francisco" in query.lower():
        tz_identifier = "America/Los_Angeles"
    else:
        return f"Sorry, I don't have timezone information for query: {query}."

    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    return f"The current time for query {query} is {now.strftime('%Y-%m-%d %H:%M:%S %Z%z')}"


def request_user_input(message: str) -> dict:
    """Request additional input from the user.

    Use this tool when you need more information from the user to complete a task.
    Calling this tool will pause execution until the user responds.

    Args:
        message: The question or clarification request to show the user.
    """
    return {"status": "pending", "message": message}


target_resource_name = "projects/526827734705/locations/us-central1/reasoningEngines/8594036320127418368"
target_a2a_url = f"https://us-central1-aiplatform.googleapis.com/v1beta1/{target_resource_name}/a2a"

conveyor_orchestrator_agent = RemoteA2aAgent(
    name="conveyor_orchestrator_agent",
    description=(
        "An advanced conveyor and logistics orchestrator that handles warehouse telemetry ingestion, "
        "mechanical runbook lookup, WMS stock check, and AGV fleet dispatch routing."
    ),
    agent_card=f"{target_a2a_url}/v1/card",
)

root_agent = Agent(
    name="conveyor_client_agent",
    model=Gemini(
        model="gemini-flash-latest",
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    description="A client agent that delegates logistics and conveyor operations to the orchestrator via A2A protocol.",
    instruction=(
        "You are a warehouse coordinator assistant. You delegate complex conveyor and logistics operations "
        "to the conveyor_orchestrator_agent. When a user asks about conveyor failures, stock status, or AGV dispatches, "
        "delegate the query to the conveyor_orchestrator_agent sub-agent."
    ),
    sub_agents=[conveyor_orchestrator_agent],
    tools=[
        get_weather,
        get_current_time,
        LongRunningFunctionTool(func=request_user_input),
    ],
)

app = App(
    root_agent=root_agent,
    name="app",
)
