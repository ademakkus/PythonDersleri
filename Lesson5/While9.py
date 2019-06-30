from random import randint


# sayısal loto :) rastgele 6 adet sayı üretip bunu bir diziye ekleyiniz. Eğer aynı sayı dizi içerisinde geçiyor ise, tekrardan yeni bir numara üretiniz, dizi içerisinde yer alan 6 rakam benzersiz olmalıdır.

sayilar = []
i = 0
while i < 6:
    i += 1
    sayi = randint(1, 49)
    if sayilar.count(sayi):
        i-=1
    else:
        sayilar.append(sayi)

sayilar.sort()
print(sayilar)





