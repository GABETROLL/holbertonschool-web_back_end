#!/usr/bin/env python3
"""
Has a single function 'concat', that
takes 2 arguments and returns them
joined together, assuming they're both strings.

Uses Python type hints to specify that
'concat' takes arguments of type 'str'
and returns a 'str'.
"""


def concat(str1: str, str2: str) -> str:
    """
    Returns 'str1' and 'str2',
    joined as a single string.

    Both 'str1' and 'str2' are
    assumed to be of type 'str',
    and 'str1 + str2' is also
    assumed to be of type 'str'.
    """
    return str1 + str2
