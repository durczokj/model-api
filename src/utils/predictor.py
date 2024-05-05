import numpy as np

class ExpectedFeaturesNotProvidedError(Exception):
    def __init__(self, missing_features):
        missing_features = ', '.join(missing_features)
        message = f"Feature(s) expected but missing: {missing_features}"
        super().__init__(message)

class Predictor:
    def __init__(
        self,
        expected_features,
        model):
        
        self.expected_features = expected_features
        self.model = model
    
    def __get_features(self, request):
        features = {}
        
        for feature in self.expected_features:
            value = request.args.get(feature, type=float)
            if value is not None:
                features[feature] = value
        
        missing_features = [feature for feature in self.expected_features if feature not in features.keys()]
        print(self.expected_features)
        print(features.values())
        print(missing_features)
        if len(missing_features) > 0:
            raise ExpectedFeaturesNotProvidedError(missing_features)
        
        return features
    
    def __get_prediction(self, features):
        freature_array = np.array(list(features.values()), ndmin = 2)    
        return self.model.predict(freature_array)[0]
    
    def predict(self, request):
        features = self.__get_features(request)
        prediction = self.__get_prediction(features)
        return self.__get_prediction(features)
