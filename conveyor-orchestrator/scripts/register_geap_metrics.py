"""
Script to register GEAP Custom Code Metrics to Google Cloud Project.
Reference: https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/evaluation/manage-metrics#register_a_custom_code_metric
"""

import sys
import os
from typing import List, Dict, Any

# Ensure project root is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tests.eval.metrics.geap_custom_metrics import get_all_geap_custom_metrics

PROJECT_ID = os.environ.get("PROJECT_ID", "ce-testing-465204")
LOCATION = os.environ.get("LOCATION", "us-central1")


def register_metrics():
    print(f"Connecting to Vertex AI Agent Platform in {PROJECT_ID} ({LOCATION})...")
    try:
        from vertexai import Client, types
    except ImportError as e:
        print(f"ERROR: Failed to import vertexai: {e}")
        print("Please install via: pip install 'google-cloud-aiplatform[adk,evaluation]'")
        sys.exit(1)

    try:
        client = Client(project=PROJECT_ID, location=LOCATION)
    except Exception as e:
        print(f"ERROR: Failed to initialize Client: {e}")
        print("Run `gcloud auth application-default login` to refresh credentials.")
        sys.exit(1)

    metrics = get_all_geap_custom_metrics()
    print(f"\nFound {len(metrics)} custom code metrics to register.")

    # Check existing metrics
    existing_metrics = {}
    try:
        listed = client.evals.list_evaluation_metrics()
        for item in listed:
            name = getattr(item, "name", str(item))
            display_name = getattr(item, "display_name", "")
            existing_metrics[display_name or name] = name
        print(f"Currently registered metrics in project: {len(existing_metrics)}")
    except Exception as e:
        print(f"Note: Could not list existing metrics ({e}), proceeding with registration.")

    results = []
    for m in metrics:
        metric_id = m["id"]
        display_name = m["display_name"]
        definition = m["definition"]
        code = m["code"]

        print(f"\nRegistering metric: '{metric_id}' ({display_name})...")
        try:
            # Construct CodeExecutionMetric per GEAP specification
            custom_metric = types.CodeExecutionMetric(
                name=metric_id,
                custom_function=code
            )

            metric_resource_path = client.evals.create_evaluation_metric(
                metric=custom_metric,
                display_name=display_name,
                description=definition
            )
            print(f"  ✓ Successfully registered: {metric_resource_path}")
            results.append({"id": metric_id, "status": "SUCCESS", "path": metric_resource_path})
        except Exception as e:
            error_str = str(e)
            if "AlreadyExists" in error_str or "already exists" in error_str or "409" in error_str:
                print(f"  ℹ Metric already exists in project registry: {metric_id}")
                results.append({"id": metric_id, "status": "ALREADY_EXISTS", "error": error_str})
            else:
                print(f"  ✗ Failed to register '{metric_id}': {e}")
                results.append({"id": metric_id, "status": "FAILED", "error": error_str})

    print("\n" + "=" * 60)
    print("REGISTRATION SUMMARY:")
    for r in results:
        status_icon = "✓" if r["status"] == "SUCCESS" else ("ℹ" if r["status"] == "ALREADY_EXISTS" else "✗")
        print(f" {status_icon} {r['id']}: {r['status']}")
    print("=" * 60)


if __name__ == "__main__":
    register_metrics()
