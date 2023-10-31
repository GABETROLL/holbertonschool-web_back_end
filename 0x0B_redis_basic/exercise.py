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
        """
        self._redis.set(uuid4(), data)
