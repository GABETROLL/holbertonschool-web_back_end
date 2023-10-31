#!/usr/bin/env python3
"""
Contains <Cache> class with Redis database.
"""
import redis
from functools import wraps
from uuid import uuid4
from typing import Union, Optional, Callable


def count_calls(method: Callable) -> Callable:
    """
    Decorator for <method>,
    that keeps count of the calls to <method>.

    Makes a calls dict to keep track of the <method>'s
    <__qualname__> and the amount of times it was called,

    makes <increment(*args, **kwargs)>, that's decorated
    with <wraps(method)>,
    that increments <method>'s counter
    and returns <method(*args, **kwargs)>.

    Returns the <increment> inner function,
    which should have the closure for the calls counter.
    """
    calls = {method.__qualname__: 0}

    @wraps(method)
    def increment(*args, **kwargs):
        calls[method.__qualname__] += 1
        return method(*args, **kwargs)

    return increment


class Cache:
    """
    Connection to Redis DB.
    Flushes the DB when instanciated.
    """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
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
