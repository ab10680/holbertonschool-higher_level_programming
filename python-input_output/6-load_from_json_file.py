#!/usr/bin/python3
"""
Creates a Python object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """Reads from a JSON file and returns the corresponding Python object."""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
