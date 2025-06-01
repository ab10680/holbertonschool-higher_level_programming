#!/usr/bin/python3
"""Defines a class BaseGeometry with an area method."""


class BaseGeometry:
    """Base class for geometry operations."""

    def area(self):
        """Raise exception because area is not implemented."""
        raise Exception("area() is not implemented")
