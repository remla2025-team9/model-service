from flask import request, jsonify, Blueprint
from sentiment_analysis_preprocessing.preprocess import *
from app.model_loader import model
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

    processed_review = prepare(review)

    prediction = model.predict(processed_review.toarray())[0]
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
