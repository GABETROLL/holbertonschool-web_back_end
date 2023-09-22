#!/usr/bin/env python3
"""
'Hello World!' figue in Python's
documentation for 'asyncio'.

Check it out!
https://docs.python.org/3/library/asyncio.html
"""
import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """
    Chooses a random number
    (somewhat) in the range of
    0 and 'max_delay',
    using 'random.uniform'.

    awaits for that amount of time IN SECONDS.

    returns the number chosen.
    """
    wait_time: float = uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
