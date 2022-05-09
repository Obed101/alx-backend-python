#!/usr/bin/env python3
"""This module parametizes a unit test"""
from typing import Any, Mapping, Sequence
import unittest
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Tests utils.access_nested_map function"""
    @parameterized.expand([
        [{"a": 1}, ("a",), 1],
        [{"a": {"b": 2}}, ("a",)],
        [{"a": {"b": 2}}, ("a", "b")]
    ],)
    def __init__(self) -> None:
        """Instance initialiser"""
        super().__init__()

    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, output: Any) -> bool:
        """This function tests access_nested_map"""
        return self.assertEqual(access_nested_map(nested_map, path), output)

    def test_access_nested_map_exception(self, nested_map,
                                         path: Sequence, output: Any) -> bool:
        """Tests to see if access_nasted_map raises exception"""
        pass