#!/usr/bin/python3
"""Defines a class Square with a private size attribute."""


class Square:
    """Represents a square with a private size."""

    def __init__(self, size):
        """Initialize the square with a given size.

        Args:
            size: The size of the square (no type/value check).
        """
        self.__size = size
