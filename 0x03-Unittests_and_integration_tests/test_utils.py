#!/usr/bin/env python3
"""unittests using nested maps.
"""
import unittest
from unittest import TestCase, mock
from parameterized import parameterized
from requests import patch
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize
from typing import Dict, Mapping, Sequence


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
        self, 
        nested_map: Mapping, 
        path: Sequence, 
        expected: int) -> None:
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
    """TestGetJson class"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @mock.patch("requests.get")
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
        mock_request_get.assert_called_with(test_url)

class TestMemoize(unittest.TestCase):
    """test memoize class"""
    def test_memoize(self)  -> None:
        """Test memoize method
        that has a method and a property and
        checks if the method is called once
        by using the property twice to get the value
        """
        class TestClass:
            """TestClass class for testing memoize method
            """
            def a_method(self):
                """a_method method used by a_property method
                to get the value of the property and cache it
                by using the memoize decorator
                """
                return 42

            @memoize
            def a_property(self):
                """a_property method that uses a_method method
                to get the value of the property and cache it
                by using the memoize decorator and return it
                """
                return self.a_method()
        with patch.object(TestClass, "a_method") as mock_object:
            test = TestClass()
            test.a_property()
            test.a_property()
            mock_object.assert_called_once()


if __name__ == "__main__":
    unittest.main()
