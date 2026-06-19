import vertexai

def main():
    print("Initializing Vertex AI Client...")
    vertexai.init(project="ce-testing-465204", location="us-central1")
    client = vertexai.Client(project="ce-testing-465204", location="us-central1")
    
    resource_name = "projects/526827734705/locations/us-central1/reasoningEngines/8594036320127418368"
    
    print("Preparing Memory Bank Configuration...")
    memory_bank_config = {
        "generation_config": {
            "model": "projects/ce-testing-465204/locations/us-central1/publishers/google/models/gemini-2.5-flash"
        },
        "similarity_search_config": {
            "embedding_model": "projects/ce-testing-465204/locations/us-central1/publishers/google/models/text-embedding-005"
        },
        "ttl_config": {
            "memory_revision_default_ttl": "31536000s"
        },
        "customization_configs": [{
            "memory_topics": [
                {"managed_memory_topic": {"managed_topic_enum": "USER_PERSONAL_INFO"}},
                {"managed_memory_topic": {"managed_topic_enum": "USER_PREFERENCES"}},
                {"managed_memory_topic": {"managed_topic_enum": "KEY_CONVERSATION_DETAILS"}},
                {"managed_memory_topic": {"managed_topic_enum": "EXPLICIT_INSTRUCTIONS"}},
                {
                    "custom_memory_topic": {
                        "label": "safety_compliance_history",
                        "description": "Information about operators' safety violations, ergonomics compliance, and lockout-tagout history."
                    }
                }
            ],
            "consolidation_config": {
                "revisions_per_candidate_count": 1
            },
            "generate_memories_examples": [],
            "enable_third_person_memories": False
        }],
        "disable_memory_revisions": False
    }
    
    print(f"Updating Reasoning Engine spec for engine: {resource_name}...")
    updated_engine = client.agent_engines.update(
        name=resource_name,
        config={
            "context_spec": {
                "memory_bank_config": memory_bank_config
            }
        }
    )
    print("Reasoning engine updated successfully with Memory Bank configuration!")

if __name__ == "__main__":
    main()
