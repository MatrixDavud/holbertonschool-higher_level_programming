#!/usr/bin/python3
"""Creating a function that adds attribute to class if it's possible."""


def add_attribute(cls, attr_name, value):
    """Add an attribute and value to class if possible."""
    setattr(cls, attr_name, value)
