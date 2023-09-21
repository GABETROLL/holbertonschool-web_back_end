#!/usr/bin/env python3
import asyncio
from random import uniform

async def wait_random(max_delay: float = 10) -> float:
    """
    Chooses a random number
    (somewhat) in the range of
    0 and 'max_delay' seconds,
    using 'random.uniform'.

    awaits for that amount of time (in seconds)

    returns the number chosen.
    """
    wait_time: float = uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
