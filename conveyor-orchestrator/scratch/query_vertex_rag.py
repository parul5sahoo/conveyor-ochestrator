import os
import vertexai
from vertexai.preview import rag

def main():
    project_id = "ce-testing-465204"
    location = "us-central1"
    corpus_id = "projects/ce-testing-465204/locations/us-central1/ragCorpora/2104922652400418816"
    
    print(f"Initializing Vertex AI SDK for project {project_id} in {location}...")
    vertexai.init(project=project_id, location=location)
    
    print(f"Querying RAG Corpus using retrieval_query: {corpus_id}")
    try:
        response = rag.retrieval_query(
            text="CV-11 calibration safety",
            rag_corpora=[corpus_id],
            similarity_top_k=3,
        )
        print("Successfully queried RAG Corpus!")
        print("Response contexts:")
        if response.contexts and response.contexts.contexts:
            for ctx in response.contexts.contexts:
                print(f"- Text: {ctx.text}")
                print(f"  Source URI: {ctx.source_uri}")
        else:
            print("No contexts returned in response.")
    except Exception as e:
        print(f"Error querying RAG: {e}")

if __name__ == "__main__":
    main()
