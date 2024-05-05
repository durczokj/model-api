import os, sys
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..')))

from utils.predictor import Predictor
from utils.get_config import get_config

config = get_config()

def get_index():
    return {"prediction_route": "/predict",
            "expected_features": config["EXPECTED_FEATURES"]}
