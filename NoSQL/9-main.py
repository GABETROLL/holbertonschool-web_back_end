#!/usr/bin/env python3
"""
9-main:

Assuming that:
- the Mongo service is running in the machine this script
is being executed in
- the service contains a database named 'my_db',
- <my_db> has a collection named 'school',

this script tests that <insert_school>, from '9-insert_school.py',
successfully and correctly adds a new document to the 'school' collection.
using <list_all> from '8-all.py' and Mongo's tools.
"""
from pymongo import MongoClient
list_all = __import__('8-all').list_all
insert_school = __import__('9-insert_school').insert_school

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school
    new_school_id = insert_school(school_collection, name="UCSF", address="505 Parnassus Ave")
    print("New school created: {}".format(new_school_id))

    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('address', "")))
