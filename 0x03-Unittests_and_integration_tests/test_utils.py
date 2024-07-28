#!/usr/bin/env python3
"""unittests using nested maps.
"""
import unittest
from parameterized import parameterized
from requests import patch
from utils import access_nested_map, get_json
from typing import Dict, Mapping, Sequence


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

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])

    def test_access_nested_map_exception(self, nested_map: Mapping, path: Sequence) -> None:
        """Test access_nested_map method with exception
        Args:
            nested_map (Mapping): A nested map
            path (Sequence): a sequence of key representing a path to the value
        """
        with self.assertRaises(Exception):
            access_nested_map(nested_map, path)

class TestGetJson(unittest.TestCase):
    """TestGetJson class
    """
    @parameterized.expand([
        ("http://example.com",{ "payload": True }),
        ("http://holberton.io", { "payload": False }),
    ])
    @patch('requests.get')
    def test_get_json(self, test_url: str, test_payload: Dict, mock_request_get) -> None:
        """
        Test get_json method
        Args:
            test_url (str): test url
            test_payload (Dict): test payload
            mock_request_get: mock request get
        """
        mock_request_get.return_value.json.return_value = test_payload
        response = get_json(test_url)
        self.assertEqual(response, test_payload)
        mock_request_get.assert_called_once_with(test_url)


if __name__ == "__main__":
    unittest.main()
