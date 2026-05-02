#!/usr/bin/env python3
"""
This module execute async_comprehension four times
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    this function execute async_comprehension four times
    """
    start_time = time.time()
    await asyncio.gather(*((async_comprehension() for _ in range(4)))
    end_time = time.time()
    return abs(tart_time - end_time)
