#!/usr/bin/env python3
"""
Write a Python function that lists all documents in a collection:
    - Prototype: def list_all(mongo_collection):
    - Return an empty list if no document in the collection
    - mongo_collection will be the pymongo collection object
"""
import pymongo
from typing import List


def list_all(mongo_collection: pymongo.collection.Collection) -> List:
    """
    RETURNS A list of all of the documents in <mongo_collection>,
    assuming that <mongo_collection> is a MongoDB collection.

    If there are no documents in <mongo_collection>,
    this function returns an empty list.
    """
    return [document for document in mongo_collection.find()]
