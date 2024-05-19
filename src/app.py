from flask import Flask, request, jsonify
from predict import predict
from get_config import get_config

config = get_config()

app = Flask(__name__)

@app.route("/")
def get_index():
    return {"prediction_route": "/predict",
            "expected_features": config["EXPECTED_FEATURES"]}

@app.route('/predict', methods=['GET'])
def predict_from_request():
    try:
        result = predict(request)
    except Exception as e:
        result = str(e)
    
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("3000"), debug=False)
