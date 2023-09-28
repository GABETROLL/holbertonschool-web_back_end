#!/usr/bin/env python3
"""
Exercise 2: Make a LIFO caching system that
keeps track of key:value pairs.

It should be a child class of 'BaseCaching',
found in 'base_caching.py', in this directory.

It should have a max capacity of 'BaseCaching.MAX_ITEMS'.
The user should be able to add a new key:value pair,
or get a key's corresponding value with methods.

If the user tries to add in a new pair,
but there are already 'MAX_ITEMS' present,
the system removes the MOST RECENTLY ADDED KEY
AND ITS CORRESPONDING VALUE, prints the discarded key,
then adds the new pair.
"""
from queue import LifoQueue, Full

BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """
    key:value pair caching system, with a maximum capacity
    equal to 'BaseCaching.MAX_ITEMS'

    This class keeps track of its instances' stored pairs
    with a dictionary, called 'self.caching_data',
    and keeps track of the most recently added keys
    using 'self.keys_stack', which is a 'queue.LifoQueue' instance.

    You can add a new key:value pair with 'self.put',
    and you can get a stored key's corresponding value with 'self.get(<key>)'.

    When putting in a new key:value pair with 'self.put',
    if 'self.keys_stack' is already at its maximum capacity
    (which should be 'BaseCaching.MAX_ITEMS),
    'self.put':
    - removes the most recently added key:value
    - pair from 'self.caching_data',
    - removes the key from 'self.keys_stack',
    - prints "DISCARD <key>",
    - then adds in the new pair.
    """
    def __init__(self):
        super().__init__()

        self.keys_stack: LifoQueue = LifoQueue(BaseCaching.MAX_ITEMS)

    def get(self, key):
        """
        Returns key's corresponding
        value in 'self.cache_data' ('self.cache_data[key]'),

        but if 'key' is None or not present in 'self.cache_data',
        this method just returns None.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]

    def put(self, key, item) -> None:
        """
        First of all, if 'key' or 'item'
        are None, this method just returns None
        without doing anything.

        Otherwise, this method
        adds 'key' and 'item' as a new key:value
        pair in 'self.cache_data',
        and adds 'key' into 'self.keys_stack' as
        the most recently added key.

        But if 'self.keys_stack' is already full, this method
        removes the newest added key:value pair from 'self.cache_data',
        removes the newest added key from 'self.keys_stack',
        and places 'key' and 'item' in instead.
        It also prints "DISCARD: <key>".
        """
        if key is None or item is None:
            return

        try:
            self.keys_stack.put_nowait(key)
        except Full:
            newest_key = self.keys_stack.get_nowait()
            del self.cache_data[newest_key]

            print(f"DISCARD: {newest_key}")

            self.keys_stack.put_nowait(key)

        self.cache_data[key] = item
