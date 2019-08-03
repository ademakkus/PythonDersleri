[
    {
        "_id": 1,
        "CategoryName": "Beverages",
        "Description": "Soft drinks, coffees, teas, beers, and ales"
    },
    {
        "_id": 2,
        "CategoryName": "Condiments",
        "Description": "Sweet and savory sauces, relishes, spreads, and seasonings"
    },
    {
        "_id": 3,
        "CategoryName": "Confections",
        "Description": "Desserts, candies, and sweet breads"
    },
    {
        "_id": 4,
        "CategoryName": "Dairy Products",
        "Description": "Cheeses"
    },
    {
        "_id": 5,
        "CategoryName": "Grains/Cereals",
        "Description": "Breads, crackers, pasta, and cereal"
    },
    {
        "_id": 6,
        "CategoryName": "Meat/Poultry",
        "Description": "Prepared meats"
    },
    {
        "_id": 7,
        "CategoryName": "Produce",
        "Description": "Dried fruit and bean curd"
    },
    {
        "_id": 8,
        "CategoryName": "Seafood",
        "Description": "Seaweed and fish"
    }
]

db.Categories.insertMany([
    {
        "CategoryID": 1,
        "CategoryName": "Beverages",
        "Description": "Soft drinks, coffees, teas, beers, and ales"
    },
    {
        "CategoryID": 2,
        "CategoryName": "Condiments",
        "Description": "Sweet and savory sauces, relishes, spreads, and seasonings"
    },
    {
        "CategoryID": 3,
        "CategoryName": "Confections",
        "Description": "Desserts, candies, and sweet breads"
    },
    {
        "CategoryID": 4,
        "CategoryName": "Dairy Products",
        "Description": "Cheeses"
    },
    {
        "CategoryID": 5,
        "CategoryName": "Grains/Cereals",
        "Description": "Breads, crackers, pasta, and cereal"
    },
    {
        "CategoryID": 6,
        "CategoryName": "Meat/Poultry",
        "Description": "Prepared meats"
    },
    {
        "CategoryID": 7,
        "CategoryName": "Produce",
        "Description": "Dried fruit and bean curd"
    },
    {
        "CategoryID": 8,
        "CategoryName": "Seafood",
        "Description": "Seaweed and fish"
    }
])

db.Categories.aggregate({  // ana tablo tablo
    $lookup:
    {
        from: "Products",  // join yapılacak olan tablo
        localField: "_id", // ana tablo içerisindeki pk (primary key) birincil anahtar
        foreignField: "CategoryID",  // ForeignKey (ikincil anahtar)
        as: "Products" // sorgu sonucu kategoriye bağlı ürünler listelenirken, verilecek olan isim (opsiyonel) dilediğiniz ismi verebilirsiniz.
    }
}).pretty()

// select * from Categories join Products on Categories._id = Products.CategoryID





db.Categories.aggregate(
    {
        $match:
        {
            _id: 1 // CategoryID
        }
    },
    {
        $lookup:
        {
            from: "Products",
            localField: "_id",
            foreignField: "CategoryID",
            as: "Products"
        }
    }
).pretty()



