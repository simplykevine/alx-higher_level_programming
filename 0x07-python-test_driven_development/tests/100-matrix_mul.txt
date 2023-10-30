'''
# Import the required function
>>> from importlib import import_module
>>> matrix_mul = import_module('100-matrix_mul').matrix_mul

# Valid arguments
>>> print(matrix_mul([[13, 12]], [[31], [21]]))
[[655]]
>>> print(matrix_mul([[6, 8], [3, 7]], [[12, 3], [3, 4]]))
[[96, 50], [57, 37]]
>>> print(matrix_mul([[3, 19, 7], [11, 12, 5], [2, 4, 8]], [[12, 3], [9, 4], [15, 2]]))
[[312, 99], [315, 91], [180, 38]]

# Invalid arguments
>>> try:
...     print(matrix_mul(12, [[4, 6]]))
... except TypeError as ex:
...     print(ex.args[0])
m_a must be a list
>>> try:
...     print(matrix_mul([[4, 6]], 12))
... except TypeError as ex:
...     print(ex.args[0])
m_b must be a list
>>> try:
...     print(matrix_mul(['[4, 6]'], 12))
... except TypeError as ex:
...     print(ex.args[0])
m_b must be a list
>>> try:
...     print(matrix_mul([(4, 6)], [12]))
... except TypeError as ex:
...     print(ex.args[0])
m_a must be a list of lists
>>> try:
...     print(matrix_mul([[4, 6]], [(12, )]))
... except TypeError as ex:
...     print(ex.args[0])
m_b must be a list of lists
>>> try:
...     print(matrix_mul([], [[12]]))
... except ValueError as ex:
...     print(ex.args[0])
m_a can't be empty
>>> try:
...     print(matrix_mul([['2', '3']], [[]]))
... except ValueError as ex:
...     print(ex.args[0])
m_b can't be empty
>>> try:
...     print(matrix_mul([[]], [[12]]))
... except ValueError as ex:
...     print(ex.args[0])
m_a can't be empty
>>> try:
...     print(matrix_mul([[], []], [[12]]))
... except ValueError as ex:
...     print(ex.args[0])
m_a can't be empty
>>> try:
...     print(matrix_mul([[1, 6], [3, 3]], [[]]))
... except ValueError as ex:
...     print(ex.args[0])
m_b can't be empty
>>> try:
...     print(matrix_mul([[4, '6', 8]], [[12]]))
... except TypeError as ex:
...     print(ex.args[0])
m_a should contain only integers or floats
>>> try:
...     print(matrix_mul([[4, '6', 8]], [['12']]))
... except TypeError as ex:
...     print(ex.args[0])
m_a should contain only integers or floats
>>> try:
...     print(matrix_mul([[4, 6, 8], []], [[(12, )]]))
... except TypeError as ex:
...     print(ex.args[0])
m_b should contain only integers or floats
>>> try:
...     print(matrix_mul([[4, 6, 8], []], [[12, 3]]))
... except TypeError as ex:
...     print(ex.args[0])
each row of m_a must be of the same size
>>> try:
...     print(matrix_mul([[4, 6, 8], [1, 2, 3]], [[12, 3], []]))
... except TypeError as ex:
...     print(ex.args[0])
each row of m_b must be of the same size
>>> try:
...     print(matrix_mul([[4, 6, 8], [1]], [[12, 3]]))
... except TypeError as ex:
...     print(ex.args[0])
each row of m_a must be of the same size
>>> try:
...     print(matrix_mul([[4, 6, 8], [4, 4, 4]], [[12, 3], [7]]))
... except TypeError as ex:
...     print(ex.args[0])
each row of m_b must be of the same size
>>> try:
...     print(matrix_mul([[4, 6, 8], [1, 3, 7]], [[12, 3]]))
... except ValueError as ex:
...     print(ex.args[0])
m_a and m_b can't be multiplied
>>> try:
...     print(matrix_mul([[6, 8], [3, 7]], [[12, 3], [3.5, 4], [15, 5]]))
... except ValueError as ex:
...     print(ex.args[0])
m_a and m_b can't be multiplied

'''
