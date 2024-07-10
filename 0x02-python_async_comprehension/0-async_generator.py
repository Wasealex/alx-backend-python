import asyncio
import random
from typing import Generator

#!/usr/bin/env python3
""" Module contain a coroutine function """




async def async_generator() -> Generator[float, None, None]:
    """coroutine that loops 10 times, wait 1 sec each time"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10