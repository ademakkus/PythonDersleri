/*
  1) show dbs            : server içerisinde yer alan database'leri gösterir
  2) use <database adı>  : çalışmak istediğiniz database adını vermeniz yeterlidir. Not : küçük büyük harf duyarlılığı vardır.
  3) show collections    : database içerisinde yer alan koleksiyonları teslim eder (table)


 alt + z wordwrap
 shift + alt + f   kodları düzenleme
*/


// db.Kisiler.insert()

[
    {
        "firstname": "Murat",
        "lastname": "vuranok",
        "phones": [
            {
                "name": "mobil",
                "phone": "+903336664477"
            },
            {
                "name": "home",
                "phone": "+903336664477"
            }
            ,
            {
                "name": "work",
                "phone": "+903336664477"
            }
        ]
    }
]




/*

TelefonReheri db içeisinde yer alacak olan Kisiler tablosuna(collection) veri ekleme



1. Adım  => mongo

2. Adım  => use TelefonRehberi
 
3. Adım  => db.Kisiler.insert({ 
        "firstname": "Murat",
        "lastname": "vuranok",  
        "phones" : [
            {
                "name":"mobil",
                "phone" :"+903336664477"
            } ,
            {
                "name":"home",
                "phone" :"+903336664477"
            } 
            ,
            {
                "name":"work",
                "phone" :"+903336664477"
            } 
        ]
    })


4. Adım => db.Kisiler.find()   => tablo(collections) içerisinde yer alan kayıtları teslim eder.
5. Adım => db.Kisiler.find().pretty() => koleksiyon içinde yer alan dataların daha tatlı(pretty) görünmesini sağlar havalıdır :D

6. Adım  =>  tablo içerisine ek bir alan eklenmesi
  "email" :"murat.vuranok@bilgeadam.com", 1 adet ise


 db.Kisiler.insert( {
        "firstname": "Murat",
        "lastname": "vuranok",
        emails: [
            {
                "email": "murat.vuranok@bilgeadam.com"
            },
            {
                "email": "murat.vuranok@hotmail.com"
            },
            {
                "email": "murat.vuranok@outlook.com"
            }
        ],
        "phones": [
            {
                "name": "mobil",
                "phone": "+903336664477"
            },
            {
                "name": "home",
                "phone": "+903336664477"
            }
            ,
            {
                "name": "work",
                "phone": "+903336664477"
            }
        ]
    })


*/

[
    {
        "_id": ObjectId("5d3c269880766821cb9d5d69"),
        "firstname": "Murat",
        "lastname": "vuranok",
        "phones": [
            {
                "name": "mobil",
                "phone": "+903336664477"
            },
            {
                "name": "home",
                "phone": "+903336664477"
            },
            {
                "name": "work",
                "phone": "+903336664477"
            }
        ]
    }
]





[
    {
        "_id": ObjectId("5d3c269880766821cb9d5d69"),
        "firstname": "Murat",
        "lastname": "vuranok",
        "phones": [
            {
                "name": "mobil",
                "phone": "+903336664477"
            },
            {
                "name": "home",
                "phone": "+903336664477"
            },
            {
                "name": "work",
                "phone": "+903336664477"
            }
        ]
    },
    {
        "_id": ObjectId("5d3c2b6580766821cb9d5d6a"),
        "firstname": "Murat",
        "lastname": "vuranok",
        "emails": [
            {
                "email": "murat.vuranok@bilgeadam.com"
            },
            {
                "email": "murat.vuranok@hotmail.com"
            },
            {
                "email": "murat.vuranok@outlook.com"
            }
        ],
        "phones": [
            {
                "name": "mobil",
                "phone": "+903336664477"
            },
            {
                "name": "home",
                "phone": "+903336664477"
            },
            {
                "name": "work",
                "phone": "+903336664477"
            }
        ]
    }
]












[
    {
        "_id": ObjectId("5d3c269880766821cb9d5d69"),
        "firstname": "Murat",
        "lastname": "vuranok",
        "phones": [
            { "name": "mobil", "phone": "+903336664477" },
            { "name": "home", "phone": "+903336664477" },
            { "name": "work", "phone": "+903336664477" }
        ]
    }
]