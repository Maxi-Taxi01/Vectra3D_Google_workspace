# Vectra3D Google Workspace Cloud Run service

This repository contains a minimal HTTP service ready for Cloud Run. It provides
`GET /` and `GET /healthz` endpoints. It does **not** yet integrate with Google
Workspace APIs or request access to Workspace data.

## Cloud Run settings

- Source: this repository, branch `main`
- Build type: Dockerfile at `/Dockerfile`
- Service name: `vectra3d-google-workspace`
- Region: `europe-west1` (Belgium)
- Authentication: **Require authentication** using IAM
- Billing: request-based; minimum instances: `0`
- Container port: `8080` (the app reads Cloud Run's `PORT` environment variable)

Deploying from the repository creates a Cloud Build trigger. Access to the
service should be granted explicitly to intended callers with the Cloud Run
Invoker role after deployment. No Workspace credentials are needed for this
scaffold.
