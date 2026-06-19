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
from pydantic import BaseModel

# Mock google.auth.default for integration tests to prevent loading expired default credentials
if os.environ.get("INTEGRATION_TEST") == "TRUE":
    try:
        import google.auth
        import google.auth.exceptions
        def mock_default(*args, **kwargs):
            raise google.auth.exceptions.DefaultCredentialsError("Mocked default credentials error for integration test.")
        google.auth.default = mock_default
    except ImportError:
        pass

from google.adk.workflow import Workflow, node, JoinNode, START, RetryConfig, Edge
from google.adk.agents import LlmAgent
from google.adk.agents.callback_context import CallbackContext
from google.adk.tools.preload_memory_tool import preload_memory_tool
from google.adk.events.event import Event
from google.adk.agents.context import Context
from google.adk.apps import App
from google.adk.models import Gemini
from google.genai import types

# Patch the pre-GA Workflow class to satisfy Vertex AI SDK evaluation requirements
if not hasattr(Workflow, "tools"):
    Workflow.tools = property(lambda self: [])

# Monkeypatch google-adk Session Service to support slash-containing session IDs from Gemini Enterprise
try:
    import re
    import google.adk.sessions.vertex_ai_session_service as sass
    
    # 1. Patch validation pattern to allow path slashes
    sass._SESSION_ID_PATTERN = re.compile(r'^[A-Za-z0-9_\-\/]+$')
    
    # 2. Wrap get_session to extract short ID if full path is passed
    original_get_session = sass.VertexAiSessionService.get_session
    async def patched_get_session(self, *, app_name: str, user_id: str, session_id: str, config=None):
        if session_id and "/" in session_id:
            session_id = session_id.split("/")[-1]
        return await original_get_session(self, app_name=app_name, user_id=user_id, session_id=session_id, config=config)
    sass.VertexAiSessionService.get_session = patched_get_session

    # 3. Wrap delete_session to extract short ID
    original_delete_session = sass.VertexAiSessionService.delete_session
    async def patched_delete_session(self, *, app_name: str, user_id: str, session_id: str):
        if session_id and "/" in session_id:
            session_id = session_id.split("/")[-1]
        return await original_delete_session(self, app_name=app_name, user_id=user_id, session_id=session_id)
    sass.VertexAiSessionService.delete_session = patched_delete_session

    # 4. Wrap create_session to extract short ID
    original_create_session = sass.VertexAiSessionService.create_session
    async def patched_create_session(self, *, app_name: str, user_id: str, state=None, session_id=None, **kwargs):
        if session_id and "/" in session_id:
            session_id = session_id.split("/")[-1]
        return await original_create_session(self, app_name=app_name, user_id=user_id, state=state, session_id=session_id, **kwargs)
    sass.VertexAiSessionService.create_session = patched_create_session

except Exception as e:
    import sys
    print(f"Failed to monkeypatch Session Service: {e}", file=sys.stderr)



# Import the tools from our tools module
from app.tools import (
    check_wms_stock_tool,
    query_runbooks_tool,
    dispatch_agv_tool,
    check_wms_stock,
    query_runbooks,
)

# Resilient environment setup supporting Google Cloud and API Keys
# Detect if running in a cloud environment (GCP / Vertex AI Reasoning Engine / Cloud Run)
# If INTEGRATION_TEST is TRUE, we force is_cloud to False to ensure local execution with API Key.
is_cloud = bool(
    (
        os.environ.get("VERTEX_AI_RE_ENV") or
        os.environ.get("AIP_PROJECT_NUMBER") or
        os.environ.get("REASONING_ENGINE_ID") or
        os.environ.get("K_SERVICE") or
        os.environ.get("GOOGLE_GENAI_USE_VERTEXAI", "").lower() in ("true", "1")
    ) and os.environ.get("INTEGRATION_TEST") != "TRUE"
)

if is_cloud:
    # In cloud environments, use Vertex AI and strictly remove API keys 
    # to avoid interfering with Application Default Credentials (ADC) OAuth2.
    use_vertexai = True
    os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "True"
    os.environ.pop("GOOGLE_API_KEY", None)
    os.environ.pop("GEMINI_API_KEY", None)
    
    os.environ["GOOGLE_CLOUD_LOCATION"] = os.environ.get("GOOGLE_CLOUD_LOCATION", "us-central1")
    model_instance = Gemini(
        model="gemini-2.5-flash",
        retry_options=types.HttpRetryOptions(attempts=3),
    )
else:
    # Local dev mode / AI Studio fallback
    use_vertexai = False
    google_api_key = os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")
    if not google_api_key:
        raise ValueError("Neither GOOGLE_API_KEY nor GEMINI_API_KEY environment variable is set. Please set your API key locally before running the playground.")
    
    os.environ["GOOGLE_API_KEY"] = google_api_key
    os.environ["GEMINI_API_KEY"] = google_api_key
    os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "False"
    
    model_instance = Gemini(
        model="gemini-2.5-flash",
        retry_options=types.HttpRetryOptions(attempts=3),
    )


# Define Schemas for structured communication
class TelemetryData(BaseModel):
    conveyor_id: str
    error_code: str
    sku: str
    status: str


class DispatcherOutput(BaseModel):
    conveyor_status: str
    repair_instructions: str
    stock_status: str
    bypass_status: str
    final_report: str


# Node A: TelemetryIngest
@node
def telemetry_ingest(node_input: types.Content) -> Event:
    """Parses raw conveyor telemetry strings and routes based on failure severity.

    Args:
        node_input: The raw telemetry content passed from the START node.

    Returns:
        An Event containing the parsed telemetry dict and routing target ('CRITICAL' or 'RECOVERABLE').
    """
    # Extract text from types.Content
    text_content = ""
    if hasattr(node_input, "parts") and node_input.parts:
        text_content = node_input.parts[0].text
    else:
        text_content = str(node_input)

    # Determine if this is structured telemetry or general natural language Q&A
    text_lower = text_content.lower()
    
    safety_keywords = ["cctv", "posture", "ppe", "safety vest", "hygiene", "audit", "lifting", "loto", "hard hat", "lockout"]
    if any(keyword in text_lower for keyword in safety_keywords):
        return Event(
            output={"query": text_content},
            route="SAFETY_AUDIT",
            state={"query": text_content}
        )

    is_telemetry = ("conveyor_id" in text_lower or "sku" in text_lower or "error_code" in text_lower)

    if not is_telemetry:
        # Route general conversational questions directly to the conversational safety officer
        return Event(
            output={"query": text_content},
            route="CONVERSATIONAL",
            state={"query": text_content}
        )

    # Parse key-value pairs (e.g., "conveyor_id: CV-09, error_code: Error 4042, sku: SKU-991, status: CRITICAL")
    parsed_data = {}
    for item in text_content.split(","):
        if ":" in item:
            key, val = item.split(":", 1)
            parsed_data[key.strip().lower()] = val.strip()

    conveyor_id = parsed_data.get("conveyor_id", "CV-UNKNOWN")
    error_code = parsed_data.get("error_code", "Error-Unknown")
    sku = parsed_data.get("sku", "SKU-UNKNOWN")
    raw_status = parsed_data.get("status", "RECOVERABLE").upper()

    # Determine deterministic route
    if "CRITICAL" in raw_status or "CRITICAL" in text_content.upper():
        route = "CRITICAL"
    else:
        route = "RECOVERABLE"

    telemetry_output = {
        "conveyor_id": conveyor_id,
        "error_code": error_code,
        "sku": sku,
        "status": route,
    }

    return Event(
        output=telemetry_output,
        route=route,
        state={"telemetry_data": telemetry_output},
    )


# Node B: RunbookLookup with Jittered Retry
@node(
    retry_config=RetryConfig(
        max_attempts=3, initial_delay=1.0, backoff_factor=2.0, jitter=0.5
    )
)
def runbook_lookup(node_input: dict) -> dict:
    """Invokes Vector Search to retrieve mechanical repair runbooks.

    Args:
        node_input: The parsed telemetry dictionary from TelemetryIngest.

    Returns:
        A dictionary containing the matched runbook instructions and metadata.
    """
    error_code = node_input.get("error_code", "Error-Unknown")
    return query_runbooks(error_code)


# Node C: WMSAccess with Jittered Retry
@node(
    retry_config=RetryConfig(
        max_attempts=3, initial_delay=1.0, backoff_factor=2.0, jitter=0.5
    )
)
def wms_access(node_input: dict) -> dict:
    """Queries WMS to verify inventory availability and blocking condition.

    Args:
        node_input: The parsed telemetry dictionary from TelemetryIngest.

    Returns:
        A dictionary containing stock availability and physical location.
    """
    sku = node_input.get("sku", "SKU-UNKNOWN")
    return check_wms_stock(sku)


# Node: Formatter for Joined Parallel Paths
@node
def format_dispatcher_input(node_input: dict, ctx: Context) -> dict:
    """Formats the joined parallel outputs into a clear structured dict for the Dispatcher LLM.

    Args:
        node_input: The dictionary containing the joined runbook search and stock lookups.
        ctx: The Workflow context containing global telemetry data in state.

    Returns:
        A consolidated dictionary ready for LLM consumption.
    """
    runbook_data = node_input.get("runbook_lookup", {})
    wms_data = node_input.get("wms_access", {})
    telemetry_data = ctx.state.get("telemetry_data", {})

    return {
        "conveyor_id": telemetry_data.get("conveyor_id", "Unknown"),
        "error_code": telemetry_data.get("error_code", "Unknown"),
        "sku": telemetry_data.get("sku", "Unknown"),
        "repair_instructions": runbook_data.get(
            "instructions", "No instructions found."
        ),
        "stock_status": wms_data.get("status", "UNKNOWN"),
        "stock_aisle": wms_data.get("location", "Unknown"),
        "stock_quantity": wms_data.get("quantity", 0),
    }


# Node D: Dispatcher Agent with RAG / Vertex AI RAG integration
from google.adk.tools import FunctionTool
from google.adk.tools.retrieval.vertex_ai_rag_retrieval import VertexAiRagRetrieval

# Programmatic RAG search for both local development and cloud execution so that tool calls are visible in Playground UI
def vertex_ai_rag_retrieval(query: str) -> str:
    """Query the internal safety guidelines, SOPs, and compliance runbooks.

    Args:
        query: The search terms or keywords to query the warehouse safety/SOP database.

    Returns:
        A string with matching guidelines and instructions.
    """
    import os
    corpus_id_env = os.environ.get("VERTEX_AI_RAG_CORPUS_ID", "projects/ce-testing-465204/locations/us-central1/ragCorpora/2104922652400418816")
    
    # If corpus_id is set or present in environment, query Vertex RAG programmatically
    if corpus_id_env:
        try:
            import vertexai
            from vertexai.preview import rag
            
            # Parse project and location from corpus_id
            parts = corpus_id_env.split('/')
            if len(parts) >= 6:
                project = parts[1]
                location = parts[3]
            else:
                project = "ce-testing-465204"
                location = "us-central1"
            
            vertexai.init(project=project, location=location)
            response = rag.retrieval_query(
                text=query,
                rag_corpora=[corpus_id_env],
                similarity_top_k=3,
            )
            
            if response.contexts and response.contexts.contexts:
                results_text = []
                for ctx in response.contexts.contexts:
                    results_text.append(f"- {ctx.text} (Source: {ctx.source_uri or 'Internal'})")
                return "\n\n".join(results_text)
            else:
                return "No matching compliance guidelines or SOP documents found in the database."
        except Exception as e:
            import sys
            print(f"Programmatic RAG search failed: {e}", file=sys.stderr)
            # Fall through to local mock text so developers can continue testing seamlessly
    
    # Local mock fallback when RAG Engine is not available or queries fail
    query_cleaned = query.lower()
    if "cv-11" in query_cleaned or "4042" in query_cleaned:
        return (
            "[SOP-4042 Compliance Runbook]\n"
            "Before calibrating sensors or resetting C-3 controllers on Conveyor CV-11:\n"
            "1. Confirm clear mechanical pathway to prevent pinch injuries.\n"
            "2. Ensure bypass mechanisms (e.g. AGV dispatches) are active to route pending load away.\n"
            "3. Operational Safety limit: Wear standard high-visibility PPE."
        )
    return (
        "[General Warehouse SOP Section 4.2]\n"
        "Conveyor system servicing requires a designated mechanical lockout-tagout (LOTO) "
        "and active dispatching of backup automated guided vehicles (AGVs) to bypass logistics bottlenecks."
    )

search_tool = FunctionTool(func=vertex_ai_rag_retrieval)


# Dynamic, thread-safe, on-demand connection runner supporting remote SSE and local fallback
def run_mcp_command_sync(tool_name: str, arguments: dict) -> str:
    """Connect to the MCP server, invoke a tool, and return the result.
    
    This function implements a resilient fallback ladder:
    1. If running on the cloud, try discovering the server in Google Cloud API Registry
       and executing the tool using ADK's native platform-mediated tracer.
    2. Fall back to direct remote SSE client session if registry fails or local.
    3. Fall back to spawning a local stdio MCP subprocess if remote fails.
    """
    import sys
    import asyncio
    import threading
    from mcp import ClientSession
    
    mcp_url = os.environ.get("MCP_SERVER_URL", "https://conveyor.agent.parulsahoo.altostrat.com/mcp")
    
    async def _call():
        # 1. Cloud-native API Registry discovery and trace context propagation
        if is_cloud:
            try:
                from google.adk.integrations.api_registry import ApiRegistry
                from opentelemetry import propagate
                
                project_id = os.environ.get("GOOGLE_CLOUD_PROJECT", "ce-testing-465204")
                location = os.environ.get("GOOGLE_CLOUD_LOCATION", "us-central1")
                
                # Fetch registered servers
                reg = ApiRegistry(api_registry_project_id=project_id, location=location)
                
                # Robustly find server resource ending with '/conveyor-orchestrator'
                target_server = None
                for name in reg._mcp_servers:
                    if name.endswith("/conveyor-orchestrator"):
                        target_server = name
                        break
                        
                if not target_server:
                    raise ValueError(f"Conveyor-orchestrator not found in API Registry under project {project_id}.")
                
                toolset = reg.get_toolset(target_server)
                
                # Inject OpenTelemetry trace context for distributed tracing across services
                trace_carrier = {}
                propagate.get_global_textmap().inject(carrier=trace_carrier)
                meta_trace_context = trace_carrier if trace_carrier else None
                
                # Create session and call tool natively using ADK's streamable http client
                session = await toolset._mcp_session_manager.create_session()
                response = await session.call_tool(
                    tool_name,
                    arguments=arguments,
                    meta=meta_trace_context,
                )
                
                text_content = ""
                for content in response.content:
                    if hasattr(content, "text"):
                        text_content += content.text
                return text_content
                
            except Exception as cloud_err:
                import sys
                print(f"Cloud API Registry trace-mediated call failed: {cloud_err}. Falling back to raw SSE client...", file=sys.stderr)
        
        # 2. Raw SSE Client (Direct remote execution fallback)
        if mcp_url:
            try:
                from mcp.client.sse import sse_client
                async with sse_client(mcp_url) as (read, write):
                    async with ClientSession(read, write) as session:
                        await session.initialize()
                        response = await session.call_tool(tool_name, arguments)
                        text_content = ""
                        for content in response.content:
                            if hasattr(content, "text"):
                                text_content += content.text
                        return text_content
            except Exception as remote_err:
                import sys
                print(f"Remote SSE MCP connection failed: {remote_err}. Falling back to local stdio...", file=sys.stderr)
        
        # 3. Local subprocess stdio (Local offline test fallback)
        from mcp import StdioServerParameters
        from mcp.client.stdio import stdio_client
        server_params = StdioServerParameters(
            command=sys.executable,
            args=["-m", "app.mcp_server"],
        )
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                response = await session.call_tool(tool_name, arguments)
                text_content = ""
                for content in response.content:
                    if hasattr(content, "text"):
                        text_content += content.text
                return text_content

    # Thread-safe event loop execution supporting running loops (e.g. in FastAPI/ADK)
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = None

    if loop and loop.is_running():
        result_container = []
        exception_container = []
        
        def thread_target():
            try:
                new_loop = asyncio.new_event_loop()
                asyncio.set_event_loop(new_loop)
                res = new_loop.run_until_complete(_call())
                result_container.append(res)
            except Exception as e:
                exception_container.append(e)
            finally:
                new_loop.close()
                
        thread = threading.Thread(target=thread_target)
        thread.start()
        thread.join()
        
        if exception_container:
            raise exception_container[0]
        return result_container[0]
    else:
        return asyncio.run(_call())


def list_available_agvs() -> str:
    """Retrieve the real-time status and battery levels of all Automated Guided Vehicles (AGVs) in the fleet.
    
    Use this tool to see the current locations, operational states, and battery percentages of the vehicles
    before selecting and dispatching an AGV for bypass routing. This ensures compliance with safety protocols.
    
    Returns:
        A JSON string containing the list of all active AGVs on the floor.
    """
    try:
        return run_mcp_command_sync("list_available_agvs", {})
    except Exception as e:
        import sys
        print(f"MCP list_available_agvs failed: {e}", file=sys.stderr)
        # Fallback list for backward-compatibility and offline tests
        return (
            '[{"bot_id": "PickerBot-Alpha", "status": "IDLE", "battery": 12, "location": "Aisle 2", "notes": "CRITICAL: Low battery. Do not dispatch."}, '
            '{"bot_id": "PickerBot-Beta", "status": "IDLE", "battery": 88, "location": "Aisle 6", "notes": "Optimal battery level (88%). Highly recommended and safe for dispatch."}]'
        )


def get_agv_vitals(bot_id: str) -> str:
    """Retrieve detailed real-time health, battery status, and notes for a specific Automated Guided Vehicle (AGV).
    
    Args:
        bot_id: The unique identifier of the AGV (e.g. 'PickerBot-Alpha', 'PickerBot-Beta', 'PickerBot-Gamma').
        
    Returns:
        A JSON string containing the detailed vitals of the requested AGV.
    """
    try:
        return run_mcp_command_sync("get_agv_vitals", {"bot_id": bot_id})
    except Exception as e:
        import sys
        print(f"MCP get_agv_vitals failed: {e}", file=sys.stderr)
        # Fallback vitals
        if bot_id == "PickerBot-Alpha":
            return '{"bot_id": "PickerBot-Alpha", "status": "IDLE", "battery": 12, "location": "Aisle 2", "notes": "CRITICAL WARNING: Battery low (12%). Below 20% safety threshold. Do not dispatch."}'
        else:
            return f'{{"bot_id": "{bot_id}", "status": "IDLE", "battery": 88, "location": "Aisle 6", "notes": "Optimal battery level (88%). Highly recommended and safe for dispatch."}}'


list_available_agvs_tool = FunctionTool(func=list_available_agvs)
get_agv_vitals_tool = FunctionTool(func=get_agv_vitals)


dispatcher_agent = LlmAgent(
    name="dispatcher_agent",
    model=model_instance,
    instruction=(
        "You are a professional warehouse logistics and dispatch coordinator.\n"
        "Your task is to review the joined results of the mechanical runbook search and stock status lookup.\n"
        "You have access to a RAG-enabled search tool (`vertex_ai_rag_retrieval`). Use it to retrieve safety compliance "
        "guidelines and SOPs related to the conveyor error or conveyor ID to ensure any dispatches align with warehouse protocols.\n"
        "Before making any bypass dispatches, you MUST call the `list_available_agvs` tool to check the live battery and status telemetry of all active vehicles.\n"
        "Reject any vehicle with a low battery level below the 20% safety threshold (such as 'PickerBot-Alpha' which has only 12% battery).\n"
        "Select the most optimal active and idle vehicle with a healthy battery level (such as 'PickerBot-Beta' which has 88% battery).\n"
        "Once the optimal vehicle is selected, if the stock status is 'BLOCKED', you MUST invoke the `dispatch_agv_tool` tool with the appropriate aisle, task, and selected bot_id "
        "to trigger a physical bypass (e.g., aisle='Aisle 4', task='Route inventory to alternate conveyor CV-12', bot_id='PickerBot-Beta').\n"
        "Otherwise, if the stock is not blocked, do NOT dispatch any vehicle.\n"
        "Finally, synthesize a professional, grounded Engineering Summary Report detailing:\n"
        "1. Conveyor ID and the reported error code.\n"
        "2. The specific repair instructions retrieved from the Runbook search.\n"
        "3. Stock level and blocking status from the WMS.\n"
        "4. Dispatch actions taken: Whether an AGV was sent, the selected bot ID, its battery level, and why this specific bot was chosen (and why any others were rejected due to safety compliance).\n"
        "5. Compliance / safety SOP requirements fetched from the search tool (such as mechanical LOTO procedures under SOP-0100).\n"
        "IMPORTANT: Stay fully grounded in the retrieved tool output. Do not hallucinate or manufacture false engineering codes, numbers, or actions."
    ),
    tools=[dispatch_agv_tool, search_tool, list_available_agvs_tool, get_agv_vitals_tool],
    output_schema=DispatcherOutput,
)


def search_cctv_footages(query: str) -> list[dict]:
    """Search for relevant CCTV footage clips in the warehouse safety library matching the query.

    Args:
        query: Keywords to search for (e.g., 'Aisle 4', 'lifting', 'PPE', 'violation').

    Returns:
        A list of dictionaries with matching footage details (GCS URI, title, location, timestamp).
    """
    mock_clips = [
        {
            "uri": "gs://ce-testing-465204-cctv-media/cctv_aisle4_lifting_correct.mp4",
            "title": "Aisle 4 CCTV - Safe Lifting Technique",
            "location": "Aisle 4",
            "timestamp": "2026-06-17T09:30:00Z",
            "tags": ["picking", "lifting", "aisle 4", "compliant"]
        },
        {
            "uri": "gs://ce-testing-465204-cctv-media/cctv_aisle2_lifting_incorrect.mp4",
            "title": "Aisle 2 CCTV - Ergonomic Injury Risk",
            "location": "Aisle 2",
            "timestamp": "2026-06-17T10:15:00Z",
            "tags": ["picking", "lifting", "aisle 2", "violation"]
        },
        {
            "uri": "gs://ce-testing-465204-cctv-media/cctv_loading_dock_no_vest.mp4",
            "title": "Loading Dock - PPE Vest Violation",
            "location": "Loading Dock",
            "timestamp": "2026-06-17T11:00:00Z",
            "tags": ["unloading", "ppe", "loading dock", "violation"]
        },
        {
            "uri": "gs://ce-testing-465204-cctv-media/cctv_cv11_loto_compliance.mp4",
            "title": "Conveyor CV-11 - Lockout-Tagout Servicing",
            "location": "Conveyor CV-11",
            "timestamp": "2026-06-17T11:45:00Z",
            "tags": ["maintenance", "loto", "conveyor", "compliant"]
        }
    ]

    query_lower = query.lower()
    project_id = os.environ.get("GOOGLE_CLOUD_PROJECT", "ce-testing-465204")
    location = os.environ.get("GOOGLE_CLOUD_LOCATION", "global")
    data_store_id = "warehouse-cctv-media-store"

    if is_cloud:
        try:
            from google.cloud import discoveryengine_v1beta as discoveryengine
            client = discoveryengine.SearchServiceClient()
            serving_config = f"projects/{project_id}/locations/{location}/collections/default_collection/dataStores/{data_store_id}/servingConfigs/default_search"
            
            request = discoveryengine.SearchRequest(
                serving_config=serving_config,
                query=query,
                page_size=3
            )
            response = client.search(request)
            results = []
            for result in response.results:
                doc = result.document
                doc_dict = discoveryengine.Document.to_dict(doc)
                struct_data = doc_dict.get("structData", {})
                
                uri = struct_data.get("uri") or doc_dict.get("content", {}).get("uri") or ""
                title = struct_data.get("title") or doc_dict.get("title") or "CCTV Clip"
                loc = struct_data.get("location") or "Unknown"
                ts = struct_data.get("timestamp") or "Unknown"
                tags = struct_data.get("tags") or []
                
                results.append({
                    "uri": uri,
                    "title": title,
                    "location": loc,
                    "timestamp": ts,
                    "tags": tags
                })
            if results:
                return results
        except Exception as e:
            import sys
            print(f"Discovery Engine Media Search failed: {e}. Falling back to local catalog...", file=sys.stderr)

    filtered_clips = []
    for clip in mock_clips:
        if (query_lower in clip["location"].lower() or 
            query_lower in clip["title"].lower() or 
            any(query_lower in tag for tag in clip["tags"])):
            filtered_clips.append(clip)
            
    return filtered_clips if filtered_clips else mock_clips[:2]


def analyze_video_posture_and_hygiene(video_uri: str, audit_criteria: str = "") -> dict:
    """Analyze the given CCTV video footage using Gemini Multimodal intelligence to audit employee posture and safety hygiene.

    Args:
        video_uri: The Cloud Storage GCS URI of the video to analyze.
        audit_criteria: Optional custom check constraints.

    Returns:
        A dictionary containing overall_status ('COMPLIANT' or 'VIOLATION'), posture_score (0-100),
        ppe_checklist (safety vest and hard hat status), violation_timestamps, and a detailed audit summary.
    """
    import os
    import json
    
    uri_lower = video_uri.lower()
    mock_results = {
        "overall_status": "COMPLIANT",
        "posture_score": 95,
        "ppe_checklist": {
            "safety_vest": "DETECTED",
            "hard_hat": "DETECTED"
        },
        "violation_timestamps": [],
        "summary": "Worker demonstrated exemplary posture and safety hygiene. All warehouse guidelines met."
    }
    
    if "aisle4" in uri_lower or "lifting_correct" in uri_lower:
        mock_results = {
            "overall_status": "COMPLIANT",
            "posture_score": 95,
            "ppe_checklist": {
                "safety_vest": "DETECTED",
                "hard_hat": "DETECTED"
            },
            "violation_timestamps": [],
            "summary": "Worker in Aisle 4 demonstrated exemplary lifting technique: bent at knees, kept back straight, and held the load close to the core. Highly compliant with Ergonomic Lift Protocol SOP-202."
        }
    elif "aisle2" in uri_lower or "lifting_incorrect" in uri_lower:
        mock_results = {
            "overall_status": "VIOLATION",
            "posture_score": 38,
            "ppe_checklist": {
                "safety_vest": "DETECTED",
                "hard_hat": "DETECTED"
            },
            "violation_timestamps": ["00:04-00:08"],
            "summary": "Ergonomic injury hazard detected. At 00:04, the employee lifted a heavy carton with straight legs and a bent back (lumbar flexion > 45 degrees), creating high spinal shear stress. Urgent coaching required."
        }
    elif "loading_dock" in uri_lower or "no_vest" in uri_lower:
        mock_results = {
            "overall_status": "VIOLATION",
            "posture_score": 88,
            "ppe_checklist": {
                "safety_vest": "NOT_DETECTED",
                "hard_hat": "DETECTED"
            },
            "violation_timestamps": ["00:00-00:15"],
            "summary": "Critical safety warning: Worker on Loading Dock was detected working near active forklift operations without high-visibility vests. This is a severe infraction of PPE guidelines (SOP-0100)."
        }
    elif "cv11" in uri_lower or "loto_compliance" in uri_lower:
        mock_results = {
            "overall_status": "COMPLIANT",
            "posture_score": 92,
            "ppe_checklist": {
                "safety_vest": "DETECTED",
                "hard_hat": "DETECTED",
                "loto_tag": "DETECTED"
            },
            "violation_timestamps": [],
            "summary": "Lockout-Tagout (LOTO) audit complete. Maintenance engineer successfully verified power-off states, locked the controller switch, and attached the yellow compliance tag. Fully compliant with SOP-4042."
        }

    if is_cloud:
        try:
            from google import genai
            from google.genai import types
            
            client = genai.Client()
            prompt = (
                "You are an expert warehouse safety and ergonomic health auditor. "
                "Analyze this CCTV footage and perform a rigorous compliance check. "
                f"Audit Criteria: {audit_criteria or 'Identify posture lifting safety, high-visibility vest presence, and hard hat detection.'} "
                "Return a JSON response conforming to this structure: "
                "{"
                '  "overall_status": "COMPLIANT" or "VIOLATION",'
                '  "posture_score": <int from 0 to 100>,'
                '  "ppe_checklist": {"safety_vest": "DETECTED"|"NOT_DETECTED", "hard_hat": "DETECTED"|"NOT_DETECTED"},'
                '  "violation_timestamps": ["<start>-<end>" or offset ranges if violations occurred],'
                '  "summary": "<detailed clinical/engineering explanation of why it is compliant or a violation with recommended coaching action>"'
                "}"
            )
            
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=[
                    types.Part.from_uri(file_uri=video_uri, mime_type="video/mp4"),
                    prompt
                ],
                config=types.GenerateContentConfig(
                    response_mime_type="application/json"
                )
            )
            parsed = json.loads(response.text)
            return parsed
        except Exception as e:
            import sys
            print(f"Multimodal video analysis failed: {e}. Falling back to default mock results...", file=sys.stderr)

    return mock_results


search_cctv_footages_tool = FunctionTool(func=search_cctv_footages)
analyze_video_posture_and_hygiene_tool = FunctionTool(func=analyze_video_posture_and_hygiene)


async def generate_memories_callback(callback_context: CallbackContext) -> None:
    """Sends the session's events to the Vertex AI Memory Bank for long-term fact extraction."""
    try:
        await callback_context.add_session_to_memory()
    except Exception as e:
        import sys
        print(f"Memory bank ingestion skipped (running locally or service unavailable): {e}", file=sys.stderr)
    return None


cctv_safety_audit_agent = LlmAgent(
    name="cctv_safety_audit_agent",
    model=model_instance,
    instruction=(
        "You are an advanced AI Warehouse Safety & CCTV Compliance Auditor.\n"
        "Your mission is to search for relevant CCTV video clips and perform multimodal analysis on employee posture "
        "and safety hygiene (e.g., high-visibility vests, hard hats, LOTO procedures).\n"
        "You have access to two tools:\n"
        "1. `search_cctv_footages`: Queries the Vertex AI Agent Search Media Store to find footage metadata and GCS URIs.\n"
        "2. `analyze_video_posture_and_hygiene`: Uses multimodal capabilities to evaluate video posture, PPE, and SOP compliance.\n"
        "Always search for clips first based on the user's query (e.g., location, aisle, action). Then, analyze the video "
        "segment using the analysis tool. Output a professional audit report including a posture safety score (0-100), "
        "PPE compliance checklist, precise timestamp offsets of violations, and recommended ergonomic coaching steps.\n"
        "Stay grounded in the tool outputs. If no footage is found, state that clearly.\n"
        "Take into account the preloaded PAST_CONVERSATIONS from the Memory Bank (if any) "
        "to personalize your audits or recognize operator safety history and past compliance issues."
    ),
    tools=[search_cctv_footages_tool, analyze_video_posture_and_hygiene_tool, preload_memory_tool],
    after_agent_callback=generate_memories_callback,
)


conversational_safety_agent = LlmAgent(
    name="conversational_safety_agent",
    model=model_instance,
    instruction=(
        "You are an expert warehouse safety officer and compliance coordinator.\n"
        "Your role is to assist warehouse technicians and operators with safety queries, "
        "lockout-tagout (LOTO) guidelines, and standard operating procedures (SOPs).\n"
        "You have access to the RAG search tool (`vertex_ai_rag_retrieval`). Use it to search the internal "
        "knowledge base for guidelines matching the user's questions.\n"
        "You also have access to the live robot telemetry tools (`list_available_agvs` and `get_agv_vitals`). Use them to "
        "check the real-time status and battery levels of the warehouse fleet if the user asks about active bots, "
        "battery status, or vehicle availability.\n"
        "Provide thorough, grounded, and helpful explanations. Cite the specific SOPs (such as SOP-0100) or documents "
        "that you retrieve from the database. If you cannot find relevant information, politely advise the user.\n"
        "Take into account the preloaded PAST_CONVERSATIONS from the Memory Bank (if any) "
        "to personalize your assistance and recall operator names, preferences, and focus areas across sessions."
    ),
    tools=[search_tool, list_available_agvs_tool, get_agv_vitals_tool, preload_memory_tool],
    after_agent_callback=generate_memories_callback,
)




# Fallback Node: LogRecoverable
@node
def log_recoverable(node_input: dict) -> Event:
    """Logs recoverable warning conveyor events and completes the workflow.

    Args:
        node_input: The parsed telemetry dictionary from TelemetryIngest.

    Returns:
        An Event containing a warning logged message.
    """
    msg = (
        f"Conveyor event logged as RECOVERABLE: Conveyor {node_input.get('conveyor_id')} "
        f"warning {node_input.get('error_code')} was logged. System is operating within safety guidelines."
    )

    return Event(
        output={"status": "LOGGED", "message": msg},
        content=types.Content(
            role="model", parts=[types.Part.from_text(text=msg)]
        ),
    )


# Instantiate Join Node
join_node = JoinNode(name="join")

# Assemble the ADK 2.0 Graph Workflow
root_agent = Workflow(
    name="stackbox_conveyor_orchestrator",
    edges=[
        ("START", telemetry_ingest),
        # Conditional Edge Routing
        Edge(from_node=telemetry_ingest, to_node=runbook_lookup, route="CRITICAL"),
        Edge(from_node=telemetry_ingest, to_node=wms_access, route="CRITICAL"),
        Edge(from_node=telemetry_ingest, to_node=log_recoverable, route="RECOVERABLE"),
        Edge(from_node=telemetry_ingest, to_node=conversational_safety_agent, route="CONVERSATIONAL"),
        Edge(from_node=telemetry_ingest, to_node=cctv_safety_audit_agent, route="SAFETY_AUDIT"),
        # Fan-in Parallel Join
        ((runbook_lookup, wms_access), join_node),
        # Flow joined data to formatter, then to dispatcher agent
        (join_node, format_dispatcher_input),
        (format_dispatcher_input, dispatcher_agent),
    ],
)

app = App(
    root_agent=root_agent,
    name="app",
)
