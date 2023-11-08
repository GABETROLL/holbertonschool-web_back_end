#!/usr/bin/env python3
import pymongo
from typing import List


def list_all(mongo_collection: pymongo.collection.Collection) -> List:
    """
    Lists all of the documents in <mongo_collection>,
    assuming that <mongo_collection> is a MongoDB collection.
    """
    return [document for document in mongo_collection.find()]
