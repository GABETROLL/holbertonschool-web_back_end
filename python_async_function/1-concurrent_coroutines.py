#!/usr/bin/env python3
"""
Creates a coroutine that runs 'wait_random(max_delay)'
n times, all in parallel, and returns a list
of the results of each 'wait_random' call
(which should be the amount of time the coroutine took
ot run)

The result list of times should be in ascending order.
To do this, this file has an INTERMEDIATE COROUTINE
that ACTUALLY RUNS and awaits for 'wait_random(max_delay)',
and appends that call's result to a result list parameter.

'wait_n' just runs 'run_and_append(max_delay, <result list>)'
n times with 'asyncio.gather', and each 'run_and_append'
coroutine appends its result when it's ready, to achieve
appending the results of the 'wait_random' calls
in the order that they finish.
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

seconds = float


async def run_and_append(max_delay: int, l: list) -> None:
    """
    Runs 'wait_random(max_delay)', awaits its return value,
    and appends its result to 'l'.
    """
    l.append(await wait_random(max_delay))


async def wait_n(n: int, max_delay: int) -> List[seconds]:
    """
    Runs 'wait_random(max_delay)' in parallel 'n' times,
    and returns a list of the amount of time
    (in floats representing seconds) each 'wait_random'
    call took, IN THE ORDER THAT THEY FINISHED.

    This function achieves this, by running an intermediary
    coroutine, 'run_and_append(max_delay, result)',
    that awaits 'wait_random(max_delay)', then
    appends its result to 'result', which should be the
    result list.

    This allows the amount of time each 'wait_random'
    call took to be appended to 'result' IN THE
    ORDER THEY FINISHED, AND TO BE RUN IN PARALLEL.

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
