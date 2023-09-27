#!/usr/bin/env python3
"""
Makes a new class, 'BasicCache',
that inherits from 'BaseCaching'.

The 'BaseCaching' class is found
in 'base_caching.py', in this directory.

This class should implement
the 'put' and 'get' methods,
which were defined in 'BaseCache',
but not implemented.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Implements the 'get' and 'put'
    methods defined in this class' parent,
    'BaseCaching'.

    Sets 'MAX_ITEMS' to None,
    AND ENFORCES NO STORAGE LIMIT!
    """
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
        return self.cache_data[key]
