#!/usr/bin/env python3
"""
Exercise 2: Make a LIFO caching system that
keeps track of key:value pairs.

It should be a child class of 'BaseCaching',
found in 'base_caching.py', in this directory.

It should have a max capacity of 'BaseCaching.MAX_ITEMS'.
The user should be able to add a new key:value pair,
or get a key's corresponding value with methods.

When a user assigns a key with its value,
the key should be marked as the most recently used
key, in a stack-like data structure.

If the user tries to add in a new pair,
but there are already 'MAX_ITEMS' present,
the system removes the MOST RECENTLY ADDED KEY
AND ITS CORRESPONDING VALUE, prints the discarded key,
then adds the new pair.
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    key:value pair caching system, with a maximum capacity
    equal to 'BaseCaching.MAX_ITEMS'

    This class keeps track of its instances' stored pairs
    with a dictionary, called 'self.caching_data',
    and keeps track of the most recently added keys
    using 'self.keys_stack', which is a list with the
    least recently added keys first, and the most recently
    added keys last.

    You can add a new key:value pair with 'self.put',
    and you can get a stored key's corresponding value with 'self.get(<key>)'.

    When putting in a new key:value pair with 'self.put',
    if 'self.keys_stack' is already at its maximum capacity
    (which should be 'BaseCaching.MAX_ITEMS),
    'self.put':
    - removes the most recently added key:value
        pair from 'self.caching_data',
    - removes the key from 'self.keys_stack',
    - prints "DISCARD <key>",
    - then adds in the new pair.
    """
    def __init__(self):
        super().__init__()

        self.keys_stack = []
        """
        Keeps track of the MRU keys,
        so that the newest one can be removed from itself
        and 'self.cache_data' when max capacity is reached.

        The MRU key is at the end.
        """

    def get(self, key):
        """
        If 'key' is None or not in 'self.cache_data',
        this method just returns None.

        Returns key's corresponding
        value in 'self.cache_data' ('self.cache_data[key]').
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
        prints "DISCARD: <key>",
        then does what the paragraph above explains.

        If the key was already present in 'self.cache_data',
        but the value is different, and
        the length of 'self.cache_data' is less than
        'BaseCaching.MAX_ITEMS':
            the key is assigned to 'item' regardless
            of what it is,
            and the key is marked as the MRU key.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.keys_stack.remove(key)
            self.keys_stack.append(key)

        elif len(self.cache_data) == BaseCaching.MAX_ITEMS:
            MOST_RECENT_KEY = self.keys_stack.pop()
            """
            Key that was most recently added to
            'self.cache_data', through this method,
            found in 'self.keys_stack[-1]'.
            """
            del self.cache_data[MOST_RECENT_KEY]

            print(f"DISCARD: {MOST_RECENT_KEY}")

        self.cache_data[key] = item
