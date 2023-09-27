#!/usr/bin/env python3
"""
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    MAX_ITEMS = None

    def put(self, key, item) -> None:
        """
        Sets 'self.cache_data[key] = item'.

        If 'key' or 'item' are None,
        this method just returns before doing anything.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Returns 'self.cache_data[key]'...

        ...But if 'key' is None or if 'key' isn't
        in 'self.cache_data',
        this method returns None.
        """
        if key is None or key not in self.cache_data:
            return
        self.cache_data[key]
