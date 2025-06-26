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
    tags:
      - prediction
    consumes:
      - application/json
    produces:
      - application/json
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - review
          properties:
            review:
              type: string
              description: The text review to be analyzed
              example: "This movie was great!"
    responses:
      200:
        description: Prediction successful
        schema:
          type: object
          properties:
            review:
              type: string
              description: The original review text
            prediction:
              type: integer
              description: The sentiment prediction (0 for negative, 1 for positive)
              enum: [0, 1]
            prediction_confidence:
              type: number
              format: float
              description: Confidence score of the prediction
              minimum: 0
              maximum: 1
      400:
        description: Invalid request (missing or invalid parameters)
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
    prediction = int(model.predict(feature_vector)[0])

    # Get the prediction probabilities
    probabilities = model.predict_proba(feature_vector)[0]
    prediction_proba = round(float(probabilities[prediction]), 4)

    # Prepare the response
    res = {
        "review": review,
        "prediction": prediction,
        "prediction_confidence": prediction_proba,
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
    return jsonify({"status": "healthy and running"})

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
