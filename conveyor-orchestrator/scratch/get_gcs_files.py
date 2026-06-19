import urllib.request
import json
import google.auth
import google.auth.transport.requests

def list_bucket_via_rest(bucket_name):
    print(f"\nListing bucket via REST: {bucket_name}")
    try:
        credentials, project = google.auth.default()
        auth_req = google.auth.transport.requests.Request()
        credentials.refresh(auth_req)
        
        token = credentials.token
        url = f"https://storage.googleapis.com/storage/v1/b/{bucket_name}/o"
        req = urllib.request.Request(url)
        req.add_header("Authorization", f"Bearer {token}")
        
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            items = data.get("items", [])
            print(f"Found {len(items)} files in {bucket_name}:")
            for item in items:
                if item['name'].endswith('.mp4') or 'cctv' in item['name'].lower() or 'video' in item['name'].lower():
                    print(f"  - gs://{bucket_name}/{item['name']} (size: {item['size']} bytes)")
            return items
    except Exception as e:
        print(f"  Error: {e}")
        return []

if __name__ == "__main__":
    list_bucket_via_rest("media-exps")
