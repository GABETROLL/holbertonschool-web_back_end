#!/usr/bin/env python3
import asyncio
from typing import 
async_generator = __import__("0-async_generator.py").async_generator


async def async_comprehension():
    """
    Returns the list of the 10 floats
    between 0 and 10 yielded by 'async_generator'.
    """
    return [f async for f in  async_generator()]
