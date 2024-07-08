#!/usr/bin/env python3
"""
Module that defines a basic async function
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that takes in 2 integer arguments (n: the number of
    times wait_random will be called and max_delay: the maximum random delay)
    named wait_n that waits for a random delay between 0 and max_delay
    (included and float value) seconds and eventually returns a list of the
    delays in ascending order.
    """
    delays = []
    tasks = []
    for _ in range(n):
        task = wait_random(max_delay)
        tasks.append(task)

    for task in asyncio.as_completed((tasks)):
        delay = await task
        delays.append(delay)

    return delays
