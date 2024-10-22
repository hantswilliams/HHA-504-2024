
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os 
from dotenv import load_dotenv

load_dotenv()

mongoDB_password = os.getenv('MONGODB_PASSWORD')

uri = f'mongodb+srv://hants:{mongoDB_password}@hants-test.hnr2i.mongodb.net/?retryWrites=true&w=majority&appName=hants-test'

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Print list of collections in the database
print(client.list_database_names())

# Get list 5 documents from sample_mflix.movies collection

db = client.sample_mflix
collection = db.movies
cursor = collection.find().limit(1)

# Print the documents
for doc in cursor:
    print(doc)