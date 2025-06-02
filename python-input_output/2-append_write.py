#!/usr/bin/python3
"""
Appends a string to the end of a UTF-8 text file
and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """Appends text to a file and returns number of characters added."""
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
