# Getting started

## Running the Flask app locally

To run the Flask app locally, you need to have Python 3.11 or higher installed.

### Setting up a Virtual Environment

First, create and activate a virtual environment:

```bash
# Linux/macOS
python -m venv venv
source venv/bin/activate

# Windows (Command Prompt)
python -m venv venv
venv\Scripts\activate.bat

# Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1
```

After activating the virtual environment, install the required packages:

```bash
pip install .
```

### Environment Configuration

The application uses environment variables for configuration. You can set these up in two ways:

1. Create a `.env` file in the root directory using the provided template:
   ```bash
   # For Linux/macOS
   cp .env.template .env
   
   # For Windows
   copy .env.template .env
   ```

2. Or set the environment variables directly in your shell:
   ```bash
   # Linux/macOS
   export MODEL_VERSION=v0.0.3-pre.0
   export SERVICE_PORT=8080
   export SERVICE_HOST=0.0.0.0

   # Windows (Command Prompt)
   set MODEL_VERSION=v0.0.3-pre.0
   set SERVICE_PORT=8080
   set SERVICE_HOST=0.0.0.0

   # Windows (PowerShell)
   $env:MODEL_VERSION="v0.0.3-pre.0"
   $env:SERVICE_PORT="8080"
   $env:SERVICE_HOST="0.0.0.0"
   ```

Available environment variables:
```
MODEL_VERSION # The version of the model to use. This is required to run the application.
SERVICE_PORT  # The port on which the service will run. Default is 8080
SERVICE_HOST  # The host on which the service will run. Default is 0.0.0.0
```

Before starting the Flask app, you need to run the preprocessor loader once:

```bash
python app/preprocessor_loader.py
```

Then, you can run the Flask app using the following command:

```bash
python app/main.py
```

Then open localhost:8080 (or the port you specified) in your browser to see the app running.
You can see the API specification by going to localhost:8080/apidocs.

## Running in Docker

To run the Flask app in Docker, you need to have Docker installed on your machine.
You can pull the Docker image from the Github Container Registry using the following command:

```bash
docker pull ghcr.io/remla2025-team9/model-service:latest
```

This will pull the latest stable image of the model service.
If you prefer a specific version, you can specify the version tag in the command above.
Additionally, you can pull the latest release candidate by using the following command:

```bash
docker pull ghcr.io/remla2025-team9/model-service:latest-rc
```

As with the local version, you can specify the following environment variables. For example, we can set the model version, host an port, by defining the variables in the `docker run` command:
```bash
docker run -e MODEL_VERSION=v0.0.3-pre.0 -e SERVICE_PORT=9000 -e SERVICE_HOST=model-service.com -p 9000:9000 ghcr.io/remla2025-team9/model-service:latest
```

To ensure that the model is cached and not downloaded every time the container is started, a volume can be mounted
```bash
docker run -e MODEL_VERSION=v0.0.3-pre.0 -p 8080:8080 -v /path/to/cache:/root/.cache ghcr.io/remla2025-team9/model-service:latest
```