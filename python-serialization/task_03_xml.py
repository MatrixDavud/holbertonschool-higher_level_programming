#!/usr/bin/python3
"""Serializing and Deserializing XML files."""
import xml.etree.ElementTree as ET
from collections import defaultdict


def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary into an XML file."""

    def build_xml_element(parent, key, value):
        """Build xml elements to create and write the tree to xml file."""
        if isinstance(value, dict):
            child = ET.SubElement(parent, key)
            for k, v in value.items():
                build_xml_element(child, k, v)

        elif isinstance(value, list):
            for item in value:
                build_xml_element(parent, key, item)

        else:
            child = ET.SubElement(parent, key)
            child.text = str(value)

    root = ET.Element("data")

    for k, v in dictionary.items():
        build_xml_element(root, k, v)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """Deserialize an XML file into a Python dictionary."""

    def parse_element(elem):
        """Parse each elements of the xml tree."""
        children = list(elem)
        if not children:
            return elem.text

        grouped = defaultdict(list)
        for child in children:
            grouped[child.tag].append(parse_element(child))

        result = {}
        for tag, values in grouped.items():
            if len(values) == 1:
                result[tag] = values[0]
            else:
                result[tag] = values
        return result

    tree = ET.parse(filename)
    root = tree.getroot()

    return parse_element(root)
