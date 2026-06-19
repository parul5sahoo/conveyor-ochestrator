import asyncio
import vertexai

async def main():
    print("Initializing Vertex AI Client...")
    vertexai.init(project="ce-testing-465204", location="us-central1")
    
    print("Retrieving ReasoningEngine resource...")
    resource_name = "projects/526827734705/locations/us-central1/reasoningEngines/8594036320127418368"
    client = vertexai.Client(project="ce-testing-465204", location="us-central1")
    agent = client.agent_engines.get(name=resource_name)
    
    print("\n--- TEST 1: CCTV Posture Audit Aisle 2 ---")
    message = "Run a safety and posture audit for employee lifting in Aisle 2"
    print(f"Query content: '{message}'")
    try:
        async for event in agent.async_stream_query(message=message, user_id="test-operator"):
            if hasattr(event, "content") and event.content and event.content.parts:
                for part in event.content.parts:
                    if part.text:
                        print(part.text, end="", flush=True)
    except Exception as e:
        print(f"\nQuery failed: {e}")
        
    print("\n\n--- TEST 2: PPE Compliance loading dock ---")
    message = "Audit safety vest and hard hat compliance in loading dock forklift zones"
    print(f"Query content: '{message}'")
    try:
        async for event in agent.async_stream_query(message=message, user_id="test-operator"):
            if hasattr(event, "content") and event.content and event.content.parts:
                for part in event.content.parts:
                    if part.text:
                        print(part.text, end="", flush=True)
    except Exception as e:
        print(f"\nQuery failed: {e}")
    print("\n\n--- Verification Finished ---")

if __name__ == "__main__":
    asyncio.run(main())
