#!/usr/bin/python3
"""
This module provides a function that prints a text with two new lines
after each of these characters: '.', '?' and ':'.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after '.', '?', and ':'.

    Args:
        text (str): The input string to format.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_line_chars = ['.', '?', ':']
    current = ""
    for char in text:
        current += char
        if char in new_line_chars:
            print(current.strip(), end="\n\n")
            current = ""
    if current.strip():
        print(current.strip(), end="")
