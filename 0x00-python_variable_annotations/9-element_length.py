#!/usr/bin/env python3
"""
This module provides a function to calculate the length of elements
in a list.

The primary function, `element_length`, returns a list of tuples,
each containing an element from the input list and its length.

Functions:
    - element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
      Returns a list of tuples with elements and their corresponding lengths.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples, each containing an element from the
    input list and its length.

    Args:
        lst (Iterable[Sequence]): An iterable of sequences. The elements
        can be of any sequence type.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple
        contains an element from the input iterable and its length.

    Example:
        >>> element_length(["hello", "world", 123])
        [('hello', 5), ('world', 5), (123, 3)]
    """
    return [(i, len(i)) for i in lst]
