#!/usr/bin/python3
"""
This module provides a function that adds two integers.
The inputs must be integers or floats (which are cast to integers).
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats (cast to integers).

    Raises:
        TypeError: If a or b are not int or float.
        ValueError: If a or b are NaN or infinite.
    """
    for arg, name in ((a, 'a'), (b, 'b')):
        if not isinstance(arg, (int, float)):
            raise TypeError(f"{name} must be an integer")
        if isinstance(arg, float) and (
            arg != arg or arg in (float('inf'), float('-inf'))
        ):
            raise ValueError(f"{name} must be a finite number")

    return int(a) + int(b)
