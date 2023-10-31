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
    Assuming that this function is being used
    as a decorator on a method in <Cache>,

    This function returns the replacement for <method>,
    which is a function: <increment(self, *args, **kwargs)>,
    which is decorated by <@wraps(method)>.

    The <increment> function, behaving like a method of
    <Cache>, increments the <method>'s __qualname__ counter
    (using <self._redis.inc(method.__qualname__)>)
    to keep count of the calls to <method>.
    The <increment> function then calls
    <method(self, *args, **kwargs)>.
    """
    @wraps(method)
    def increment(self, *args, **kwargs):
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)

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
