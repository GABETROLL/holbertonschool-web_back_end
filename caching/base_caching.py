#!/usr/bin/env python3
"""
BaseCaching module
"""

class BaseCaching():
    """
    Dictionary caching system.

    The data is stored in 'self.cache_data'.

    You can print the data present with 'self.print_cache',
    put in a new key:value pair with 'self.put',
    or get the value in 'cache_data' that corresponds to a key
    using 'self.get(<key>)'.
    """
    MAX_ITEMS = 4

    def __init__(self):
        """
        Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """
        Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """
        Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """
        Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")
