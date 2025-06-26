"""
Configuration module for the model service.
Loads environment variables using python-dotenv.
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

# Required configuration
MODEL_VERSION = os.getenv("MODEL_VERSION", "v1.0.0")
if not MODEL_VERSION:
    raise ValueError("MODEL_VERSION environment variable is required")

# Service configuration
SERVICE_HOST = os.getenv("SERVICE_HOST", "0.0.0.0")
SERVICE_PORT = int(os.getenv("SERVICE_PORT", 8080))

# Flask configuration
FLASK_DEBUG = os.getenv("FLASK_DEBUG", "False").lower() in ("true", "1", "yes", "on")

# Derived configuration
BASE_URL = f"https://github.com/remla2025-team9/model-training/releases/download/{MODEL_VERSION}"
MODEL_URL = f"{BASE_URL}/model.joblib"
VECTORIZER_URL = f"{BASE_URL}/vectorizer.joblib"

MODEL_CACHE_PATH = os.path.join(".cache", MODEL_VERSION, "model.joblib")
VECTORIZER_CACHE_PATH = os.path.join(".cache", MODEL_VERSION, "vectorizer.joblib")
