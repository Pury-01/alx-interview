#!/usr/bin/python3
"""module that rotates a 2D matrix at 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matriix 90 degrees clockwise in-place

    Args:
        matrix (list of list of int): the n xn 2D matrix to
        rotate
    Returns:
        None: matrix is edited in-place returning nothing
    """
    n = len(matrix)

    # swap rows with columns
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i],  matrix[i][j]

    # Reverse each row
    for row in matrix:
        row.reverse()
