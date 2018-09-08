import redis

from redisml import LinearRegression, LogisticRegression

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

model = LinearRegression('test', r)
model.set(**features)
y = model.predict(**predict_features)
print(y)

model2 = LogisticRegression('test2', r)
model2.set(**features)
y2 = model2.predict(**predict_features)
print(y2)
