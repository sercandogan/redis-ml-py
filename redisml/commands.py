from enum import Enum


class LinReg(Enum):
    SET = 'ML.LINREG.SET'
    PREDICT = 'ML.LINREG.PREDICT'

    def __get__(self, *args):
        return self.value


class LogReg(Enum):
    SET = 'ML.LOGREG.SET'
    PREDICT = 'ML.LOGREG.PREDICT'

    def __get__(self, *args):
        return self.value
