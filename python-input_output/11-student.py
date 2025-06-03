#!/usr/bin/python3
"""
Student class with serialization and deserialization support.
"""


class Student:
    """Represents a student with basic attributes."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the Student.
        If attrs is a list of strings, only those attributes are returned.
        """
        if isinstance(attrs, list) and all(
            isinstance(attr, str) for attr in attrs
        ):
            return {
                attr: getattr(self, attr)
                for attr in attrs if hasattr(self, attr)
            }
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance using the json dict."""
        for key in json:
            setattr(self, key, json[key])
