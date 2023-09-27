#!/usr/bin/env python3
"""
Import 'async_generator', which yields
10 random floats in the range of 0 to 10,
from `0-async_generator`, found in this directory.

Write a coroutine called 'async_comprehension'.
It should take no arguments.
It should return
a list of the numbers yielded by 'async_generator',
USING AN ASYNC COMPREHENSION.
"""
import asyncio
from typing import List
async_generator = __import__("0-async_generator.py").async_generator


async def async_comprehension() -> List[float]:
    """
    Returns the list of the 10 floats
    between 0 and 10 yielded by 'async_generator'.
    """
    return [f async for f in async_generator()]
