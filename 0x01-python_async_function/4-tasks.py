#!/usr/bin/env python3
"""
Module that defines a basic async function
"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes task_wait_random n times in parallel using asyncio.
    Args:
        n (int): The number of times task_wait_random should be called.
        max_delay (int): The maximum delay for each task.

    Returns:
        List[float]: A list of the delays for each task.
    """
    delays = []
    tasks = []

    for _ in range(n):
        tasks.append(task_wait_random(max_delay))

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
