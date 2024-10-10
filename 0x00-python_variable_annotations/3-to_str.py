#!usr/bin/env python3
"""
This module provides a function for converting a floating-point number to
a string.

The primary function, `to_str`, takes a floating-point number as input and
returns its string representation.

Functions:
    - to_str(n: float) -> str: Converts a float to its string representation.
"""


def to_str(n: float) -> str:
    """
    Converts a floating-point number to a string.

    Args:
        n (float): The floating-point number to convert.

    Returns:
        str: The string representation of the input number.

    Example:
        >>> to_str(3.14)
        '3.14'
        >>> to_str(-1.0)
        '-1.0'
    """
    return str(n)
