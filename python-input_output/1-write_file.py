#!/usr/bin/python3
"""
Writes a string to a UTF-8 text file and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """Writes text to a file and returns number of characters written."""
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
