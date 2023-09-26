#!/usr/bin/env python3
"""
We were provided with the function 'element_length',
and we must annotate it.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples that each contain:
    the corresponding item in 'lst', and its len (int).

    'lst' is assumed to be an iterable (you should be able
    to iterate over it with a for loop),
    and each item in 'lst' is assumed to have
    the '__len__' attribute (you should be able
    to call 'len(<item>)'.
    """
    return [(i, len(i)) for i in lst]
