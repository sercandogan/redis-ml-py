# redis-ml-py

It's python client of Redis-ML.
It basically provide a basis for real-time machine learning apps.

Primary Algorithms of Client:
* Linear Regression
* Logistic Regression
* Matrix Operations


## Dependencies
* redis and redis-ml module
* numpy

## How to use

### Linear Regression
Coefficients' keys and values are stored. 

```python
from redisml import LinearRegression

r = redis.StrictRedis(host='localhost', port=6379)
model = LinearRegression('cars', r)
# Model Coefficients
coefficients = {
    "intercept": -22.657,
    "speed": 4.316
}
# Inputs to predict
inputs = {
    "speed": 10
}

model.set(**coefficients)
dist = model.predict(**inputs)
print(dist)
# 20.502999999999997
```
### Logistic Regression

Default cut-off point is 0.5.
Coefficients' keys and values are stored.
```python
from redisml import LogisticRegression

r = redis.StrictRedis(host='localhost', port=6379)
model = LogisticRegression('titanic', r)
# Model Coefficients
coefficients = {
    "intercept": 5.137627,
    "Pclass": -1.087156,
    "Sexmale": -2.756819,
    "Age": -0.037267,
    "SibSp": -0.292920
}
# Inputs to predict
inputs = {
    "Pclass": 1,
    "Sexmale": 0,
    "Age": 24,
    "SibSp": 3
}

model.set(**coefficients)
survived_or_not = model.predict(**inputs)
print(survived_or_not)
#0 
```
### Matrix Operations

First, let's create a matrix
```python
from redisml import Matrix
import numpy

r = redis.StrictRedis(host='localhost', port=6379)

matrix_1 = numpy.array(((1.23, 212.123, 3,), (4.10, 5, 6), (7, 8, 9))) 
a = Matrix('a', r)
a.set(matrix_1)
print(a.get())

# [[  1.23  212.123   3.   ]
#  [  4.1     5.      6.   ]
#  [  7.      8.      9.   ]]
```
then let's create another matrix and perform the operations
```python
matrix_2 = numpy.array(((9, 8, 7), (6, 5, 4), (3, 2, 1)))
b = Matrix('b', r)
b.set(matrix_2)
```
Adds two matrices
```python
c = Matrix('c', r)
c.add(a, b) # adds two matrices
print(c.get())

# [[ 10.23  220.123  10.   ]
#  [ 10.1    10.     10.   ]
#  [ 10.     10.     10.   ]]
```
Multilplies two matrices
```
d = Matrix('d', r)
d.multiply(b, c) # Multiplies the matrices
print(d.get())

# [[ 242.87  2131.107  240.   ]
#  [ 151.88  1410.738  150.   ]
#  [  60.89   690.369   60.   ]]
```
Scale matrix with scalar
```
scalar = 3.14
d.scale(scalar)
print(d.get())
# [[ 762.6118  6691.67598  753.6    ]
#  [ 476.9032  4429.71732  471.     ]
#  [ 191.1946  2167.75866  188.4    ]]
```

 
## TODO
* K-Means Implementation
* RandomForest Implementation