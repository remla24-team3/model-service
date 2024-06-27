""" Main application file. """

from flask import Flask, request, jsonify
from flasgger import Swagger
from lib_ml_group3.load_model import load_model

model = load_model(
    "model/model.keras", "model/encoder.pickle", "model/tokenizer.pickle"
)

app = Flask(__name__)
swagger = Swagger(app)


@app.route("/API/v1.0/predict", methods=["GET", "POST"])
def predict():
    """
    Endpoint for making predictions.
    ---
    parameters:
      - name: url
        in: query
        type: string
        required: true
        description: The URL of the input data.
    responses:
      200:
        description: The predicted value.
        schema:
          type: string
    """
    url = str(request.args["url"])
    prediction = model.predict([url])[0]
    return jsonify(prediction=prediction)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=105, debug=True)
