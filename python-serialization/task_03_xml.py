#!/usr/bin/env python3
"""
Module: task_03_xml
Provides functions to serialize and deserialize a Python dictionary using XML.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a dictionary to an XML file.

    Args:
        dictionary (dict): Dictionary to serialize.
        filename (str): Name of the XML output file.
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize XML content from a file into a dictionary.

    Args:
        filename (str): Name of the XML input file.

    Returns:
        dict: Dictionary representation of the XML content.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        return {child.tag: child.text for child in root}
    except (ET.ParseError, FileNotFoundError):
        return {}
