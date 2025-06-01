#!/usr/bin/python3
"""Defines a function to check if object inherits from a class."""


def inherits_from(obj, a_class):
    """Return True if obj is instance of subclass (not the class itself)."""
    return isinstance(obj, a_class) and type(obj) is not a_class
