#!/bin/bash
set -e

# Activate virtual environment
source /opt/venv/bin/activate

# Navigate to code directory
cd /code

# Read env vars or use defaults
RUN_PORT="${PORT:-8000}"
RUN_HOST="${HOST:-0.0.0.0}"

# Start FastAPI using Gunicorn + Uvicorn worker
exec gunicorn -k uvicorn.workers.UvicornWorker -b "$RUN_HOST:$RUN_PORT" main:app
