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
        self.name = name
        if not isinstance(value, int):
            raise TypeError(f"{self.name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{self.name} must be greater than 0")
        self.value = value
