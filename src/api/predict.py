import os, sys, pickle
sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..')))

from utils.predictor import Predictor
from utils.get_config import get_config

config = get_config()

with open(config["MODEL_FILE_NAME"], 'rb') as f_in:
    model = pickle.load(f_in)

predictor = Predictor(expected_features=config["EXPECTED_FEATURES"], model = model)

def predict(request):
    return predictor.predict(request)
