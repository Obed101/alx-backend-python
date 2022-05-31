#!/usr/bin/env python3
"""This module parametizes a unit test"""
from typing import Any, Mapping, Sequence
import unittest
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Tests utils.access_nested_map function"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",)),
        ({"a": {"b": 2}}, ("a", "b"))
        ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, output: Any) -> Any:
        """This function tests access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), output)

    @parameterized.expand([
        ({}, ["a"]),
        ({"a": 1}, ["a", "b"])
        ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence, output: Any) -> Any:
        """Tests to see if access_nasted_map raises exception"""
        with self.assertRaises(KeyError) as raised:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test case for json getter"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, payload):
        """testing result"""
        with patch('utils.get_json', return_value=payload) as mock:
            mock(url)
            mock.assert_called_once_with(url)


class TestMemoize(unittest.TestCase):
    """This class tests memoization"""

    def test_memoize(self):
        """Memoization test method"""

        class TestClass:
            """inner test class"""

            def a_method(self):
                """returns int"""
                return 42

            @memoize
            def a_property(self):
                """property method"""
                return self.a_method

        with patch.object(TestClass, 'a_method') as mocker:
            tester = TestClass()
            tester.a_property
            tester.a_property

            mocker.assert_called_once
