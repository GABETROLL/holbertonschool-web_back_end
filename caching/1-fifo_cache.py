#!/usr/bin/env python3
"""
Exercise 1: Make a FIFO Caching system
that keeps track of key:value pairs,

has a maximum capacity same as 'BaseCaching.MAX_SIZE',
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
    in a dictionary called 'self.cache_data',
    and in a queue.Queue object called 'self.keys_queue'.

    Has a max capacity equal to 'BaseCaching.MAX_SIZE",
    and 'self.keys_queue' has that same capacity.

    Getting a key's corresponding value from 'self.cache_data'
    can be achieved by calling 'self.get(<key>)', then
    getting the key's corresponding value.

    Putting a key:value pair into 'self.cache_data' can be achieved
    using 'self.put'. If there's enough space,
    'self.put' will add the new key to 'self.keys_queue',
    and the new key:value pair to 'self.cache_data'.

    If there's no more space, 'self.put' first removes
    the oldest key, and adds the new key:value pair.
    """
    def __init__(self):
        super().__init__()

        self.keys_queue: queue.Queue = queue.Queue(BaseCaching.MAX_SIZE)

    def put(self, key, item):
        """
        Stores 'key' and 'item' in 'self.cache_data'
        as a key:value pair, and puts 'key'
        in 'self.keys_queue'.

        if 'self' is full,
        this method gets the oldest inserted
        key from 'self.keys_queue',
        removes it and its value from 'self.cache_data',
        THEN executes the paragraph above.
        """
        try:
            self.keys_queue.put_nowait(key)
        except queue.Full:
            oldest_key = self.keys_queue.get_nowait()
            del self.cache_data[oldest_key]

            self.keys_queue.put_nowait(key)
        self.cache_data[key] = item

    def get(self, key):
        """
        Returns 'self.cache_data[key]'...

        ...But if 'key' is None,
        or if 'key' isn't a key in 'self.cache_data',
        just returns None.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
