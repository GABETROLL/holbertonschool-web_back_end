#!/usr/bin/env python3
"""
Main file for exercise 2
"""
from exercise import Cache

cache = Cache()

cache.store(b"first")
print(cache.get(cache.store.__qualname__))

cache.store(b"second")
cache.store(b"third")
print(cache.get(cache.store.__qualname__))
