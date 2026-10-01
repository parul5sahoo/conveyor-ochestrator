#!/usr/bin/env python3
"""Sync Open Knowledge Format (OKF) documents and catalog index to Google Cloud Storage (GCS)."""

import os
import sys
import json

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
KNOWLEDGE_DIR = os.path.join(BASE_DIR, "knowledge", "okf")
INDEX_PATH = os.path.join(BASE_DIR, "knowledge", "okf_catalog_index.json")

GCP_PROJECT = os.environ.get("GOOGLE_CLOUD_PROJECT", "ce-testing-465204")
GCS_BUCKET_NAME = os.environ.get("GCS_OKF_BUCKET", "ce-testing-465204-conveyor-orchestrator-knowledge")
GCS_PREFIX = "okf"

def sync_to_gcs():
    print(f"============================================================")
    print(f"Syncing OKF Knowledge Corpus to Google Cloud Storage")
    print(f"Target Project: {GCP_PROJECT}")
    print(f"Target Bucket : gs://{GCS_BUCKET_NAME}/{GCS_PREFIX}/")
    print(f"Local Source  : {KNOWLEDGE_DIR}")
    print(f"============================================================")

    if not os.path.exists(INDEX_PATH):
        print(f"Error: Catalog index not found at {INDEX_PATH}")
        sys.exit(1)

    try:
        from google.cloud import storage
        client = storage.Client(project=GCP_PROJECT)
        
        # Check or create bucket if possible
        try:
            bucket = client.get_bucket(GCS_BUCKET_NAME)
            print(f"Connected to existing bucket: {GCS_BUCKET_NAME}")
        except Exception as b_err:
            print(f"Bucket {GCS_BUCKET_NAME} not found or inaccessible: {b_err}")
            print(f"Attempting to create bucket {GCS_BUCKET_NAME} in us-central1...")
            bucket = client.create_bucket(GCS_BUCKET_NAME, location="us-central1")
            print(f"Created bucket {GCS_BUCKET_NAME}")

        # Upload Catalog Index
        index_blob = bucket.blob(f"{GCS_PREFIX}/okf_catalog_index.json")
        index_blob.upload_from_filename(INDEX_PATH, content_type="application/json")
        print(f"Uploaded: gs://{GCS_BUCKET_NAME}/{GCS_PREFIX}/okf_catalog_index.json")

        # Upload All OKF Documents
        for fname in os.listdir(KNOWLEDGE_DIR):
            if fname.endswith(".md"):
                local_file = os.path.join(KNOWLEDGE_DIR, fname)
                blob = bucket.blob(f"{GCS_PREFIX}/{fname}")
                blob.upload_from_filename(local_file, content_type="text/markdown")
                print(f"Uploaded: gs://{GCS_BUCKET_NAME}/{GCS_PREFIX}/{fname}")

        print(f"\nAll OKF documents successfully synchronized to Cloud Storage.")
        return True

    except Exception as e:
        print(f"\n[INFO] Cloud Storage remote sync encountered notice: {e}")
        print(f"[INFO] Local cache fallback active at: {KNOWLEDGE_DIR}")
        print(f"[INFO] The agent tools are designed with dual-layer fallback:")
        print(f"       1. Remote GCS bucket 'gs://{GCS_BUCKET_NAME}/okf/'")
        print(f"       2. Local high-speed cache '{KNOWLEDGE_DIR}'")
        print(f"\nManual upload command if desired:")
        print(f"  gcloud storage cp -r {KNOWLEDGE_DIR} gs://{GCS_BUCKET_NAME}/")
        print(f"  gcloud storage cp {INDEX_PATH} gs://{GCS_BUCKET_NAME}/{GCS_PREFIX}/")
        return False

if __name__ == "__main__":
    sync_to_gcs()
