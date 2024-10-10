#!usr/bin/env python3
"""
This module provides a function for finding the floor value of a floating-point
number.

The primary function, `floor`, takes a floating-point number as input and
returns the largest integer less than or equal to the given number.

Functions:
    - floor(n: float) -> int: Returns the floor value of the given float.
"""


import math


def floor(n: float) -> int:
    """
    Returns the floor value of the given floating-point number.

    Args:
        n (float): The floating-point number for which to find the floor value.

    Returns:
        int: The largest integer less than or equal to the input number.

    Example:
        >>> floor(3.7)
        3
        >>> floor(-2.8)
        -3
    """
    return math.floor(n)
