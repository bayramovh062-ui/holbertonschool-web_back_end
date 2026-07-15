#!/usr/bin/env python3
"""
that is a module that it remains itself function
"""
from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    this function returns a tuple corresponding to the range of indexes
    """

    return ((page - 1) * page_size, page * page_size)
