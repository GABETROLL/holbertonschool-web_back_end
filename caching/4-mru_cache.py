#!/usr/bin/env python3
"""
Create a new class, called 'MRUCache',
that inherits from 'BaseCaching'.

It should have a max capacity of 'BaseCaching.MAX_ITEMS'.

It should return a key's corresponding value
with 'get', and set a key's corresponding value
with 'put'.

(The keys and values should be kept in
'cache_data', inherited from 'BaseCaching')

If the dictionary reaches the max capacity,
and 'put' is called with a non-None key and value,
the MRU (Most Recently Used) key should be evicted
from dictionary, along with its value.

The system should keep track of each key in the dictionary,
in a list, from LRU (Least Recently Used)
to MRU (Most Recently Used).
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    Caching system that uses a dictionary (named 'self.cache_data')
    and a list to keep track of the MRU (most recently used)
    key.

    The most-recently used key is the key that was most recently
    inputted as an argument in 'self.get' or 'self.put'.
    """
    def __init__(self):
        super().__init__()

        self.mru_keys: list = []
        """
        The list of all of the keys
        in 'self.cache_data',
        in order of LRU to MRU
        (least recently used to most recently used).

        It was made like this, because Python lists
        behave like stacks, the the MRU key
        is always at the top, so popping it out of the list
        may be better for performance.
        """

    def get(self, key):
        """
        If 'key' is None or if 'key' isn't present in
        'self.cache_data', this method returns None.

        If 'key' is a valid key in 'self.cache_data',
        this method marks this key as the MRU (most
        recently used) key, by removing it from 'self.mru_keys'
        and appending it back at the end of 'self.mru_keys',

        then returns 'self.cache_data[key]'.
        """
        if key is None or key not in self.cache_data:
            return None

        # 'key' should also be 'self.mru_keys'
        # if it's in 'self.cache_data'
        # and if the user only modified
        # them through 'self.get' and 'self.put'.
        self.mru_keys.remove(key)
        self.mru_keys.append(key)

        return self.cache_data[key]

    def put(self, key, item) -> None:
        """
        If 'key' or 'item' are None,
        this method returns None before doing anything else.

        Sets 'self.cache_data[key] = item'.

        If the amount of key:item pairs
        in 'self.cache_data' are equal to
        'BaseCaching.MAX_ITEMS', this method:
        - removes the MRU key from 'self.cache_data' and 'self.mru_keys',
        - prints f"DISCARD {MRU_key}",
        - adds 'key' and 'item' to 'self.cache_data' as a key:value pair,
        - and appends 'key' to 'self.mru_keys'.

        If 'key' is already present in 'self.cache',
        then this method:
        - marks the key as the new MRU key in 'self.mru_keys',
        by moving the key to the end of the list,
        - assigns 'self.cache_data[key] = item'.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.mru_keys.remove(key)

        elif len(self.cache_data) == BaseCaching.MAX_ITEMS:
            # pop MRU key
            MRU_key = self.mru_keys.pop(-1)
            del self.cache_data[MRU_key]

            print(f"DISCARD: {MRU_key}")

        self.mru_keys.append(key)
        self.cache_data[key] = item
