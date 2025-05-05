from setuptools import setup, find_packages
from app.version import __version__

setup(
    name="model_service",
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Flask~=3.1.0",
        "flasgger~=0.9.7.1",
        "joblib~=1.5.0",
        "requests~=2.32.3",
        "sentiment-analysis-preprocessing @ git+https://github.com/remla2025-team9/lib-ml.git@v0.0.15",
    ],
    entry_points={
        "console_scripts": [
            "model-service=app.main:app",
        ],
    },
)