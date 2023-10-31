#!/usr/bin/env python3
"""
Contains <Cache> class with Redis database.
"""
import redis
from uuid import uuid4
from typing import Union, Optional, Callable


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

    def get(self, key: str, fn: Optional[Callable] = None):
        """
        <get>s the value for <key> in <self>'s DB.

        If <fn> is defined, this method uses <fn>
        to convert the value to the user's desired format.
        """
        result = self._redis.get(key)

        if fn is not None:
            result = fn(result)

        return result

    def get_str(self, key):
        """
        Returns <self.get(key)> with the <fn>
        being defined to return the string form
        of the value (fn=lambda x: x.decode()).
        """
        return self.get(key, lambda x: x.decode())

    def get_int(self, key):
        """
        Returns <self.get(key)> with the <fn>
        being defined to return the int form
        of the value (fn=lambda x: int(x.decode())).
        """
        return self.get(key, lambda x: int(x.decode()))


if __name__ == "__main__":
    cache = Cache()
    KEY = cache.store(3)
    print(f"KEY: {KEY}")
    print(f"VALUE: {cache.get(KEY)}")
    print(f"CONVERTED_VALUE: {cache.get(KEY, lambda x: x.decode().split(', '))}")
    print(f"STR VALUE: {cache.get_str(KEY)}")
    print(f"INT_VALUE: {cache.get_int(KEY)}")
