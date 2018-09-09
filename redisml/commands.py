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
