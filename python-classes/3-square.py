#!/usr/bin/python3
"""Defines a class Square with size validation and area computation."""


class Square:
    """Represents a square with validated size."""

    def __init__(self, size=0):
        """Initialize the square with a given size.

        Args:
            size (int): The size of the square. Must be >= 0.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2
