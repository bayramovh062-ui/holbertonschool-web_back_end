#!/usr/bin/env python3
"""
that is a module that it remains itself a helper function
"""


def index_range(page, page_size):
    """
    this function returns a tuple corresponding to the range of indexes
    """

    return ((page-1)*page_size, page*page_size)