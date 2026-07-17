#!/usr/bin/env python3
"""
This module implements simple pagination for a dataset of popular
baby names using a CSV file as the data source.
"""
import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple of size two containing a start index and an end
    index corresponding to the range of indexes to return in a list
    for those particular pagination parameters.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves a specific page of the dataset based on the given
        page number and page size.
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Retrieves pagination information alongside the requested page,
        including hypermedia metadata such as next/previous page numbers
        and the total number of pages.
        """
        total_pages = math.ceil(len(self.dataset()) / page_size)
        data = self.get_page(page, page_size)
        next_page = page + 1
        prev_page = page - 1
        if total_pages < next_page:
            next_page = None
        if prev_page <= 0:
            prev_page = None

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
