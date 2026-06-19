import vertexai
from vertexai.preview import reasoning_engines

def main():
    print("Initializing Vertex AI...")
    vertexai.init(project="ce-testing-465204", location="us-central1")
    
    print("Listing Reasoning Engines...")
    engines = reasoning_engines.ReasoningEngine.list()
    for eng in engines:
        print(f"ID: {eng.resource_name}")
        print(f"Display Name: {eng.display_name}")
        print("-" * 40)

if __name__ == "__main__":
    main()
