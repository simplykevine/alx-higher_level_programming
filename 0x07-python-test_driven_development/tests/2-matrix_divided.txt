Import `matrix_divided`

>>> matrix_divided = __import__('2-matrix_divided').matrix_divided

>>> matrix = [[1, 2, 3], [4, 5, 6]]

>>> matrix_divided(matrix, 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]

>>> matrix_divided(matrix, '3')
Traceback (most recent call last):
TypeError: div must be a number

>>> matrix_divided(matrix, 0)
Traceback (most recent call last):
ZeroDivisionError: division by zero

>>> matrix_divided(0, 3)
Traceback (most recent call last):
TypeError: matrix must be a matrix (list of lists) of integers/floats

>>> matrix_divided([[1, 3],[1]], 3)
Traceback (most recent call last):
TypeError: Each row of the matrix must have the same size

>>> matrix_divided(matrix, float('inf'))
[[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]

>>> matrix_divided([[1, 2, float('inf')], [4, 5, 6]], 3)
[[0.33, 0.67, inf], [1.33, 1.67, 2.0]]

>>> matrix_divided(matrix)
Traceback (most recent call last):
TypeError: matrix_divided() missing 1 required positional argument: 'div'

>>> matrix_divided()
Traceback (most recent call last):
TypeError: matrix_divided() missing 2 required positional arguments: 'matrix' and 'div'
