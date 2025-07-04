#!/usr/bin/python3
"""Script that creates an Object from a “JSON file”."""
import json


def load_from_json_file(filename):
    """Load JSON file into python object."""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
