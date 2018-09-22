from .commands import MatrixCommand
import numpy as np


class Matrix(object):
    """
        Implementation of Redis-ML Matrix Operations
    """

    def __init__(self, matrix_name, conn):
        self.matrix_name = matrix_name
        self.conn = conn
        self.shape = None
        self.dtype = None

    def set(self, matrix):
        arr = np.array(matrix)
        shape = self.get_shape(arr)
        nrow = shape[0]
        ncol = shape[1]
        self.conn.execute_command(MatrixCommand.SET, self.matrix_name, nrow, ncol, *arr.flatten())

    def get(self):
        data = self.conn.execute_command(MatrixCommand.GET, self.matrix_name)

        if data:
            nrow = data[0]
            ncol = data[1]
            data = [float(x) for x in data[2:]]
            data = np.array(data).reshape(nrow, ncol)
            return data
        return False

    @staticmethod
    def get_shape(array):
        if not isinstance(array, np.ndarray):
            raise Exception('Its not a array')

        ndim = array.ndim
        shape = array.shape
        if ndim > 2:
            raise ValueError("matrix must be 2-dimensional")
        elif ndim == 0:
            shape = (1, 1)
        elif ndim == 1:
            shape = (1, shape[0])

        return shape
