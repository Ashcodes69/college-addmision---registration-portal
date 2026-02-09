import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))
from pymongo import MongoClient, errors
from config.settings import MONGO_URI, DB_NAME

try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=3000)
    db = client[DB_NAME]
    client.admin.command("ping")
    print("MongoDB connected")
except errors.ServerSelectionTimeoutError as err:
    print("MongoDB connection failed:", err)
