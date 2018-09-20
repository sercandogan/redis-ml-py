from enum import Enum


class LinRegCommand(Enum):
    SET = 'ML.LINREG.SET'
    PREDICT = 'ML.LINREG.PREDICT'

    def __get__(self, *args):
        return self.value


class LogRegCommand(Enum):
    SET = 'ML.LOGREG.SET'
    PREDICT = 'ML.LOGREG.PREDICT'

    def __get__(self, *args):
        return self.value


class MatrixCommand(Enum):
    SET = 'ML.MATRIX.SET'
    GET = 'ML.MATRIX.GET'
    ADD = 'ML.MATRIX.ADD'
    MULTIPLY = 'ML.MATRIX.MULTIPLY'
    SCALE = 'ML.MATRIX.SCALE'

    def __get__(self, *args):
        return self.value
