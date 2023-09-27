#!/usr/bin/env python3
"""
Import 'async_comprehension' from "1-async_comprehension",
in this directory.

Create a coroutine that runs
'async_comprehension()' 4 times in parallel
using 'asyncio.gather'.

Make the coroutine also measure the amount of time
it took to run the 4 coroutines,
and return it (AS A FLOAT REPRESENTING SECONDS).
"""
import asyncio
import time
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Runs 'async_comprehension()'
    4 times in parallel
    (using 'asyncio.gather(async_comprehension(), +3)')
    and returns the amount of time it took.

    The return type should be a float representing
    seconds.
    It should be about 10 seconds.
    """
    before: float = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    after: float = time.perf_counter()

    return after - before
