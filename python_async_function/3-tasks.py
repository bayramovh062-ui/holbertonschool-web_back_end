#!/usr/bin/env python3
"""
this module contains a normal function
and this function will return async task
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    this function returns a async task
    """
    return asyncio.create_task(wait_random(max_delay))
