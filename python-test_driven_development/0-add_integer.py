#!/usr/bin/python3
"""
This module provides a function that adds two integers.
The inputs must be integers or floats (which are cast to integers).
"""

def add_integer(a, b=98):
    """
    Returns the sum of two integers (after casting floats to ints).
    Raises TypeError if a or b are not int or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
