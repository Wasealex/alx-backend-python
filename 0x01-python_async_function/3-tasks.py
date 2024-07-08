#!/usr/bin/env python3
"""
Module that defines a basic async function
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Function that takes in an integer argument (max_delay, with a default value
    of 10) named task_wait_random that waits for a random delay between 0 and
    max_delay (included and float value) seconds and eventually returns it.
    """
    return asyncio.create_task(wait_random(max_delay))
