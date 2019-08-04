import pymongo


myClient = pymongo.MongoClient("mongodb://localhost:27017/")
myDb = myClient["Northiwnd"]  # Northwind
myCollection = myDb["Products"]

products = myCollection.find({}, {"ProductName": 1, "_id": 0})

for x in products:
    print(x)
