# Getting started

## Running the Flask app locally

To run the Flask app locally, you need to have Python 3.11 or higher installed.
After cloning the repository, install the required packages using pip:

```bash
pip install .
```
Before running the application you can configure the following environment variables:
```bash
MODEL_VERSION # The version of the model to use. This is required to run the application.
SERVICE_PORT # The port on which the service will run. Default is 8080
SERVICE_HOST # The host on which the service will run. Default is 0.0.0.0
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