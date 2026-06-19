import os
import urllib.request
import json
import google.auth
import google.auth.transport.requests

TARGET_BUCKET = "ce-testing-465204-cctv-media"
LOCAL_MP4_PATH = "/Users/parulsahoo/Documents/CE-github/vertex-ai-creative-studio/experiments/VTO/vto_demo.mp4"

CCTV_FILENAMES = [
    "cctv_aisle4_squat_lift.mp4",
    "cctv_aisle2_bad_lift.mp4",
    "cctv_loading_dock_no_vest.mp4",
    "cctv_cv11_loto_compliance.mp4"
]

def upload_to_gcs(bucket_name, object_name, data, token):
    print(f"Uploading {object_name} to bucket {bucket_name} ({len(data)} bytes)...")
    url = f"https://storage.googleapis.com/upload/storage/v1/b/{bucket_name}/o?uploadType=media&name={object_name}"
    
    req = urllib.request.Request(url, data=data)
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Content-Type", "video/mp4")
    req.add_header("Content-Length", str(len(data)))
    
    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode())
            print(f"  Successfully uploaded: gs://{bucket_name}/{result['name']} ({result['size']} bytes)")
            return True
    except Exception as e:
        print(f"  Failed to upload {object_name}: {e}")
        return False

def main():
    if not os.path.exists(LOCAL_MP4_PATH):
        print(f"Error: Local MP4 file not found at {LOCAL_MP4_PATH}")
        return
        
    print(f"Reading local MP4 file: {LOCAL_MP4_PATH}")
    with open(LOCAL_MP4_PATH, "rb") as f:
        video_data = f.read()
    print(f"Read {len(video_data)} bytes.")

    print("Getting GCP credentials...")
    try:
        credentials, project = google.auth.default()
        auth_req = google.auth.transport.requests.Request()
        credentials.refresh(auth_req)
        token = credentials.token
    except Exception as e:
        print(f"Error getting credentials: {e}")
        return

    print(f"\nUploading to GCS bucket: {TARGET_BUCKET}")
    for filename in CCTV_FILENAMES:
        upload_to_gcs(TARGET_BUCKET, filename, video_data, token)

if __name__ == "__main__":
    main()
