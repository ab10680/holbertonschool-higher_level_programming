#!/usr/bin/env python3
"""
Module: task_02_csv
Converts CSV data into JSON format and saves it to data.json
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file to JSON format and save it to 'data.json'.

    Args:
        csv_filename (str): Path to the input CSV file.

    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        with open(csv_filename, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            data = [row for row in reader]

        with open("data.json", mode='w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=4)

        return True

    except FileNotFoundError:
        return False
    except Exception:
        return False
