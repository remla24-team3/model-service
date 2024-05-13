""" Main application file. """

from flask import Flask, request
from lib_ml_group3.load_model import load_model

model = load_model(
    "model/model.keras", "model/encoder.pickle", "model/tokenizer.pickle"
)
app = Flask(__name__)


@app.route("/API/v1.0/predict", methods=["GET", "POST"])
def predict():
    """
    Endpoint for making predictions.

    This endpoint expects a URL parameter called 'url'
    which represents the URL of the input data.

    Returns:
        str: The predicted value.

    """
    url = str(request.args["url"])
    return model.predict([url])[0]


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=105, debug=True)
