#!/usr/bin/env python3
"""
This module provides a function for creating a key-value tuple.

The primary function, `to_kv`, takes a string key and a numerical value
(integer or float), and returns a tuple where the first element is the
string key and the second element is the square of the numerical value.

Functions:
    - to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]: Creates a
      tuple from a string key and the square of a numerical value.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Creates a tuple from a string key and the square of a numerical value.

    Args:
        k (str): The string key.
        v (Union[int, float]): The numerical value (int/ float) to be squared.

    Returns:
        tuple: A tuple where the first element is the string key and the
        second element is the square of the numerical value.

    Example:
        >>> to_kv("age", 4)
        ('age', 16.0)
        >>> to_kv("height", 2.5)
        ('height', 6.25)
    """
    return (k, float(v ** 2))
