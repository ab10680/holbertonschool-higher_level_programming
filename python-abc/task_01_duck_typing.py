#!/usr/bin/env python3
"""Defines abstract Shape class and shape implementations using duck typing."""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Calculate area of shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate perimeter of shape."""
        pass


class Circle(Shape):
    """Circle with radius."""

    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be a positive number")
        self.__radius = radius  # Private attribute

    def area(self):
        return math.pi * (self.__radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    """Rectangle with width and height."""

    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Dimensions must be positive")
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)


def shape_info(obj):
    """Print area and perimeter of any shape object."""
    print(f"Area: {obj.area()}")
    print(f"Perimeter: {obj.perimeter()}")
