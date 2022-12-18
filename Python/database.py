import pymongo
from pymongo import MongoClient

studData = MongoClient(
    "mongodb+srv://shawnjumawan:VM6YYjXFTDmoAd9a@shawncluster.ywjvagz.mongodb.net/?retryWrites=true&w=majority")
# studData = MongoClient("mongodb://localhost:27017/")
db = studData["AMSDatabase"]
collect = db["Student Info"]

cursor = collect.find({"tag": "student"})
counter = {
    "student_count": collect.count_documents({"tag": "student"}),
    "visitor_count": collect.count_documents({"tag": "visitor"})
}

for cursors in cursor:
    print("NAME: ", cursors["name"])
    print("STUDENT NO.: ", cursors["studnum"])
    print("____________________________________________")

print("No. of students: ", counter["student_count"])
print("No. of visitors: ", counter["visitor_count"], "\n")

print(type(cursor))
print(type(cursors))
