import  datetime
now = datetime.datetime.now()

print(str(now))
# 2019-07-21 10:20:04.182442
print(repr(now))
# datetime.datetime(2019, 7, 21, 10, 20, 4, 182442)

class Personel:
    def __init__(self, isim):
        self.FirstName = isim

    def __repr__(self):
        return "Personel('{}','{}')".format(self.FirstName, self.FirstName)

    def __str__(self):
        return '{}-{}'.format(self.FirstName, self.FirstName)



per = Personel("Murat")
print(str(per))
print(per)
print(repr(per))
print(str(per))

print(per.__repr__())   # developer için devam niteliğinde kod verir
print(per.__str__())    # son kullanıcı için çıktı verir


