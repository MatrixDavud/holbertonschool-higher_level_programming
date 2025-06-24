#!/usr/bin/python3
"""Script with Geometry class."""


class BaseGeometry:
    """Geometry class."""

    def __init__(self):
        """Initialize object."""
        pass

    def area(self):
        """Raise an exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate the value passed as int."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
