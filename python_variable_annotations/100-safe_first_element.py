#!/usr/bin/env python3
"""
We were provided with 'safe_first_element', and we must
use the 'typing' module(?) to properly annotete it.

This time I was feeling confident,
but still failed to annotate properly,
and ended up accidentally seeing the answers.

I'll get it next time...
"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    If 'lst' is not empty,
    this function returns 'lst[0]'.
    Otherwise, this function returns None.

    'lst' is annotated as a 'Sequence',
    because this function assumes
    it supports indexes, and its
    bool representation must be True when
    full, and False when empty.

    To see ALL of the Sequence attributes, see:

https://docs.python.org/3.7/library/collections.abc.html#collections-abstract-base-classes
    """
    if lst:
        return lst[0]
    else:
        return None
