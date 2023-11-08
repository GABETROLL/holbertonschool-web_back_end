#!/usr/bin/env python3
"""
Write a Python function that inserts a new document in a collection based on kwargs:

    - Prototype: def insert_school(mongo_collection, **kwargs):
    - mongo_collection will be the pymongo collection object
    - Returns the new _id
"""
import pymongo


def insert_school(mongo_collection: pymongo.collection.Collection, **kwargs):
    """
    Inserts the <kwargs> dictionary, as a BSON object,
    into <mongo_collection>, assuming that <mongo_collection>
    is a Mongo collection object.

    The <kwargs> dictionary should be the remaining
    keyword=value pairs after the first argument, <mongo_collection>,
    and will be treated as the object to insert, whith each
    arg name as the key, and each value as the value in the new
    object to insert to the collection:

    RESULT = mongo_collection.insertOne(kwargs)
    return RESULT.inserted_id
    """
    RESULT = mongo_collection.insert_one(kwargs)
    return RESULT.inserted_id
