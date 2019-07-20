class Personel:
    baslangic_maas = 1.400

    def __init__(self,Ad,Soyad,Telefon):
        self.Ad      = Ad
        self.Soyad   = Soyad
        self.Telefon = Telefon

    def TamAdi(self):
        return  "{} {}".format(self.Ad, self.Soyad)

    def Telefon(self):
        return  "+(90){}".format(self.Telefon)

    def __str__(self):
        return  "{} {} {}".format(self.Ad, self.Soyad, self.Telefon)





class Yazilimci(Personel):
    baslangic_maas = 10.000

    def __init__(self,Ad, Soyad, Telefon, YazilimDili):

        #self.Ad      = Ad
        #self.Soyad   = Soyad
        #self.Telefon = Telefon
        super().__init__(Ad,Soyad,Telefon)  # miras aldığımız sınıfın Constructor (yapıcı metot) (__init__) değerine parametre gönderiyoruz.

        # Personel.__init__(Ad,Soyad,Telefon) => süper metodu ile aynı işi görür, fakat sınıf ismini değiştirdiğinizde Personel Employee olursa bu alanıda değiştirmeniz gerekecektir. super() kullanırsanız size dinamiklik katacaktır.

        self.YazilimDili = YazilimDili


    def __str__(self):
        return "{} {}".format(super().__str__(),self.YazilimDili)



personel = Personel("Murat","Vuranok","21321321")
yazilimci = Yazilimci("Murat","Vuranok","2332131","C#,Python,Sql,vs...")


print(personel)
print(yazilimci)


print(issubclass(Personel, Yazilimci))
print(issubclass(Yazilimci,Personel)) # Personel, yazılımcı class'ının alt sınıfıdır.

































