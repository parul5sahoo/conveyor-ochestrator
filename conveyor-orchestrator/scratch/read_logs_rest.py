import json
import urllib.request
import urllib.error
import google.auth
from google.auth.transport.requests import Request

def main():
    project_id = "ce-testing-465204"
    print("Fetching Google Application Default Credentials (ADC)...")
    credentials, project = google.auth.default(scopes=["https://www.googleapis.com/auth/cloud-platform"])
    
    print("Refreshing credentials...")
    credentials.refresh(Request())
    access_token = credentials.token
    
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    url = "https://logging.googleapis.com/v2/entries:list"
    payload = {
        "resourceNames": [f"projects/{project_id}"],
        "filter": 'resource.type="aiplatform.googleapis.com/ReasoningEngine"',
        "orderBy": "timestamp desc",
        "pageSize": 15
    }
    
    print("Querying Cloud Logging REST API...")
    req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req) as response:
            res = json.loads(response.read().decode("utf-8"))
            entries = res.get("entries", [])
            print(f"Retrieved {len(entries)} log entries:")
            for entry in entries:
                timestamp = entry.get("timestamp")
                payload_text = entry.get("textPayload", json.dumps(entry.get("jsonPayload", {}), indent=2))
                print(f"\n--- Log Entry: {timestamp} ---")
                print(payload_text)
    except urllib.error.HTTPError as e:
        print(f"Error querying logs: {e.code} - {e.read().decode('utf-8')}")

if __name__ == "__main__":
    main()
