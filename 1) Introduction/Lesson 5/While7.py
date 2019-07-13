

# dizi içerisinde yer alan elemanları teK ve çift olarak ayırıp ayrı ayrı dizilere eklemeni ve işlem sonucunda adatlerini kullanıcıya bildirmeniz

sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

i = 0
tek = []
cift = []
while i < len(sayilar):
    if sayilar[i] % 2 == 0:
        cift.append(sayilar[i])
    else:
        tek.append(sayilar[i])
    i = i + 1

print("Tek Sayıların Adedi :",len(tek),"\nÇift Sayıların Adedi :",len(cift))


