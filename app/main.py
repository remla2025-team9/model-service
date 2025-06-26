import os
from flask import Flask
from flasgger import Swagger
from app.model_loader import load_model
from app.config import SERVICE_HOST, SERVICE_PORT, FLASK_DEBUG

app = Flask(__name__)
swagger = Swagger(app)

if __name__ == "__main__":
    # Downloaded the model and vectorizer if they are not already cached
    load_model()

    # Start the Flask app
    from app import routes
    app.register_blueprint(routes.bp)
    app.run(host=SERVICE_HOST, port=SERVICE_PORT, debug=FLASK_DEBUG)
