import joblib
import requests
import os

model = None

def init():
    """
    Load the model, downloading it if necessary.
    """
    global model
    print("Loading model...")
    model_path = ".cache/model-v0.0.0.joblib"
    if not os.path.exists(model_path):
        # If the model does not exist, download it
        print("Model not found in cache. Downloading...")
        model_path = download_model()
    model = joblib.load(model_path)
    print("Model loaded")


def download_model():
    """
    Download the model from GitHub Packages and save it in the .cache directory.
    """
    model_version = os.getenv("MODEL_VERSION")
    url = f"https://github.com/remla2025-team9/model-training/releases/download/{model_version}/sentiment-pipeline-{model_version}.joblib"  # Replace with the actual URL

    response = requests.get(url)
    response.raise_for_status()  # Raise an error for failed requests

    os.makedirs(".cache", exist_ok=True)
    model_path = ".cache/model.joblib"
    with open(model_path, "wb") as f:
        f.write(response.content)
    return model_path