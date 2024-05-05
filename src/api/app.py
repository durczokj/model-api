import os, sys
from flask import Flask, request, jsonify
from predict import predict
from get_index import get_index

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify(get_index())

@app.route('/predict', methods=['GET'])
def predict_from_request():
    try:
        result = predict(request)
    except Exception as e:
        result = str(e)
    
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("3000"), debug=True)
