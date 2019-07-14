# __str__     C# ToString() metodunun karşılığıdır. Class'ın override edilmesi

class Personel:
    isim    = ""
    soyisim = ""
    yas     = 0

    def __str__(self):
        return "{} {}".format(self.isim, self.soyisim)


p = Personel()
p.isim ="Murat"
p.soyisim ="Vuranok"
p.yas = 88

print(p)  # <__main__.Personel object at 0x03850930> => ilgili sınıfın ram(heap) üzerindeki adresini teslim eder.


print(p.isim + " "+ p.soyisim)
print(p)