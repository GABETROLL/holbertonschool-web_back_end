#!/usr/bin/env python3
"""
Here, we use 'typing.Callable' to specify
that we're returning a function.

The '[float]' in the return type represents
the argument the 'multiplier_function' takes
(in this case, it was x, the float),
and the other 'float' represents its return type.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function named 'multiplier_function'
    that multiplies a float 'x' by 'multiplier'.
    """
    def multiplier_function(x: float) -> float:
        """
        Returns x times a closure named 'multiplier'.
        """
        return x * multiplier
    return multiplier
