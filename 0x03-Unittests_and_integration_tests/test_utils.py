#!/usr/bin/env python3
"""This module parametizes a unit test"""
from typing import Any, Mapping, Sequence
import unittest
from utils import access_nested_map
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

    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence, output: Any) -> Any:
        """Tests to see if access_nasted_map raises exception"""
        with self.assertRaises(KeyError) as raised:
            access_nested_map(nested_map, path)

        self.assertEqual(str(raised.exception)[1:-1], output)
