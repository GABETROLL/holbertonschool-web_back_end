#!/usr/bin/env python3
"""
Write a Python script that provides some stats
about Nginx logs stored in MongoDB:
    - Database: logs
    - Collection: nginx
    - Display (same as the example):
        - first line: x logs where x is the number of documents
            in this COLLECTION
        - second line: Methods:
        - 5 lines with the number of documents with
            the method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
            in this order (see example below - warning:
                it’s a tabulation before each line)
        - one line with the number of documents with:
            - method=GET
            - path=/status

You can use this dump as data sample: dump.zip
"""
import pymongo


def main():
    """
    Runs the task.
    """
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


if __name__ == "__main__":
    main()
