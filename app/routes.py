from flask import request, jsonify, Blueprint
from sentiment_analysis_preprocessing.preprocesser import Preprocessor
from app.model_loader import load_model
from app.version import __version__


bp = Blueprint('routes', __name__)

@bp.route("/v1/predict", methods=["POST"])
def predict():
    """
        Submit a review message to be predicted as positive or negative.
        ---
        consumes:
          - application/json
        parameters:
          - name: review
            in: body
            required: true
            schema:
              type: object
              properties:
                review:
                  type: string
            description: The review to be analyzed
        responses:
          200:
            description: Prediction result.
        """
    input_data = request.get_json()
    review = input_data.get("review")

    preprocessor = Preprocessor()
    processed_review = preprocessor.transform([review])

    # Load the model and vectorizer
    model, vectorizer = load_model()

    # Take the processed review and predict
    feature_vector = vectorizer.transform(processed_review)

    # Predict the sentiment
    prediction = model.predict(feature_vector)[0]

    # Prepare the response
    res = {
        "review": review,
        "prediction": int(prediction),
    }

    return jsonify(res)

@bp.route("/health", methods=["GET"])
def health():
    """
        Health check endpoint.
        ---
        responses:
          200:
            description: Service is healthy.
        """
    return jsonify({"status": "healthy"})

@bp.route("/version", methods=["GET"])
def version():
    """
        Version endpoint.
        ---
        responses:
          200:
            description: Service version.
        """
    return jsonify({"version": __version__})
