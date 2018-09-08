from redisml.commands import LogReg
from redisml.utils import (intercept,
                           to_list)


class LogisticRegression(object):
    def __init__(self, model_name, conn, cutoff=0.5):
        self.conn = conn
        self.model_name = model_name
        self.intercept = 0  # default model is without intercept.
        self.coefficients = None
        self.cutoff = cutoff

    def set(self, **features):
        self.intercept = intercept(**features)
        features.pop('intercept', None)
        self.coefficients = features  # features has to be saved as dict without intercept.
        coefficients_list = to_list(**self.coefficients)
        self.conn.execute_command(LogReg.SET, self.model_name, self.intercept, *coefficients_list)

    def predict(self, **features):
        features = self.to_sorted_list(**features)
        y = self.conn.execute_command(LogReg.PREDICT, self.model_name, *features)
        return self.prob2binary(float(y))

    def to_sorted_list(self, **features):
        features_list = list()
        for key in self.coefficients.keys():
            features_list.append(features.get(key, 0))
        return features_list

    def prob2binary(self, cutoff):
        return 1 if cutoff > self.cutoff else 0
