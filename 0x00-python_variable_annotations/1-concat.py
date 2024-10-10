#!usr/bin/env python3
"""
This module provides a function for concatenating two strings.

The primary function, `concat`, takes two strings as input and returns their
concatenation as a single string.

Functions:
    - concat(str1: str, str2: str) -> str: Concatenates two strings and
    returns the result.
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenates two strings.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        str: The concatenated result of the two input strings.

    Example:
        >>> concat("Hello, ", "World!")
        'Hello, World!'
    """
    return str1 + str2
