#!/usr/bin/env python3
"""
This module provides a function for summing all the elements in a mixed list.

The primary function, `sum_mixed_list`, takes a list of integers and 
floating-point numbers and returns their sum as a float value.

Functions:
    - sum_mixed_list(mxd_lst: List[int | float]) -> float: Sums up the 
      elements in a mixed list of integers and floats and returns the total.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums up all the elements in a mixed list of integers and floats.

    Args:
        mxd_lst (List[int | float]): A list containing integers and/or 
        floating-point numbers to sum.

    Returns:
        float: The sum of all the elements in the input list.

    Example:
        >>> sum_mixed_list([1, 2.5, 3, 4.0])
        10.5
    """
    total: float = 0
    for i in mxd_lst:
        total += i
    return total
