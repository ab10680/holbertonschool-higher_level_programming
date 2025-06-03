#!/usr/bin/python3
"""
Returns the dictionary description for JSON serialization of an object.
"""


def class_to_json(obj):
    """Converts object attributes to a serializable dictionary."""
    return obj.__dict__
