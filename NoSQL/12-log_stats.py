#!/usr/bin/env python3
"""
Write a Python script that provides some stats about Nginx logs stored in MongoDB:
    - Database: logs
    - Collection: nginx
    - Display (same as the example):
        - first line: x logs where x is the number of documents in this COLLECTION
        - second line: Methods:
        - 5 lines with the number of documents with the method = ["GET", "POST", "PUT", "PATCH", "DELETE"] in this order (see example below - warning: it’s a tabulation before each line)
        - one line with the number of documents with:
            - method=GET
            - path=/status

You can use this dump as data sample: dump.zip

The output of your script must be EXACTLY LIKE THE EXAMPLE:
```
$ ./12-log_stats.py
94778 logs
Methods:
    method GET: 93842
    method POST: 229
    method PUT: 0
    method PATCH: 0
    method DELETE: 0
47415 status check
```
"""
import pymongo

CLIENT = pymongo.MongoClient()
DB = CLIENT.logs
COLLECTION = DB.nginx

LOG_COUNT = COLLECTION.count_documents({})
print(f"{LOG_COUNT} logs")

print("Methods:")
for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
    METHOD_COUNT = COLLECTION.count_documents({"method": method})
    print(f"\tmethod {method}: {METHOD_COUNT}")

STATUS_LOG_COUNT = COLLECTION.count_documents({"path": "/status"})
print(f"{STATUS_LOG_COUNT} status check")
