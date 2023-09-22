"""
Imports 'wait_random' from '0-basic_async_syntax.py'
and creates a function that calls 'wait_randon'
n times with a 'max_delay', all in parallel.

The output of delays should be in ascending order,
since the functions should be running at the same time,
and they print the amount of time they waited,
and the ones that finish first print smaller numbers.
"""
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int):
    """
    Calls and awaits 'wait_random(max_delay)'
    'n' times.

    Since each 'wait_random' should be running
    in parallel, each float output to the stdout
    should be bigger and bigger, corresponding
    to the time each 'wait_random' took to finish.
    """
    for w in range(n):
        await wait_random(max_delay)

