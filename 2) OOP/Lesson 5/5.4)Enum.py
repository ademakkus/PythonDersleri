from enum import Enum, unique, auto

@unique   # sınıf içerisinde aynı index değerine sahip enum oluşturmanıza izin vermez!
class Icecek(Enum):
    Vanilya  = auto()
    Çikolata = auto()
    Vişne    = 7
    Muzlu    = auto()
    Çilek    = 35
    Kahveli  = auto()


liste = list(Icecek)
print(liste)


