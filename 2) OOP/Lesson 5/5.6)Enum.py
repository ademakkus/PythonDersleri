# Flag kullanımı, oluşturduğunuz enum değerlerinin sayısal karşılığının benzersiz ve birden fazla enum değerinin bir enum değerine karşılık gelmemesi için kullanılır.

from enum import Flag, auto, Enum


class Renkler (Flag):
    Kırmızı = auto() # enum = 1  flag = 1
    Sarı    = auto() # enum = 2  flag = 2
    Mavi    = auto() # enum = 3  flag = 4
    Turuncu = auto() # enum = 4  flag = 8
    Yeşil   = auto() # enum = 5  flag = 16
    Pembe   = auto() # enum = 6  flag = 32
    Beyaz   = Kırmızı | Mavi | Sarı     # 7

# print( Renkler.Sarı and Renkler.Pembe)

liste = list(Renkler)
print(liste)

print(Renkler.Kırmızı.value + Renkler.Mavi.value + Renkler.Sarı.value)
print(repr(Renkler.Beyaz))

