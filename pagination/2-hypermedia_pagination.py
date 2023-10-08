#!/usr/bin/env python3
"""
Exercise 2:

Implement the 'get_hyper' method.
"""
from typing import Tuple, List, Mapping, Union
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Assuming that 'page' represents the current page
    the user is on (1-INDEXED),
    and 'page_size' is the amount of articles per page,

    This function returns the index of the first
    and last article in that page (0-INDEXED).
    """
    START: int = page_size * (page - 1)
    END: int = START + page_size
    return (START, END)


class Server:
    """
    Caches a file of the top 19419 most popular baby names
    from the CSV file named like the contents of
    'DATA_FILE'.

    Is used to paginate the rows of data, and has a method
    'get_page' that returns each page's content.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Returns the cached dataset.

        If there's no cached data,
        this method first reads it from 'DATA_FILE',
        caches it (into RAM), and returns it.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Asserts that 'page' and 'page_size' are >= 1.

        Tries to return the data rows from 'self's data
        belonging to the page numbered 'page',
        using 'index_range'.

        If the 'index_range' item indxes are out of the range
        of the data, this method returns an empty list."""
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page >= 1
        assert page_size >= 1

        INDEXES: Tuple[int, int] = index_range(page, page_size)

        try:
            return self.dataset()[INDEXES[0]:INDEXES[1]]
        except IndexError:
            return []

    def get_hyper(
            self,
            page: int = 1,
            page_size: int = 10) -> Mapping[str, Union[int, None]]:
        """
        Given a page index (STARTING A 1) 'page',
        and the amount of data items per page 'page_size',

        returns a dictionary:
        {
            "page_size": <page_size>,
            "page": <page>,
            "data": <data for the page, according to 'self.get_page'>,
            "next_page": <number of the next page from 'page', if there is one>
            "prev_page": <number of the page prev to 'page', if there is one>
        }

        (There shouldn't be pages less than 1,
        and there shouldn't be more pages than
        the 'math.ceil(<total rows> / <page_size>)')
        """
        TOTAL_ROWS: int = len(self.dataset())
        TOTAL_PAGES: int = math.ceil(TOTAL_ROWS / page_size)

        PAGE_DATA: List[List] = self.get_page(page, page_size)

        return {
            "page_size": page_size,
            "page": page,
            "data": PAGE_DATA,
            "next_page": page + 1 if page + 1 <= TOTAL_PAGES else None,
            "prev_page": page - 1 if page - 1 >= 1 else None,
            "total_pages": TOTAL_PAGES
        }
