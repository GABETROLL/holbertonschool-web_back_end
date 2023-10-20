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
from utils import memoize
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
    def test_access_nested_map(
        self,
        nested_map: Mapping,
        path: Sequence,
        expected: Any
    ) -> None:
        """
        Tests that 'utils.access_nested_map' returns
        what it's supposed to.

        It is supposed to return the value at the end
        of the path through each nested mapping,
        like a file path:

        >>> utils.access_nested_map({"a": 1}, ("a",))
        1
        >>> utils.access_nested_map({"a": {"b": 2}}, ("a",))
        {"b": 2}
        >>> utils.access_nested_map({"a": {"b": 2}}, ("a", "b"))
        2
        """
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)

    @parameterized.expand(
        [
            ({}, ("a",)),
            ({"a": 1}, ("a", "b"))
        ]
    )
    def test_access_nested_map_exception(
        self,
        nested_map:
        Mapping,
        path: Sequence
    ) -> None:
        """
        Tests that inputting a path that's too long or wrong
        for the nested mapping results in 'utils.access_nested_map'
        to raise a KeyError with the first wrong key in 'path'
        as the error message.

        >>> utils.access_nested_map({}, ("a",))
        KeyError
        >>> utils.access_nested_map({"a": 1}, ("a", "b"))
        KeyError
        """
        with self.assertRaises(KeyError):
            utils.access_nested_map(nested_map, path)


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
    def test_get_json(self, test_url: str, test_payload) -> None:
        """
        Tests that <utils.get_json>
        returns <test_payload> for <test_url>,
        while mocking <utils.requests.get> to return
        a mocked <utils.requests.Request> object that has the <json> method
        mocked to return <test_payload>.
        """
        with unittest.mock.patch(
            'utils.requests.get',
            new=unittest.mock.Mock(
                return_value=unittest.mock.Mock(
                    json=unittest.mock.Mock(
                        return_value=test_payload
                    )
                )
            )
        ):
            self.assertEqual(utils.get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """
    Tests the 'utils.memoize' decorator.
    """
    def test_memoize(self):
        """
        Tests that using 'utils.memoize' as a decorator
        on a method

        first runs the method normally, then returns
        the cached result of the method every other time.

        >>> class TestClass:
            def a_method(self):
                return 42
            @memoize
            def a_property(self):
                return self.a_method()

        >>> t = TestClass()
        >>> t.a_property
        42
        >>> t.a_property
        42
        >>> t.a_property
        42

        This method mocks <TestClass.a_method> to just return 42,
        and tests that the mocked <TestClass.a_method> only gets run once,
        to verify that <TestClass.a_property> is properly chached.
        """
        EXPECTED_OUTPUT = 42

        class TestClass:
            def a_method(self):
                return EXPECTED_OUTPUT

            @memoize
            def a_property(self):
                return self.a_method()

        TestClass.a_method = unittest.mock.Mock(return_value=EXPECTED_OUTPUT)

        t = TestClass()

        self.assertEqual(t.a_property, EXPECTED_OUTPUT)
        t.a_method.assert_called_once()
        self.assertEqual(t.a_property, EXPECTED_OUTPUT)
        t.a_method.assert_called_once()
