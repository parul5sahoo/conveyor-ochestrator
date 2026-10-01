#!/bin/bash
set -e

PROJECT_ID="ce-testing-465204"
REGION="us-central1"
SERVICE_NAME="conveyor-orchestrator-app"
IMAGE_TAG="${REGION}-docker.pkg.dev/${PROJECT_ID}/agent-repo/${SERVICE_NAME}:latest"
SERVICE_ACCOUNT="geap-user-sa@${PROJECT_ID}.iam.gserviceaccount.com"

echo "--------------------------------------------------------"
echo "📦 Containerizing and Deploying Conveyor Orchestrator"
echo "--------------------------------------------------------"

echo "Step 1: Setting active Google Cloud Project..."
gcloud config set project "${PROJECT_ID}"

echo "Step 2: Submitting container build to Google Cloud Build..."
gcloud builds submit --tag "${IMAGE_TAG}" --project="${PROJECT_ID}"

echo "Step 3: Deploying container to Google Cloud Run (Region: ${REGION})..."
gcloud run deploy "${SERVICE_NAME}" \
  --image "${IMAGE_TAG}" \
  --platform managed \
  --region "${REGION}" \
  --allow-unauthenticated \
  --service-account="${SERVICE_ACCOUNT}" \
  --set-env-vars="GOOGLE_CLOUD_PROJECT=${PROJECT_ID},GOOGLE_CLOUD_LOCATION=${REGION}" \
  --project="${PROJECT_ID}"

echo "--------------------------------------------------------"
echo "✅ DEDEPLOYMENT COMPLETED SUCCESSFULLY!"
echo "👉 Dashboard URL: https://${SERVICE_NAME}-<hash>.run.app/dashboard"
echo "--------------------------------------------------------"
