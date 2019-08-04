import pymongo

myClient = pymongo.MongoClient("mongodb://localhost:27017/")

myDb = myClient["PhoneBook"]
myCollection = myDb["People"]


person = {
    "FirstName": "Murat",
    "LastName": "Vuranok",
    "Phone": "+90(532) 352 09 97",
    "Mail": "murat.vuranok@bilgeadam.com"
}

# myCollection.insert_one(person)
# print(myClient.list_database_names())
people = myCollection.find({}, {"_id": 0})
for i in people:
    print("-"*40)
    for x, y in i.items():
        print("{} : {}".format(x, y))
