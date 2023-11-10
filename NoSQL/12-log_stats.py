#!/usr/bin/env python3
"""
Write a Python script that provides some stats
about Nginx logs stored in MongoDB.
"""
import pymongo


CLIENT = pymongo.MongoClient('mongodb://127.0.0.1:27017')
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
