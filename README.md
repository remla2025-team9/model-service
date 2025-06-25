# Model Service

This is a Flask-based web service that provides machine learning model inference capabilities. The service loads pre-trained models and provides RESTful API endpoints for making predictions. It includes built-in data preprocessing and supports various model versions through configuration.

## Features

- RESTful API for model inference
- OpenAPI/Swagger documentation
- Docker containerization
- Multi-architecture support (AMD64/ARM64)
- Configurable model versions
- Health check endpoints

## CI/CD Workflows

This repository includes several GitHub Actions workflows for automated testing, building, and deployment:

- **Integration Workflow** (`integration.yml`): Validates pull requests by building Docker images without pushing them. Runs on PRs to main branch.
- **Delivery Workflow** (`delivery.yml`): Automatically creates pre-release tags (e.g., v1.0.0-pre.1) when code is pushed to main branch.
- **Deployment Workflow** (`deployment.yml`): Manual workflow for creating stable releases. Builds and pushes Docker images with proper version tags and creates GitHub releases.
- **Canary Deployment Workflow** (`canary_deployment.yml`): Manual workflow for deploying experimental features with custom tags for A/B testing.

All workflows build Docker images with the service version passed as a build argument and set as an environment variable (`MODEL_SERVICE_VERSION`) in the container.

## Running the Flask app locally

### Prerequisites

- Python 3.11 or higher
- pip package manager

### Installation

Using a virtual environment is recommended to avoid conflicts with other Python projects.

1. **Clone the repository**:
```bash
git clone <repository-url>
cd model-service
```

2. **Create a virtual environment**:

**On Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**On Windows (Command Prompt):**
```cmd
python -m venv .venv
.venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. **Install the required packages**:
```bash
pip install --upgrade pip
pip install .
```

To deactivate the virtual environment when you're done:
```bash
deactivate
```

### Environment Variables

Before running the application, you need to configure the following environment variables:

| Variable        | Description                                   | Required | Default Value |
| --------------- | --------------------------------------------- | -------- | ------------- |
| `MODEL_VERSION` | The version of the model to use for inference | **Yes**  | None          |
| `SERVICE_PORT`  | The port on which the service will run        | No       | 8080          |
| `SERVICE_HOST`  | The host address to bind the service to       | No       | 0.0.0.0       |

#### Setting Environment Variables

**On Windows (PowerShell):**
```powershell
$env:MODEL_VERSION = "v1.0.0"
$env:SERVICE_PORT = "8080"
$env:SERVICE_HOST = "0.0.0.0"
```

**On Windows (Command Prompt):**
```cmd
set MODEL_VERSION=v1.0.0
set SERVICE_PORT=8080
set SERVICE_HOST=0.0.0.0
```

**On macOS/Linux (Bash):**
```bash
export MODEL_VERSION=v1.0.0
export SERVICE_PORT=8080
export SERVICE_HOST=0.0.0.0
```

### Running the Application

**If using a virtual environment, make sure it's activated first**:

**On Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**On Windows (Command Prompt):**
```cmd
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
source venv/bin/activate
```

Once you have set the required environment variables and activated your virtual environment (if using one), run the Flask app:

```bash
python app/main.py
```

The application will start and be available at `http://localhost:8080` (or the port you specified).

### API Documentation

You can view the interactive API specification by navigating to:
- Swagger UI: `http://localhost:8080/apidocs`


## Building and Running with Docker

### Prerequisites

- Docker installed on your machine
- Git (for cloning the repository)

### Building the Docker Image

The service includes a multi-stage Dockerfile that builds the application and creates an optimized runtime image.

1. **Clone the repository** (if you haven't already):
```bash
git clone <repository-url>
cd model-service
```

2. **Build the Docker image**:
```bash
docker build -t model-service:local --build-arg VERSION=local .
```

### Running the Container

#### Basic Usage
```bash
docker run -e MODEL_VERSION=v1.0.0 -p 8080:8080 model-service:local
```

#### Advanced Configuration
You can customize the service by setting environment variables:

```bash
docker run \
  -e MODEL_VERSION=v1.0.0 \
  -e SERVICE_PORT=9000 \
  -e SERVICE_HOST=0.0.0.0 \
  -p 9000:9000 \
  model-service:local
```

View logs:
```bash
docker logs model-service-instance
```

Stop the container:
```bash
docker stop model-service-instance
docker rm model-service-instance
```
