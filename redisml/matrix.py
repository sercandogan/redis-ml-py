from .commands import MatrixCommand
import numpy as np


class Matrix(object):
    """
        Implementation of Redis-ML Matrix Operations
    """

    def __init__(self, data, name, conn, dtype=None):

        if dtype is None:
            dtype = float

        self.data = np.array(data, dtype=dtype)
        ndim = self.data.ndim
        self.shape = self.data.shape
        if ndim > 2:
            raise ValueError("matrix must be 2-dimensional")
        elif ndim == 0:
            self.shape = (1, 1)
        elif ndim == 1:
            self.shape = (1, self.shape[0])

        self.name = name
        self.conn = conn

        self._set()

    def _set(self):
        """
            Set the matrix
        """
        nrow = self.shape[0]
        ncol = self.shape[1]
        self.conn.execute_command(MatrixCommand.SET, self.name, nrow, ncol, *self.data.flatten())

    def get(self):
        return self.get_from_redis()

    def get_from_redis(self):
        data = self.conn.execute_command(MatrixCommand.GET, self.name)

        if data:
            nrow = data[0]
            ncol = data[1]
            data = [float(x) for x in data[2:]]
            data = np.array(data).reshape(nrow, ncol)
            return data
        return False

    def __add__(self, other):
        self.conn.execute_command(MatrixCommand.ADD, self.name, other.name, 'add')

    def __mul__(self, other):
        self.conn.execute_command(MatrixCommand.MULTIPLY, self.name, other.name, 'mul')

    def scale(self, scalar):
        self.conn.execute_command(MatrixCommand.SCALE, self.name, scalar)
