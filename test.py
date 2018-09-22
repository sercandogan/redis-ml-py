import redis

import numpy
from redisml.matrix import Matrix
from redisml import LinearRegression, LogisticRegression
from redisml.utils import get_coefficients

r = redis.StrictRedis(host='192.168.99.100', port=6379, decode_responses=True)
print(r.ping())

a = numpy.array(((1.23, 212.123, 3,), (4.100000, 5, 6), (7, 8, 9)))
print(a)
b = Matrix('data', r)
b.set(a)
c = b.get()
print(c)
# b = Matrix(a, 'key', r)
# print(b)
# print(b.shape)

# features = {
#     'intercept': 1,
#     'road': 2,
#     'gas': 3,
#     'car_type': 4
# }
#
# predict_features = {
#     'gas': 1,
#     'road': 1,
#     'name': 1,
#     'asd': 1
# }
# predict_features2 = {
#     'gas': 0,
#     'road': 0,
#     'name': 0,
#     'asd': 0
# }
#
# model = LinearRegression('test', r)
# model.set(**features)
# y = model.predict(**predict_features)
# print(y)
#
# model2 = LinearRegression('test', r)
# y = model2.predict(**predict_features2)
# print(y)
# y = model2.predict(**predict_features)
# print(y)
#
# model3 = LogisticRegression('test2', r)
# model3.set(**features)
# y2 = model3.predict(**predict_features)
# print(y2)
#
# model4 = LogisticRegression('test2', r)
# y = model4.predict(**predict_features2)
# print(y)
