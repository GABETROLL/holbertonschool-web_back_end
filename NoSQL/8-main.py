#!/usr/bin/env python3
"""
8-main:

Tests exercise 8, which has one exercise file: <8-all.py>.

This file assumes that the Mongo service is running
in the machine this file being executed in,
that mongo has a DB named 'my_db',
and that 'my_db' has a collection named 'school'.
"""
from pymongo import MongoClient
list_all = __import__('8-all').list_all

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school
    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {}".format(school.get('_id'), school.get('name')))
