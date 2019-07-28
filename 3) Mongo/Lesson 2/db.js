[
    {
        "_id"      : 1,
        "FirstName": "Ahmet",
        "LastName" : "Şahin",
        "Phone"    : "+90232445582",
        "Address"  : "Maslak",
        "Gender"   : "Erkek",
        "Movies"   : [1,2,3,4]
    },
    {
        "_id"      : 2,
        "FirstName": "Mehmet",
        "LastName" : "Subaşı",
        "Phone"    : "+90232445582",
        "Address"  : "Maslak",
        "Gender"   : "Erkek",
        "Movies"   : [3,6,8,9,10]
    }  ,
    {
        "_id"      : 3,
        "FirstName": "Şeyma",
        "LastName" : "Musluk",
        "Phone"    : "+90232445582",
        "Address"  : "Maslak",
        "Gender"   : "Kadın",
        "Movies"   : [3,4,11]
    },
    {
        "_id"      : 4,
        "FirstName": "Türkan",
        "LastName" : "Tarkan",
        "Phone"    : "+90232445582",
        "Address"  : "Maslak",
        "Gender"   : "Kadın",
        "Movies"   : [19,20]
    }  ,
    {
        "_id"      : 5,
        "FirstName": "Serkan",
        "LastName" : "Sarkan",
        "Phone"    : "+90232445582",
        "Address"  : "Maslak",
        "Gender"   : "Erkek",
        "Movies"   : [5,8,12,15]
    }
]

/* db.Movies.insertMany([
    {
        "_id": 1,
        "title": "Carmencita",
        "year": 1894,
        "imdbId": "tt0000001",
        "mpaaRating": "NOT RATED",
        "genre": "Documentary, Short",
        "viewerRating": 5.9,
        "viewerVotes": 1032,
        "runtime": 1,
        "director": "William K.L. Dickson",
        "cast": [
            "Carmencita"
        ],
        "plot": "Performing on what looks like a small wooden stage, wearing a dress with a hoop skirt and white high-heeled pumps, Carmencita does a dance with kicks and twirls, a smile always on her face."
    },
    {
        "_id": 2,
        "title": "Un bon bock",
        "year": 1892,
        "imdbId": "tt0000004",
        "genre": "Animation, Short",
        "viewerRating": 6.6,
        "viewerVotes": 78,
        "director": "èmile Reynaud"
    },
    {
        "_id": 3,
        "title": "Edison Kinetoscopic Record of a Sneeze",
        "year": 1894,
        "imdbId": "tt0000008",
        "genre": "Documentary, Short",
        "viewerRating": 5.9,
        "viewerVotes": 988,
        "runtime": 1,
        "director": "William K.L. Dickson",
        "cast": [
            "Fred Ott"
        ],
        "plot": "A man (Thomas Edison's assistant) takes a pinch of snuff and sneezes. This is one of the earliest Thomas Edison films and was the first motion picture to be copyrighted in the United States."
    },
    {
        "_id": 4,
        "title": "Chinese Opium Den",
        "year": 1894,
        "imdbId": "tt0000006",
        "genre": "Short",
        "viewerRating": 6,
        "viewerVotes": 56,
        "runtime": 1,
        "director": "William K.L. Dickson",
        "language": "English"
    },
    {
        "_id": 5,
        "title": "Corbett and Courtney Before the Kinetograph",
        "year": 1894,
        "imdbId": "tt0000007",
        "mpaaRating": "NOT RATED",
        "genre": "Short, Sport",
        "viewerRating": 5.5,
        "viewerVotes": 390,
        "runtime": 1,
        "director": "William K.L. Dickson, William Heise",
        "cast": [
            "James J. Corbett",
            "Peter Courtney"
        ],
        "plot": "James J. Corbett and Peter Courtney meet in a boxing exhibition."
    },
    {
        "_id": 6,
        "title": "Autour d'une cabine",
        "year": 1894,
        "imdbId": "tt0000015",
        "genre": "Animation, Short",
        "viewerRating": 6.3,
        "viewerVotes": 377,
        "runtime": 2,
        "director": "èmile Reynaud"
    },
    {
        "_id": 7,
        "title": "Akrobatisches Potpourri",
        "year": 1895,
        "imdbId": "tt0000011",
        "genre": "Documentary, Short",
        "viewerRating": 5.5,
        "viewerVotes": 111,
        "runtime": 1,
        "director": "Max Skladanowsky",
        "cast": [
            "Grunato"
        ],
        "plot": "Eight circus performers known as the Grunato family perform their famous balancing act."
    },
    {
        "_id": 8,
        "title": "Blacksmith Scene",
        "year": 1893,
        "imdbId": "tt0000005",
        "mpaaRating": "UNRATED",
        "genre": "Short",
        "viewerRating": 6.2,
        "viewerVotes": 1189,
        "runtime": 1,
        "director": "William K.L. Dickson",
        "cast": [
            "Charles Kayser",
            "John Ott"
        ],
        "plot": "Three men hammer on an anvil and pass a bottle of beer around."
    },
    {
        "_id": 9,
        "title": "Pauvre Pierrot",
        "year": 1892,
        "imdbId": "tt0000003",
        "genre": "Animation, Comedy, Short",
        "viewerRating": 6.7,
        "viewerVotes": 566,
        "runtime": 4,
        "director": "èmile Reynaud",
        "plot": "One night, Arlequin come to see his lover Colombine. But then Pierrot knocks at the door and Colombine and Arlequin hide. Pierrot starts singing but Arlequin scares him and the poor man goes away."
    },
    {
        "_id": 10,
        "title": "The Derby 1895",
        "year": 1895,
        "imdbId": "tt0000020",
        "genre": "Documentary, Short, Sport",
        "viewerRating": 5.2,
        "viewerVotes": 145,
        "runtime": 1,
        "director": "Birt Acres",
        "plot": "A stationary camera, looking diagonally across a racetrack toward the infield, records the horses as they race past. Once they are out of view and the race is over, police officers run onto..."
    },
    {
        "_id": 11,
        "title": "The Photographical Congress Arrives in Lyon",
        "year": 1895,
        "imdbId": "tt0000013",
        "mpaaRating": "NOT RATED",
        "genre": "Documentary, Short",
        "viewerRating": 5.6,
        "viewerVotes": 872,
        "runtime": 1,
        "director": "Louis Lumière",
        "cast": [
            "Auguste Lumi�re"
        ],
        "plot": "Another milestone in film history - this may well have been the very first film to have been developed and shown to its subjects (the members of the Congress of Photographic Societies) on ..."
    },
    {
        "_id": 12,
        "title": "Blacksmith Scene",
        "year": 1895,
        "imdbId": "tt0000022",
        "genre": "Documentary, Short",
        "viewerRating": 5.1,
        "viewerVotes": 468,
        "runtime": 1,
        "director": "Louis Lumière",
        "plot": "Two blacksmiths are at work, facing the camera, a wall, window, and stacked boxes behind them. Both are mustachioed with dark hair. On our right, a smith in the dark clothes of a laborer ..."
    },
    {
        "_id": 13,
        "title": "Jumping the Blanket",
        "year": 1895,
        "imdbId": "tt0000031",
        "genre": "Documentary, Short",
        "viewerRating": 5.5,
        "viewerVotes": 435,
        "runtime": 1,
        "director": "Louis Lumière",
        "plot": "Outdoors, with a nondescript building in the background, four men stand, each holding the corner of a blanket stretched parallel to the ground. They wear the clothes of laborers. By the ..."
    },
    {
        "_id": 14,
        "title": "Opening of the Kiel Canal",
        "year": 1895,
        "imdbId": "tt0000024",
        "genre": "Short, News",
        "viewerRating": 5.2,
        "viewerVotes": 19,
        "director": "Birt Acres",
        "cast": [
            "Empress Augusta Victoria",
            "Kaiser Wilhelm II"
        ]
    },
    {
        "_id": 15,
        "title": "The Sea",
        "year": 1895,
        "imdbId": "tt0000023",
        "genre": "Documentary, Short",
        "viewerRating": 5.5,
        "viewerVotes": 599,
        "runtime": 1,
        "director": "Louis Lumière",
        "plot": "Several little boys run along a pier, then jump into the ocean."
    },
    {
        "_id": 16,
        "title": "Das boxende Kènguruh",
        "year": 1895,
        "imdbId": "tt0000018",
        "genre": "Short",
        "viewerRating": 5.5,
        "viewerVotes": 253,
        "runtime": 1,
        "director": "Max Skladanowsky",
        "cast": [
            "Delaware"
        ],
        "plot": "A man and a kangaroo stand up in front of each other with boxing gloves, and simulate a boxing match on a theatre stage."
    },
    {
        "_id": 17,
        "title": "Arrivèe d'un train gare de Vincennes",
        "year": 1896,
        "imdbId": "tt0000034",
        "genre": "Documentary, Short",
        "viewerRating": 6,
        "viewerVotes": 44,
        "director": "Georges Mèliès"
    },
    {
        "_id": 18,
        "title": "Italienischer Bauerntanz",
        "year": 1895,
        "imdbId": "tt0000017",
        "genre": "Documentary, Short",
        "viewerRating": 5.2,
        "viewerVotes": 103,
        "runtime": 1,
        "director": "Emil Skladanowsky, Max Skladanowsky",
        "cast": [
            "Ploetz",
            "Larella"
        ],
        "plot": "Two children, Ploetz and Larella, perform an Italian peasant dance."
    },
    {
        "_id": 19,
        "title": "Die Serpentintènzerin",
        "year": 1895,
        "imdbId": "tt0000032",
        "genre": "Short",
        "viewerRating": 5.4,
        "viewerVotes": 183,
        "runtime": 1,
        "director": "Max Skladanowsky",
        "cast": [
            "Ancion"
        ],
        "plot": "A young woman dancer with large, flowing robes, swirls round herself quickly, making her light robe flow around her like a butterfly's wings."
    },
    {
        "_id": 20,
        "title": "Bataille de neige",
        "year": 1897,
        "imdbId": "tt0000041",
        "genre": "Short, Documentary",
        "viewerRating": 6.8,
        "viewerVotes": 804,
        "runtime": 1,
        "director": "Louis Lumière",
        "plot": "Wintertime in Lyons. About a dozen people, men and women, are having a snowball fight in the middle of a tree-lined street. The cyclist coming along the road becomes the target of ..."
    }
])*/