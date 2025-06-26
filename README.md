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

4. **Configure environment variables**:
```bash
cp .env.template .env
```

Then edit the `.env` file with your preferred text editor and set the required values:

```bash
# Required
MODEL_VERSION=v1.0.0

# Optional (defaults shown)
SERVICE_HOST=0.0.0.0
SERVICE_PORT=8080
FLASK_DEBUG=False
```

To deactivate the virtual environment when you're done:
```bash
deactivate
```

### Environment Variables

The application uses a `.env` file for configuration. Copy the template and modify as needed:

| Variable        | Description                                   | Required | Default Value |
| --------------- | --------------------------------------------- | -------- | ------------- |
| `MODEL_VERSION` | The version of the model to use for inference | **Yes**  | None          |
| `SERVICE_HOST`  | The host address to bind the service to       | No       | 0.0.0.0       |
| `SERVICE_PORT`  | The port on which the service will run        | No       | 8080          |
| `FLASK_DEBUG`   | Enable Flask debug mode                       | No       | False         |

### Running the Application

Once you have configured your `.env` file and activated your virtual environment (if using one), run the Flask app:

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
docker logs {{ CONTAINER_NAME }}
```

Stop the container:
```bash
docker stop {{ CONTAINER_NAME }}
docker rm {{ CONTAINER_NAME }}
```
