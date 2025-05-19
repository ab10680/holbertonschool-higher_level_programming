#!/usr/bin/python3
"""Defines a class Square with size validation, area computation, and accessors."""


class Square:
    """Represents a square with validated size."""

    def __init__(self, size=0):
        """Initialize the square with a given size."""
        self.size = size  # use the setter to validate

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (int): The new size to set.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2
