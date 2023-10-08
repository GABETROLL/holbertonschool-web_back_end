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
        Dataset indexed by sorting position, starting at 0
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
            "index": index,
            "next_index": <
                the next available index in the cached data.
                Normally, it would be 'index + 1', but some rows may be deleted,
                so this number is the next available row
            >
            "page_size": <the amount of items in the requested page>
            "data": <the rows that survived deletions, and can be returned for this page>
        }
        Returns a list of rows from the data,
        from 'index' to 'index + page_size'.

        Normally, this object should have the data from
        'DATA_FILE' cached and indexed (you can get it with
        'self.index_dataset()').
        If a row gets deleted, the other rows are still indexed
        how they were indexed before (because they're cached
        in a dictionary). And this method just returns all of the
        rows of data that have the indexes from 'index' to 'index + page_size'.
        """

        INDEXED_DATASET: Dict[int, List] = self.indexed_dataset

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
