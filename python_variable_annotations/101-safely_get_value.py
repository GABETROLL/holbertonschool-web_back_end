#!/usr/bin/env python3
"""
Add type annotations to this file.
"""
import typing


def safely_get_value(
            dct: Mapping,
            key: Any,
            default: Union[T, NoneType] = None) -> Union[Any, T]:
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
