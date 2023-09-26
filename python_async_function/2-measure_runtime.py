#!/usr/bin/env python3
"""
Imports 'wait_n' 1-concurrent_coroutines.py,
'asyncio' and 'time' from 'time'.

Makes a coroutine that calls 'wait_n(n, max_delay)',
and using 'time',
measures the amount of time it took to run,
then returns it divided by n.
"""
import asyncio
from time import time 
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the amount of time
    running 'wait_n(n, max_delay)'.

    Then, this function
    returns the amount of time that took to run,
    divided by 'n'.
    """
    before: float = time.perf_counter()
    await wait_n(n, max_delay)
    after: float = time.perf_counter()

    total_time = after - before
    return total_time / n
