#!/usr/bin/env python3
"""
Has one function named 'sum_mixed_list'.

'sum_mixed_list' takes one argument 'mxd_lst',
which should be a list of ints or floats,
and returns their sum, which should be a float.

Uses 'typing' and python type annotations
to specify that the input for 'sum_mixed_list'
is a list of ints/floats, and that
'sum_mixed_list' returns a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of all of the numbers in 'mxd_list',
    assuming that 'mxd_list' is a list,
    and that anything 'mxd_list' contains
    is a float or an int.
    """
    return sum(mxd_lst)
