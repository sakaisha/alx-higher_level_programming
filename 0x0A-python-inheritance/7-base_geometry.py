#!/usr/bin/python3
"""
This module defines the BaseGeometry class as a base for geometry operations.
"""


class BaseGeometry:
    """Base class for geometry."""


    def area(self):
        """Calculate area - to be implemented in subclasses."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate integer values for geometry methods.

        Args:
            name (str): The name of the value.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        
        Returns:
            int: The validated integer value.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        else:
            return value
