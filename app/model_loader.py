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
    model_version = os.getenv("MODEL_VERSION")
    model_path = f".cache/model-{model_version}.joblib"
    if not os.path.exists(model_path):
        # If the model does not exist, download it
        print("Model not found in cache. Downloading...")
        model_path = download_model()
    model = joblib.load(model_path)
    print("Model loaded")


def download_model():
    """
    Download the model from a GitHub Release and save it in the .cache directory.
    """
    model_version = os.getenv("MODEL_VERSION")

    url = f"https://github.com/remla2025-team9/model-training/releases/download/{model_version}/model.joblib"

    print(f"Downloading model from: {url}")
    response = requests.get(url, allow_redirects=True)
    response.raise_for_status()

    os.makedirs(".cache", exist_ok=True)
    
    model_path = f".cache/model-{model_version}.joblib" 
    with open(model_path, "wb") as f:
        f.write(response.content)
        
    print(f"Model saved to: {model_path}")
    return model_path