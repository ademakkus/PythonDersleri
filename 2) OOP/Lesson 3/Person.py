class  Person:
    FirstName = "",
    LastName  = "",
    Phone     = "",
    Mail      = ""

    def __init__(self, FirstName, LastName, Phone, Mail):
        pass
    def __str__(self):
        return  "{} {}".format(self.FirstName , self.LastName)

"""
print(
    "Adına Göre Arama İçin : a\nSoyadına Göre Arama İçin : s\nTelefon Numarasına Göre Arama İçin : t\nMail Adresine Göre Arama İçin : m")
key = input("Lütfen Bir Anahtar Kelime Giriniz : ")

if (key == "a"):
    metin = input("Lütfen Kişinin Adını Giriniz : ")
    Liste(metin)
elif key == "s":
    pass
elif key == "t":
    pass
elif key == "m":
    pass
else:
    print("Uyulama Sonlandırıldı")
    result = False"""