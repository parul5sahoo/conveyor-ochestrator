import asyncio
import vertexai

async def main():
    print("Initializing...")
    vertexai.init(project="ce-testing-465204", location="us-central1")
    resource_name = "projects/526827734705/locations/us-central1/reasoningEngines/8594036320127418368"
    client = vertexai.Client(project="ce-testing-465204", location="us-central1")
    agent = client.agent_engines.get(name=resource_name)
    
    print("Querying...")
    message = "Run a safety and posture audit for employee lifting in Aisle 2"
    async for event in agent.async_stream_query(message=message, user_id="test-operator"):
        print(f"EVENT TYPE: {type(event)}")
        print(f"EVENT DIR: {dir(event)}")
        print(f"EVENT STR: {event}")
        print("="*40)

if __name__ == "__main__":
    asyncio.run(main())
