def Kayitlar(**params):
    print("-"*25)
    for key,value  in params.items():
        print("{0:<8}: {1}".format(key,value))
    print("-"*25)


Kayitlar(
    Ad      = "Murat Vuranok",
    Soyad   = "Vuranok",
    Telefon = "213213213",
    Mail    = "murat.vuranok@bilgeadam.com")
 