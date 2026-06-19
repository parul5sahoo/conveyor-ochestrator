import urllib.request
import json
import google.auth
import google.auth.transport.requests

# Sample public videos from Google's GTV Videos Bucket
SAMPLES = {
    "cctv_aisle4_squat_lift.mp4": "https://storage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4",
    "cctv_aisle2_bad_lift.mp4": "https://storage.googleapis.com/gtv-videos-bucket/sample/ForBiggerEscapes.mp4",
    "cctv_loading_dock_no_vest.mp4": "https://storage.googleapis.com/gtv-videos-bucket/sample/ForBiggerFun.mp4",
    "cctv_cv11_loto_compliance.mp4": "https://storage.googleapis.com/gtv-videos-bucket/sample/ForBiggerJoyrides.mp4"
}

def upload_to_gcs(bucket_name, object_name, data, token):
    print(f"Uploading {object_name} to bucket {bucket_name}...")
    url = f"https://storage.googleapis.com/upload/storage/v1/b/{bucket_name}/o?uploadType=media&name={object_name}"
    
    req = urllib.request.Request(url, data=data)
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Content-Type", "video/mp4")
    req.add_header("Content-Length", str(len(data)))
    
    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode())
            print(f"Successfully uploaded: gs://{bucket_name}/{result['name']} ({result['size']} bytes)")
            return True
    except Exception as e:
        print(f"Failed to upload {object_name}: {e}")
        return False

def main():
    bucket_name = "ce-testing-465204-cctv-media"
    
    print("Getting GCP credentials...")
    try:
        credentials, project = google.auth.default()
        auth_req = google.auth.transport.requests.Request()
        credentials.refresh(auth_req)
        token = credentials.token
    except Exception as e:
        print(f"Error getting credentials: {e}")
        return

    for filename, download_url in SAMPLES.items():
        print(f"\nDownloading sample video for {filename} from {download_url}...")
        try:
            req = urllib.request.Request(download_url)
            # Add a standard User-Agent header to avoid 403 Forbidden
            req.add_header("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36")
            with urllib.request.urlopen(req) as response:
                video_data = response.read()
                print(f"Downloaded {len(video_data)} bytes.")
                
            upload_to_gcs(bucket_name, filename, video_data, token)
        except Exception as e:
            print(f"Failed during download/upload of {filename}: {e}")

if __name__ == "__main__":
    main()
