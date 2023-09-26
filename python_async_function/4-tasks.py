#!/usr/bin/env python3
"""
Copy '1-concurrent_coroutines.wait_n'
and paste it here.
Make it call 'task_wait_random',
Change its name to 'task_wait_n'.
"""
import asyncio
from typing import List
task_wait_random = __import__("3-tasks").task_wait_random

seconds = float


async def run_and_append(max_delay: int, l: list) -> None:
    """
    Runs 'task_wait_random(max_delay)', awaits its return value,
    and appends its result to 'l'.
    """
    l.append(await task_wait_random(max_delay))


async def task_wait_n(n: int, max_delay: int) -> List[seconds]:
    """
    Runs 'task_wait_random(max_delay)' in parallel 'n' times,
    and returns a list of the amount of time
    (in floats representing seconds) each 'task_wait_random'
    call took, IN THE ORDER THAT THEY FINISHED.

    This function achieves this, by running an intermediary
    awaitable, 'run_and_append(max_delay, result)',
    that awaits 'task_wait_random(max_delay)', then
    appends its result to 'result', which should be the
    result list.

    This allows the amount of time each 'task_wait_random'
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

