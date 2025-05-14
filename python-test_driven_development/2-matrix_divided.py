#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix
by a given number and returns a new matrix with the result rounded
to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """
    Divides each element of a matrix by div.

    Args:
        matrix: A list of lists of integers or floats.
        div: The number to divide by (must be int or float, not 0 or inf/nan).

    Returns:
        A new matrix with each value divided by div and rounded to 2 decimals.

    Raises:
        TypeError: If matrix is not a list of lists of ints/floats,
                   or if div is not a number or is inf/nan,
                   or if rows are not of equal size.
        ZeroDivisionError: If div is zero.
    """
    if not isinstance(matrix, list) or not all(
        isinstance(row, list) for row in matrix
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    if not all(
        isinstance(num, (int, float)) for row in matrix for num in row
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_len = len(matrix[0])
    if any(len(row) != row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if isinstance(div, float) and (
        div != div or div in (float('inf'), float('-inf'))
    ):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
