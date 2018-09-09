import redis

from redisml import LinearRegression, LogisticRegression
from redisml.utils import get_coefficients

r = redis.StrictRedis(host='192.168.99.100', port=6379)
print(r.ping())

features = {
    'intercept': 1,
    'road': 2,
    'gas': 3,
    'car_type': 4
}

predict_features = {
    'gas': 1,
    'road': 1,
    'name': 1,
    'asd': 1
}
predict_features2 = {
    'gas': 0,
    'road': 0,
    'name': 0,
    'asd': 0
}

model = LinearRegression('test', r)
model.set(**features)
y = model.predict(**predict_features)
print(y)

model2 = LinearRegression('test', r)
y = model2.predict(**predict_features2)
print(y)
y = model2.predict(**predict_features)
print(y)

model3 = LogisticRegression('test2', r)
model3.set(**features)
y2 = model3.predict(**predict_features)
print(y2)

model4 = LogisticRegression('test2', r)
y = model4.predict(**predict_features2)
print(y)
