#!/usr/bin/env python3
"""
Make a coroutine called 'async_generator'.
It should do this 10 timeS:
    sleep for 1 second,
    yield a number between 0 and 10.
"""
import asyncio
import random


async def async_generator():
    """
    An async generator that yields 10 floats.

    Does this 10 times:
        Sleeps for 1 second,
        then yields a random float between 0 and 10.
    """
    for _ in range(10):
        asyncio.sleep(1)
        yield random.random() * 10
