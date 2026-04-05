#!/usr/bin/env bash
set -euo pipefail
ENVIRONMENT="${1:-dev}"
terraform plan -var-file="environments/${ENVIRONMENT}.tfvars"
