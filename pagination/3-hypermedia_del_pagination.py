#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Dataset from 'DATA_FILE',
        cached as a dictionary of the rows' indexes
        and their contents,

        so that even if a row is deleted,
        the other rows don't offset.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Returns a dictionary:
        {
            "index": 'index',
            "next_index":
                the index of the first row of the next page
                from this one. Should be 'index + page_size'.
            "page_size":
                the amount of items in the requested page.
                It may not always be 'page_size', since some
                items may have been deleted.
            data:
                the rows that, according to their indeces,
                are supposed to be displayed in this page,
                from 'index' to 'index + page_size'.
                Some of them may be deleted, but their indexes
                remain the same.
        }

        Normally, the data in 'self.indexed_data()'
        has all of the rows in 'DATA_FILE',
        all indexed properly, from [0, rows).

        But, if a row gets deleted from 'self',
        since the cache in 'self.indexed_data()' is a dictionary
        instead of a list, the row being deleted doesn't offset
        the indexes of the other items.

        In this method, we return all of the items
        in the range of ['index', 'index + page_size'),
        but skipping the rows that were deleted.
        """

        INDEXED_DATASET: Dict[int, List] = self.indexed_dataset()

        PAGE_DATA: List[List] = [
            INDEXED_DATASET[i]
            for i in range(index, index + page_size)
            if i in INDEXED_DATASET
        ]

        return {
            "index": index,
            "next_index": index + page_size,
            "page_size": len(PAGE_DATA),
            "data": PAGE_DATA
        }
