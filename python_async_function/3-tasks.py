#!/usr/bin/env python3
"""
Make a FUNCTION that takes in an 'int' 'max_delay'
and returns an 'asyncio.Task'.
"""
import asyncio
wait_random = __import__("0-basic_async_syntax")


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns 'wait_random(max_delay)' as an 'asyncio.Task'.
    """
    return asyncio.Task(wait_random(max_delay))
