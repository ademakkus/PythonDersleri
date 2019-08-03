// Equality  == 
// db.Products.find({"ProductID":77}).pretty()

// 8 numaralı CategoryID değerine sahip olan ürünleri listeleyiniz

// db.Products.find({"CategoryID" : 8}).pretty()

// Less Than 
// Fiyatı 50$'dan az olan ürünlerin listelenmesi

// db.Products.find({"UnitPrice": {$lt:50}}).pretty()

// Ürünlerin sıralanması..

// Ascending   +1  A'dan Z'ye, 0'dan 9'a (fakirden zengine)
// Descending  -1  Z'den A'ya, 9'dan 0'a (zenginden fakire)

// db.Products.find().pretty().sort({"UnitPrice": 1}) ascending
// db.Products.find().pretty().sort({"UnitPrice": -1}) descending

// Less Than Equals   <= 
// db.Products.find({"UnitsInStock": {$lte:50}}).pretty()
// db.Products.find({"UnitsInStock": {$lte:50}}).pretty().sort({"UnitsInStock":1})

// Grather Than
// fiyatı 100$ fazla olanları listeleyiniz.

// db.Products.find({"UnitPrice": {$gt:100}}).pretty()

// Grather Than Equals
// db.Products.find({"UnitPrice": {$gte: 50}}).pretty().sort({"UnitPrice":-1})


// Not Equals  
// CategoryID değeri, 8 olmayan ürünlerin listelenmesi

// db.Products.find({"CategoryID" : {$ne:8}}).pretty().sort({"CategoryID" : 1})


// and ve or kullanımı

// and kullanımı :

// db.Products.find({$and:[{"CategoryID" : 8},{"UnitPrice": {$lte: 30}}]}).pretty()


// Fiyatı 30$ büyük ve stok adedi 100'den küçük olanların listelenmesi

// db.Products.find({$and:[{"UnitPrice": {$gte: 30}},{"UnitsInStock": {$lte:100}}]}).pretty()


// or Kullanımı

// fiyatı 100$ üzeri veya stok adedi 100 üzeri olan ürünlerin fiyata göre ascending olarak sıralı listelenmesi.

// db.Products.find({$or:[{"UnitPrice": {$gte:100}}, {"UnitsInStock": {$gte:100}} ]}).sort({"UnitPrice":1}).pretty()

// db.Products.find({},{ProductName:1,_id:0})
// ürünadı fiyat ve stok adedini listeleyiniz.

// db.Products.find({},{ProductName:1,UnitPrice:1,UnitsInStock:1, _id:0}).sort({ProductName:1})



// pymongo 5 saat
// 5 saat html css js
// 15 saat django örnek uygulama
