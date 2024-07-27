#!/usr/bin/env python3
"""unittests using nested maps.
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Mapping, Sequence


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence, expected: int) -> None:
        """Test access_nested_map method
        Args:
            nested_map (Mapping): A nested map
            path (Sequence): a sequence of key representing a path to the value
            expected (int): expected output
        """
        response = access_nested_map(nested_map, path)
        self.assertEqual(response, expected)

if __name__ == "__main__":
    unittest.main()
