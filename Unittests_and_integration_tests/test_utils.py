#!/usr/bin/env python3
"""
Uses the 'unittest' and 'parameterized' modules
to test 'utils.py'.
"""
import unittest
from parameterized import parameterized
import unittest.mock
from fixtures import TEST_PAYLOAD
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
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
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


utils.requests.get = unittest.mock.patch('utils.requests.get')


class TestGetJson(unittest.TestCase):
    """
    Tests 'utils.get_json'.
    """
    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False})
        ]
    )
    @unittest.mock.patch(
        'utils.requests.get',
        new=unittest.mock.Mock(
            return_value=unittest.mock.Mock()
        )
    )
    def test_get_json(self, url: str, expected) -> None:
        """
        Tests that 'utils.get_json' returns
        the expected payload for each URL:

        "http://example.com" -> not the payload in 'fixtures.py'.
        "http://holberton.io" -> the payload in 'fixtures.py'

        Without actually making a request to those sites,
        and mocking 'utils.requests.get', as weitten above.
        """
        with unittest.mock.patch("utils.requests.get"):
            if expected["payload"]:

                self.assertEqual(
                    utils.get_json(url),
                    TEST_PAYLOAD
                )
