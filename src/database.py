from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGODB_URI")


def get_database():
    client = MongoClient(MONGO_URI)
    db_name = "student_management"
    db = client[db_name]

    return db
