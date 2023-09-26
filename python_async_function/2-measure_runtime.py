#!/usr/bin/env python3
"""
Imports 'wait_n' 1-concurrent_coroutines.py,
'asyncio' and 'time' from 'time'.

Makes a FUNCTION that calls
runs 'wait_n(n, max_delay)',
and using 'time',
measures the amount of time
'wait_n(...)' took to run,
then returns it divided by n.

The time is returned as a float,
representing milliseconds.
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n

milliseconds = float


def measure_time(n: int, max_delay: int) -> milliseconds:
    """
    Runs 'wait_n(n, max_delay)' using asyncio.

    Then, this function
    returns the amount of time that took to run,
    divided by 'n'.

    The amount of time is measured by using
    'time.process_time'.

    The type of this function's returned result
    is a float representing milliseconds.
    """
    before: milliseconds = time.process_time()
    asyncio.run(wait_n(n, max_delay))
    after: milliseconds = time.process_time()

    total_time: milliseconds = after - before
    return total_time / n
