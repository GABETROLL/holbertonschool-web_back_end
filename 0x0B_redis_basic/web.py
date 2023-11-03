#!/usr/bin/env python3
"""
Has <DB = redis.Redis()>, that keeps track
of the amount of calls per URL through <get_page>
in the last 10 seconds,
and <get_page>.
"""
import requests
import redis
from typing import Callable
from functools import wraps

DB = redis.Redis()


def count_url(get_page_: Callable) -> Callable:
    """
    Decorator for <get_page> that INCR's
    the <get_page>'s <url> argument
    in <DB>, using f"count:{url}" as the key,
    with an expiration time of 10 seconds.
    """
    @wraps(get_page_)
    def cached_get_page(url: str) -> str:
        URL_CACHE_KEY = f"count:{url}"
        DB.incr(URL_CACHE_KEY)

        RESPONSE_HTML = get_page_(url)
        DB.setex(url, 10, RESPONSE_HTML)

        return RESPONSE_HTML

    return cached_get_page


@count_url
def get_page(url: str) -> str:
    """
    Makes a request to <url>.
    Increments the cache counter for the <url>
    in DB, under the <f"count:{url}"> key.
    Sets the key's expiration time of 10 seconds.
    Returns the result.
    """
    response = requests.get(url).text
    return response
