import asyncio
import vertexai

async def main():
    print("Connecting to deployed Agent Runtime...")
    vertexai.init(project="ce-testing-465204", location="us-central1")
    resource_name = "projects/526827734705/locations/us-central1/reasoningEngines/8594036320127418368"
    client = vertexai.Client(project="ce-testing-465204", location="us-central1")
    agent = client.agent_engines.get(name=resource_name)
    
    query = "Incident Alert: conveyor_id: CV-09, error_code: Error 4042, sku: SKU-991, status: CRITICAL. Technician Dave Miller (TECH-402) on site in Zone B - Aisle 4. Please diagnose and provide immediate remediation steps."
    print(f"Sending prompt to deployed agent: {query[:80]}...")
    
    response_text = ""
    async for event in agent.async_stream_query(message=query, user_id="eval-smoke-test"):
        content = None
        if isinstance(event, dict):
            content = event.get("content")
        elif hasattr(event, "content"):
            content = event.content
        if content:
            parts = content.get("parts") if isinstance(content, dict) else getattr(content, "parts", None)
            if parts:
                for part in parts:
                    text = part.get("text") if isinstance(part, dict) else getattr(part, "text", None)
                    if text:
                        response_text += text
    print("\n--- DEPLOYED AGENT RESPONSE RECEIVED ---")
    print(response_text[:400] + "...")
    assert len(response_text) > 0, "Response should not be empty"
    print("SUCCESS: Deployed revision is responding.")

if __name__ == "__main__":
    asyncio.run(main())
