#!/usr/bin/env python3
"""
Uses the 'unittest' and 'parameterized' modules
to test 'utils.py'.
"""
import unittest
import parameterized
import utils
from typing import (
    Mapping,
    Sequence,
    Any,
)


class TestAccessNestedMap(unittest.TestCase):
    """
    Tests that 'utils.access_nested_map' works correctly.
    """
    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b", 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2)
        ]
    )
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence, expected: Any) -> None:
        """
        Tests that 'utils.access_nested_map' returns
        what it's supposed to.

        It is supposed to return the value at the end
        of the path through each nested mapping,
        like a file path:

        >>> access_nested_map({"a": 1}, ("a",))
        1
        >>> access_nested_map({"a": {"b": 2}}, ("a",))
        {"b": 2}
        >>> access_nested_map({"a": {"b": 2}}, ("a", "b"))
        2
        """
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)

    @parameterized.expand(
        [
            ({}, ("a",)),
            ({"a": 1}, ("a", "b"))
        ]
    )
    def test_access_nested_map_exception(self, nested_map: Mapping, path: Sequence) -> None:
        """
        Tests that inputting a path that's too long or wrong
        for the nested mapping results in 'utils.access_nested_map'
        to raise a KeyError with the first wrong key in 'path'
        as the error message.
        """
        with self.assertRaises(KeyError):
            utils.access_nested_map(nested_map, path)
