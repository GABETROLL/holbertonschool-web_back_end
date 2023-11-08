#!/usr/bin/env python3
"""
Write a Python function that returns the list of school having a specific topic:
    - Prototype: def schools_by_topic(mongo_collection, topic):
    - mongo_collection will be the pymongo collection object
    - topic (string) will be topic searched
"""
import pymongo
from typing import List


def schools_by_topic(
    mongo_collection: pymongo.collection.Collection,
    topic: str
) -> List:
    """
    -> return [
        school
        for school in
        mongo_collection.find({"topic": topic})
    ]

    Returns a list of all of the documents in the
    <mongo_collection> that have {"topic": topic}.
    """
    return [
        school
        for school in
        mongo_collection.find({"topic": topic})
    ]
