#!/usr/bin/env python3
"""
This module contains a function task_wait_n that calls task_wait_random.
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Returns a list of delays from task_wait_random in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
        
    return delays
