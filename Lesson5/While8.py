# dışarıdan girilen metin içerisinde yer alan sessli ve sessiz karakterleri ayrıştırınız ve kullanıcıya metin içerisinde kaç adet sessli, kaç adet sessiz harf var mesaj veriniz.
#ssdasd.aüğppoıkçöm
metin = input("Lütfen metin giriniz").lower()
sesli_harfler = ["a","e","i","ı","o","ö","u","ü"]
sesli =[]
sessiz = []

i = 0
while i < len(metin):
    if sesli_harfler.count(metin[i]):
        sesli.append(metin[i])
    else:
        sessiz.append(metin[i])

    i = i + 1

print("Sesli harf sayısı :", len(sesli),"\nSessiz harf sayısı :",len(sessiz))
