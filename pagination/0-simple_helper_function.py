#!/usr/bin/env python3
"""
Contains function 'index_range'.
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
