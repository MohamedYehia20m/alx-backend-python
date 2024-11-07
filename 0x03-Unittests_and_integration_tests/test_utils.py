#!/usr/bin/env python3
"""
Unit tests for the utils.access_nested_map function.

This module contains a unit test class that tests the functionality of
accessing values within a nested dictionary structure by following a sequence
of keys (path). The tests are parameterized to cover multiple cases.
"""

import unittest
from typing import Any, Dict, Tuple
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Test case for the access_nested_map function in the utils module.

    This class contains parameterized test methods to validate that the
    access_nested_map function returns the correct values for various nested
    dictionary structures and key paths.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
        self, nested_map: Dict[str, Any], path: Tuple[str, ...], expected: Any
    ) -> None:
        """
        Test access_nested_map with various nested maps and paths.

        Args:
            nested_map (Dict[str, Any]): The nested dictionary to access.
            path (Tuple[str, ...]): The sequence of keys to follow in the
            nested dictionary.
            expected (Any): The expected result after accessing the path.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == "__main__":
    unittest.main()
