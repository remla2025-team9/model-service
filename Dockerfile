# This is the Multi-stage Dockerfile for the model-service

# Build stage
FROM python:3.11-slim AS builder

WORKDIR /build

# Install git for pip to clone repositories
RUN apt-get update \
    && apt-get install -y git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy setup file and app directory
COPY setup.py .
COPY app/ ./app/

# Install build dependencies and Python packages
RUN python -m venv /build/venv \
    && /build/venv/bin/pip install --upgrade pip \
    && /build/venv/bin/pip install --no-cache-dir .

# Runtime stage
FROM python:3.11-slim

WORKDIR /app

# Copy virtual environment from builder
COPY --from=builder /build/venv /app/venv

# Copy application code
COPY app/ ./app/

# Set environment variables
ARG VERSION
ENV MODEL_SERVICE_VERSION=${VERSION}
ENV SERVICE_PORT=8080
ENV SERVICE_HOST=0.0.0.0

LABEL version=${VERSION}

# Set the entrypoint to the application
# Use the virtual environment's Python interpreter
CMD ["/app/venv/bin/python", "-m", "app.main"]