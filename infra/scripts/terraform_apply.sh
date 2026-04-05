#!/usr/bin/env bash
set -euo pipefail
ENVIRONMENT="${1:-dev}"
terraform apply -auto-approve -var-file="environments/${ENVIRONMENT}.tfvars"
