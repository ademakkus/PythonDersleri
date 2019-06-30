sehirler = ["Adana","Ankara","Ardahan","Amasya","Edirne"]

# dizi içerisinde yer alan elemanların ismi içerisinde "m" harfi bulunanların yazdırılması


for sehir in sehirler:
    if("m" in sehir):
        print(sehir)
    else:
        print(sehir,"ismi içerisinse \"m\" harfi geçmemektedir")