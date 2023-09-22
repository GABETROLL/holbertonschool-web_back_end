#!/usr/bin/env python3
"""
Imports 'wait_n' 1-concurrent_coroutines.py,
'asyncio' and 'time' from 'time'.

Uses 'time' make a coroutine that calls 'wait_n',
measures the amount of time it takes to run,
and returns it.
"""
wait_n = __import__('1-concurrent_coroutines.py').wait_n
import asyncio
from time import time


async def measure_time(n: int, max_delay: int) -> float:
    """
    Runs 'wait_n(n, max_delay)',
    then returns the amount of time it took to run.
    """
    before = time.now()
    await wait_n(n, max_delay)
    after = time.now()

    return after - before
