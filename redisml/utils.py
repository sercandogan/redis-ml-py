def to_list(**features):
    return features.values()


def intercept(**features):
    intercept = features.get('intercept', 0)
    return intercept
