#!/usr/bin/env python3
"""
Add type annotations to this file.
"""
from typing import Mapping, Union, Any, TypeVar

T = TypeVar('T')


def safely_get_value(
            dct: Mapping,
            key: Any,
            default: Union[T, type(None)] = None) -> Union[Any, T]:
    """
    If 'key' is a valid 'key' in 'dct',
        this function returns 'dct[key]'.
    Otherwise,
        this function returns 'default'.
    """
    if key in dct:
        return dct[key]
    else:
        return default
