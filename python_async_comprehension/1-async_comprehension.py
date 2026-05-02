#!/usr/bin/env python3
"""
We will import generator from 0-async_generator
file and then we will use this generator for create
async comprehension
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    this function returns 10 random numbers
    with using async generator
    """
    return [i async for i in async_generator()]
