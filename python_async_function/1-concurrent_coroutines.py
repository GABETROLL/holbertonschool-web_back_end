#!/usr/bin/env python3
"""
Imports 'wait_random' from '0-basic_async_syntax.py'.
Creates a coroutine named 'wait_n' that calls 'wait_randon'
n times with a 'max_delay', all in parallel.
Makes 'wait_n' return a list of floats
representing the amount of time each coroutine took.

The list of floats should be in ascending order,
since the 'corountine's should be running at the same time,
and they print the amount of time they waited,
and the ones that finish first print smaller numbers.

(ALTHOUGH I DON'T KNOW IF COROUTINES THAT FINISH VERY CLOSELY
CAN ALTER THE ORDER)
"""
wait_random = __import__('0-basic_async_syntax').wait_random

from typing import List
seconds = float


async def wait_n(n: int, max_delay: int) -> List[seconds]:
    """
    Calls and awaits 'wait_random(max_delay)'
    'n' times.

    Returns a list of floats that represent
    the time, IN SECONDS,
    each coroutine took. The result should
    be in ascending order, since the coroutines
    that finish first should also be appended first.
    """
    result: List[seconds] = []

    for w in range(n):
        result.append(await wait_random(max_delay))

    return result
