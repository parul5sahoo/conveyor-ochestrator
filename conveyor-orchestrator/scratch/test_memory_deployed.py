import asyncio
import vertexai

async def main():
    print("Initializing Vertex AI Client...")
    vertexai.init(project="ce-testing-465204", location="us-central1")
    
    resource_name = "projects/526827734705/locations/us-central1/reasoningEngines/8594036320127418368"
    client = vertexai.Client(project="ce-testing-465204", location="us-central1")
    agent = client.agent_engines.get(name=resource_name)
    
    # We use a unique user_id to ensure a clean session sequence
    user_id = "Dave-Audit-123"
    
    print("\n" + "="*50)
    print("SESSION 1: Establishing Context")
    print("="*50)
    message_1 = "Hi, I am Dave and today I'm focusing strictly on lockout-tagout audits."
    print(f"Query: '{message_1}'\n")
    print("Response: ", end="", flush=True)
    
    try:
        async for event in agent.async_stream_query(message=message_1, user_id=user_id):
            if isinstance(event, dict):
                content = event.get("content")
                if content:
                    parts = content.get("parts")
                    if parts:
                        for part in parts:
                            text = part.get("text")
                            if text:
                                print(text, end="", flush=True)
    except Exception as e:
        print(f"\nQuery 1 failed: {e}")
        
    print("\n\nWaiting 10 seconds for backend Memory Bank extraction to fully settle...")
    await asyncio.sleep(10)
    
    print("\n" + "="*50)
    print("SESSION 2: Recalling Persistent Context")
    print("="*50)
    message_2 = "What am I auditing today and what is my name?"
    print(f"Query: '{message_2}'\n")
    print("Response: ", end="", flush=True)
    
    try:
        async for event in agent.async_stream_query(message=message_2, user_id=user_id):
            if isinstance(event, dict):
                content = event.get("content")
                if content:
                    parts = content.get("parts")
                    if parts:
                        for part in parts:
                            text = part.get("text")
                            if text:
                                print(text, end="", flush=True)
    except Exception as e:
        print(f"\nQuery 2 failed: {e}")
        
    print("\n" + "="*50)
    print("Verification complete.")
    print("="*50)

if __name__ == "__main__":
    asyncio.run(main())
