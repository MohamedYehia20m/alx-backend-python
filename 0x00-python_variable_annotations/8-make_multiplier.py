#!/usr/bin/env python3
"""
This module provides a function to create a multiplier function.

The primary function, `make_multiplier`, takes a float as a multiplier
and returns a function that multiplies a given float by the multiplier.

Functions:
    - make_multiplier(multiplier: float) -> Callable[[float], float]:
      Returns a function that multiplies a float by the given multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a given float by the multiplier.

    Args:
        multiplier (float): The multiplier to be used in multiplication.

    Returns:
        Callable[[float], float]: A function that takes a float and
        returns the product of that float and the multiplier.

    Example:
        >>> multiply_by_2 = make_multiplier(2.0)
        >>> multiply_by_2(3.0)
        6.0
        >>> multiply_by_2(4.5)
        9.0
    """

    def multiply(value: float) -> float:
        """Multiplies the given value by the multiplier."""
        return value * multiplier

    return multiply
