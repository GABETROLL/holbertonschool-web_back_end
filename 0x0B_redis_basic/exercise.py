#!/usr/bin/env python3
"""
Contains <Cache> class with Redis database.
"""
import redis
from uuid import uuid4
from typing import Union


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores <data> as a value with
        a uuid key in the Redis database
        stored in <self>.

        This method then returns the uuid key,
        as a string.
        """
        KEY = str(uuid4())
        self._redis.set(KEY, data)
        return KEY


if __name__ == "__main__":
    cache = Cache()
    KEY = cache.store("Hello, World!")
    print(f"KEY: {KEY}")
    VALUE = cache._redis.get(KEY)
    print(f"VALUE: {VALUE}")
