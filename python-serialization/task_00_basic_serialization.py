#!/usr/bin/env python3
"""
Module: task_00_basic_serialization
Provides functions to serialize a Python dictionary to a JSON file,
and deserialize it back to a dictionary.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a dictionary and save it to a JSON file.

    Args:
        data (dict): Python dictionary to serialize.
        filename (str): Name of the file to save the JSON data to.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load and deserialize a JSON file into a dictionary.

    Args:
        filename (str): Name of the file containing the JSON data.

    Returns:
        dict: Deserialized Python dictionary.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

