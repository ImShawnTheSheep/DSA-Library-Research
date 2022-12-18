import pymongo
from pymongo import MongoClient


studData = MongoClient(
    "mongodb+srv://shawnjumawan:VM6YYjXFTDmoAd9a@shawncluster.ywjvagz.mongodb.net/?retryWrites=true&w=majority")
# studData = MongoClient("mongodb://localhost:27017/")
db = studData["AMSDatabase"]
collect = db["Student Info"]

def find(key, value):
    cursor = collect.find({key: value})
    return cursor