import os
from google.cloud import storage

def list_buckets_and_objects():
    project_id = "ce-testing-465204"
    print(f"Listing buckets for project: {project_id}")
    try:
        client = storage.Client(project=project_id)
        buckets = list(client.list_buckets())
        print(f"Found {len(buckets)} buckets:")
        for bucket in buckets:
            print(f"- {bucket.name}")
            # If the bucket seems related to media, list some files
            if "media" in bucket.name or "demo" in bucket.name or "exps" in bucket.name:
                try:
                    blobs = list(client.list_blobs(bucket.name, max_results=10))
                    print(f"  Files (up to 10):")
                    for blob in blobs:
                        print(f"    - gs://{bucket.name}/{blob.name} (size: {blob.size} bytes)")
                except Exception as e:
                    print(f"    Failed to list blobs: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    list_buckets_and_objects()
