import pymongo


class Person:
    def __str__(self):
        return "{} {} {} {}".format(self.FirstName, self.LastName, self.Phone, self.Mail)


def Create():
    person = Person()
    person.FirstName = input("Lütfen isminizi giriniz : ")
    person.LastName = input("Lütfen soyisminizi giriniz : ")
    person.Mail = input("Lütfen mail adresinizi giriniz : ")
    person.Phone = input("Lütfen telefon numaranızı giriniz : ")
    return person


def ConnectClient():
    return pymongo.MongoClient("mongodb://localhost:27017/")


def Insert(person):
    myClint = ConnectClient()
    myDb = myClint["PhoneBook"]
    myCollection = myDb["People"]
    myCollection.insert_one(person)


def List():
    myClint = ConnectClient()
    myDb = myClint["PhoneBook"]
    myCollection = myDb["People"]

    people = myCollection.find({}, {"_id": 0})
    for i in people:
        print("-"*45)
        for x, y in i.items():
            print("{0:<12}: {1}".format(x, y))


def Delete(param):
    myClint = ConnectClient()
    myDb = myClint["PhoneBook"]
    myCollection = myDb["People"]
    myQuery = {"FirstName": param}
    myCollection.delete_one(myQuery)


def Update(param):
    myClint = ConnectClient()
    myDb = myClint["PhoneBook"]
    myCollection = myDb["People"]
    myQuery = {"FirstName": param}

    per = Create()

    newValue = {"$set": per.__dict__}
    myCollection.update_one(myQuery, newValue)


def Start():
    key = "y"
    while key != "e":
        key = input(
            "Lütfen İşlem Seçiniz! \n\nListe       l \nSilme       d \nGüncelleme  u\nEkleme      a \nÇıkış       e\n\nSeçiminiz : ").lower()
        if key == "l":
            List()
        elif key == "a":
            per = Create()
            Insert(per.__dict__)
        elif key == "d":
            Delete(input("Lütfen isim giriniz : "))
        elif key == "u":
            Update(input("Lütfen Güncellemek İstediğiniz Kişinin Adını Giriniz : "))


Start()

 