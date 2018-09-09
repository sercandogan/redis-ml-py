def get_coef_list(**features):
    return to_list(**get_coefficients(**features))


def get_coefficients(**features):
    features.pop('intercept', None)
    return features


def to_list(**features):
    return features.values()


def get_intercept(**features):
    intercept = features.get('intercept', 0)
    return intercept
