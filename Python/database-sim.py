import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://shawnjumawan:VM6YYjXFTDmoAd9a@shawncluster.ywjvagz.mongodb.net/?retryWrites=true&w=majority")
db = cluster["sampledatabase"]
collection = db["studentinfo"]

# print(db.list_collection_names())

collection.insert_one({
    '_id': 'student1',
    'studentname': 'Shawn Jumawan',
    'studentnumber': '2021-00363-CM-0',
    'loglocation': 'Rothlener Bldg',
    'time': 1030
})

cursor = collection.find_one({})

print(cursor)