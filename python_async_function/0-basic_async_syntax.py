#!/usr/bin/env python3
import asyncio
from random import uniform

async def wait_random(max_delay: float = 10):
    """
    Waits for a random amount of time
    (somewhat) in the range of
    0 and 'max_delay' seconds.
    """
    await asyncio.sleep(
            uniform(0, max_delay)
    )
