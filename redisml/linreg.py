from .commands import LinReg
from redisml.utils import (to_list,
                           intercept)


class LinearRegression(object):
    def __init__(self, model_name, conn):
        self.conn = conn
        self.model_name = model_name
        self.intercept = 0  # default model is without intercept.
        self.coefficients = None

    def set(self, **features):
        self.intercept = intercept(**features)
        features.pop('intercept', None)
        self.coefficients = features  # features has to be saved as dict without intercept.
        coefficients_list = to_list(**self.coefficients)
        self.conn.execute_command(LinReg.SET, self.model_name, self.intercept, *coefficients_list)

    def predict(self, **features):
        features = self.to_sorted_list(**features)
        y = self.conn.execute_command(LinReg.PREDICT, self.model_name, *features)
        return float(y)

    def to_sorted_list(self, **features):
        features_list = list()
        for key in self.coefficients.keys():
            features_list.append(features.get(key, 0))
        return features_list
