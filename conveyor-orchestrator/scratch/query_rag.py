import os
from google import genai
from google.genai import types

def main():
    print("Initializing GenAI client with Vertex AI enabled...")
    # Instantiate with vertexai=True to use Google Cloud / Application Default Credentials
    client = genai.Client(vertexai=True)
    
    corpus_id = "projects/ce-testing-465204/locations/us-central1/ragCorpora/2104922652400418816"
    print(f"Querying RAG Corpus: {corpus_id}")
    
    try:
        response = client.rag.query(
            rag_resources=[
                types.RagResource(
                    rag_corpus=corpus_id
                )
            ],
            text="CV-11 calibration safety",
        )
        print("Successfully queried RAG Corpus!")
        print("Response results:")
        if response.results:
            for context in response.results:
                print(f"- Text: {context.text}")
                print(f"  Source: {context.source_uri}")
        else:
            print("No results returned.")
    except Exception as e:
        print(f"Error querying RAG Corpus: {e}")

if __name__ == "__main__":
    main()
