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
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")


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

    def __str__(self):
        """Display Square with its size."""
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
