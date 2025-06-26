#!/usr/bin/python3
"""Script with Geometry class."""


BaseGeometry = __import__('9-rectangle').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inherited from BaseGeometry class."""

    def __init__(self, width, height):
        """Initialize rectangle with width and height and validate both."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return rectangle area."""
        return self.__height * self.__width

    def __str__(self):
        """Display Rectangle with its width and height."""
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """Square class inherited from Rectangle class."""

    def __init__(self, size):
        """Initialize square with size and validate it."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return square area."""
        return self.__size ** 2
