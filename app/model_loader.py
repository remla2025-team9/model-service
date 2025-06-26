import joblib
import requests
import os
from app.config import (
    MODEL_URL,
    VECTORIZER_URL,
    MODEL_CACHE_PATH,
    VECTORIZER_CACHE_PATH
)

def load_model():
    """
    Load the model and the vectorizer, downloading them if necessary.
    """
    print("Loading model and vectorizer...")
    if not os.path.exists(MODEL_CACHE_PATH):
        # If the model does not exist, download it
        print("Model not found in cache. Downloading...")
        download_model()
    model = joblib.load(MODEL_CACHE_PATH)

    if not os.path.exists(VECTORIZER_CACHE_PATH):
        # If the vectorizer does not exist, download it
        print("Vectorizer not found in cache. Downloading...")
        download_vectorizer()
    vectorizer = joblib.load(VECTORIZER_CACHE_PATH)
    print("Model and vectorizer loaded")

    return model, vectorizer


def download_model():
    """
    Download the model from a GitHub Release and save it in the .cache directory.
    """
    print(f"Downloading model from: {MODEL_URL}")
    response = requests.get(MODEL_URL, allow_redirects=True)
    response.raise_for_status()

    os.makedirs(os.path.dirname(MODEL_CACHE_PATH), exist_ok=True)

    with open(MODEL_CACHE_PATH, "wb") as f:
        f.write(response.content)

    print(f"Model saved to: {MODEL_CACHE_PATH}")
    return MODEL_CACHE_PATH

def download_vectorizer():
    """
    Download the vectorizer from a GitHub Release and save it in the .cache directory.
    """
    print(f"Downloading vectorizer from: {VECTORIZER_URL}")
    response = requests.get(VECTORIZER_URL, allow_redirects=True)
    response.raise_for_status()

    os.makedirs(os.path.dirname(VECTORIZER_CACHE_PATH), exist_ok=True)

    with open(VECTORIZER_CACHE_PATH, "wb") as f:
        f.write(response.content)

    print(f"Vectorizer saved to: {VECTORIZER_CACHE_PATH}")
    return VECTORIZER_CACHE_PATH