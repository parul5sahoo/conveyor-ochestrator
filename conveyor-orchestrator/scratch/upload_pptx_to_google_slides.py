# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "google-api-python-client>=2.0.0",
#     "google-auth>=2.0.0",
# ]
# ///
"""
Stackbox Conveyor Orchestrator - Upload & Convert PPTX to Google Slides

This script uploads the locally generated PowerPoint file (.pptx) to Google Drive
and automatically converts it into a native Google Slides presentation.
"""

import os
import sys
import subprocess
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import google.auth
import google.oauth2.credentials

def upload_and_convert():
    pptx_path = os.path.join(os.path.dirname(__file__), "stackbox_conveyor_gep_features.pptx")
    if not os.path.exists(pptx_path):
        print(f"Error: PowerPoint file not found at {pptx_path}")
        print("Please run `generate_gep_slides.py` first.")
        sys.exit(1)

    creds = None

    # Method 1: Acquire token directly from gcloud application-default CLI
    print("Acquiring token from `gcloud auth application-default print-access-token`...")
    try:
        token = subprocess.check_output(["gcloud", "auth", "application-default", "print-access-token"], stderr=subprocess.DEVNULL).decode().strip()
        if token:
            creds = google.oauth2.credentials.Credentials(token)
            print("Successfully acquired active ADC access token.")
    except Exception:
        pass

    # Method 2: Fall back to standard Python Application Default Credentials
    if not creds:
        print("Falling back to standard Python Application Default Credentials...")
        try:
            creds, project = google.auth.default(scopes=["https://www.googleapis.com/auth/drive.file"])
        except Exception as e:
            print(f"\n[!] Authentication failed: {e}")
            sys.exit(1)

    try:
        service = build("drive", "v3", credentials=creds)
        
        file_metadata = {
            "name": "Stackbox Conveyor Orchestrator - GEP Features Showcase",
            "mimeType": "application/vnd.google-apps.presentation"  # Instructs Drive to convert to Google Slides
        }
        
        media = MediaFileUpload(
            pptx_path,
            mimetype="application/vnd.openxmlformats-officedocument.presentationml.presentation",
            resumable=True
        )

        print(f"Uploading and converting `{os.path.basename(pptx_path)}` to Google Slides...")
        file = service.files().create(
            body=file_metadata,
            media_body=media,
            fields="id, webViewLink"
        ).execute()

        print("\n" + "="*70)
        print("🎉 SUCCESS! Google Slides presentation created.")
        print("Presentation ID:", file.get("id"))
        print("Google Slides URL:", file.get("webViewLink"))
        print("="*70 + "\n")

    except Exception as e:
        print(f"\n[!] Upload failed: {e}")
        if "insufficient permissions" in str(e).lower() or "scope" in str(e).lower() or "403" in str(e):
            print("\nYour current token lacks Google Drive upload permissions.")
            print("To grant Drive upload access, please run:\n")
            print('    gcloud auth application-default login --scopes="https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/drive.file"\n')
        sys.exit(1)

if __name__ == "__main__":
    upload_and_convert()
