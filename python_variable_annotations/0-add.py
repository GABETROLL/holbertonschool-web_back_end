#!/usr/bin/env python3
"""
Uses Python type hints to specify that 'add'
takes float arguments and returns a float.
"""


def add(a: float, b: float) -> float:
    """
    Returns a + b.

    'a', 'b' and the returned result
    are assumed to be of type 'float'.
    """
    return a + b
