from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Important: Load environment variables from the PROJECT ROOT
load_dotenv('../.env')

# Get MongoDB URI
MONGO_URI = os.getenv("MONGODB_URI")


def test_connection():
    try:
        # Ensure you're using the full MongoDB Atlas connection string
        print("Attempting to connect with URI:", MONGO_URI)

        # Create a new client
        client = MongoClient(MONGO_URI)

        # Send a ping to confirm a successful connection
        client.admin.command('ping')
        print("Successfully connected to MongoDB!")

        # List databases (optional)
        print("Available Databases:")
        print(client.list_database_names())

    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")


# Run the test
if __name__ == "__main__":
    test_connection()