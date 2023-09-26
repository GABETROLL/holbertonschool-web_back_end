#!/usr/bin/env python3
"""
Imports 'wait_random' from '0-basic_async_syntax.py'.
Creates a coroutine named 'wait_n' that calls 'wait_randon'
n times with a 'max_delay', all in parallel, then
returns a list of their results.

The results should be the amount of time each corountine
took, in ascending order, since the ones that finish
first are appended first!
"""
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio

seconds = float


async def run_and_append(max_delay: int, l: list) -> None:
    l.append(await wait_random(max_delay))


async def wait_n(n: int, max_delay: int) -> List[seconds]:
    """
    Calls 'asyncio.gather' with a list of coroutines
    produced by 'wait_random(max_delay)'. The amount
    of the coroutines in that list should be 'n'.
    This should run the coroutines in parallel.

    Returns a list of floats that represent
    the time, IN SECONDS,
    each coroutine took. The result should
    be in ascending order, since 'asyncio.gather'
    appends first the coroutines that finish first.
    """
    result = []

    await asyncio.gather(
        *(
            run_and_append(max_delay, result)
            for _ in range(n)
        )
    )

    return result
