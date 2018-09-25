from .commands import MatrixCommand
import numpy as np


class Matrix(object):
    """
        Implementation of Redis-ML Matrix Operations
    """

    def __init__(self, matrix_name, conn):
        """
        Stores matrices and performs matrix operations
        :param matrix_name: The name of Matrix
        :param conn: Redis connector
        """
        self.matrix_name = matrix_name
        self.conn = conn

    def set(self, matrix):
        """
        Sets the matrix.
        :param matrix: numpy array/matrix or list
        :return: True or False
        """
        arr = np.array(matrix)
        shape = self.get_shape(arr)
        nrow = shape[0]
        ncol = shape[1]
        command = self.conn.execute_command(MatrixCommand.SET, self.matrix_name, nrow, ncol, *arr.flatten())
        if command:
            return True
        return False

    def get(self):
        """
        Gets the stored matrix as Numpy Array then reshapes it.
        :return: Numpy array
        """
        data = self.conn.execute_command(MatrixCommand.GET, self.matrix_name)

        if data:
            nrow = data[0]
            ncol = data[1]
            data = [eval(x) for x in data[2:]]
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

    def add(self, matrix_1, matrix_2):
        """
        Adds two matrices
        :param matrix_1: first matrix
        :param matrix_2: second matrix
        :return: True or False
        """
        if not isinstance(matrix_1, Matrix) or not isinstance(matrix_2, Matrix):
            raise Exception("Arguments' type must be Matrix")

        # Matrix dimensions control by Redis
        # if matrix_1.shape == matrix_2.shape

        command = self.conn.execute_command(MatrixCommand.ADD, matrix_1.matrix_name, matrix_2.matrix_name,
                                            self.matrix_name)

        if command:
            return True
        return False

    def multiply(self, matrix_1, matrix_2):
        """
        Multiplies two matrices.
        :param matrix_1: first matrix
        :param matrix_2: second matrix
        :return: True or False
        """
        if not isinstance(matrix_1, Matrix) or not isinstance(matrix_2, Matrix):
            raise Exception("Arguments' type must be Matrix")

        # Matrix dimensions are controled by Redis.
        # if matrix_1.shape[1] == matrix_2.shape[0]

        command = self.conn.execute_command(MatrixCommand.MULTIPLY, matrix_1.matrix_name, matrix_2.matrix_name,
                                            self.matrix_name)

        if command:
            return True
        return False

    def scale(self, scalar):
        """
        Scales a matrix.
        Updates the entries of the matrix stored in key by multiplying them with scalar.
        :param scalar: Scalar: int or float
        :return: True or False
        """
        if not isinstance(scalar, int) or isinstance(scalar, float):
            raise Exception('Scalar should be int or float')

        command = self.conn.execute_command(MatrixCommand.SCALE, self.matrix_name, scalar)

        if command:
            return True
        return False
