#!/usr/bin/python3
""" A function that divs a martix with a number """
'''
File_name: 0-rectangle.py
Created: 5-OCT-2023
Author: UMUTONI Kevine (simplykevine)
Size: Large
Project: 0x08-python-more_classes
Status: Not yet submitted.
'''


def matrix_divided(matrix, div):
    """"A function that divs a martix with a number"""
    if not isinstance(matrix, (list,)):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    for row in matrix:
        if type(row) != list:
            raise TypeError("matrix must be a matrix "
                            "(list of lists) of integers/floats")
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError("matrix must be a matrix"
                                " (list of lists) of integers/floats")
    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    mat_new = []
    for i in range(len(matrix)):
        mat_new.append(list())
        for j in range(len(matrix[i])):
            mat_new[i].append(round(matrix[i][j] / div, 2))
    return mat_new
