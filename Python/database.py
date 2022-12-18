import pymongo
from pymongo import MongoClient

studData = MongoClient("mongodb+srv://shawnjumawan:VM6YYjXFTDmoAd9a@shawncluster.ywjvagz.mongodb.net/?retryWrites=true&w=majority")

mydb = studData["AMSDatabase"]
mycol = mydb["Student Info"]

