# Dışarıdan aldığı metin içerisindeki sesli karakterlerin ve sessiz karakterlerin sayısını ekrana yazdıran metot

def sessliKontrolu(string):
    sesli_harfler = ["a","e","ı","i","o","ö","u","ü"]
    liste = list(string)
    sesliCount  = 0
    sessizCount = 0

    for i in liste:
        if i in sesli_harfler:
            sesliCount += 1
        else:
            sessizCount += 1
    print("Toplam Sesli Harf Sayısı : {}\nToplam Sessiz Harf Sayısı : {}".format(sesliCount, sessizCount))



sessliKontrolu("sadsadsadasdaddsadsa")
# ['s', 'a', 'd', 's', 'a', 'd', 's', 'a', 'd', 'a', 's', 'd', 'a', 'd', 'd', 's', 'a', 'd', 's', 'a']