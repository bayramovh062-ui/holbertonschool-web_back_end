#!/usr/bin/env python3
"""
this module contains a function
and will spawn wait_random n times
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    this function returns a list of delay's values
    """
    delay_list = []
    tasks = [wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        delay_list.append(delay)
    return delay_list
