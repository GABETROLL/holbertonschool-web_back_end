#!/usr/bin/env python3
"""
Exercise 0:

Make a funtion 'index_range' that takes in a
page number and the amount of items per page,
and returns the indexes of the start end end
items in that page.
"""
from typing import Tuple


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
