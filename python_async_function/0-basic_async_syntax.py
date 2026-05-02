#!/usr/bin/env python3
"""
this is an example of async function
"""
import random
import asyncio


async def wait_random(max_delay=10):
    """
    this function await between 0 and
    max_delay then it returns random value
    """
    random_sleep_time = random.uniform(0, max_delay)
    await asyncio.sleep(random_sleep_time)
    return random_sleep_time
