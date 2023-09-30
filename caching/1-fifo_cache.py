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
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Keeps track of key:value pairs
    in a dictionary called 'self.cache_data'.

    Keeps track of the keys added to 'self.cache_data',
    in the order that they came in, through 'self.put'.

    The user of this class can get a key's corresponding value
    with 'self.get(<key>)'.

    The user of this class can add a key:value pair
    using 'self.put(key, value).
    When a key is added through 'self.put', it gets added
    to 'self.cache_data' with its value, and it
    gets added to 'self.cache_data' as the newest added key.
    If there's already 'BaseCaching.MAX_ITEMS' keys
    in 'self.cache_data', the oldest added key
    gets removed from both 'self.cache_data' and
    'self.keys_queue', and the new key and value are
    added.

    If the key already exists in 'self.cache_data',
    and 'self' isn't full yet, 'self.put'
    assigns the key to the new value, and moves
    the key to the end of 'self.keys_queue',
    to mark it as the newest added key.
    """
    def __init__(self) -> None:
        super().__init__()

        self.keys_queue = []
        """
        Should be all of the keys added to
        'self.cache_data' THROUGH 'self.put'.

        They're ordered from least-recent
        to most-recently added.
        """

    def put(self, key, item) -> None:
        """
        If 'key' or 'item' are None,
        this method just returns without doing anything.

        Stores 'key' and 'item' in 'self.cache_data'
        as a key:value pair, and appends 'key'
        into 'self.keys_queue', to mark it as
        the MRU key.

        If 'key' is already present in 'self.cache_data',
        the key's corresponding value is set to be 'item',
        and 'key' is moved to the end of 'self.keys_queue',
        to mark it as the newest added key.

        if 'self.cache_data' has reached 'BaseCaching.MAX_ITEMS',
        this method gets the oldest inserted
        key from 'self.keys_queue',
        removes it and its value from 'self.cache_data',
        prints "DISCARD: key",
        THEN executes the paragraph above.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Mark 'key' as the most recently
            # added key, since it was used
            # to modify its value
            self.keys_queue.remove(key)
            self.keys_queue.append(key)

        elif len(self.cache_data) == BaseCaching.MAX_ITEMS:
            LRU_KEY = self.keys_queue.pop(0)
            del self.cache_data[LRU_KEY]

            print(f"DISCARD: {LRU_KEY}")

        self.cache_data[key] = item
        # Add 'key' to 'self.keys_queue',
        # with its position indicating that it's the
        # most recently added key
        self.keys_queue.append(key)

    def get(self, key):
        """
        If 'key' is None,
        or if 'key' isn't a key in 'self.cache_data',
        just returns None.

        Otherwise,
        this method returns 'self.cache_data[key]'.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
