#!/usr/bin/env python3
"""
Main file
"""
import redis
from exercise import Cache, replay

cache = Cache()

data = b"hello"
key = cache.store(data)
print(key)

local_redis = redis.Redis()
print(local_redis.get(key))

print("1 -------------------------------------")

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value

print("2 -------------------------------------")

cache.store(b"first")
print(cache.get(cache.store.__qualname__))

cache.store(b"second")
cache.store(b"third")
print(cache.get(cache.store.__qualname__))

print("3 -------------------------------------")

s1 = cache.store("first")
print(s1)
s2 = cache.store("secont")
print(s2)
s3 = cache.store("third")
print(s3)

inputs = cache._redis.lrange(
    "{}:inputs".format(cache.store.__qualname__), 0, -1
)
outputs = cache._redis.lrange(
    "{}:outputs".format(cache.store.__qualname__), 0, -1
)

print("inputs: {}".format(inputs))
print("outputs: {}".format(outputs))

assert [o.decode() for o in outputs[-3:]] == [s1, s2, s3]

print("4 -------------------------------------")

replay(cache.store)
