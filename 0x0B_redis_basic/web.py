#!/usr/bin/env python3
"""
Has <DB = redis.Redis()>, that keeps track
of the amount of calls per URL through <get_page>
in the last 10 seconds,
and <get_page>.
"""
import requests
import redis

DB = redis.Redis()


def get_page(url: str) -> str:
    """
    Makes a request to <url>.
    Increments the cache counter for the <url>
    in DB, under the <f"count:{url}"> key.
    Sets the key's expiration time of 10 seconds.
    Returns the result.
    """
    URL_HTML = requests.get(url).content

    URL_CACHE_KEY = f"count:{url}"
    DB.incr(URL_CACHE_KEY)
    DB.expire(URL_CACHE_KEY, 10)

    return URL_HTML
