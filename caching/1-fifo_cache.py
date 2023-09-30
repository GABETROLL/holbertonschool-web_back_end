#!/usr/bin/env python3
"""
Exercise 1: Make a FIFO Caching system
that keeps track of key:value pairs,

has a maximum capacity same as 'BaseCaching.MAX_ITEMS',
can add new pairs, and if it runs out of space,
removes the oldest added pair to make space for the new one.

'BaseCaching' should be found in the file named
'0-basic_cache.py', which should be in the
same directory as this file.
"""
import queue

BaseCaching = __import__("0-basic_cache").BaseCaching


class FIFOCache(BaseCaching):
    """
    Keeps track of key:value pairs
    in a dictionary called 'self.cache_data'.

    Keeps track of the keys that were most recently
    used as arguments in 'self.get' or 'self.put',
    in a list functioning as a queue, called 'self.keys_queue'.

    Has a max capacity equal to 'BaseCaching.MAX_ITEMS",
    and 'self.keys_queue' has that same capacity.

    'self.get(<key>)' returns the key's corresponding
    value in 'self.cache_data', if the key is not None,
    and exists in 'self.cache_data'.
    It also marks that key as the MRU (Most Recently Used) key,
    by moving it to the end of 'self.keys_queue'.

    'self.put(<key> <value>) will assign
    'self.cache_data[key] = value'.
    If the length of 'self.cache_data' is already
    'BaseCaching.MAX_ITEMS', then: the LRU (Least Recently Used)
    key, found in 'self.keys_queue[0]', gets removed,
    the new key gets added to 'self.cache_data' with
    its corresponding value,
    and the new key gets added to 'self.keys_queue'
    as the MRU (Most Recently Used) key.
    """
    def __init__(self) -> None:
        super().__init__()

        self.keys_queue = []

    def put(self, key, item) -> None:
        """
        If 'key' or 'item' are None,
        this method just returns without doing anything.

        Stores 'key' and 'item' in 'self.cache_data'
        as a key:value pair, and appends 'key'
        into 'self.keys_queue', to mark it as
        the MRU key.

        if 'self.cache_data' has reached 'BaseCaching.MAX_ITEMS',
        this method gets the oldest inserted
        key from 'self.keys_queue',
        removes it and its value from 'self.cache_data',
        prints "DISCARD: key",
        THEN executes the paragraph above.
        """
        if key is None or item is None:
            return

        if len(self.cache_data) == BaseCaching.MAX_ITEMS:
            LRU_KEY = self.keys_queue.pop(0)
            del self.cache_data[LRU_KEY]

            print(f"DISCARD: {LRU_KEY}")

        self.cache_data[key] = item
        self.keys_queue.append(key)

    def get(self, key):
        """
        If 'key' is None,
        or if 'key' isn't a key in 'self.cache_data',
        just returns None.

        Otherwise,
        this method marks 'key' as the MRU key
        in 'self.keys_queue'
        (by removing the key from 'self.keys_queue',
        then appending it again at the end of 'self.keys_queue'),
        then returns 'self.cache_data[key]'.
        """
        if key is None or key not in self.cache_data:
            return None

        self.keys_queue.remove(key)
        self.keys_queue.append(key)

        return self.cache_data[key]
