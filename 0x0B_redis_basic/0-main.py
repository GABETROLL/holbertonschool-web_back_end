#!/usr/bin/env python3
"""
Main file for exercise 0
"""
import redis
from exercise import Cache

cache = Cache()

data = b"hello"
key = cache.store(data)
print(key)

local_redis = redis.Redis()
print(local_redis.get(key))
