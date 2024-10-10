#!/usr/bin/env python3
"""
This module provides a function for summing all the elements in a list of
floating-point numbers.

The primary function, `sum_list`, takes a list of floats and returns their
sum as a float value.

Functions:
    - sum_list(input_list: list[float]) -> float: Sums up the elements in a
    list of floats and returns the total.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sums up all the elements in a list of floating-point numbers.

    Args:
        input_list (list[float]): A list of floating-point numbers to sum.

    Returns:
        float: The sum of all the elements in the input list.

    Example:
        >>> sum_list([1.5, 2.3, 3.1])
        6.9
    """
    total = 0.0
    for i in input_list:
        total += i
    return total
