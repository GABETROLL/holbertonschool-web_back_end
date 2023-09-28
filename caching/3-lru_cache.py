#!/usr/bin/env python3
"""
Create a new class, called 'LRUCache',
that inherits from 'BaseCaching'.
"""
import queue

BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """
    Caching system that uses a dictionary (named 'self.cache_data')
    and a list to keep track of the LRU (least recently used)
    key.

    The least-recently used key is the key that,
    was used to get its corresponding value through 'self.get'
    or was added with its corresponding value to 'self.cache_data'
    through 'self.put',
    the longest ago.
    """
    def __init__(self):
        super().__init__()

        self.lru_keys: list = []
        """
        The list of all of the keys
        in 'self.cache_data',
        in order of LRU to MRU
        (least recently used to most recently used).
        """

    def get(self, key):
        """
        If 'key' is None or if 'key' isn't present in
        'self.cache_data', this method returns None.

        If 'key' is a valid key in 'self.cache_data',
        this method marks this key as the MRU (most
        recently used) key, by removing it from 'self.lru_keys'
        and appending it back at the end of 'self.lru_keys',

        then returns 'self.cache_data[key]'.
        """
        if key is None or key not in self.cache_data:
            return None

        # 'key' should also be 'self.lru_keys'
        # if it's in 'self.cache_data'
        # and if the user only modified
        # them through 'self.get' and 'self.put'.
        self.lru_keys.remove(key)
        self.lru_keys.append(key)

        return self.cache_data[key]

    def put(self, key, item) -> None:
        """
        If 'key' or 'item' are None,
        this method returns before doing anything else.

        Sets 'self.cache_data[key] = item'.

        If the amount of key:item pairs
        in 'self.cache_data' are equal to
        'BaseCaching.MAX_ITEMS',
        this method first removes the LRU
        key from 'self.cache_data' and 'self.lru_keys',
        and places 'key' and 'item' where the removed
        key and value were.

        If 'key' is already present in 'self.cache',
        then this method just marks the key as the new
        MRU key in 'self.lru_keys', by moving the key
        to the end of the list,
        then this method assigns 'self.cache_data[key] = item'.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.lru_keys.remove(key)

        elif len(self.cache_data) == BaseCaching.MAX_ITEMS:
            self.lru_keys.pop(0)

        self.lru_keys.append(key)
        self.cache_data[key] = item
