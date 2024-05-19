import pickle
import numpy as np
from get_config import get_config

config = get_config()

class ExpectedFeaturesNotProvidedError(Exception):
    def __init__(self, missing_features):
        missing_features = ', '.join(missing_features)
        message = f"Feature(s) expected but missing: {missing_features}"
        super().__init__(message)

class _Predictor:
    def __init__(
        self,
        expected_features,