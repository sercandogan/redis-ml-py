from .commands import LinRegCommand
from redisml.utils import (get_coefficients,
                           get_coef_list,
                           get_intercept)


class LinearRegression(object):
    """
        Implementation of Redis-ML Linear Regression Commands

    """

    def __init__(self, model_name, conn):
        """
        It uses the redis hash for saving model intercept and slope coefficients.
        The key of coefficients is {model_name}_attributes

        :param model_name: Model Name
        :param conn: Redis connection using whether strict redis or connection pool

        """
        self.conn = conn
        self.model_name = model_name
        self.hkey = '{0}_attributes'.format(self.model_name)
        self.attributes = self.get_attributes

    def set(self, **features):
        """
        Sets predictor's intercept and slope coefficients to redis using redis-ml command.

        :param features: Features dictionary consist of intercept and coefficients
        """
        self.attributes = self.to_redis_hash(**features)
        intercept = get_intercept(**features)
        coefficients = get_coef_list(**features)
        self.conn.execute_command(LinRegCommand.SET, self.model_name, intercept, *coefficients)

    def predict(self, **features):
        """
        Predicts output by given features
        :param features: Features (independent variables' values)
        :return: float Output (dependent variable)
        """
        if self.attributes is None:
            raise Exception('Attribute not found.')
        features = self.to_sorted_list(**features)
        y = self.conn.execute_command(LinRegCommand.PREDICT, self.model_name, *features)
        return float(y)

    def to_sorted_list(self, **features):
        """
        Dict to list ordered by attribute dict's keys in order to send predict function
        :param features: Features
        :return: Features list
        """
        features_list = list()
        coefficients = get_coefficients(**self.attributes)
        for key in coefficients.keys():
            features_list.append(features.get(key, 0))
        return features_list

    def to_redis_hash(self, **features):
        """
        Add features to redis as dict
        """
        if self.conn.hmset(self.hkey, features):
            return features
        return False

    @property
    def get_attributes(self):
        """
        Get model's attributes from redis
        :return:
        """
        if self.conn.exists(self.hkey):
            attributes = self.conn.hgetall(self.hkey)
            return {key.decode('utf-8'): float(value) for (key, value) in attributes.items()}
        return None
