from flask import Flask
from flasgger import Swagger
from sentiment_analysis_preprocessing.preprocess import *
from app.model_loader import init

app = Flask(__name__)
swagger = Swagger(app)

if __name__ == "__main__":
    # Load the model
    init()

    port = os.getenv("SERVICE_PORT", 8080)
    host = os.getenv("SERVICE_HOST", "0.0.0.0")

    # Start the Flask app
    from app import routes
    app.register_blueprint(routes.bp)
    app.run(host=host, port=port, debug=True)
