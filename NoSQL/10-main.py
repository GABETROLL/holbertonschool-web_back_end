#!/usr/bin/env python3
"""
9-main:

Assuming that:
- the Mongo service is running in the machine this script
is being executed in
- the service contains a database named 'my_db',
- <my_db> has a collection named 'school',
- and THAT THE PREVIOUS EXERCISE IS CORRECT,

this script tests that <update_topics>, from '10-update_topics.py',
successfully and correctly UPDATES ONE of the documents in
the 'school' collection to have the "topics" key,
and the specified "topics" corresponding value.
"""
from pymongo import MongoClient
list_all = __import__('8-all').list_all
insert_school = __import__('9-insert_school').insert_school
update_topics = __import__('10-update_topics').update_topics


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school

    # empty and re-populate 'school' collection
    school_collection.delete_many({})
    for _ in range(10):
        insert_school(school_collection, name="Holberton school")

    # run <update_topics>
    update_topics(school_collection, "Holberton school", ["Sys admin", "AI", "Algorithm"])

    # Print 'school' documents
    print("---")
    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('topics', "")))

    # run <update_topics> again
    update_topics(school_collection, "Holberton school", ["iOS"])

    # Print 'school' documents again
    print("---")
    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('topics', "")))
