#!/usr/bin/python3
"""
Module for generating Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle of size n.

    Args:
        n (int): The number of rows in Pascal's Triangle.

    Returns:
        list of list of ints: Pascal's Triangle up to n rows
    """

    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        # generate the next row
        previous_row = triangle[-1]
        new_row = [1]
        for j in range(1, len(previous_row)):
            # sum two adjacent elements from tthe previous row
            new_row.append(previous_row[j - 1] + previous_row[j])
        new_row.append(1)
        triangle.append(new_row)

    return triangle
