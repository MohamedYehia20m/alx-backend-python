#!usr/bin/env python3
"""
This module provides a basic arithmetic function for adding two numbers.

The main function in this module is `add`, which takes two floating-point numbers 
as arguments and returns their sum. This can be used in various contexts where 
simple addition is needed.

Functions:
    - add(a: float, b: float) -> float: Returns the sum of two float numbers.
"""


def add(a: float, b: float) -> float:
    """
    Adds two floating-point numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of the two input numbers.

    Example:
        >>> add(2.5, 3.1)
        5.6
    """
    return a + b
