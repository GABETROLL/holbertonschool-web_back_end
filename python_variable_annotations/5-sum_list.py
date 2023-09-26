#!/usr/bin/env python3
"""
Has one function called 'sum_list'
that takes in an 'input_list',
which should be a list of floats,
and returns the 'float' sum of
the floats inside the list.

Uses a complex type hint to specify that
sum_list's 'input_list' argument
should be a list of floats,
and 'sum_list' returns a 'float'.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of all of the items
    inside 'input_list', using sum(input_list).

    Assumes that 'input_list' is a list
    of floats.
    """
    return sum(input_list)
