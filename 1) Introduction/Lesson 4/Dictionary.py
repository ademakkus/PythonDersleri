# Dictionary key value formatında dataları listelemek için kullanılır. Json formatında data tutar, MongoDb, WebApi (servisler), JavaScript (vue js, angular js, angular io, react, react-native, cordova vs) gibi  bir çok platform bunu destekler.

personeller = [
    {
        "Id"        :1,
        "IndexNo"   :0,
        "FirstName" :"Murat",
        "LastName"  :"Vuranok"
    },
    {
        "Id"       : 2,
        "IndexNo"  : 1,
        "FirstName": "Ahmet Berke",
        "LastName" : "Aksu"
    },{
        "Id"       :3,
        "IndexNo"  :2,
        "FirstName":"Ahmet Faruk",
        "LastName" :"Karademir"
    }
]

# listenin verilen index değerine göre, o elemanı ekrana yazdırma
print(personeller[0])
# {'Id': 1, 'FirtsName': 'Murat', 'LastName': 'Vuranok'}

# dizi içerisinde eğer bir index değerindeki elemanın herhangi bir property'sini ekrana yazdırmak için ;

print(personeller[0]["FirstName"])
# Murat

print(personeller[0]["LastName"])
# Vuranok


# liste içerisinde yer alan bir elemanın güncellemek istiyorsanız!


guncellenecekIndex  = 2
guncellenecekKey    = "FirstName"



oldName = personeller[guncellenecekIndex][guncellenecekKey]
personeller[guncellenecekIndex][guncellenecekKey] = "Okan"

print(oldName,"Adlı, Personelin Yeni Adı :", personeller[2]["FirstName"],"Olarak Güncellenmiştir")

# Ahmet Faruk Adlı, Personelin Yeni Adı : Okan Olarak Güncellenmiştir

personeller.append({"Id":4 ,"IndexNo":3, "FirstName":"Mehmet","LastName":"Uçak",})

print(personeller[:])



# [{'Id': 1, 'IndexNo': 0, 'FirtsName': 'Murat', 'LastName': 'Vuranok'}, {'Id': 2, 'IndexNo': 1, 'FirtsName': 'Ahmet Berke', 'LastName': 'Aksu'}, {'Id': 3, 'IndexNo': 2, 'FirstName': 'Okan', 'LastName': 'Karademir'}, {'Id': 4, 'IndexNo': 3, 'FirstName': 'Mehmet', 'LastName': 'Uçak'}]

# print("Personeli Adı :", personeller[0]["FirstName"] ,"Personelin Soyadı :",   personeller[0]["LastName"])

print("Personeli Adı : {1}\nPersonelin Soyadı : {0}".format(personeller[0]["FirstName"], personeller[0]["LastName"]))
# KeyError: 'FirstName'


print("Personel Adı : " + personeller[0]["FirstName"] +"\nPersonel Soyadı : "+ personeller[0]["LastName"])

print("Personel Adı :",personeller[0]["FirstName"],"\nPersonel Soyadı :",personeller[0]["LastName"])

print("Personel Adı : {0}\nPersonel Soyadı : {1}".format(personeller[0]["FirstName"],personeller[0]["LastName"]))

# eğer format içerisinde index değeri belirtmezseniz default olarak 0,1,2 ... gibi devam eder.

# format içerisine verdiğiniz ilk değer 0. index değeridir.